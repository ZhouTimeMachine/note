<link rel="stylesheet" href="../../../css/counter.css" />

# Denoising Diffusion Implicit Models

!!! info "Main Reference: [Denoising Diffusion Implicit Models](http://arxiv.org/abs/2010.02502), ICLR 2021 Poster"

??? note "Gossip"
    正如 DDPM，DDIM 在投稿 ICLR 2021 时也仅仅是 Poster，2025.5.27 查阅时引用已经达到 8000+ 了。尽管 DDIM arxiv 的最初提交时间 (2020.10) 早于 SGM (2020.11)，但自 2021.11 开始便在 arxiv 上更新了和 ODE 相关联系的内容，因此这部分理论在投稿时应当是没有作为贡献的。

## Denoising of DDPM: Time Consuming

回顾原始 DDPM 的去噪，是通过让去噪转移核 $p_{\theta}(x_{t-1}|x_t)$ 趋近于 ground truth 的 $p(x_{t-1}|x_t, x_0)$，一步步去噪得到的。由于 $p(x_{t-1}|x_t, x_0)=\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)$，我们也将 $p_{\theta}(x_{t-1}|x_t)$ 重参数化为 $\mathcal{N}(\mu_{\theta}(x_t, t), \sigma_t^2I)$，因此实际上操作为

$$
x_{t-1} = \mu_{\theta}(x_t, t) + \sigma_t\varepsilon
$$

> 这里的 $\varepsilon\sim \mathcal{N}(0, 1)$ 是随机采样的去噪过程中的加噪扰动，和 epsilon-prediction 中模型预测的 $\varepsilon_{\theta}^{(t)}(x_t)$ 不同，后者是用来构造 $\mu_{\theta}(x_t, t)$ 的 

$\varepsilon_t$ 导致去噪过程的每一步都具有一定的随机性，从而需要一步步去噪。训练时加噪点最大时间步数如果为 $T$（DDPM 中 $T=1000$），则 DDPM 去噪时也需要去噪 $T$ 步。

- 训练时，通过对每一步加噪的噪声进行重参数化合并，我们只需要 $1$ 步就可以完成 $1\leqslant t\leqslant T$ 步的加噪
- 但推理时我们只能一步步去噪，是这是非常耗时的

## Denoising of DDIM

DDIM 的核心思想为

- 将加噪时的 Markovian 扩散过程转化为 non-Markovian 扩散过程，但从 $x_0$ 到 $x_t$ 的**等效单步加噪公式不变**，这样能依照 non-Markovian 扩散过程跨步去噪，而不必一步步去噪
- （理论解释）将 SDE 转化成 ODE，从而**去噪的每一步都不再需要随机项**，从而可以使用解 ODE 的加速方法加速

> 第二条相当于后期解释了，最初提出 DDIM 时对 DDPM 的 SDE 视角解释还没有出来

由于我们希望保持加噪公式不变，从需要保持的加噪公式出发

$$
x_ {t-\Delta t} = \sqrt{\overline{\alpha}_ {t-\Delta t}} x_0 + \sqrt{1 - \overline{\alpha}_   {t-\Delta t}} \varepsilon _{t-\Delta t}
$$

为了让去噪的随机性能够平滑地被去除，相对于原来的去噪方差 $\sigma_t^2 = \tilde{\beta}_t$，使用可调整的新的去噪方差 $\sigma_t^2$，然后我们将随机项进行重参数化

$$
\sqrt{1 - \overline{\alpha}_ {t-\Delta t}} \varepsilon_ {t-\Delta t}\to \sqrt{1 - \overline{\alpha}_ {t-\Delta t} - \sigma_t^2} \varepsilon_ {t} + \sigma_t \varepsilon
$$

其中 $\varepsilon_t$ 实际上会根据 $x_t$ 通过模型预测，可以写作 $\varepsilon_ {\theta}^{(t)}(x_t)$；而推断时 $x_0$ 是未知的，会使用一个预测的 $x_0$（去噪公式变换得到）代替

$$
x_0 \to \frac{x_t-\sqrt{1-\overline{\alpha}_ t}\varepsilon_ {\theta}^{(t)}(x_t)}{\sqrt{\overline{\alpha}_ t}} 
$$

于是原来的加噪公式就变成了如下的去噪公式的形式：

$$
    x_{t-\Delta t}
    = \sqrt{\overline{\alpha}_ {t-\Delta t}}
    \underbrace{
        \left( \frac{x_t-\sqrt{1-\overline{\alpha}_ t}\varepsilon_ {\theta}^{(t)}(x_t)}{\sqrt{\overline{\alpha}_ t}} \right)
    }_ {\text{“ predicted }x_0\text{”}}
    + \underbrace{
        \sqrt{1-\overline{\alpha}_ {t-\Delta t}-\sigma_ t^2}\varepsilon_ {\theta}^{(t)}(x_ t)
    }_ {\text{“direction pointing to }x_t\text{”}}
    + \underbrace{
        \sigma_ t \varepsilon
    }_ {\text{random noise}}
$$

> 详见 [Denoising Diffusion Implicit Models](http://arxiv.org/abs/2010.02502) 的公式 (12)

其中 $\sigma_t^2=\eta \tilde{\beta}_t$ 是去噪过程中的噪声方差，注意到有

- $\eta = 1$ 时，就等价于 DDPM 的去噪公式
- $\eta = 0$ 时，就是 DDIM 的去噪公式，不确定项 $\varepsilon_ t$ 不再存在
- $\eta \in (0, 1)$ 既不是 DDPM 也不是 DDIM

!!! abstract "DDIM denoising formula"
    $$
        x_{t-\Delta t}
        = \sqrt{\overline{\alpha}_{t-\Delta t}}
        \left(
            \frac{
                x_t - \sqrt{1-\overline{\alpha}_t}\varepsilon_{\theta}^{(t)}(x_t)
            } {
                \sqrt{\overline{\alpha}_t}
            }
        \right)
        +
        \sqrt{1-\overline{\alpha}_{t-\Delta t}}
        \varepsilon_{\theta}^{(t)}(x_t)
    $$

如果取 $\Delta t>1$，就可以实现跨步去噪了，除去 Markov 性的假设之后，这样的跨步去噪就显得合理了。DDIM 去噪公式中，随机性被完全去除，求解 SDE 实际变成了求解 ODE，从而可以用 ODE 的数值解法的视角去看待这种加速。

??? general "ODE 数值解法的简单回顾"

    对于以下 ODE 初值问题，其数值解法希望求取 $a=t_0<t_1<\cdots < t_n=b$ 这一系列离散点上的 $y$ 的值。往往迭代求取，从 $t_0$ 开始到 $t_n$。最简单的，如 Euler 方法，有 $y(t_{i+1})\approx y(t_i)+(t_{i+1}-t_i)f(t_n, y_n)$。

    $$
    \begin{cases}
        \frac{\mathrm d y}{\mathrm d t} = f(t, y), \quad t\in [a, b] \\
        y(a)=\alpha
    \end{cases}
    $$

!!! tip "Remark"
    - DDPM 的去噪本质上是在求解一个 reverse SDE，该 reverse SDE 的整体过程刻画了数据的**联合概率分布** $p(\bm x, y)$
    - 但是实际上，我们实际只想要得到给定 $y$ 时的 $\bm x$，即我们关心的只是**边缘概率分布** $p(\bm x|y)$
    - DDIM 所求解的 ODE，实际上只是在边缘概率分布 $p(\bm x|y)$ 的意义上与原始的 SDE 相等，但由于这正是我们唯一关心的内容，因此确实只需要求解该 ODE 即可
    - 需要注意的是，训练时加噪最大步数仍然是 $T$，只会在推断去噪时使用 DDIM 的去噪公式加速。DDIM 论文的实验中，$1000$ 步去噪 DDIM 的生成质量还是略微不如 $1000$ 步去噪 DDPM，但是 $10, 20, 50, 100$ 步推断 DDIM 的生成质量会比 DDPM 高，尤其 $50, 100$ 步的生成质量实际上已经可以接受

## DDIM Inversion

[Diffusion Models Beat GANs on Image Synthesis](http://arxiv.org/abs/2105.05233) 最早给出了无条件扩散模型的 DDIM 反演 (inversion) 的方法。令上文中的 $\eta=1$，就有 DDIM 的确定去噪公式：

$$
x_{t-1} - x_t = \sqrt{\overline{\alpha}_{t-1}} \left[
    \left( \sqrt{\frac{1}{\overline{\alpha}_{t}}} - \sqrt{\frac{1}{\overline{\alpha}_{t-1}}} \right) x_t
    + \left( \sqrt{\frac{1}{\overline{\alpha}_{t-1}} - 1} - \sqrt{\frac{1}{\overline{\alpha}_{t}} - 1} \right) \varepsilon_{\theta}^{(t)}(x_t)
\right]
$$

??? general "Proof"
    random noise 项归 0，而 direction pointing to $x_t$ 项变换如

    $$
    \begin{aligned}
        \sqrt{1-\overline{\alpha}_{t-1}}\varepsilon_{\theta}^{(t)}(x_t)
        &= \sqrt{\overline{\alpha}_{t-1}} \cdot \sqrt{\frac{1}{\overline{\alpha}_{t-1}}-1} \cdot \varepsilon_{\theta}^{(t)}(x_t)\\
    \end{aligned}
    $$

    predicted $x_0$ 项与 $\sqrt{\overline{\alpha}_{t-1}}$ 相乘，变形为

    $$
    \sqrt{\overline{\alpha}_{t-1}} \left[\sqrt{\frac{1}{\overline{\alpha}_ t}}x_t
    - \sqrt{\frac{1}{\overline{\alpha}_ t}-1}\cdot \varepsilon_ {\theta}^{(t)}(x_t)\right]
    $$

在 [Diffusion Models Beat GANs on Image Synthesis](http://arxiv.org/abs/2105.05233) 的附录 F 中，认为在小步长的前提下，可以用以下公式进行 DDIM 反演：

$$
x_{t+1} - x_t = \sqrt{\overline{\alpha}_{t+1}} \left[
    \left( \sqrt{\frac{1}{\overline{\alpha}_{t}}} - \sqrt{\frac{1}{\overline{\alpha}_{t+1}}} \right) x_t
    + \left( \sqrt{\frac{1}{\overline{\alpha}_{t+1}} - 1} - \sqrt{\frac{1}{\overline{\alpha}_{t}} - 1} \right) \varepsilon_{\theta}^{(t)}(x_t)
\right]
$$

显然这样直接的反演会导致相当的误差，无法反演回到原图。

> 在 2023 年我第一次写这篇笔记的时候，找到了一篇对 DDIM 反演进行了一定改进的参考工作 [Null-text Inversion for Editing Real Images using Guided Diffusion Models](http://arxiv.org/abs/2211.09794)