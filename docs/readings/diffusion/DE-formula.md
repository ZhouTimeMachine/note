<link rel="stylesheet" href="../../../css/counter.css" />

# SDE/ODE Formulation

!!! info "References"
    - [Elucidating the Design Space of Diffusion-Based Generative Models](http://arxiv.org/abs/2206.00364), NeurIPS 2022 Outstanding Paper
    - [Score-Based Generative Modeling through Stochastic Differential Equations](http://arxiv.org/abs/2011.13456), ICLR 2021 Oral

## SDE/ODE Formulation in SGM

[Score-Based Generative Modeling through Stochastic Differential Equations](http://arxiv.org/abs/2011.13456) (SGM) 给出了如下用于描述前向扩散过程的 SDE 公式：

$$
\mathrm{d}x = f(x, t) \mathrm{d}t + g(t) \mathrm{d}w_t
$$

其中

- $w_t$: 标准维恩过程 (standard Wiener process)
- $f(x, t)$: $\mathbb{R}^{d+1}\to \mathbb{R}^d$, 漂移系数 (drift coefficient)
- $g(t)$: $\mathbb{R}\to\mathbb{R}$, 扩散系数 (diffusion coefficient)

在 VP (Variational Preserving) 和 VE (Variational Exploding) SDE 中都有 $f(x, t)=f(t)x$, $f(\cdot): \mathbb{R}\to\mathbb{R}$，这种情况下前向 SDE 重写为

$$
\mathrm{d}x = f(t)x \mathrm{d}t + g(t) \mathrm{d}w_t
$$

!!! abstract "SGM 中的命名"
    在 SGM 中，VE 的 SDE 形式为原论文公式 (9)：

    $$
    \mathrm{d}x = \sqrt{
        \frac{
            \mathrm{d}[\sigma^2(t)]
        } {
            \mathrm{d}t
        }
    }\mathrm{d}w
    $$

    VP 的 SDE 形式为原论文公式 (11)：

    $$
    \mathrm{d}x = -\frac{1}{2} \beta(t)x \mathrm{d}t + \sqrt{\beta(t)} \mathrm{d}w
    $$

    > [Score-Based Generative Modeling through Stochastic Differential Equations](http://arxiv.org/abs/2011.13456) 中对应的原文：
    > 
    > Interestingly, the SDE of Eq. (9) always gives a process with **exploding variance** when $t\to \infty$, whilst the SDE of Eq. (11) yields a process with a **fixed variance** of one when the initial distribution has unit variance (proof in Appendix B).
    > 
    > VE 对应的是 Langevin Dynamics，VP 对应的是 DDPM，推导的细节需要一点小量分析技术，详见 SGM 论文附录 B
    
    而 SGM 所提出的加噪形式为一种 sub-VP，即

    $$
    \mathrm{d}x = -\frac{1}{2} \beta(t)x \mathrm{d}t + \sqrt{\beta(t)(1 - e^{-2\int_0^t\beta(s)\mathrm{d}s})} \mathrm{d}w
    $$

接下来我们需要解这个 SDE，想要得到加噪转移核函数 $p_{0t}(x(t)\mid x(0))$。设均值 $m(t) = \mathbb{E}[x(t)]$，协方差 $Cov(t) = \mathbb{E}[(x(t)-m(t))(x(t)-m(t))^{\top}]$，则根据 SDE 理论有：

$$
\begin{aligned}
    m(t) &= s(t)x(0), \quad s(t) = \exp\left(\int_0^t f(\xi) \mathrm{d}\xi \right) \\
    Cov(t) &= \left[
        s^2(t) \int_0^t \frac{g^2(\eta)}{s^2(\eta)}\mathrm{d}\eta
    \right] I
\end{aligned}
$$

> Eqs. (5.50) and (5.51) in Simo Särkkä and Arno Solin. [Applied stochastic differential equations](https://www.cambridge.org/core/books/applied-stochastic-differential-equations/6BB1B8B0819F8C12616E4A0C78C29EAA), volume 10. Cambridge University Press, 2019.

??? general "Details"
    针对 SDE

    $$
    \frac{
        \mathrm{d}x
    } {
        \mathrm{d}t
    } = f(x, t) + L(x, t) w(t)
    $$

    - $w(t)\in \mathbb{R}^{d_w}$: 均值为 0，谱密度矩阵为 $Q$ 的白噪声过程。
    - $L(x, t)\in \mathbb{R}^{d\times {d_w}}$

    !!! info "白噪声 (white noise)"
        白噪声过程 $w(t)\in \mathbb{R}^S$ 是一个具有以下性质的随机函数：
        
        1. 当 $t\neq t'$ 时，$w(t)$ 和 $w(t')$ 相互独立
        2. 从 $t$ 到 $w(t)$ 的映射是一个高斯过程，具有 zero mean 和 Dirac delta correlation
        
        $$
        \begin{aligned}
            m_w(t) &= \mathbb{E}[w(t)] = 0 \\
            C_w(t, s) &= \mathbb{E}[w(t)w^{\top}(s)] = \delta(t-s)Q
        \end{aligned}
        $$

        其中 $Q$ 是过程的谱密度 (spectral density)。具有常数谱密度是白噪声过程的特征。
    
    根据 *Applied stochastic differential equations* Eqs. (5.50) and (5.51) 有

    $$
    \begin{aligned}
        \frac{
            \mathrm{d} m(t)
        } {
            \mathrm{d}t
        } &= \mathbb{E}[f(x, t)] \\
        \frac{
            \mathrm{d} Cov(t)
        } {
            \mathrm{d}t
        } &= \mathbb{E}[f(x, t)(x-m)^{\top}] + \mathbb{E}[(x-m)f^{\top}(x, t)] + \mathbb{E}[L(x, t)QL^{\top}(x, t)]
    \end{aligned}
    $$

    根据 *Applied stochastic differential equations* Eqs. (5.52) and (5.53)，由于有 $\mathbb{E}[\mathbb{E}[f(x, t)](x-m)^{\top}]=0$，有

    $$
    \mathbb{E}[f(x, t)(x-m)^{\top}]=\mathbb{E}[(f(x, t) - \mathbb{E}[f(x, t)])(x-m)^{\top}]
    $$

    对于高斯噪声 $Q = I$，而我们现在有 $f(x, t) = f(t)x$ 和 $L(x, t) = g(t)I$, $d_w=d$，因此

    $$
    \begin{aligned}
        \frac{
            \mathrm{d} m(t)
        } {
            \mathrm{d}t
        } &= f(t)\mathbb{E}[x] = f(t)m(t) \\
        \frac{
            \mathrm{d} Cov(t)
        } {
            \mathrm{d}t
        } &= \mathbb{E}[f(t)(x-m)(x-m)^{\top}] + \mathbb{E}[(x-m)(x-m)^{\top}f(t)] + g^2(t)I \\
        &= 2f(t)Cov(t) + g^2(t)I \\
    \end{aligned}
    $$

    解关于 $m(t)$ 的一阶齐次线性 ODE 有

    $$
    m(t) = m(0)\exp\left(\int_0^t f(\xi) \mathrm{d}\xi \right)
    $$

    > $m(0)=x(0)$

    解关于 $Cov(t)$ 的一阶非齐次线性 ODE 有

    $$
    \begin{aligned}
        Cov(t)
        &= \left[
            \exp\left(
                \int_0^t 2f(\xi) \mathrm{d} \xi
            \right)
            \int_0^t g^2(\eta)
            \exp\left(
                -\int_0^{\eta} 2f(\xi) \mathrm{d}\xi
            \right)
            \mathrm{d}\eta
        \right] I \\
        &= \left[
            s^2(t) \int_0^t \frac{g^2(\eta)}{s^2(\eta)}\mathrm{d}\eta
        \right] I
    \end{aligned}
    $$

由此我们可以得到

$$
\begin{gathered}
    p_{0t}(x(t)\mid x(0)) = \mathcal{N}\left(
        s(t)x(0), s^2(t) \sigma^2 I
    \right) \\
    s(t) = \exp\left(\int_0^t f(\xi) \mathrm{d}\xi \right), \quad
    \sigma^2(t) = \int_0^t \frac{g^2(\eta)}{s^2(\eta)}\mathrm{d}\eta
\end{gathered}
$$

根据全概率公式，加噪边缘分布可以通过对加噪转移核在 $x(0)$ 上积分得到：

$$
p_t(x) = \int p_{0t}(x\mid x_0)p_{\text{data}}(x_0)\mathrm{d}x_0
$$

> $p_t(x, x_0)=p_{0t}(x\mid x_0)p_{\text{data}}$

用 $*$ 表示概率分布的卷积算子，可以证明有

$$
p_t(x) = s(t)^{-d} p_{\sigma \text{data}} \left(
    \frac{x}{s(t)}
\right),\quad p_{\sigma \text{data}}=p_{\text{data}} * \mathcal{N}(0, \sigma^2 I)
$$

这个式子很形象地展示了从原始数据分布和加噪数据分布之间的关系。

??? general "Proof"
    注意到有

    $$
    \begin{aligned}
        p_{0t}(x\mid x_0)
        &= \mathcal{N}\left(
            x; s(t)x_0, s^2(t) \sigma^2 I
        \right) \\
        &= \frac{1}{
                \sqrt{(2\pi)^{d} \cdot [s^2(t)\sigma^2]^{d}}
            } \exp \left(
            -\frac{1}{2}\cdot \frac{
                [x - s(t)x_0]^{\top}\cdot [x - s(t)x_0]
            }{
                s^2(t)\sigma^2
            }
        \right) \\
        &= s(t)^{-d} \frac{1}{
                \sqrt{(2\pi)^{d}}
            } \exp \left(
            -\frac{1}{2\sigma^2}\cdot
            \left[
                \frac{x}{s(t)} - x_0
            \right]^{\top} \cdot \left[
                \frac{x}{s(t)} - x_0
            \right]
        \right) \\
        &= s(t)^{-d} \mathcal{N}\left(
            \frac{x}{s(t)}-x_0; 0, \sigma^2 I
        \right)
    \end{aligned}
    $$

    所以

    $$
    \begin{aligned}
        p_t(x)
        &= \int p_{0t}(x\mid x_0)p_{\text{data}}(x_0)\mathrm{d}x_0 \\
        &= s(t)^{-d} \int \mathcal{N}\left(
            \frac{x}{s(t)}-x_0; 0, \sigma^2 I
        \right)p_{\text{data}}(x_0)\mathrm{d}x_0 \\
        &= s(t)^{-d} p_{\sigma \text{data}} \left(
            \frac{x}{s(t)}
        \right),\quad p_{\sigma \text{data}}=p_{\text{data}} * \mathcal{N}(0, \sigma^2 I)
    \end{aligned}
    $$

!!! info "概率分布的卷积"
    > Reference: [Convolution of probability distributions - Wikipedia](https://en.wikipedia.org/wiki/Convolution_of_probability_distributions)，这里仅讨论连续随机变量

    两个或多个独立随机变量之和的概率分布是它们各个分布的卷积。具体而言，对连续随机变量 $Z=X+Y$ 有

    $$
    p_Z(z) = \int_{-\infty}^{\infty} p_{XY}(x, z-x)\mathrm{d}x
    $$

    如果 $X, Y$ 相互独立，那么就有 $p_{XY}(x, y) = p_X(x)p_Y(y)$，因此有

    $$
    p_Z(z) = \int_{-\infty}^{\infty} p_X(x)p_Y(z-x)\mathrm{d}x
    $$

    我们就可以把 $p(z)$ 记为 $p_X * p_Y$。

从 Markov 的 DDPM 到 non-Markov 的 DDIM，需要保持的就是加噪边缘分布 $p_t(x)$ 的一致性，这样就可以做到跨步去噪。[SGM](http://arxiv.org/abs/2011.13456) 就在加噪边缘分布恒定的条件下，利用 Fokker-Planck 方程导出了和原始 SDE 保持加噪边缘分布一致性的概率流 ODE：

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = f(t)x - \frac{1}{2}g^2(t) \nabla_x \log p_t(x)
$$

??? general "根据 F-P 方程导出概率流 ODE"
    来自[生成扩散模型漫谈（六）：一般框架之ODE篇 - 科学空间](https://spaces.ac.cn/archives/9228)，苏剑林的该文给出的推导和 [SGM](http://arxiv.org/abs/2011.13456) 的附录 D.1 是一致的，且更容易理解。
    
    > 在 [SGM](http://arxiv.org/abs/2011.13456) 的附录 D.1 中，作者表示该推导是 [Interacting particle solutions of fokker-planck equations through gradient-log-density estimation](https://arxiv.org/pdf/2006.00702) 中 idea 的简化版。
    
    首先需要引入 Fokker-Planck 方程：
    
    $$
    \frac{\partial p_t(x)}{\partial t} = -\nabla_x \left[ f(x, t) p_t(x)\right] + \frac{1}{2}g^2(t) \nabla_x \cdot \nabla_x p_t(x) 
    $$

    为了方便，我们将记 $f(x, t)=f_t(x)$, $g(t)=g_t$，这样就可以在下标的层次关注变量 $t$，在自变量的层次关注变量 $x$。

    ??? general "Proof of F-P equation"
        首先我们的目标是 $p_t(x)$，为了使用期望这一强大工具，需要将其转化为期望形式——利用 Dirac delta function:
        
        $$
        p(x) = \mathbb{E}_y[\delta(x - y)]
        = \int \delta(x - y)p(y)\mathrm{d}y
        $$

        > 注意 Dirac delta function 的一个不严格的描述是 $\delta(x)=\begin{cases}
        0, & x\neq 0 \\
        \infty, & x=0
        \end{cases}$
        
        给出前向 SDE 的离散形式：

        $$
        x_{t+\Delta t} = x_t + f_t(x_t)\Delta t + g_t\sqrt{\Delta t}\varepsilon, \quad \varepsilon\sim\mathcal{N}(0, I)
        $$

        对于维恩过程，$\mathrm{d}w \approx \sqrt{\mathrm{d} t}$。可以发现这个离散形式和 Langevin Dynamics 的形式一致：
        
        $$
        x_{i+1} = x_i + \varepsilon\nabla_x\log p(x) + \sqrt{2\varepsilon}z_i, \quad z_i\sim\mathcal{N}(0, I)
        $$

        在前向 SDE 的离散形式下，我们有

        $$
        \begin{aligned}
            \delta(x - x_{t+\Delta t})
            =& \delta\left(x - \left(x_t + f_t(x_t)\Delta t + g_t\sqrt{\Delta t}\varepsilon\right)\right) \\
            \approx& \delta(x - x_t) - \left(f_t(x_t)\Delta t + g_t\sqrt{\Delta t}\varepsilon\right)\cdot \nabla_x\delta(x - x_t) \\
            &+ \frac{1}{2}\left(g_t\sqrt{\Delta t}\varepsilon\cdot \nabla_x\right)^2\delta(x - x_t)
        \end{aligned}
        $$

        > 对 $\delta$ 像普通函数一样做泰勒展开，只保留到 $O(\Delta t)$，舍去了 $O(\Delta t^{3/2})$ 及更高阶项

        两边取期望，有

        $$
        \begin{aligned}
            &p_{t+\Delta t}(x) \\
            \approx&
                p_{t}(x)
                - \mathbb{E}_{x_{t}, \varepsilon}\left[
                    \left(
                        { \color{red} f_t(x_t)\Delta t }
                        + 
                        { \color{purple} g_t\sqrt{\Delta t}\varepsilon }
                    \right)
                    \cdot \nabla_x\delta(x - x_t)
                \right]\\
            &+ { \color{skyblue}
                \frac{1}{2}\mathbb{E}_{x_t, \varepsilon}\left[
                    g^2_t\Delta t\varepsilon^2
                    \nabla_x \cdot \nabla_x \delta(x - x_t)
                \right]
            } \\
            =& p_{t}(x) - {\color{red}
                \Delta t\mathbb{E}_{x_{t}}\left[
                    f_t(x_t)
                    \cdot \nabla_x\delta(x - x_t)
                \right]
            } + { \color{skyblue}
                \frac{1}{2}g^2_t\Delta t
                \nabla_x\cdot \nabla_x p_t(x)
            }
        \end{aligned}
        $$

        > ${\color{purple} \mathbb{E}_{\varepsilon}\varepsilon=0}$, ${\color{skyblue} \mathbb{E}_{\varepsilon}\varepsilon^2}={\color{skyblue} \operatorname{Var}(\varepsilon)} + ({\color{purple} \mathbb{E}_{\varepsilon}\varepsilon})^2={\color{skyblue} I}$

        将 $p_t$ 移到左侧，两侧同除以 $\Delta t$，并取极限 $\Delta t\to 0$，有

        $$
        \frac{\partial p_t(x)}{\partial t} =
        - { \color{red}
            \mathbb{E}_{x_{t}}\left[
                f_t(x_t)
                \cdot \nabla_x\delta(x - x_t)
            \right]
        }
        + { \color{skyblue}
            \frac{1}{2}g^2_t 
            \nabla_x \cdot \nabla_x p_t(x)
        }
        $$

        由于

        $$
        p(x)f_t(x)
        = \int \delta(x - y)p(y)f_t(y)\mathrm{d}y
        = {\color{orange} \mathbb{E}_y[\delta(x - y)f_t(y)]}
        $$

        有

        $$
        \nabla_x[p(x)f_t(y)]
        = \mathbb{E}_y[\nabla_x(\delta(x - y)f_t(y))]
        = {\color{red} \mathbb{E}_y[f_t(y)\nabla_x\delta(x - y)]}
        $$

        于是得到 Fokker-Planck 方程：

        $$
        \frac{\partial p_t(x)}{\partial t} =
        - { \color{red}
            \nabla_x \left[ f_t(x) p_t(x)\right]
        } + { \color{skyblue}
            \frac{1}{2}g^2_t \nabla_x \cdot \nabla_x p_t(x)
        }
        $$
    
    对于任意满足 $\tilde{g}_t^2\leqslant g_t^2$ 的 $\tilde{g}_t^2$，我们可以将 Fokker-Planck 方程重写为

    $$
    \begin{aligned}
        \frac{\partial p_t(x)}{\partial t}
        &= - \nabla_x\cdot \left[
            f_t(x) p_t(x)
            - \frac{1}{2}(g_t^2 - \tilde{g}_t^2)\nabla_x p_t(x)
        \right] + 
        \frac{1}{2}\tilde{g}^2_t
        \nabla_x \cdot \nabla_x p_t(x) \\
        &= - \nabla_x\cdot \left[
            \left(
                f_t(x)
                - \frac{1}{2}(g_t^2 - \tilde{g}_t^2)\nabla_x \log p_t(x)
            \right) p_t(x)
        \right] + 
        \frac{1}{2}\tilde{g}^2_t
        \nabla_x \cdot \nabla_x p_t(x) \\
    \end{aligned}
    $$

    > $\nabla_x \log p_t(x) = [\nabla_x p_t(x)] / p_t(x)$

    仍从 F-P 方程的角度看，上式直接对应的前向 SDE 为

    $$
    \mathrm{d}x = \tilde{f}_t(x)\mathrm{d}t + \tilde{g}_t \mathrm{d}w,\quad
    \tilde{f}_t(x) = f_t(x) - \frac{1}{2}(g_t^2 - \tilde{g}_t^2)\nabla_x \log p_t(x)``
    $$

    令 $\tilde{g}_t\equiv 0$ 时，该前向 SDE 就退化为 ODE，且保持边缘分布 $p_t(x)$ 不变，因此得证

    > $\tilde{g}_t = g_t$ 时，就是原始的前向 SDE。在 [DDIM](http://arxiv.org/abs/2010.02502) 中，作者令 $\tilde{g}_t=\eta g_t$，$\eta=0$ 时为 DDIM，$\eta=1$ 时为 DDPM。
    >
    > $\tilde{g}_t = 0$ 时，F-P 方程退化，又称为连续性方程 (continuity equation)

$f$ 和 $g$ 在确定前向过程的时候就已经定义好了，因此模型只需要学 $\nabla_x \log p_t(x)$，也就是 score function。

## ODE Formulation in EDM

从前面的表示中，我们发现其实可以用 $s(t), g(t)$ 来代替 $f(t), g(t)$ 的形式，具体地我们可以得到

$$
f(t) = \frac{\dot{s}(t)}{s(t)},\quad g(t) = s(t) \sqrt{2\dot{\sigma}(t)\sigma(t)}
$$

??? general "Proof"
    对于 $f(t)$，根据 $s(t) = \exp\left(\int_0^t f(\xi) \mathrm{d}\xi \right)$ 有

    $$
    f(t)
    = \frac{\mathrm{d}}{\mathrm{d}t} \int_0^t f(\xi) \mathrm{d}\xi
    = \frac{\mathrm{d} \log s(t)}{\mathrm{d}t} 
    = \frac{\dot{s}(t)}{s(t)}
    $$

    而对于 $g(t)$，根据 $\sigma^2(t) = \int_0^t \frac{g^2(\eta)}{s^2(\eta)}\mathrm{d}\eta$ 两边对 $t$ 求导有

    $$
    2\sigma(t)\dot{\sigma}(t) = \frac{g^2(t)}{s^2(t)}
    \;\Rightarrow\; g(t) = s(t) \sqrt{2\dot{\sigma}(t)\sigma(t)}
    $$

由此我们可以把 [SGM](http://arxiv.org/abs/2011.13456) 所得到的概率流 ODE 重写为

$$
\frac{\mathrm{d}x}{\mathrm{d}t}
= \frac{\dot{s}(t)}{s(t)}\cdot x - \frac{1}{2} \left[s^2(t)\cdot 2\dot{\sigma}(t)\sigma(t)\right]\cdot  \nabla_x \log p_t(x)
= \frac{\dot{s}(t)}{s(t)} x - s^2(t)\dot{\sigma}(t)\sigma(t) \nabla_x \log p_t(x)
$$

将 $p_t(x)$ 用 $p_{\sigma \text{data}}$ 表示有

$$
\nabla_x \log p_t(x)
= \nabla_x \left[\log \frac{1}{s(t)} + \log p_{\sigma \text{data}}\left(\frac{x}{s(t)}\right) \right]
= \nabla_x \log p_{\sigma \text{data}}\left(\frac{x}{s(t)}\right)
$$

即

$$
\frac{\mathrm{d}x}{\mathrm{d}t}
= \frac{\dot{s}(t)}{s(t)} x - s^2(t)\dot{\sigma}(t)\sigma(t) \nabla_x \log p_{\sigma \text{data}}\left(\frac{x}{s(t)}\right)
$$

特别地，如果就令前向过程有 $s(t)=1$，那么就有 [EDM](http://arxiv.org/abs/2206.00364) 中的加噪 ODE 形式：

$$
\frac{\mathrm{d}x}{\mathrm{d}t}
= -\dot{\sigma}(t)\sigma(t) \nabla_x \log p_{\sigma \text{data}}\left( x \right)
$$

$\nabla_x \log p_{\sigma \text{data}}\left( x \right)$ 也就成为 [EDM](http://arxiv.org/abs/2206.00364) 中建模的 score function。