<link rel="stylesheet" href="../../../css/counter.css" />

# Denoising Diffusion Implicit Models

## Denoising of DDIM

回顾原始 DDPM 的去噪，是通过 $p_{\theta}(x_{t-1}|x_t)$ 近似去噪转移核 $q(x_{t-1}|x_t)$，一步步去噪得到的。由于转移核服从高斯分布 $\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)$，因此实际上操作为

$$
x_{t-1} = \tilde{\mu}_t + \sqrt{\tilde{\beta}_t}\varepsilon_t
$$

$\varepsilon_t$ 导致去噪过程的每一步都具有一定的随机性，从而需要一步步去噪，加噪需要多少步（DDPM 中往往加噪 1000 步）去噪也需要多少步。这是非常耗时的，DDIM 的核心思想就是将 SDE 转化成 ODE，从而去噪的每一步都不再需要随机项，从而可以使用解 ODE 的加速方法加速。

对于以下 ODE 初值问题，其数值解法希望求取 $a=t_0<t_1<\cdots < t_n=b$ 这一系列离散点上的 $y$ 的值。往往迭代求取，从 $t_0$ 开始到 $t_n$。最简单的，如 Euler 方法，有 $y(t_{i+1})\approx y(t_i)+(t_{i+1}-t_i)f(t_n, y_n)$。

$$
\begin{cases}
    \frac{\mathrm d y}{\mathrm d t} = f(t, y), \quad t\in [a, b] \\
    y(a)=\alpha
\end{cases}
$$

为了让去噪的随机性能够平稳地被去除，相对于原来的去噪方差 $\tilde{\beta}_t$，使用新的去噪方差 $\sigma_t^2$。从加噪公式出发，

$$
x_ {t-1} = \sqrt{\overline{\alpha}_ {t-1}} x_0 + \sqrt{1 - \overline{\alpha}_   {t-1}} \varepsilon _{t-1}
$$

将随机项进行重参数化

$$
\sqrt{1 - \overline{\alpha}_ {t-1}} \varepsilon_ {t-1}\to \sqrt{1 - \overline{\alpha}_ {t-1} - \sigma_t^2} \varepsilon_ {t} + \sigma_t \varepsilon
$$

其中 $\varepsilon_t$ 实际上会根据 $x_t$ 通过模型预测，可以写作 $\varepsilon_ {\theta}^{(t)}(x_t)$；而推断时 $x_0$ 是未知的，会使用一个预测的 $x_0$（去噪公式变换得到）代替

$$
x_0 \to \frac{x_t-\sqrt{1-\overline{\alpha}_ t}\varepsilon_ {\theta}^{(t)}(x_t)}{\sqrt{\overline{\alpha}_ t}} 
$$

于是原来的加噪公式就变成了如下的去噪公式的形式：

$$
    x_{t-1} = \sqrt{\overline{\alpha}_ {t-1}}
    \underbrace{\left( \frac{x_t-\sqrt{1-\overline{\alpha}_ t}\varepsilon_ {\theta}^{(t)}(x_t)}{\sqrt{\overline{\alpha}_ t}} \right)}_ {\text{“ predicted }x_0\text{”}}
    + \underbrace{\sqrt{1-\overline{\alpha}_ {t-1}-\sigma_ t^2}\varepsilon_ {\theta}^{(t)}(x_ t)}_ {\text{“direction pointing to }x_t\text{”}}
    + \underbrace{\sigma_ t \varepsilon_ t}_ {\text{random noise}}
$$

其中 $\sigma_t^2=\eta \tilde{\beta}_t$ 是去噪过程中的噪声方差，注意到有

- $\eta = 1$ 时，就等价于 DDPM 的去噪公式
- $\eta = 0$ 时，就是 DDIM 的去噪公式，不确定项 $\varepsilon_ t$ 不再存在
- $\eta \in (0, 1)$ 既不是 DDPM 也不是 DDIM

注意到有

- DDPM 的去噪本质上是在求解一个 reverse SDE，该 reverse SDE 的整体过程刻画了数据的联合概率分布 $p(\bm x, y)$
- 但是实际上，我们实际只想要得到给定 $y$ 时的 $\bm x$，即我们关心的只是边缘概率分布 $p(\bm x|y)$
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

显然这样直接的反演会导致相当的误差，无法反演回到原图。目前对 DDIM 反演做得比较好的工作是 [Null-text Inversion for Editing Real Images using Guided Diffusion Models](http://arxiv.org/abs/2211.09794)。