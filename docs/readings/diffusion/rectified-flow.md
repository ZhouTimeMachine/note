<link rel="stylesheet" href="../../../css/counter.css" />

# Rectified Flow

!!! info "References"
    - [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](http://arxiv.org/abs/2209.03003), ICLR2023 Spotlight

!!! warning "该页面还在建设中"

## Overview

数据分布为 $p(x_0)$，先验分布为 $p(x_1)$（常为标准正态分布），我们需要在这两个分布之间构建映射。简而言之，Rectified Flow 通过

$$
\min_{\theta} \int_0^1 \mathbb{E}_{x_0, x_1}\left[\left\|(x_1 - x_0) - v_{\theta}(x_t, t)\right\|^2\right]\mathrm{d}t,\quad x_t = (1-t)x_0 + tx_1
$$

学习一个向量场 $v_{\theta}(x_t, t)$。这个向量场是为了刻画 Rectified Flow 所想要的一个良定义 (well-defined) 的 ODE:

$$
\frac{\mathrm{d}z_t}{\mathrm{d}t} = v(z_t, t)
$$

其中 $p(z_0)=p(x_0)$，$p(z_1)=p(x_1)$。给定 $z_0=x_0$，可以通过解这个 ODE 得到 $z_1$。

!!! tip "直观理解"
    直观来看，$x_0$ 和 $x_1$ 是相互独立的，而 $z_0$ 和 $z_1$ 存在因果关系，即从 $x_0$ 和 $x_1$ 学到 $\{z_t\}_{[0, 1]}$ —— 即，我们称 $\{z_t\}_{[0, 1]}$ 是从 $\{x_t\}_{[0, 1]}$ 中诱导的 **Rectified Flow**。

## Marginal Preserving

正如 DDIM 从 Markov 到 non-Markov 需要保证边缘分布 $p(x_t)$ 不变，Rectified Flow 希望“走直线”，也需要保证边缘分布不变：

$$
p(z_t) = p(x_t), \quad \forall t \in [0, 1]
$$

> 从希望高质量地跨步去噪的角度来看，Rectified Flow 和 DDIM 都希望保证边缘分布不变的这一点达成了一致

??? tip "probability density function v.s. probability law"
    [原论文](http://arxiv.org/abs/2209.03003)使用 **Law** 而不是**概率密度函数**进行描述，对于两者之间的区别，我截取了 [wikipedia Random variable 词条](https://en.wikipedia.org/wiki/Random_variable)中的一段：

    In measure-theoretic terms, we use the random variable $X$ to "push-forward" the measure $P$ on $\Omega$ to a measure $p_{X}$ on $\mathbb {R}$. The measure $p_{X}$ is called the "(probability) distribution of $X$" or the "law of $X$". The density $f_{X}=\mathrm{d}p_{X}/\mathrm{d}\mu$, the [Radon–Nikodym derivative](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem#Radon%E2%80%93Nikodym_derivative) of $p_{X}$ with respect to some reference measure $\mu$ on $\mathbb {R}$ (often, this reference measure is the Lebesgue measure in the case of continuous random variables, or the counting measure in the case of discrete random variables).

    也就是说，Law 只是将概率测度 $P: \Omega\to \mathbb{R}$ 变换到了 $p_X: \mathcal{B}(\mathbb{R})\to \mathbb{R}$，两者意义相近

    > $\mathcal{B}(\mathbb{R})$ 是 $\mathbb{R}$ 上的 Borel 集，$\mathbb{R}$ 上最小的 $\sigma$-algebra，由所有开集构成

    !!! info "probability law of a random variable"
        对概率空间 $(\Omega, \mathcal{F}, P)$ 上的随机变量 $X: \Omega \to \mathbb{R}$，我们定义其 probability law $p_{X}$ 为

        $$
        p_{X}(B) = P(X \in B), \quad \forall B \in \mathcal{B}(\mathbb{R})
        $$

    为了方便，我们假定讨论连续随机变量，直接使用概率密度函数描述概率分布

先引入必要的定义：

!!! info "Expected Velocity"
    对沿路径连续可微 (path-wise continuously differentiable) 的随机过程 $\{x_t\}_{[0, 1]}$，定义其期望速度 (expected velocity) 为

    $$
    v^x(x, t) = 
    \begin{cases}
        \mathbb{E}[\dot{x}_t | x_t = x], & x \in \mathrm{supp}(x_t) \\
        0, & \text{otherwise}
    \end{cases}
    $$

    > 随机变量的支撑集 (support) 可以认为是该随机变量所有可能值的闭包，例如对于离散随机变量就是 $\{x\in \mathbb {R} :P(X=x)>0\}$，对于连续随机变量就是 $\{x\in \mathbb {R} :f_{X}(x)>0\}$，详细可见 [Support (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Support_(mathematics)#In_probability_and_measure_theory)

!!! info "Rectifiable"
    当满足以下条件时，我们把随机过程 $\{x_t\}_{[0, 1]}$ 称为 **Rectifiable** 的

    1. $v^x$ 局部有界 (locally bounded)
    2. 通过如下积分式，可以解得唯一的 $z_t$（当然首先要存在）

    $$
    z_t = x_0 + \int_0^t v^x(z_s, s)\mathrm{d}s, \quad \forall t \in [0, 1], \quad z_0 = x_0
    $$

    由此，$\{z_t\}_{[0, 1]}$ 就称为从 $\{x_t\}_{[0, 1]}$ 中诱导的 **Rectified Flow**。

接下来正式地描述 Rectified Flow 的目标定理：边缘分布保持一致

!!! abstract "Marginal Preserving"
    假设 $\{x_t\}_{[0, 1]}$ 是 Rectifiable 的，而 $\{z_t\}_{[0, 1]}$ 是其 Rectified Flow，则

    $$
    p(z_t) = p(x_t), \quad \forall t \in [0, 1]
    $$

    > 原论文中是 $\mathrm{Law}(z_t) = \mathrm{Law}(x_t)$

??? general "Proof"
    将会使用测试函数法证明，首先简单介绍测试函数法。

    !!! abstract "测试函数法"
        [测试函数法推导连续性方程和 Fokker-Planck 方程 - 科学空间](https://spaces.ac.cn/archives/9461)中简单地给出了测试函数法的基本原理：如果对于任意函数 $\phi(x)$ 都成立

        $$
        \int f(x)\phi(x)\mathrm{d}x
        = \int g(x)\phi(x)\mathrm{d}x
        $$

        那么就成立 $f(x)=g(x)$，而 $\phi(x)$ 就被称为测试函数。

        > 然而还存在一些细节，$\phi(x)$ 的选取空间？等号的具体含义（如严格相等/几乎处处相等/依概率相等之类）？参考 [Weak solution - Wikipedia](https://en.wikipedia.org/wiki/Weak_solution#A_concrete_example)，可以发现取了紧支撑的光滑（连续可微）的测试函数，这和 Rectified Flow 中的假设一致。由于暂时没有找到测试函数法比较严谨权威的介绍页面，也只能先理解到这一步为止了。

    注意，在 [SGM](http://arxiv.org/abs/2011.13456) 中，边缘分布一致的证明是通过 Fokker-Planck 方程完成的，而实际上 Fokker-Planck 方程的推导也可以通过测试函数法完成（详见[测试函数法推导连续性方程和 Fokker-Planck 方程 - 科学空间](https://spaces.ac.cn/archives/9461)），因此在基本证明路径上其实是相似的。

    ??? general "测试函数法证明连续性方程 (continuity equation)"
        连续性方程作为 F-P 方程的特例，对应 ODE 情形，正如 [SGM](http://arxiv.org/abs/2011.13456) 利用 F-P 方程证明边缘分布一致一样，其实 Rectified Flow 也可以通过连续性方程去证明（正如原论文中所做）。
        
        在这里将测试函数法简单应用于连续性方程的证明（来自[测试函数法推导连续性方程和 Fokker-Planck 方程 - 科学空间](https://spaces.ac.cn/archives/9461)），首先阐明 ODE:
        
        $$
        \frac{\mathrm{d}x_t}{\mathrm{d}t} = f_t(x_t)
        $$
        
        泰勒展开、舍去高阶项：

        $$
        \phi(x_{t + \Delta t}) = \phi(x_t + f_t(x_t)\Delta t) \approx \phi(x_t) + \Delta t\cdot  f_t(x_t) \nabla_{x_t}\phi(x_t)
        $$

        两边取期望有

        $$
        { \color{red}
            \int \phi(x_{t + \Delta t}) p_{t + \Delta t}(x_{t + \Delta t})\mathrm{d}x_{t + \Delta t}
        } \approx 
        \int \left[
            { \color{orange} \phi(x_t) } + 
            { \color{skyblue}
                \Delta t\cdot  f_t(x_t) \nabla_{x_t}\phi(x_t)
            }
        \right] p_t(x_t)\mathrm{d}x_t
        $$

        注意到有

        $$
        \int \phi(x_{t + \Delta t}) p_{t + \Delta t}(x_{t + \Delta t})\mathrm{d}x_{t + \Delta t}
        = { \color{red}
            \int \phi(x_t) p_{t + \Delta t}(x_t)\mathrm{d}x_t
        }
        $$

        另一方面，根据分部积分有

        $$
        \int p_t(x_t) f_t(x_t) \nabla_{x_t}\phi(x_t) \mathrm{d}x_t
        = - {\color{skyblue}
            \int \nabla_{x_t}\left[p_t(x_t) f_t(x_t) \right] \phi(x_t)\mathrm{d}x_t
        }
        $$

        > 测试函数 $\phi$ 紧支撑，使得高维分部积分的面积积分项为零

        ??? abstract "高维空间分部积分"
            在高维空间中，分部积分的公式为
            
            $$
            \int _{\Omega} v\nabla u \mathrm{d}x = \int _{\partial\Omega} u v\cdot \hat{n} \mathrm{d}S - \int _{\Omega} u \nabla\cdot v \mathrm{d}x
            $$

            其中 $u$ 是关于 $x$ 的标量函数，$v$ 是关于 $x$ 的向量函数，而

            - $\Omega$: 积分区域, $\partial\Omega$ 为其边界
            - $\hat{n}$: 边界的外向单位法向量，$\mathrm{d}S$ 为边界上的面积微元

            ??? general "Proof"
                基于

                $$
                \nabla(u v) = u \nabla v + v \nabla u
                $$

                我们有 
                
                $$
                \int _{\Omega} v\nabla u \mathrm{d}x = \int _{\Omega} \nabla(u v) \mathrm{d}x - \int _{\Omega} u \nabla\cdot v \mathrm{d}x
                $$

                根据[高斯散度定理 (divergence theorem)](https://en.wikipedia.org/wiki/Divergence_theorem)，有

                $$
                \int _{\Omega} \nabla(u v) \mathrm{d}x = \int _{\partial\Omega} u v\cdot \hat{n} \mathrm{d}S
                $$

            特别地，我们考虑概率密度函数 $p(x)$，分别考虑 $u=p(x)$ 和 $v=\nabla p(x)$ 两种情况，$\Omega$ 选为全空间，则边界处（无穷远处）有 $p(x)\to 0$ 和 $\nabla p(x)\to 0$，因此上面式子在边界上的面积积分均为 0，得到

            $$
            \begin{aligned}
                \int v \nabla p \mathrm{d}x
                &= -\int p \nabla\cdot v \mathrm{d}x \\
                \int u \nabla\cdot \nabla p \mathrm{d}x
                &= -\int \nabla p \cdot \nabla u \mathrm{d}x
            \end{aligned}
            $$

            上面给了一个比较模糊的“无穷远处”“趋向于0”的描述，严格来说需要说 $p$ 是紧支撑的（具有紧的支撑集），这样才能让面积积分为 0。因此我们可以知道我们为什么要在这里假设测试函数是紧支撑的了。

        于是

        $$
        \begin{aligned}
            &\int [
                {\color{red} p_{t + \Delta t}(x_t)}
                - {\color{orange} p_t(x_t)}
            ]\phi(x_t)\mathrm{d}x_t
            = - {\color{skyblue}
                \Delta t
                \int \nabla_{x_t}\left[p_t(x_t) f_t(x_t) \right] \phi(x_t)\mathrm{d}x_t
            } \\
            \Rightarrow & \int \frac{\partial p_t(x_t)}{\partial t} \phi(x_t)\mathrm{d}x_t = -\int \nabla_{x_t}\left[p_t(x_t) f_t(x_t)\right] \phi(x_t)\mathrm{d}x_t \\
            \Rightarrow & \frac{\partial p_t(x_t)}{\partial t} = -\nabla_{x_t}\left[p_t(x_t) f_t(x_t)\right]
        \end{aligned}
        $$

        > 先让 $\Delta t\to 0$，最后使用测试函数法。
    
    Rectified Flow 最关键的设计就是 $x_t=\varphi_t(x_0, x_1)$，代表流模型中关键的基础**可逆**变换，可以与 normalizing flow 相对照；在这里我们简写 $\varphi_t(x_0, x_1)$ 为 $\varphi_t$。

    > 在 Rectified Flow 中，直接取线性函数 $\varphi_t(x_0, x_1)=(1-t)x_0 + tx_1$，即“走直线”

    在 $\varphi_t$ 关于 $x_1$ 可逆的设计下，可以解出 $x_1 = \psi_t(x_0, x_t)$，代入到 $\varphi_t(x_0, x_1)$ 可以让其成为 $\varphi_t(x_0, x_t) = \varphi_t(x_0, \psi_t(x_0, x_t))$，于是有

    $$
    \begin{aligned}
        {\color{red} v^x(x_t, t)}
        &= \mathbb{E}[\dot{x_t}\mid x_t] \\
        &= \mathbb{E}_{x_0, x_1\mid x_t}[\dot{\varphi_t}(x_0, x_1)] \\
        &= \mathbb{E}_{x_0\mid x_t}[\dot{\varphi_t}(x_0, x_t)]
        \xrightarrow{\text{simplify symbol}}
        {\color{red} 
            \mathbb{E}_{x_0\mid x_t}[\dot{\varphi_t}]
        } \\
    \end{aligned}
    $$

    注意到，在测试函数法证明连续性方程时，实际上是利用了
    
    $$
    \mathbb{E}_{x_t + \Delta t}\left[\phi(x_{t + \Delta t})\right]
    = \mathbb{E}_{x_t}\left[\phi(x_t + f_t(x_t)\Delta t)\right]
    $$
    
    也就是说，我们也只需证到这一步即可**证明连续性方程**，**也就证明边缘分布一致了**。对于任意紧支撑 ([compact support](https://en.wikipedia.org/wiki/Support_(mathematics)#Compact_support)) 的连续可微测试函数 $\phi(x): \mathbb{R}^n\to \mathbb{R}$，我们有

    $$
    \begin{aligned}
        \mathbb{E}_{x_{t + \Delta t}}\left[
            \phi({\color{orange}
                x_{t + \Delta t}
            })
        \right]
        &= \mathbb{E}_{x_0, x_1}\left[
            \phi({\color{orange}
                \varphi_{t + \Delta t}
            })
        \right] & {\color{orange}
            x_{t+\Delta t} = \varphi_{t + \Delta t}(x_0, x_1)
        } \\
        &\approx \mathbb{E}_{x_0, x_1}\left[
            \phi({
                \color{green} \varphi_t
            }) +
            \Delta t
            {\color{green}
                \frac{\partial \varphi_t}{\partial t}
            } \cdot
            \nabla_{\varphi_t} \phi({\color{green}
                \varphi_t
            })
        \right] & \text{Taylor Expansion to }O(\Delta t)\\
        &= \mathbb{E}_{\color{skyblue} x_0, x_1}\left[
            \phi({\color{green}
                x_t
            }) + 
            \Delta t
            {\color{green}
                \dot{\varphi_t}
            } \cdot
            \nabla_{\varphi_t} \phi({\color{green}
                x_t
            })
        \right] & { \color{green}
            x_t = \varphi_t(x_0, x_1)
        }\\
        &= \mathbb{E}_{\color{skyblue} x_t}[\phi(x_t)]
        + \Delta t 
        \mathbb{E}_{\color{skyblue} x_0, x_t}\left[
            \dot{\varphi_t}
            \nabla_{\varphi_t} \phi(x_t)
        \right] & { \color{skyblue}
            \varphi_t(x_0, x_1) \to \varphi_t(x_0, x_t)
        }\\
        &= \mathbb{E}_{x_t}[\phi(x_t)]
        + \Delta t 
            \mathbb{E}_{x_t}\left[
            { \color{red}
                \mathbb{E}_{x_0\mid x_t}\left[
                    \dot{\varphi_t}
                \right]
            }
            \nabla_{\varphi_t} \phi(x_t)
        \right] \\
        &= \mathbb{E}_{x_t}[\phi(x_t)]
        + \Delta t 
            \mathbb{E}_{x_t}\left[
            { \color{red}
                v^x(x_t, t)
            }
            \nabla_{\varphi_t} \phi(x_t)
        \right] & { \color{red}
            v^x(x_t, t) = \mathbb{E}_{x_0\mid x_t}\left[
                \dot{\varphi_t}
            \right]
        }\\
        &= \mathbb{E}_{x_t}\left[
            \phi(x_t)
            + \Delta t
            v^x(x_t, t)
            \nabla_{\varphi_t} \phi(x_t)
        \right] \\
        &\approx \mathbb{E}_{x_t}\left[
            \phi\left(
                x_t
                + \Delta t
                v^x(x_t, t)
            \right)
        \right] & \text{Reverse Taylor Expansion}
    \end{aligned}
    $$

    对任意测试函数都成立。于是我们证明了连续性方程，有

    $$
    x_{t + \Delta t} = x_t + \Delta t v^x(x_t, t) \Rightarrow
    \frac{\mathrm{d}x_t}{\mathrm{d}t} = v^x(x_t, t)
    $$

    根据 $v^x$ 的定义，$v^x$ 是可以通过训练如下目标得到的 $v_{\theta}$ 近似的

    $$
    \min_{\theta} \int_0^1 \mathbb{E}_{x_0, x_1}\left[\left\|\dot{\varphi_t} - v_{\theta}\right\|^2\right]\mathrm{d}t,\quad \dot{\varphi_t}(x_0, x_1) = x_1 - x_0
    $$

    注意到我们这里的证明全程没有提及 $z_t$，是因为连续性方程才是边缘分布的关键，$z_t$ 前面和 Rectifiable 相关的定义也类似先有了 ODE 再定义的“先射箭后画靶”式的定义法。更具体地，所满足的连续性方程中 $f_t(x_t)$ 就是 $v^x(x_t, t)$，连续性方程为

    $$
    \frac{\partial p_t(x_t)}{\partial t} = -\nabla_{x_t}\left[p_t(x_t) v^x(x_t, t)\right]
    $$

    也就是说，我们训练拟合的最优解 $v^x$ 满足连续性方程，所以得证。

    > 从更直接的角度理解，我们实际上证明的是从任意的 $p(z_t)=p(x_t)$ 出发，总能得到 $p(z_{t + \Delta t}) = p(x_{t + \Delta t})$，所以从 $p(z_0)=p(x_0)$ 出发，能够得到 $p(z_t)=p(x_t)$。

这个保持边缘分布一致的性质非常重要，实际上保证了从 $z_0$ 出发解 $v_{\theta}(x_t, t)$ 所构造的良定义 ODE 所得到的 $z_1$ 满足 $p(z_1)=p(x_1)$，也就是 Rectified Flow 的目标。