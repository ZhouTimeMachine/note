<link rel="stylesheet" href="../../../../css/counter.css" />

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
    <img src="../../../imgs/Intro2SDE/trajectory.png" alt="trajectory" style="zoom:50%;" />
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
        <img src="../../../imgs/Intro2SDE/stock_trajectory.png" alt="stock_trajectory" style="zoom:50%;" />
    </div>

## A Crash Course in Probability Theory

### Basic Definitions

#### Probability Space

Bertrand's paradox 说明，“随机”只有在确定的概率空间下才确定。给定同心的大圆和小圆，大圆的弦与小圆相交的概率在不同概率空间下有不同的答案。

!!! info "概率空间 (probability space)"
    若 Triple $(\Omega,\mathcal{U},P)$

    $$
    (\Omega,\mathcal{U},P)
    $$

    满足

    - $\Omega\neq\emptyset$
    - $\mathcal{U}$ 是关于 $\Omega$ 子集的 $\sigma$-algebra
    - $P$ 是 $\mathcal{U}$ 上的概率测度

    则 $(\Omega,\mathcal{U},P)$ 被称为**概率空间**。

$\sigma$-algebra $\mathcal{U}$ 可以理解为合法事件集，正式定义为

??? info "$\sigma$-algebra"

    $\sigma$-algebra $\mathcal{U}\subseteq\Omega$ 需满足以下性质:

    1. $\emptyset, \Omega\in \mathcal{U}$
    2. If $A\in \mathcal{U}$, then $A^c\in \mathcal{U}$.
    3. If $A_1, A_2, \cdots \in \mathcal{U}$, then

    $$
    \bigcup_{k=1}^{\infty}A_k,\bigcap_{k=1}^{\infty}A_k\in\mathcal{U}.
    $$

    这里 $A^{c}:=\Omega-A$，为补集的含义。

概率测度 $P$ 是一个从 $\mathcal{U}$ 到 $[0, 1]$ 的映射，可以给出任何合法事件的一个“概率”，正式定义为

??? info "概率测度 (probability measure)"
    令 $\mathcal{U}$ 为关于 $\Omega$ 子集的 $\sigma$-algebra，则称

    $$
    P:{\mathcal{U}}\to[0,1]
    $$

    为**概率测度 (probability measure)**，若满足:
    
    (1) $\:P(\emptyset)=0,P(\Omega)=1.$

    (2) If $A_1,A_2,\ldots\in\mathcal{U}$, then
    
    $$ 
        P\left(\bigcup_{k=1}^{\infty}A_k\right) \leqslant \sum_{k=1}^{\infty} P (A_k)
    $$
    
    (3) If $A_1,A_2,\ldots$ are **disjoint** sets in $\mathcal{U}$, then
    
    $$ 
        P\left(\bigcup_{k=1}^{\infty}A_k\right) = \sum_{k=1}^{\infty} P (A_k)
    $$

    It follows that if $A,B\in\mathcal{U}$, then

    $$
    A\subseteq B\Rightarrow P(A)\leq P(B).
    $$

由此产生了一些术语 (terminology)：

- 集合 $A\in\mathcal{U}$ 被称为**事件 (event)**，点 $\omega\in\Omega$ 被称为样本点 (sample points)
- $P(A)$ 是事件 $A$ 的**概率 (probability)**
- $P(A^c)=0$，则认为 $A$ **几乎必然 (almost surely, a.s.)**

??? example "Examples"
    书上提供了 4 个例子：

    - 有限点集的测度
    - Borel $\sigma$-algebra，概率密度函数
    - Dirac measure，或 Dirac point mass
    - Buffon's needle problem

#### Random Variables

!!! info "Borel $\sigma$-algebra"
    Borel $\sigma$-algebra $\mathcal{B}\:$ 表示最小的 $\mathbb{R}^n$ 子集构成的 $\:\sigma$-algebra，包含了所有的开集。

!!! info "随机变量 (random variable)"
    在概率空间 $(\Omega,\mathcal{U},P)$ 下，$\mathcal{U}$-可测函数

    $$
        \bm X: \Omega\to \mathbb{R}^n
    $$

    被称为 $n$ 维随机变量。

??? info "可测 (measurable)"
    测度论中，一个集合 $A$ 可测指的是 $A\in\mathcal{U}$。
    
    随后定义可测函数：在测度空间 $(\Omega,\mathcal{U},P)$ 下，考虑 $\bm X: \Omega\to \mathbb{R}^n$，若 $\:\forall B\in\mathcal{B}$, 

    $$
        \bm X^{-1}(B) = \{\omega: X(\omega)\in B\}\in\mathcal{U}
    $$

    那么就称 $\bm X$ 为 $\:\mathcal{U}$-可测 ($\,\mathcal{U}$-measurable)。即对 $\mathbb{R}$ 上任意开集 $B$ 的逆像可测。

!!! tip "remark"
    - 这里的随机变量 (random variable) 包括中文语境中的一元随机变量和多元随机向量
    - $P(\bm X^{-1}(B))$ 往往写作
    
    $$
        P(\bm X\in B)
    $$

    赋与开集在 $\bm X$ 的逆像的概率测度以意义：$\bm X$ 取值落在这个开集中的概率。

通过随机变量 $\bm X$ 可以生成 $\:\sigma$-algebra $\mathcal{U}(\bm X)$，它“包含了所有 $\bm X$ 的相关**信息**”。

??? info "生成 $\:\sigma$-algebra"
    由 $\bm X$ 生成的 $\:\sigma$-algebra $\:\mathcal{U}(\bm X)$ 定义为

    $$
        \mathcal{U}(\bm X):=\{\bm X^{-1}(B) \;|\; B\in\mathcal{B}\}
    $$

    如果随机变量 $\bm Y$ 是 $\bm X$ 的函数，即 $\bm Y = \phi (\bm X)$，那就意味着 $\bm Y$ 是 $\:\mathcal{U}(\bm X)$-可测的。
    
    反之，如果 $\bm Y$ 是 $\:\mathcal{U}(\bm X)$-可测的，那么将会存在函数 $\phi$ 使得 $\bm Y = \phi(\bm X)$，即如果确定 $X(\omega)$ 的值，那么 $\bm Y$ 的值也将被确定，尽管我们不一定能实际构造出这个 $\phi$。

#### Stochastic Processes

!!! info "随机过程 (stochastic process) 与采样路径 (sample path)"
    - 随机变量集合 $\{\bm X(t) \;|\; t\geqslant 0\}$ 被称为**随机过程 (stochastic process)**
    - 给定样本点 $\:\omega\in \Omega$, 映射 $t\to \bm X(\omega, t)$ 被称为**采样路径 (sample path)**

<div style="text-align:center;">
    <img src="../../../imgs/Intro2SDE/sample_paths.png" alt="sample_paths" style="zoom:70%;" />
</div>

### Expected Value, Variance

!!! warning "本小节还在施工中"