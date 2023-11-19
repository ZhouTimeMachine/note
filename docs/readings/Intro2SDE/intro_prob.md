<link rel="stylesheet" href="../../../css/counter.css" />

# An Introduction to Stochastic Differential Equations

!!! info "Part of note of *An Introduction to Stochastic Differential Equations*, Lawrence C. Evans"

!!! warning "本页面还在施工中"

## Introduction

### Deterministic and Random Differential Equations

关注系统状态 $\bm x$ 关于时间 $t$ 变化的 ODE:

$$
\begin{cases}
    \dot{\bm x}(t) = \bm b (\bm x(t)) \quad (t>0)\\
    \bm x (0) = \bm x_0
\end{cases}
$$

!!! abstract "向量场 (vector field)"
    给定 $S\subseteq \mathbb{R}^n$, 则标准笛卡尔坐标 $(x_1,\cdots,x_n)$ 下的 $V: S\to \mathbb{R}^n$ 被称为**向量场**。

    若 $V$ 的每个分量都连续，则称为**连续向量场**。同理有**光滑向量场**。

!!! abstract "光滑 (smooth)"
    考虑可微函数类 $C^k$，即 $f\in C^k$ 等价于 $f', f'', f^{(k)}$ 都存在且连续。

    $f$ 光滑即指 $f\in C^{\infty}$，即**无限阶可微**。

$\bm b: \mathbb{R}^n \to \mathbb{R}^n$ 为光滑向量场。将能够确定**轨迹 (trajectory)** $\bm x: [0, \infty)\to \mathbb{R}^n$。

<div style="text-align:center;">
    <img src="../../imgs/Intro2SDE/trajectory.png" alt="trajectory" style="zoom:50%;" />
</div>

然而实践中，由于**随机扰动 (random perturbations)** 的存在，往往不精准地位于轨迹上。考虑随机扰动之后，就可以得到

$$
\begin{cases}
    \dot{\bm X}(t) = \bm b (\bm X(t)) + \bm B (\bm X(t))\bm\xi(t) \quad (t>0)\\
    \bm X (0) = \bm X_0
\end{cases}
$$

其中 $\bm B: \mathbb{R}^n \to \mathbb{R}^{n\times m}$，映射到一个 $n\times m$ 矩阵。针对这个方程组有问题：

- 定义 $\xi(\cdot)$ ($m$ 维“白噪声”)
- 定义解得的 $X(\cdot)$ 的意义
- 讨论解的存在性，唯一性，渐进 (asymptotic) 行为

### Stochastic Differentials

若令 $m=n, \bm X_0=0, \bm b\equiv 0, \bm B \equiv I$，那么此时的 $\bm X$ 具有了**布朗运动 (Bronwian motion)** 或者说**维恩过程 (Wiener process)** 的意义，重写为 $\bm W(\cdot)$，有

$$
    \dot{\bm W} = \bm \xi (\cdot)
$$

所以，**“白噪声” 实际上是布朗运动关于时间的导数**。将“白噪声”这样替换，就可以得到

$$
\begin{cases}
    \mathrm{d}\bm X(t) = \bm b (\bm X(t)) \mathrm{d}t + \bm B (\bm X(t))\mathrm{d}\bm W(t) \quad (t>0)\\
    \bm X (0) = \bm X_0
\end{cases}
$$

这就是**随机微分方程** (stochastic differential equations, SDE)。其中，$\mathrm{d}\bm W$ 或者 $\bm B\mathrm{d}\bm W$ 被称为**随机微分** (stochastic differential)。解写作

$$
\bm X(t) = \bm X_0 + \int_0^t \bm b(\bm X (s))\mathrm{d}s + \int_0^t \bm B (\bm X(t))\mathrm{d}\bm W(t)
$$

为了使这个形式的解有意义（良定义），我们需要

- 构造布朗运动 $\bm W(\cdot)$：Chap3
- 定义随机积分 (stochastic integral) $\int_0^t\cdots \mathrm{d}\bm W$：Chap4
- 解的存在性：Chap5

对于这个解的实际意义，存在以下问题

- SDE 是否真的在建模物理问题？
- “白噪声” $\bm \xi$ 是否真的是白噪声，还是只是一系列光滑高震荡函数的组合？：Chap6

### Itô's Chain Rule

在 SDE 中，链式法则并不是 trivial 的。为了便于理解，以 $n=m=1$ 的简单情况为例介绍

$$
\mathrm{d}X = b(X)\mathrm{d}t + \mathrm{d}W
$$

给定 $Y(t)=u(X(t))$, $u: \mathbb{R}\to\mathbb{R}$ 是一个给定的光滑函数。按照 trivial 的链式法则，你或许会认为

$$
\mathrm{d}Y = u'\mathrm{d}X=u'b\mathrm{d}t+u'\mathrm{d}W
$$

!!! warning "注意上面的式子是错的"

上面的式子错误，主要来自于一个非常规 (irregular) “事实”：布朗运动的微分近似于根号的时间微分

$$
\mathrm{d} W\approx \sqrt{\mathrm{d}t}
$$

!!! tip "常规链式法则"
    常规链式法则实际上来自泰勒展开后省略高阶小量。即

    $$
    \begin{aligned}
        Y + \mathrm{d}Y
        &= u(X + \mathrm{d}X) \\
        &= u(X) + u'\mathrm{d}X + \frac{1}{2}u''(\mathrm{d}X)^2 + \cdots\\
        &\approx u(X) + u'\mathrm{d}X
    \end{aligned}
    $$

    由于 $X$ 关于 $t$ 再展开至少也是一阶，所以可以直接在 $X$ 的层面消除高阶小量。

然而此时泰勒展开后有

$$
\begin{aligned}
    \mathrm{d}Y
    &= u'\mathrm{d}X + \frac{1}{2}u''(\mathrm{d}X)^2 + \cdots\\
    &\approx u'(b(X)\mathrm{d}t + \mathrm{d}W) + \frac{1}{2}u''(b(X)\mathrm{d}t + \mathrm{d}W)^2 + \cdots\\
    &\approx \left(u'b + \frac{1}{2}u''\right)\mathrm{d}t + u'\mathrm{d} W + o((\mathrm{d}t)^{3/2})
\end{aligned}
$$

高阶项可以略去。这种奇怪的链式法则就是 Itô's Chain Rule 的一个实例化。

??? example "Example1"
    使用 Itô's Chain Rule 可以解得
    
    $$
    \begin{cases}
        \mathrm{d}Y = Y\mathrm{d}W \\
        Y(0) = 1
    \end{cases}
    \Rightarrow
    Y(t) := e^{W(t)-\frac{t}{2}}
    $$

    而不是普通的
    
    $$
        Y(t) := e^{W(t)}
    $$

??? example "Example2"
    设 $S(t)$ 为 $t$ 时刻股价 (price of **stock**)，一个标准模型认为 $\frac{\mathrm{d}S}{S}$ 对特定的 $\mu>0$ 和 $\sigma$ 满足

    $$
        \frac{\mathrm{d}S}{S} = \mu \mathrm{d}t + \sigma \mathrm{d}W
    $$
    
    所以有 SDE

    $$
    \begin{cases}
        \mathrm{d}S = \mu S\mathrm{d}t + \sigma S\mathrm{d}W \\
        S(0) = S_0
    \end{cases}
    \Rightarrow
    Y(t) := e^{W(t)-\frac{t}{2}}
    $$

    使用 Itô's Chain Rule 可以解得

    $$
        S(t) = S_0e^{\sigma W(t)+(\mu-\frac{\sigma^2}{2})t}
    $$

    <div style="text-align:center;">
        <img src="../../imgs/Intro2SDE/stock_trajectory.png" alt="stock_trajectory" style="zoom:50%;" />
    </div>

## A Crash Course in Probability Theory