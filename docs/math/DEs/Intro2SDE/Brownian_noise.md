<link rel="stylesheet" href="../../../../css/counter.css" />

# Brownian Motion and "White Noise"

!!! info "Part of note of *An Introduction to Stochastic Differential Equations*, Lawrence C. Evans"

!!! warning "本页面还在施工中"

## Motivation

### Some History

**布朗运动 (brownian motion)** 是一种具有连续时间参数和连续状态空间的随机过程。考虑充满清水的长细管，$t=0$ 时在 $x=0$ 处注入一滴墨水

$$
u(x, 0) = \delta_0
$$

$\delta_0$ 是 $0$ 处的 Dirac point mass，即

$$
\delta_0(x) = \begin{cases}
1, & x = 0\\
0, & x \neq 0
\end{cases}
$$

墨水随着时间的推移，将会在管道中扩散。设一段短时间 $\tau$ 后，墨水从 $x$ 扩散到 $x+y$ 处的概率密度为 $f(y, \tau)$，则

$$
\begin{aligned}
    u(x, t + \tau)
    &= \int_{-\infty}^{+\infty} u(x-y, t) f(y, \tau) \mathrm{d}y\\
    &= \int_{-\infty}^{+\infty} \left( u - u_x y + \frac{1}{2} u_{xx} y^2 + \cdots \right) f(y, \tau) \mathrm{d}y\\
\end{aligned}
$$

这里对偏导用了简记，即

$$
u_x = \frac{\partial u}{\partial x}(x, t), \quad u_{xx} = \frac{\partial^2 u}{\partial x^2}(x, t)
$$

这个式子实际上把 $u(x, t+\tau)$ 拆分成了**各阶矩的线性组合**，下面开始考虑其各阶矩的值。

!!! general "零至二阶矩的考虑"

    - 零阶矩 $\int_{-\infty}^{+\infty} f(y, \tau) \mathrm{d}y = 1$ （概率密度函数）
    - 由对称性 $f(y, \tau) = f(-y, \tau)$（$f$ 关于 $y$ 是偶函数），$f(y, \tau)$ 关于 $y$ 的一阶矩（期望）为

    $$
    \int_{-\infty}^{+\infty} y f(y, \tau) \mathrm{d}y = 0
    $$

    > $y f(y, \tau)$ 关于 $y$ 是一个奇函数，对称性导致积分为 $0$

    - 考虑二阶矩（方差），**假定**关于 $\tau$ 是**线性**的

    $$
    \int_{-\infty}^{+\infty} y^2 f(y, \tau) \mathrm{d}y = D\tau
    $$

    这里的 $D>0$ 是一个正常数，并不是求导算子。

!!! tip "Remark"
    这里给出了一个重要假设：方差关于 $\tau$ 是线性的

二阶以上的矩都省去，则原式可化为

$$
\frac{u(x, t+\tau) - u(x, t)}{\tau} = \frac{D}{2}u_{xx}(x, t)
$$

令 $\tau\to 0^+$，就可以得到

$$
u_t=\frac{D}{2}u_{xx}
$$

这就是**扩散方程 (diffusion equation)**，也称**热方程 (heat equation)**。在同作者的 PDE 书的 [2.3 节](../PDE/4linearPDEs.md#heat-equation)给出了这类方程的解法，结合其初值条件 $u(x, 0)=\delta_0$，在这里直接给出它的解：

$$
u(x, t) = \frac{1}{(2\pi Dt)^{1/2}}e^{-\frac{x^2}{2Dt}}
= \frac{1}{\sqrt{Dt} \sqrt{2\pi}}e^{-\frac{x^2}{2(\sqrt{Dt})^2}}
$$

从中可见，在 $t$ 时刻扩散的墨水的密度服从 $N(0, Dt)$ 的分布。关于常数 $D$，[Einstein relation](https://en.wikipedia.org/wiki/Einstein_relation_(kinetic_theory)) 揭示了

$$
D=\mu k_B T
$$

??? general "各符号的解释"
    - $\mu$: “流动性 (mobility)”，其表达式为 $v_d/F$
        - $v_d$ 是粒子的 terminal drift velocity，即流体中从静止受力加速后能达到的最大平衡速度
        - $F$ 则是受力
    - $k_B$: Boltzmann 常数
    - $T$: 绝对温度

在本书中，则把这个关系写为

$$
D=\frac{RT}{N_Af}
$$

??? general "各符号的解释"
    - $R$ 是理想气体常数，$N_A$ 是阿伏伽德罗常数 (Avogadro constant)，所以有 $R = k_BN_A$
    - $f$ 是摩擦系数，所以有 $F=fv_d=v_d/\mu$

### Random Walks

**随机游走 (random walks)** 也可以用于导出扩散方程。考虑横坐标为空间 $x$，纵坐标为时间 $t$ 的二维网格，网格具有空间最小单位 $\Delta x$ 和时间最小单位 $\Delta$。每个 $\Delta t$，相对上一时刻的位置，各有 $1/2$ 的概率向左/向右移动 $\Delta x$。使用 $(m, n)$ 表示 $n\Delta t$ 时刻位于 $m\Delta x$，则初始有

$$
p(m, 0) = \begin{cases}
    0, &m\neq 0\\
    1, &m=0
\end{cases}
$$

考虑状态转移，有

$$
p(m, n+1) = \frac{1}{2}p(m-1, n) + \frac{1}{2}p(m+1, n)
$$

因此就有

$$
\begin{aligned}
    p(m, n+1) - p(m, n)
    &= \frac{1}{2}p(m-1, n) + \frac{1}{2}p(m+1, n) - p(m, n)\\
    &= \frac{1}{2}\left( p(m-1, n) - 2p(m, n) + p(m+1, n) \right)
\end{aligned}
$$

!!! tip "Important Assumption"
    假设空间尺度和时间尺度满足如下关系

    $$
    \frac{(\Delta x)^2}{\Delta t}=D\quad\text{for some positive constant }D
    $$

这样就有

$$
\begin{aligned}
    \frac{p(m, n+1) - p(m, n)}{\Delta t}
    &= \frac{1}{2}\left( \frac{p(m-1, n) - 2p(m, n) + p(m+1, n)}{(\Delta x)^2} \right)\\
    &= \frac{D}{2}\left( \frac{p(m-1, n) - 2p(m, n) + p(m+1, n)}{(\Delta x)^2} \right)
\end{aligned}
$$

令 $\Delta x\to 0$，$\Delta t\to 0$，$m\Delta x\to x$，$n\Delta t\to t$，这样就有 $p(m, n)\to u(x, t)$，则上式就变成了

$$
u_t = \frac{D}{2}u_{xx}
$$

于是我们重新获得了扩散方程。

### Mathematical Justification

利用 [De Moivre-Laplace 中心极限定理](../../../courses/probability/prob_lim.md#de-moivre-laplace)，可以给出随机游走到特定时间位置的概率分布的一种更概率论的推导方式。

使用随机变量 $X(t)$ 表示 $t=n\Delta t$ 时刻的位置，再定义 $n$ 次游走中向右游走的次数为

$$
S_n = \sum_{k=1}^n \xi_k
$$

这里 $\xi_k$ 是独立同分布的随机变量，满足 $p=1/2$ 的两点分布，即

$$
\begin{cases}
P(\xi_k=1)=1/2\\
P(\xi_k=0)=1/2
\end{cases},\quad
Var(\xi_k)=p(1-p)=\frac{1}{4}
$$

可以得到

$$
X(t)=S_n\Delta x + (n-S_n)\Delta x = (2S_n-n)\Delta x
$$

研究其方差，发现有

$$
\begin{aligned}
    Var(X(t))
    &= 4(\Delta x)^2Var(S_n)\\
    &= 4(\Delta x)^2(nVar(\xi_1))\\
    &= n(\Delta x)^2 \\
    &= \frac{(\Delta x)^2}{\Delta t}t
\end{aligned}
$$

!!! tip "Remark"
    由此可以注意到，Einstein 的研究中令方差关于 $\tau$ 是线性的假设，和假设 $(\Delta x)^2$ 和 $\Delta t$ 的线性假设是一致的。在这里同样给出这个假设。

$$
X(t) = (2S_n - n)\Delta x
= \frac{S_n - \frac{n}{2}}{\sqrt{\frac{n}{4}}} \sqrt{n} \Delta x
= \frac{S_n - \frac{n}{2}}{\sqrt{\frac{n}{4}}} \sqrt{tD}
$$

然后利用 De Moivre-Laplace 中心极限定理，可以得到

$$
\begin{aligned}
    \lim_{\substack{n\to\infty \\ t=n\Delta t,\; \frac{(\Delta x)^2}{\Delta t}=D}}P\left(a\leqslant X(t)\leqslant b\right)
    &= \lim_{n\to \infty}\left( \frac{a}{\sqrt{tD}}\leqslant \frac{S_n - \frac{n}{2}}{\sqrt{\frac{n}{4}}}\leqslant \frac{b}{\sqrt{tD}} \right) \\
    &= \frac{1}{\sqrt{2\pi}}\int_{a/\sqrt{tD}}^{b/\sqrt{tD}}e^{-\frac{x^2}{2}}\mathrm{d}x\\
    &= \frac{1}{\sqrt{2\pi tD}}\int_a^b e^{-\frac{x^2}{2tD}}\mathrm{d}x
\end{aligned}
$$

> 由于 $S_n$ 满足二项分布，所以可以说是在使用 De Moivre-Laplace 中心极限定理，而不必说是在用 Lindeberg–Lévy 中心极限定理

再次导出 $t$ 时刻的位置满足 $N(0, Dt)$ 的分布。

## Definition, Elementary Properties

### Definition & Computation

!!! info "Brownian Motion/Wiener Process"
    **布朗运动 (Brownian motion)**，或**维恩过程 (Wiener process)** 是满足如下条件的实值随机过程 $W(\cdot)$：

    1. $W(0)=0$ a.s.
    2. (Gaussian increments) $W(t) - W(s)\sim N(0, t-s), \quad \forall\; t\geqslant s\geqslant 0$
    3. (independent increments) $W(t_1), W(t_2) - W(t_1), \cdots, W(t_n) - W(t_{n-1})$ are independent for all times $0\leqslant t_1 < t_2 < \cdots < t_n$

!!! tip "a.s. 是 [almost surely](intro_prob.md#probability-space) 的缩写"

中心极限定理提供了如此定义布朗运动的动机：由一系列合适地缩放了的独立随机分布的和构成的位置随机变量，服从正态分布。

给出布朗运动的定义之后，应当得到相关的计算方式。从一个简单的问题出发，计算联合概率，即给定 $[a_i, b_i], t_i, i=1, \cdots, n$，希望计算

$$
P(a_1\leqslant W(t_1)\leqslant b_1, \cdots, a_n\leqslant W(t_n)\leqslant b_n)
$$

首先最基础的，对于 $\forall t > 0$ 和 $a\leqslant b$，由于 $W(0)=0$，根据 Gaussian increments 有

$$
P(a\leqslant W(t)\leqslant b) = \frac{1}{\sqrt{2\pi t}} \int_a^b e^{-\frac{x^2}{2t}}\mathrm{d}x
$$

取 $t=t_1$, $[a, b] = [a_1, b_1]$，就可以得到 $P(a_1\leqslant W(t_1)\leqslant b_1)$ 的值。进一步地，给定了 $W(t_1)=x_1$，同样从 Gaussian increments 出发可以得到

$$
P(a_2\leqslant W(t_2)\leqslant b_2 | W(t_1)=x_1) = \int_{a_2}^{b_2} \frac{1}{\sqrt{2\pi(t_2-t_1)}}e^{-\frac{(x_2-x_1)^2}{2(t_2-t_1)}}\mathrm{d}x
$$

定义

$$
g(x, t\mid y) = \frac{1}{\sqrt{2\pi t}}e^{-\frac{(x-y)^2}{2t}}
$$

那就有

$$
P(a_1\leqslant W(t_1)\leqslant b_1, a_2\leqslant W(t_2)\leqslant b_2)
= \int_{a_1}^{b_1} \int_{a_2}^{b_2} g(x_1, t_1\mid 0) g(x_2, t_2 - t_1 \mid x_1) \mathrm{d}x_2\mathrm{d}x_1
$$

以此类推，那就有

$$
\begin{aligned}
    &P(a_1\leqslant W(t_1)\leqslant b_1, \cdots, a_n\leqslant W(t_n)\leqslant b_n) \\
    = &\int_{a_1}^{b_1}\cdots \int_{a_n}^{b_n} g(x_1, t_1\mid 0) g(x_2, t_2 - t_1 \mid x_1)\cdots g(x_n, t_n - t_{n-1} \mid x_{n-1}) \mathrm{d}x_n\cdots\mathrm{d}x_1
\end{aligned}
$$

更一般地，以上这个计算的式子是以下定理中 $f(x_1, \cdots, x_n)=\chi_{[a_1, b_1]}(x_1)\cdots \chi_{[a_n, b_n]}(x_n)$ 的特例。

!!! abstract "一维布朗运动的计算"
    设 $W(\cdot)$ 为一维布朗运动，对于$\forall n\in \mathbb{N}^+$, $0=t_0<t_1<\cdots<t_n$, $f:\mathbb{R}^n\to\mathbb{R}$，我们有

    $$
    \begin{aligned}
        & \mathbb{E}(f(W(t_1), \cdots, W(t_n))) \\
        =& \int_{-\infty}^{\infty}\cdots \int_{-\infty}^{\infty} f(x_1, \cdots, x_n) g(x_1, t_1\mid 0) g(x_2, t_2 - t_1 \mid x_1)\cdots g(x_n, t_n - t_{n-1} \mid x_{n-1}) \mathrm{d}x_n\cdots\mathrm{d}x_1
    \end{aligned}
    $$

??? general "Proof"
    记 $X_i:= W(t_1), Y_i:=X_i-X_{i-1}, i=1, \cdots, n$，并定义

    $$
    h(y_1, \cdots, y_n) := f(y_1, y_1 + y_2, \cdots, y_1 + \cdots + y_n)
    $$

    > 好处是 $Y_i\sim N(0, t_i - t_{i-1})$ 直接相互之间独立了

    则有

    $$
    \begin{aligned}
        & \mathbb{E}(f(W(t_1), \cdots, W(t_n))) = \mathbb{E} h(Y_1, \cdots, Y_n) \\
        =& \int_{-\infty}^{\infty}\cdots \int_{-\infty}^{\infty} h(y_1, \cdots, y_n) g(y_1, t_1\mid 0) g(y_2, t_2 - t_1 \mid 0)\cdots g(y_n, t_n - t_{n-1} \mid 0) \mathrm{d}y_n\cdots\mathrm{d}y_1 \\
        =& \int_{-\infty}^{\infty}\cdots \int_{-\infty}^{\infty} f(x_1, \cdots, x_n) g(x_1, t_1\mid 0) g(x_2, t_2 - t_1 \mid x_1)\cdots g(x_n, t_n - t_{n-1} \mid x_{n-1}) \mathrm{d}x_n\cdots\mathrm{d}x_1
    \end{aligned}
    $$

### More on White Noise

本节的内容旨在提供对白噪声更多的一些直觉。首先为了计算方便，先证明如下引理：

!!! abstract "一维布朗运动的期望计算性质"
    设 $W(\cdot)$ 为一维布朗运动，则

    $$
    \begin{gathered}
        \mathbb{E}(W(t)) = 0 ,\quad \mathbb{E}(W^2 (t)) = t, \quad \forall t\geqslant 0 \\
        \mathbb{E}(W(t)W(s)) = t \wedge s = \min\{t, s\},\quad \forall t, s \geqslant 0
    \end{gathered}
    $$

> $t \wedge s := \min\{t, s\}$

??? general "Proof"
    由于 $W(t)\sim N(0, t)$，第一行显然。对于第二行，不妨令 $t\geqslant s$（反之对称），则

    $$
    \begin{aligned}
        \mathbb{E}(W(t)W(s))
        &= \mathbb{E}((W(s) + W(t) - W(s))W(s)) \\
        &= \mathbb{E}(W^2(s)) + \mathbb{E}((W(t) - W(s))W(s)) \\
        &= s + \mathbb{E}(W(t) - W(s))\mathbb{E}(W(s)) \\
        &= s
    \end{aligned}
    $$

    注意，倒数第三行到倒数第二行利用了 $W(t)-W(s)\sim N(0, t-s)$ 和 $W(s)\sim N(0, s)$ 相互独立的结论。

接下来将阐述白噪声为什么“白”。不正式地，给出如下启发 (heuristic) 公式：

$$
\mathbb{E}(\xi(t)\xi(s)) = \delta_0(s-t)
$$

> 注意 $\delta_0(x)$ 是 Dirac delta function

??? general "Informal Proof"
    设 $\:h>0$, 对于给定的 $t>0$，设

    $$
    \begin{aligned}
        \phi_h(s)
        &:= \mathbb{E}\left(
            \left(\frac{W(t+h) - W(t)}{h}\right)
            \left(\frac{W(s+h) - W(s)}{h}\right)
        \right) \\
        &= \frac{1}{h^2}\left[
            \mathbb{E}(W(t+h)W(s+h)) - \mathbb{E}(W(t+h)W(s)) - \mathbb{E}(W(t)W(s+h)) + \mathbb{E}(W(t)W(s))
        \right] \\
        &= \frac{1}{h^2}\left[
            (t+h)\wedge(s+h) - (t+h)\wedge s - t\wedge(s+h) + t\wedge s
        \right]
    \end{aligned}
    $$

    分类讨论，容易得到 $\phi_h(s)$ 的图像如下图所示。

    <div style="text-align:center;">
        <img src="../../../imgs/Intro2SDE/hw1.gif" alt="hw1" style="zoom:50%;" />
    </div>

    可以注意到，$\phi_h(s)$ 满足 $\phi_h\geqslant 0$，且

    $$
    \int_{-\infty}^{+\infty} \phi_h(s) \mathrm{d}s = 
    \frac{1}{2} \cdot (2h) \cdot \frac{1}{h} = 1
    $$

    可以看出，当 $h\to 0^+$ 时，$\phi_h(s)$ 逐渐变得尖锐，在以上两个条件满足的情况下，凭感觉最终就是 $\delta_0(s-t)$。另一方面，$h\to 0^+$ 时我们根据 $\phi_h(s)$ 的定义式，可以感觉到其趋向于 $\mathbb{E}(\xi(t)\xi(s))$。从这两方面，我们可以不正式地完成证明。

在最后阐释“白”噪声之前，我们需要先引入自相关 (autocorrelation) 函数和广义平稳 (wide-sense stationary) 的概念。

!!! info "自相关函数"
    对于满足 $\:\mathbb{E}(X^2(t)) < \infty$, $t\geqslant 0\:$ 的实值随机过程 $X(\cdot)$，定义

    $$
        r(t, s) := \mathbb{E}(X(t)X(s))
    $$

    为 $X(\cdot)$ 的自相关函数 (autocorrelation function)。

!!! info "广义平稳"
    对于满足 $\:\mathbb{E}(X^2(t)) < \infty$, $t\geqslant 0\:$ 的实值随机过程 $X(\cdot)$，如果存在 $c: \mathbb{R}\to \mathbb{R}$ 使得

    $$
        r(t, s) = c(t-s), \quad
        \mathbb{E}(X(t)) = \mathbb{E}(X(s)), \quad
        \forall t, s\geqslant 0
    $$

    则称 $X(\cdot)$ 是广义平稳 (wide-sense stationary) 的。

对于任意广义平稳函数，将其自相关函数进行 Fourier 变换，可以得到其谱密度 (spectral density) $f(\lambda)$：

$$
f(\lambda) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} c(t)e^{-i\lambda t}\mathrm{d}t,\quad \lambda \in \mathbb{R}
$$

对于白噪声过程，根据前面的启发式公式，我们可以认为取 $c(\cdot)=\delta_0$ 的情况下，可以得到白噪声过程 $\xi(\cdot)$ 是广义平稳的。计算白噪声的谱密度

$$
f(\lambda) = \frac{1}{2\pi}\int_{-\infty}^{+\infty} \delta_0(t)e^{-i\lambda t}\mathrm{d}t = \frac{1}{2\pi},\quad \forall \lambda \in \mathbb{R}
$$

可以看出白噪声过程的谱密度是常数，即所有“频率”在自相关函数的构成中的贡献相当。因此类比所有颜色的光在白光的构成中贡献相当，我们将 $\xi(\cdot)$ 称为“白”噪声。

## Construction of Brownian Motion

前面直接定义了符合什么性质的实值随机过程是布朗运动，并进一步研究了其一些简单性质，但是并没有证明**布朗运动的存在性**，即存在一个实值随机过程 $W(\cdot)$ 满足布朗运动的定义。

本节将花大篇幅在 $[0, 1]$ 上构造布朗运动，随后简单地将 $[0, 1]$ 扩展到 $[0, +\infty)$。在 $[0, 1]$ 上构造布朗运动的主要过程为：

- 选择一组 $L^2(0, 1)$ 上的**规范正交基** (orthonormal basis)，$L^2(0, 1)$ 是 $[0, 1]$ 上的平方可积实值函数空间（可以理解为函数的 2-范数存在，与 2.6 中的定义是相容的）
- $L^2(0, 1)$ 是无限维空间，将白噪声使用该规范正交基**线性表示**，会是级数的形式
- 进一步地构造的布朗运动，依然会是级数的形式，需要证明该级数的**一致收敛性**

> 以上过程中用到了许多小波分析 (wavelet analysis) 的技术

### Expansions in an orthonormal basis

对于基 $\{\psi_n\}_{n=0}^{\infty}$，规范正交性要求有

$$
\int_0^1 \psi_n(s)\psi_m(s)\mathrm{d}s = \delta_{mn} = \begin{cases}
    1, & m=n\\
    0, & m\neq n
\end{cases},\quad \forall\: m, n
$$

将白噪声使用规范正交基 $\{\psi_n\}_{n=0}^{\infty}$ 线性表示有

$$
\xi(t) = \sum_{n=0}^{\infty} A_n \psi_n(t)
$$

这里的系数 $A_n$ 都是随机变量，根据规范正交基的性质，上式两边都乘上 $\psi_n(t)$ 后积分就容易得知有

$$
A_n = \int_0^1 \xi(t)\psi_n(t)\mathrm{d}t
$$

构造时，我们**希望** $A_n$ 之间相互独立，且符合均值为 0 的高斯分布。给出这样严格的限制之后，要满足正交基的规范性，已经其实已经对方差有了要求，我们有

$$
\begin{aligned}
    \mathbb{E}(A_nA_m)
    & = \mathbb{E}\left( \int_0^1 \xi(t)\psi_n(t)\mathrm{d}t \int_0^1 \xi(s)\psi_m(s)\mathrm{d}s \right) \\
    & = \int_0^1 \int_0^1 \mathbb{E}(\xi(t)\xi(s))\psi_n(t)\psi_m(s)\mathrm{d}t\mathrm{d}s \\
    & = \int_0^1 \int_0^1 \delta_0(t-s)\psi_n(t)\psi_m(s)\mathrm{d}t\mathrm{d}s & \text{heuristic formula}\\
    & = \int_0^1 \psi_n(t)\psi_m(t)\mathrm{d}t & \delta_0(t-s) = \begin{cases}
        1, & t=s\\
        0, & t\neq s
    \end{cases}
\end{aligned}
$$

对于 $m\neq n$ 的情况，前面已经约定 $\mathbb{E}(A_n)=0$，因此就有 $\mathbb{E}(A_mA_n) = \mathbb{E}(A_m)\mathbb{E}(A_n)=0$，与规范正交基的定义一致。而对于 $m=n$ 的情况，就有

$$
\mathbb{E}(A_n^2) = \int_0^1 \psi_n^2(t)\mathrm{d}t
$$

要使其与规范正交基的定义一致，就需要 $\mathbb{E}(A_n^2)=1$，因此就有 $Var(A_n)=\mathbb{E}(A_n^2) - \mathbb{E}(A_n)^2 = 1$。

综上可知，如果 i.i.d. 地取 $A_n\sim N(0, 1)$，那么对于规范正交基 $\{\psi_n\}_{n=0}^{\infty}$，所构造的 $\xi(t)=\sum A_n\psi_n(t)$ 就是有意义的。于是，布朗运动 $W(\cdot)$ 就可以被下式给定：

$$
W(t) := \int_0^t \xi(s)\mathrm{d}s = \sum_{n=0}^{\infty} A_n \int_0^t \psi_n(s)\mathrm{d}s
$$

尽管看起来任意规范正交基 $\{\psi_n\}_{n=0}^{\infty}$ 都是可行的，但是为了使整个构造过程更严格、性质更优雅，之后将使用 Haar functions 作为规范正交基。

### Construction of Brownian Motion

!!! info "Haar Functions"
    **Haar functions** $\{h_k(\cdot)\}_{k=0}^{\infty}\:$ 是一系列在 $L^2(0, 1)$ 上的函数。首先定义 $h_0$

    $$
    h_0(t) := 1,\quad t\in [0, 1]
    $$

    然后对于 $2^n\leqslant k < 2^{n+1}-1$, $n\in \mathbb{N}$，定义

    $$
    h_k(t) := \begin{cases}
        2^{n/2}, & t\in [\frac{k-2^n}{2^n}, \frac{k-2^n+1/2}{2^n})\\
        -2^{n/2}, & t\in [\frac{k-2^n+1/2}{2^n}, \frac{k-2^n+1}{2^n}]\\
        0, & \text{otherwise}
    \end{cases}
    $$

对于单个 Haar function，原书上给了这张图：

<div style="text-align:center;">
    <img src="../../../imgs/Intro2SDE/graph-of-a-haar-function.jpg" alt="graph-of-a-haar-function" style="zoom:50%;" />
</div>

为了更加形象地展示 Haar functions，下图展示了前 8 个 Haar functions $h_k(t)$ 和后面将会提及的 $s_k(t)$ 的图像：

<div style="text-align:center;">
    <img src="../../../imgs/Intro2SDE/first-eight-Haar-functions-and-their-integrals.png" alt="first-eight-Haar-functions-and-their-integrals" style="zoom:50%;" />
</div>

!!! abstract "Haar functions 的规范正交性 (Lemma 1)"
    Haar functions $\{h_k(\cdot)\}_{k=0}^{\infty}$ 构成了 $L^2(0, 1)$ 上的一组完全的 (complete) 规范正交基。

??? general "Proof"
    首先，显然有

    $$
    \int_0^1 h_k^2(t)\mathrm{d}t = 2^n \left(\frac{1}{2^{n+1}} + \frac{1}{2^{n+1}}\right) = 1
    $$

    考虑交叉相乘求积，设 $l > k$，要么 $h_k$ 和 $h_l$ 的支撑集 (support) 要么交集为空，要么必然有 $\operatorname{supp}(h_l) \subseteq \operatorname{supp}(h_k)$。支撑集交集为空，则 $h_lh_k=0$，而对于支撑集存在包含关系这一情况有

    $$
    \int_0^1 h_l(t)h_k(t)\mathrm{d}t = \pm 2^{n/2}\int_0^1h_l(t)\mathrm{d}t = 0,\quad 2^n\leqslant k < 2^{n+1}
    $$

    > 支撑集 (support) 是指使得函数取值非零的定义域的子集，详细可见 [Support (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Support_(mathematics))

    现在规范正交性已经得到证明，下面需要证明的就是 $\{h_k(\cdot)\}_{k=0}^{\infty}$ 构成了 $L^2(0, 1)$ 上的一组**完全的基**。利用上已经证明的正交性，只需要证明 $\forall f\in L^2(0, 1)$，如果 $\forall k\in \mathbb{N}^+$ 都有 $\int_0^1 f(t)h_k(t)\mathrm{d}t = 0$，那么就有 $f=0$ a.e.。

    对于 $k=0$ 的情况，有 $\int_0^1 f\mathrm{d}t = 0$。接下来考虑 $2^n\leqslant k < 2^{n+1}$。

    对于 $n=0$ 的情况，有 $k=1$，那么有 $\int_0^{1/2} f\mathrm{d}t = \int_{1/2}^1 f\mathrm{d}t$。结合 $k=0$ 时的 $\int_0^1 f\mathrm{d}t = (\int_0^{1/2} + \int_{1/2}^1)f\mathrm{d}t = 0$，就有 $\int_0^{1/2} f\mathrm{d}t = \int_{1/2}^1 f\mathrm{d}t = 0$。

    同理，让 $n$ 的下一层依照上一层，总能得到 $\int_{k/2^{n+1}}^{(k+1)/2^{n+1}} f\mathrm{d}t = 0$, $\forall\: 0\leqslant k < 2^{n+1}$。这样就可以得到 $\int_0^1 f\mathrm{d}t = 0$，即 $f=0$ a.e.。

由此，我们将构造

$$
W(t) := \sum_{k=0}^{\infty} A_k \int_0^t h_k(s)\mathrm{d}s
$$

为了证明所构造的 $W(\cdot)$ 在 $[0, 1]$ 上确实是布朗运动，需要首先研究几个引理。

!!! info "Schauder function"
    $k$-th **Schauder function** $s_k(t)$ 被定义为

    $$
    s_k(t) := \int_0^t h_k(s)\mathrm{d}s, \quad 0\leqslant t\leqslant 1
    $$

$s_k(t)$ 的图像是高度为 $2^{-n/2-1}$ 的“帐篷”，具体可见前面的图。因此有

$$
\max\limits_{0\leqslant t\leqslant 1} |s_k(t)| = 2^{-n/2-1},\quad 2^n \leqslant k < 2^{n+1}
$$

可以看出，$s_k$ 就成为了 $W(\cdot)$ 的基。为了方便后续 $W(\cdot)$ 的一些计算，引入如下引理：

!!! abstract "Lemma 2"
    $\forall\: 0\leqslant t, s \leqslant 1$，有

    $$
    \sum_{k=0}^{\infty} s_k(s)s_k(t) = s \wedge t
    $$

??? general "Proof"
    定义

    $$
    \phi_s(\tau) := \begin{cases}
        1, & 0 \leqslant \tau \leqslant s \\
        0, & s < \tau \leqslant 1
    \end{cases}
    $$

    考虑 $\:0\leqslant s \leqslant t \leqslant 1$, 理解 $\phi_s$ 和 $\phi_t$ 的图像如下图所示：

    <div style="text-align:center;">
        <img src="../../../imgs/Intro2SDE/3.3_lemma2_phi.png" alt="3.3_lemma2_phi" style="zoom:50%;" />
    </div>

    因此，考虑 $0\leqslant s, t\leqslant 1$，有

    $$
    \int_0^1 \phi_s(\tau)\phi_t(\tau)\mathrm{d}\tau = s \wedge t
    $$

    另一方面，将 $\phi_s$ 和 $\phi_t$ 分别展开为 Haar functions 的线性组合

    $$
    \phi_s(\tau) = \sum_{k=0}^{\infty} a_kh_k(\tau),\quad \phi_t(\tau) = \sum_{k=0}^{\infty} b_kh_k(\tau)
    $$

    这样就有

    $$
    \begin{aligned}
        \int_0^1 \phi_s(\tau)\phi_t(\tau)\mathrm{d}\tau
        &= \int_0^1 \left(\sum_{k=0}^{\infty} a_kh_k(\tau)\right) \left(\sum_{k=0}^{\infty} b_kh_k(\tau)\right)\mathrm{d}\tau \\
        &= \int_0^1 \sum_{k=0}^{\infty} a_kb_kh_k^2(\tau)\mathrm{d}\tau \\
        &= \sum_{k=0}^{\infty} a_kb_k\int_0^1 h_k^2(\tau)\mathrm{d}\tau \\
        &= \sum_{k=0}^{\infty} a_kb_k
    \end{aligned}
    $$

    而

    $$
        a_k = \int_0^1 \phi_s(\tau)h_k(\tau)\mathrm{d}\tau = \int_0^s h_k(\tau)\mathrm{d}\tau = s_k(s),\quad b_k = s_k(t)
    $$

    由此得证。

为了正式证明所构造的 $W(\cdot)$ 的级数表示的一致收敛性了，需要如下的引理。

!!! abstract "Lemma 3"
    设 $\{a_k\}_{k=0}^{\infty}$ 是满足如下性质的实数序列：$\exists$ 常数 $C > 0$ 和 $0\leqslant \delta < 1/2$ 使得 $\forall\: k\in \mathbb{N}^+$ 有

    $$
    |a_k|\leqslant Ck^\delta
    $$

    那么对于 $0\leqslant t\leqslant 1$，以下函数项级数一致收敛 (converge uniformly): 

    $$
    \sum_{k=0}^{\infty} a_ks_k(t)
    $$

??? general "Proof"

    从前面的 $h_k$ 和 $s_k$ 示例的图像中，我们可以看出对于所有正整数 $k\in [2^n, 2^{n+1})$，$s_k$ 的支撑集都是不相交的，因此这系列 $k$ 决定的 $a_ks_k(t)$ 中至多只有一项非零。给定这样 $k$ 的范围，$|s_k(t)|$ 的最大值前面已经给出，而对于 $a_k$ 我们有

    $$
        \max\limits_{2^n \leqslant k < 2^{n+1}} |a_k| \leqslant C(2^{n+1})^\delta
    $$

    于是可以得到

    $$
    \begin{aligned}
        \sum_{k=2^m}^{\infty} |a_k|\cdot |s_k(t)|
        \leqslant & \sum_{n=m}^{\infty} \max\limits_{2^n \leqslant k < 2^{n+1}} |a_k|  \cdot \max\limits_{2^n \leqslant k < 2^{n+1}} |s_k(t)|\\
        \leqslant & C\sum_{n=m}^{\infty} (2^{n+1})^\delta \cdot 2^{-n/2-1} \\
        = & 2^{\delta - 1}C\sum_{n=m}^{\infty} \left[2^{(\delta - 1/2)}\right]^n \\
        = & 2^{\delta - 1}C \cdot \frac{2^{m(\delta - 1/2)}}{1 - 2^{(\delta - 1/2)}}
    \end{aligned}
    $$

    第一行即考虑到 $k\in [2^n, 2^{n+1})$ 时最多只有一个 $k$ 可以使得 $a_k s_k(t)$ 非零，对这一项进行放缩即可。第三到第四行应用了几何级数的公式（等比数列求和）。注意 $\delta$ 为常数，因此当 $m$ 足够大时，以上优级数的余项和可以被控制在任意小的 $\varepsilon > 0$ 内，因此通过优级数判别法可以得到函数项级数 $\sum a_k s_k(t)$ 一致收敛。

有了 Lemma 3，就只需要再证明用于构造 $W(\cdot)$ 的级数的各系数 $A_k$ 满足 Lemma3 的条件了。当然，因为 $A_k$ 实际上是一系列随机变量，因此满足条件的形式上略有不同。

!!! abstract "Lemma 4"
    设 $\{A_k\}_{k=0}^{\infty}$ 是 i.i.d. 地服从 $N(0, 1)$ 分布的一系列随机变量，那么对于 almost every 样本点 $\omega$ 有

    $$
    |A_k(\omega)| = O(\sqrt{\ln k}), \quad k\to \infty
    $$

由于 $k$ 足够大时，$\sqrt{\ln k}\leqslant Ck^{1/4}$，因此 $\{A_k\}_{k=0}^{\infty}$ almost surely 满足 Lemma 3 的条件。

??? general "Proof"
    首先对于给定的 $x>0$，对于 $P(|A_k|>x)$ 进行一个比较松的放缩：

    $$
    \begin{aligned}
        P(|A_k| > x) 
        &= \frac{2}{\sqrt{2\pi}}\int_x^{+\infty} e^{-s^2/2}\mathrm{d}s \\
        &\leqslant \frac{2}{\sqrt{2\pi}} e^{-x^2/4} \int_x^{+\infty} e^{-s^2/4}\mathrm{d}s \\
        &\leqslant C e^{-x^2/4}
    \end{aligned}
    $$

    这里的 $C$ 是某个常数。第一行考虑了 $A_k > x$ 和 $A_k < -x$，第二行的无穷积分显然依然是收敛的。这样，取 $x=4\sqrt{\ln k}$，就有

    $$
        P(|A_k|\geqslant 4\sqrt{\ln k}) \leqslant Ce^{-4\ln k} = \frac{C}{k^4}
    $$

    由于 $\sum P(|A_k|\geqslant 4\sqrt{\ln k}) \leqslant \sum C/k^4<\infty$，根据 Borel-Cantelli 引理就有

    $$
        P(|A_k| \geqslant 4\sqrt{\ln k}\text{ i.o.}) = 0
    $$

    这意味着样本点 $\omega$ 使得存在无限多个 $k$ 满足 $|A_k(\omega)|\geqslant 4\sqrt{\ln k}$ 的概率为 0。也就是说，对于 almost every $\omega$，都仅有有限个 $k$ 满足这个关系式。取这有限个 $k$ 中的最大值 $K(\omega)$（意为 $K$ 取决于给定的 $\omega$），有

    $$
    |A_k(\omega)| \leqslant 4\sqrt{\ln k}, \quad k > K(\omega)
    $$

    由此完成了证明。

有了以上的引理准备，我们最终可以用如下定理的形式说明我们关于所构造的 $W(\cdot)$ 的结论。

!!! abstract "构造布朗运动"
    令 $\{A_k\}_{k=0}^{\infty}$ 是一系列相互独立的 $N(0, 1)$ 随机变量，定义于相同概率空间。则级数

    $$
        W(t, \omega) := \sum_{k=0}^{\infty} A_k(\omega) s_k(t)
    $$

    在 almost every $\omega$ 下都关于 $t$ 一致收敛，并且有结论

    1. $W(\cdot)$ 是 $t\in [0, 1]$ 上的布朗运动
    2. 对于 a.e. $\omega$，采样路径 $t\mapsto W(t, \omega)$ 是连续的 

??? general "Proof"
    对于级数的一致收敛性，结合 Lemma 3 和 Lemma 4 就可以得到证明，而且采样路径的连续性也成为了其导出结论。
    
    > 对于采样路径的连续性，将在下一节 ([Sample Path Properties](#sample-path-properties)) 中详细阐述。

    接下来将重点阐述 $W(\cdot)$ 符合布朗运动定义中的三条性质。

    首先，任意 $k$ 都有 $s_k(0)=0$，所以 a.e. $\omega$ 有 $W(0, \omega)=\sum A_k(\omega)\cdot 0 = 0$。

    为了证明任意 $0\leqslant s \leqslant t \leqslant 1$ 都有 $W(t) - W(s)\sim N(0, t-s)$，我们使用特征函数的方法：

    $$
    \begin{aligned}
        \phi_{W(t) - W(s)}(\lambda)
        &= \mathbb{E}(e^{i\lambda(W(t) - W(s))}) \\
        &= \mathbb{E}\left(e^{i\lambda\sum A_k(s_k(t) - s_k(s))}\right) \\
        &= \prod \mathbb{E}\left(e^{i\lambda A_k(s_k(t) - s_k(s))}\right) & \text{independence}\\
        &= \prod e^{-\frac{1}{2}\lambda^2(s_k(t) - s_k(s))^2} & \text{$A_k\sim N(0, 1)$}\\
        &= e^{-\frac{1}{2}\lambda^2\sum (s_k(t) - s_k(s))^2} \\
        &= e^{-\frac{1}{2}\lambda^2\sum (s_k^2(t) - 2 s_k(t) s_k(s) + s_k^2(s))^2} \\
        &= e^{-\frac{1}{2}\lambda^2\sum (t - 2s + s)} & \text{Lemma 2}\\
        &= e^{-\frac{1}{2}\lambda^2(t-s)}
    \end{aligned}
    $$

    得到的结果是标准的 $N(t-s)$ 的特征函数，所以得证。

    前面完成了 Gaussian increments 的证明，最后证明 independent increments，即对于任意 $\:m\in \mathbb{N}^+$, $0=t_0<t_1<\cdots<t_m\leqslant 1$ 有 $W(t_1), \cdots, W(t_m) - W(t_{m-1})$ 相互独立。只需要证明

    $$
        F_{W(t_1), \cdots, W(t_m) - W(t_{m-1})} = \prod F_{W(t_j) - W(t_{j-1})}
    $$

    依然使用特征函数的方法，只需要证明

    $$
    \mathbb{E}\left( e^{i\sum \lambda_j (W(t_j) - W(t_{j-1}))} \right) = \prod e^{-\frac{1}{2}\lambda_j^2(t_j - t_{j-1})}
    $$

    下面以证明 $m=2$ 为例，其他情况完全类似：

    $$
    \begin{aligned}
        \mathbb{E}\left( e^{i[\lambda_1 W(t_1) + \lambda_2(W(t_2) - W(t_1))]} \right)
        &= \mathbb{E}\left( e^{i[(\lambda_1 - \lambda_2)W(t_1) + \lambda_2W(t_2)]} \right) \\
        &= \mathbb{E}\left( e^{i[(\lambda_1 - \lambda_2)\sum A_k s_k(t_1) + \lambda_2\sum A_k s_k(t_2)]} \right) \\
        &= \mathbb{E}\left( e^{i\sum A_k[(\lambda_1 - \lambda_2)s_k(t_1) + \lambda_2s_k(t_2)]} \right) \\
        &= \prod \mathbb{E}\left( e^{iA_k[(\lambda_1 - \lambda_2)s_k(t_1) + \lambda_2s_k(t_2)]} \right) \\
        &= \prod e^{-\frac{1}{2}[(\lambda_1 - \lambda_2)s_k(t_1) + \lambda_2s_k(t_2)]^2} \\
        &= e^{-\frac{1}{2}\sum (\lambda_1 - \lambda_2)^2s_k^2(t_1) + 2(\lambda_1 - \lambda_2)\lambda_2s_k(t_1)s_k(t_2) + \lambda_2^2s_k^2(t_2)} \\
        &= e^{-\frac{1}{2}\left[(\lambda_1 - \lambda_2)^2t_1 + 2(\lambda_1 - \lambda_2)\lambda_2 t_1 + \lambda_2^2 t_2\right]} \\
        &= e^{-\frac{1}{2}(\lambda_1^2 t_1 + \lambda_2^2 (t_2 - t_1))} \\
    \end{aligned}
    $$

最后，我们还需要把所构造的 $t\in[0, 1]$ 上的布朗运动扩充到 $t\in [0, +\infty)$ 上。

!!! abstract "一维布朗运动的存在性"
    对于概率空间 $(\Omega, \mathcal{U}, P)$，在其上定义可数无穷多个相互独立的 $N(0, 1)$ 随机变量 $\{A_k\}_{k=0}^{\infty}$，则存在一个定义于 $\omega\in \Omega, t\geqslant 0$ 的一维布朗运动 $W(\cdot)$。

!!! general "Outline of Proof"
    将 $[0, +\infty)$ 间隔为 $1$ 进行分割，每个区域的随机变量系数序列都是 i.i.d. 的，只需要让基函数 $s_k$ 关于 $t$ 进行平移变换即可。具体地，只需要让

    $$
    W(t) := W(n-1) + W^n (t-(n-1)),\quad n-1\leqslant t \leqslant n
    $$

    注意这里的 $W^n$ 只是表示标号为 $n$ 而已。这样定义的 $W(\cdot)$ 就是 $t\geqslant 0$ 的一维布朗运动了。

### Brownian Motion in $\mathbb{R}^n$

要把 $\mathbb{R}$ 上的一维布朗运动扩展到 $\mathbb{R}^n$ 上的 $n$ 维布朗运动，其实是非常直接的。

!!! info "$n$ 维布朗运动"
    对于 $\mathbb{R}^n$-valued 随机过程 $\bm W(\cdot) = (W^1(\cdot), \cdots, W^n(\cdot))$，如果满足

    1. $W^k(\cdot)$ 是 $\mathbb{R}$ 上的一维布朗运动
    2. $\sigma$-代数 $\mathcal{W}^k := \mathcal{U}(W^k(t)|t\geqslant 0)$ 之间相互独立，$k=1, \cdots, n$

    > 即每条分路径都独立采样

下面简单地阐述 $n$ 维布朗运动的计算。

!!! abstract "Lemma"
    给定 $n$ 维布朗运动 $\bm W(\cdot)$，对于 $\forall k, l=1, \cdots, n$，有

    $$
    \begin{aligned}
        \mathbb{E}(W^k(t)W^l(s)) & = (t\wedge s)\delta_{kl} \\
        \mathbb{E}((W^k(t) - W^k(s))(W^l(t) - W^l(s))) & = (t-s)\delta_{kl}\quad (t\geqslant s\geqslant 0)
    \end{aligned}
    $$

!!! general "Outline of Proof"
    对于 $k=l$ 的情况，就是单个一维布朗运动的性质，因此我们只需要处理 $k\neq l$ 的情况。然而，根据定义，$W^k(t), W^k(s), W^l(t), W^l(s)$ 之间都是相互独立的，因此就非常容易证明了，在此略去具体的证明。

!!! abstract "$n$ 维布朗运动的计算"
    给定 $n$ 维布朗运动 $\bm W(\cdot)$，则对于 $\forall t > 0$ 有 $\bm W(t)\sim N(0, tI)$，且任意 Borel 集 $A\subseteq \mathbb{R}^n$ 都有

    $$
        P(\bm W(t)\in A) = \frac{1}{(2\pi t)^{n/2}}\int_A e^{-\frac{1}{2t}|\bm x|^2}\mathrm{d}\bm x
    $$

    更一般地，对于 $m\in \mathbb{N}^+$ 和函数 $f: \mathbb{R}^n\times \mathbb{R} ^n\times \cdots \mathbb{R}^n\to \mathbb{R}$，我们有

    $$
    \begin{aligned}
        &\mathbb{E}(f(\bm W(t_1), \cdots, \bm W(t_m))) \\
        =& \int_{\mathbb{R}^n} \cdots \int_{\mathbb{R}^n} f(\bm x_1, \cdots, \bm x_m) g(x_1, t_1 | 0)g(x_w, t_2 - t_1 | x_1)\cdots g(x_m, t_m - t_{m-1} | x_{m-1})\mathrm{d}\bm x_1\cdots \mathrm{d}\bm x_m
    \end{aligned}
    $$

    其中

    $$
        g(x, t | y) = \frac{1}{(2\pi t)^{n/2}}e^{-\frac{1}{2t}|x-y|^2}
    $$

??? general "Proof"
    对于每个点 $(x_1, \cdots, x_n)\in \mathbb{R}^n$，考虑 $\bm W(t)$ 的密度函数

    $$
    \begin{aligned}
        f_{\bm W(t)}(x_1, \cdots, x_n)
        &= f_{W^1(t)}(x_1)\cdots f_{W^n(t)}(x_n) \\
        &= \frac{1}{(2\pi t)^{1/2}}e^{-\frac{1}{2t}x_1^2}\cdots \frac{1}{(2\pi t)^{1/2}}e^{-\frac{1}{2t}x_n^2} \\
        &= \frac{1}{(2\pi t)^{n/2}}e^{-\frac{1}{2t}(|x_1|^2 + \cdots + |x_n|^2)} \\
        &= \frac{1}{(2\pi t)^{n/2}}e^{-\frac{1}{2t}|\bm x|^2} = g(\bm x, t | 0)
    \end{aligned}
    $$

    对于更普遍的情况，模仿一维布朗运动的计算推导过程即可，请读者自证。

## Sample Path Properties

布朗运动的采样路径具有一定的 Hölder 连续性，为了详细阐述与证明，需要首先阐明 Hölder 连续性的定义。

> 可以参考 [Hölder condition - Wikipedia](https://en.wikipedia.org/wiki/H%C3%B6lder_condition)，另外对于各种连续性在本笔记的 [Continuities](../../analysis/continuities.md) 中也有详细的阐述

!!! info "Hölder Continuity"
    考虑函数 $f:[0, T]\to \mathbb{R}$ 与 $0 < \gamma \leqslant 1$：

    **(1)** 如果存在常数 $K$ 使得下式成立，则称 $f$ 是 $\:\gamma$-Hölder 一致连续 (uniformly $\:\gamma$-Hölder continuous) 的：

    $$
    |f(t) - f(s)| \leqslant K|t-s|^\gamma, \quad \forall t, s\in [0, T]
    $$

    **(2)** 如果存在常数 $K$ 使得下式成立，则称 $f$ 是在 $s$ 点是 $\:\gamma$-Hölder 连续的：

    $$
    |f(t) - f(s)| \leqslant K|t-s|^\gamma, \quad \forall t\in [0, T]
    $$

对于随机过程的采样路径的 Hölder 连续性，Kolmogorov 连续性定理常常被使用：

!!! abstract "Kolmogorov continuity theorem"
    asd

> 详见 [Kolmogorov continuity theorem - Wikipedia](https://en.wikipedia.org/wiki/Kolmogorov_continuity_theorem)

## Markov Property
