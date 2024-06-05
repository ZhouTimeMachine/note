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
    - 由对称性 $f(y, \tau) = f(-y, \tau)$，$f(y, \tau)$ 关于 $y$ 的一阶矩（期望）为

    $$
    \int_{-\infty}^{+\infty} y f(y, \tau) \mathrm{d}y = 0
    $$

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

这就是**扩散方程 (diffusion equation)**，也称**热方程 (heat equation)**。在同作者的 PDE 书的 [2.3 节](../../PDE/4linearPDEs/#heat-equation)给出了这类方程的解法，在这里直接给出它的解：

$$
u(x, t) = \frac{1}{(2\pi Dt)^{1/2}}e^{-\frac{x^2}{2Dt}}
$$

从中可见，在 $t$ 时刻扩散的墨水的密度服从 $N(0, Dt)$ 的分布。关于常数 $D$，[Einstein relation](https://en.wikipedia.org/wiki/Einstein_relation_(kinetic_theory)) 揭示了

$$
D=\mu k_B T
$$

??? general "各符号的解释"
    - $\mu$: “流动性 (mobility)”，其表达式为 $v_d/F$
        - $v_d$ 是粒子的 terminal drift velocity，terminal velocity 即流体中从静止受力加速后能达到的最大平衡速度
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

### Mathematical Justification

利用 [De Moivre-Laplace 中心极限定理](../../../../courses/probability/prob_lim/#de-moivre-laplace)，可以给出随机游走到特定时间位置的概率分布的一种更概率论的推导方式。

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

再次导出 $t$ 时刻的位置满足 $N(0, Dt)$ 的分布。

## Definition, Elementary Properties

### Definition & Computation

!!! info "Brownian Motion/Wiener Process"
    **布朗运动 (Brownian motion)**，或**维恩过程 (Wiener process)** 是满足如下条件的实值随机过程 $W(\cdot)$：

    1. $W(0)=0$ a.s.
    2. (Gaussian increments) $W(t) - W(s)\sim N(0, t-s), \quad \forall\; t\geqslant s\geqslant 0$
    3. (independent increments) $W(t_1), W(t_2) - W(t_1), \cdots, W(t_n) - W(t_{n-1})$ are independent for all times $0\leqslant t_1 < t_2 < \cdots < t_n$

!!! tip "a.s. 是 [almost surely](../intro_prob/#probability-space) 的缩写"

中心极限定理提供了如此定义布朗运动的动机：由一系列合适地缩放了的独立随机分布的和构成的位置随机变量，服从正态分布。

### More on White Noise



## Construction of Brownian Motion

## Sample Path Properties

## Markov Property
