<link rel="stylesheet" href="../../../css/counter.css" />

# Elucidating the Design Space of Diffusion-Based Generative Models

!!! info "References: [Elucidating the Design Space of Diffusion-Based Generative Models](http://arxiv.org/abs/2206.00364), NeurIPS 2022 Outstanding Paper"

!!! warning "本页面还在建设中"

## Sampling

在此直接给出 [EDM](http://arxiv.org/abs/2206.00364) 中统一的前向 ODE 公式，详细推导见 [SDE/ODE Formulation](DE-formula.md)

$$
\frac{\mathrm{d}x}{\mathrm{d}t}
= \frac{\dot{s}(t)}{s(t)} x - s^2(t)\dot{\sigma}(t)\sigma(t) \nabla_x \log p_{\sigma \text{data}}\left(\frac{x}{s(t)}\right)
$$

这里通过**加噪转移核定**义了缩放因子 $s(t)$ 和（不带缩放的）加噪 schedule 标准差 $\sigma(t)$：

$$
\begin{gathered}
    p_{0t}(x(t)\mid x(0)) = \mathcal{N}\left(
        s(t)x(0), s^2(t) \sigma^2 I
    \right)
\end{gathered}
$$

> 注意加噪转移核条件分布 $p(x_t\mid x_0)$ 和加噪边缘分布 $p(x_t)$ 不一样

它们和经典的 $\mathrm{d}x = f(t)x\mathrm{d}t + g(t)\mathrm{d}w$ 之间存在关系

$$
\begin{gathered}
    s(t) = \exp\left(\int_0^t f(\xi) \mathrm{d}\xi\right), \quad
    \sigma^2(t) = \int_0^t \frac{g^2(\eta)}{s^2(\eta)} \mathrm{d}\eta, \\
    f(t) = \frac{\dot{s}(t)}{s(t)}, \quad
    g(t) = s(t)\sqrt{2\dot{\sigma}(t)\sigma(t)}, \\
\end{gathered}
$$

当限定反向去噪过程为 ODE 求解时，就可以直接从预定义的前向过程获得，因此 $s(t)$ 和 $\sigma(t)$ 代替之前的 $f(t)$ 和 $g(t)$ 定义了这个反向过程。除此之外，推理 sampling 时的 ODE 求解器和 timesteps 的选择当然也非常重要。

!!! abstract "Summary for sampling: 4 design choices"
    - $s(t)$: scaling factor, 缩放因子
    - $\sigma(t)$: noise schedule, 加噪 schedule
    - ODE solver: 反向去噪过程的 ODE 数值求解器
    - timesteps: 反向去噪过程的采样的离散时间步

!!! tip "Sampling in practice"
    实践中，我们采样时实际上求解的 ODE 为

    $$
    \frac{\mathrm{d}x}{\mathrm{d}t}
    = \left(
        \frac{
            \dot{\sigma}(t)
        } {
            \sigma(t)
        }
        + \frac{
            \dot{s}(t)
        } {
            s(t)
        }
    \right)x
    - \frac{
        \dot{\sigma}(t)s(t)
    }{
        \sigma(t)
    } D_{\theta} \left(
        \frac{x}{s(t)}; \sigma(t)
    \right)
    $$

    ??? general "Proof"
        定义代换 $x:=s(t)\hat{x}$，则有

        $$
            \nabla_x \log p_{\sigma \text{data}}\left(
                \frac{x}{s(t)}
            \right)
            = \nabla_{s(t)\hat{x}} \log p_{\sigma \text{data}}\left(
                \hat{x}
            \right)
            = \frac{1}{s(t)} \nabla_{\hat{x}} \log p_{\sigma \text{data}}\left(
                \hat{x}
            \right)
        $$

        再利用下一节将得到的 score function 与 Denoiser 之间的关系，我们可以得到

        $$
            \nabla_x \log p_{\sigma \text{data}}\left(
                \frac{x}{s(t)}
            \right) = \frac{1}{
                s(t)\sigma^2(t)
            } \left(
                D_{\theta}\left(
                    \frac{x}{s(t)}; \sigma(t)
                \right) - \frac{x}{s(t)}
            \right)
        $$

        代入到原本用 score function 表示的统一前向 ODE 即可得证。

## Denoising vs Score Matching

[Estimation of Non-Normalized Statistical Models by Score Matching](https://www.jmlr.org/papers/volume6/hyvarinen05a/hyvarinen05a.pdf) (JMLR2005) 提出了 score matching 方法来最小化数据分布 $p_{\text{data}}$ 和模型分布 $p_{\text{model}}$ 之间的 Fisher 散度，从而避免处理从模型输出到合法概率密度分布的归一化项。

> 这个说法出自 [Sliced Score Matching: A Scalable Approach to Density and Score Estimation](https://arxiv.org/abs/1905.07088), UAI2019

$$
\mathcal{L}(\theta) = \frac{1}{2} \mathbb{E}_{x\sim p_{\text{data}}}\left[
    \| s_{\text{model}}(x; \theta) - \nabla_x \log p_{\text{data}}(x) \|_2^2
\right]
$$

然而 [EDM](http://arxiv.org/abs/2206.00364) 采用的损失函数是基于加噪数据 $x+n$，对干净数据 $y$ 的直接预测，即

$$
    \mathcal{L}(D; \sigma)
    = \mathbb{E}_{y\sim p_{\text{data}}}
    \mathbb{E}_{n\sim\mathcal{N}(0, \sigma^2 I)}\left[
        \| D(y+n) - y \|_2^2
    \right]
$$

> 依然可以将 $\sigma$ 理解为噪声尺度

在 [EDM](http://arxiv.org/abs/2206.00364) 所定义的 score function $\nabla_x \log p_{\sigma \text{data}}\left(x\right)$ 下，可以证明该 score function 可以被 Denoiser $D$ 表示为：

$$
\nabla_x \log p_{\sigma \text{data}}\left(x\right) = \frac{D(x; \sigma) - x}{\sigma^2}
$$

> $p_{\sigma \text{data}} = p_{\text{data}} * \mathcal{N}(0, \sigma^2 I)$

!!! general "Proof"
    !!! warning "TBD"

## Preconditioning

> There are various known good practices for training neural networks in a supervised fashion. For example, it is advisable to keep input and output signal magnitudes fixed to, e.g., unit variance, and to avoid large variation in gradient magnitudes on a per-sample basis.

实践中，直接将 $D(x; \sigma)$ 建模为 $D_{\theta}(x; \sigma)$ 是不太好的，一般都会加 preconditioner，例如 [iDDPM](https://arxiv.org/abs/2102.09672), [DDIM](http://arxiv.org/abs/2010.02502), [SGM](http://arxiv.org/abs/2011.13456) 都采用了 $D_{\theta}(x;\sigma) = x - \sigma F_{\theta}(\cdot)$ 形式的 preconditioner。特别地，[EDM](http://arxiv.org/abs/2206.00364) 提出一种更统一的 preconditioner 形式：

$$
D_{\theta}(x; \sigma)
= c_{\text{skip}}(\sigma) x
+ c_{\text{\text{out}}}(\sigma) F_{\theta}(
    c_{\text{in}}(\sigma) x; c_{\text{noise}}(\sigma)
)
$$


!!! abstract "Summary for preconditioning: 4 design choices"
    - $c_{\text{skip}}(\sigma)$ 将 skip connection 模块化
    - $c_{\text{out}}(\sigma)$ 和 $c_{\text{in}}(\sigma)$ 分别控制输出和输入的缩放
    - $c_{\text{noise}}(\sigma)$ 控制作为网络条件的噪声尺度

## Training

结合前面初步的损失函数和 preconditioner，我们再加入 loss weighting $\lambda(\sigma)$，可以重新组织得到如下训练目标：

$$
\mathbb{E}_{\sigma, y, n} \left[
    \underbrace{
        \lambda(\sigma) c_{\text{out}}(\sigma)^2
    }_{\text{effective weight}}
    \left\|
        \underbrace{
            F_{\theta}\left(
                c_{\text{in}}(\sigma) \cdot (y + n); c_{\text{noise}}(\sigma)
            \right)
        }_{\text{network output}}
        -
        \underbrace{
            \frac{1}{c_{\text{out}}}
            \left(
                y
                - c_{\text{skip}}(\sigma) \cdot (y + n)
            \right)
        }_{\text{effective training target}}
    \right\|_2^2
\right]
$$

$\lambda(\sigma)$ 用于确定不同 noise level 的训练样本的损失函数项应该占多大的权重，具有类似作用的还有应当从什么分布中采样 $\sigma$。不同的现有方法在这两方面 (noise distribution & loss weighting) 有不同的设计，而 [EDM](http://arxiv.org/abs/2206.00364) 也给出了自己的方案。

!!! abstract "Summary for training: 2 design choices"
    - $\lambda(\sigma)$: loss weighting, 损失函数权重
    - $\sigma\sim p_{\text{train}}$: noise distribution, 训练时采样的噪声水平分布

## Design Choices

<figure style="text-align:center;">
    <img src="../../imgs/diffusion/edm-main-table-light.png#only-light" alt="edm-main-table-light" style="zoom:40%;" />
    <img src="../../imgs/diffusion/edm-main-table-dark.png#only-dark" alt="edm-main-table-dark" style="zoom:40%;" />
    <figcaption><small>
        Specific design choices employed by different model families in EDM unified framework.
    </small></figcaption>
</figure>

!!! warning "TBD"

### Variance Preserving

### Variance Exploding

### improved DDPM + DDIM

### EDM