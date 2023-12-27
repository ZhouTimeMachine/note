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

??? general "零至二阶矩的考虑"

    - 零阶矩 $\int_{-\infty}^{+\infty} f(y, \tau) \mathrm{d}y = 1$ （概率密度函数）
    - 由对称性 $f(y, \tau) = f(-y, \tau)$，$f(y, \tau)$ 关于 $y$ 的一阶矩（期望）为

    $$
    \int_{-\infty}^{+\infty} y f(y, \tau) \mathrm{d}y = 0
    $$

    - 考虑二阶矩（方差），假定关于 $\tau$ 是线性的

    $$
    \int_{-\infty}^{+\infty} y^2 f(y, \tau) \mathrm{d}y = D\tau
    $$

    这里的 $D>0$ 是一个正常数，并不是求导算子。

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

### Mathematical Justification

## Definition, Elementary Properties

## Construction of Brownian Motion

## Sample Path Properties

## Markov Perperty