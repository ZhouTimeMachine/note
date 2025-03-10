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
    若 Triple $(\Omega, \mathcal{U}, P)$

    $$
    (\Omega, \mathcal{U}, P)
    $$

    满足

    - $\Omega\neq\emptyset$
    - $\mathcal{U}$ 是关于 $\Omega$ 子集的 $\sigma$-algebra
    - $P$ 是 $\mathcal{U}$ 上的概率测度

    则 $(\Omega, \mathcal{U}, P)$ 被称为**概率空间**。

$\sigma$-algebra $\;\mathcal{U}\;$ 可以理解为合法事件集，正式定义为

!!! info "$\sigma$-algebra"

    $\sigma$-algebra $\;\mathcal{U}\subseteq 2^{\Omega}\;$ 需满足以下性质:

    1. $\emptyset, \;\Omega\in \mathcal{U}$
    2. If $A\in \mathcal{U}$, then $A^c\in \mathcal{U}$.
    3. If $A_1, A_2, \cdots \in \mathcal{U}$, then

    $$
    \bigcup_{k=1}^{\infty}A_k,\; \bigcap_{k=1}^{\infty}A_k\in\mathcal{U}.
    $$

    这里 $A^{c}:=\Omega-A$，为补集的含义。

    > 一种更简单的定义方式为，$\sigma$-algebra $\;\mathcal{U}\;$即为 $\Omega$ 的子集族，其中 $\Omega\in \mathcal{U}$，且 $\mathcal{U}$ 在补、可数交、可数并操作下封闭。

概率测度 $P$ 是一个从 $\mathcal{U}$ 到 $[0, 1]$ 的映射，可以给出任何合法事件的一个“概率”，正式定义为

!!! info "概率测度 (probability measure)"
    令 $\mathcal{U}$ 为关于 $\Omega$ 子集的 $\;\sigma$-algebra，则称

    $$
    P:{\mathcal{U}}\to[0,1]
    $$

    为**概率测度 (probability measure)**，若满足:
    
    **(1)** $P(\emptyset)=0,\;P(\Omega)=1.$

    **(2)** 若 $A_1,A_2,\ldots\in\mathcal{U}$，则
    
    $$ 
        P\left(\bigcup_{k=1}^{\infty}A_k\right) \leqslant \sum_{k=1}^{\infty} P (A_k)
    $$
    
    **(3)** (2) 式在 $A_1,A_2,\ldots\in \mathcal{U}$ 是不相交的集合时取等。

    一个简单的导出结论是若 $A,B\in\mathcal{U}$，则

    $$
    A\subseteq B\Rightarrow P(A)\leq P(B).
    $$

由此产生了一些术语 (terminology)：

- 集合 $A\in\mathcal{U}$ 被称为**事件 (event)**，点 $\omega\in\Omega$ 被称为样本点 (sample points)
- $P(A)$ 是事件 $A$ 的**概率 (probability)**
- $P(A^c)=0$，则认为 $A$ **几乎必然 (almost surely, a.s.)**

先举两个相对比较简单的例子：

!!! example "Examples"
    - 有限点集的测度：为每个点分配对应的概率，所有点的概率和为 1。一个集合（该有限点集的子集）的概率，即其中所有样本点概率的和。
    - Buffon's needle problem: 平面由无限多平行线分割，相邻平行线之间相隔 2cm。一根长度为 1cm 的针随机抛掷，求针与平行线相交的概率。问题分析中，构建概率空间、需要分析的随机变量，最后进行求解。

接下来的例子会有一些困难，因为即将引入一些后面依然会用到的概念。

!!! info "Borel $\sigma$-algebra"
    Borel $\sigma$-algebra 表示拓扑空间上最小的包含所有开集的 $\:\sigma$-algebra。

> 在拓扑空间中，任何一个可以通过开集之间的补、可数交、可数并获得的集合，都是 Borel set。Borel $\sigma$-algebra 事实上就是拓扑空间上所有 Borel set 的集合。

!!! example "Examples"
    - 使用 $\mathcal{B}$ 表示 $\mathbb{R}^n$ 上的 Borel $\;\sigma$-algebra。设 $f:\mathbb{R}^n\to \mathbb{R}$ 是一个满足 $\int_{\mathbb{R}^n} f\mathrm{d}x=1$ 的非负可积函数，则定义关于 $\mathcal{B}$ 的概率测度
    
    $$
    P(B) = \int_{B} f(x)\mathrm{d}x,\quad \forall B\in\mathcal{B}
    $$
    
    这样 $(\mathbb{R}^n, \mathcal{B}, P)$ 就构成了一个概率空间。我们称 $f$ 为关于概率测度 $P$ 的概率密度函数。

    - 同样在 $\mathbb{R}^n$ 和 $\mathcal{B}$ 下，对于定点 $x_0\in \mathbb{R}^n$ 可以定义新的测度：Dirac measure，或 Dirac point mass
    
    $$
    P(B) = \delta_{x_0}(B) =\begin{cases}
        1, & x_0\in B\\
        0, & x_0\notin B
    \end{cases}
    $$

> $n=1$ 时，$\mathcal{B}$ 实际上就是实数轴上的所有区间（开、闭、半开半闭）。

注意区分 Dirac measure 和 Dirac delta function 的区别。Dirac delta function 的定义为

$$
\delta(x) = 0, \quad x\neq 0;\quad \int_{-\infty}^{\infty}\delta(x)\mathrm{d}x = 1
$$

这是一个实际上不存在的函数，不能粗暴地定义 $\delta(0)=+\infty$。事实上，Dirac measure 和 Dirac delta function 可以通过以下关系联系起来：

$$
\delta(x) = \frac{\mathrm{d}H(x)}{\mathrm{d}x},\quad
H(x) = \begin{cases}
    1, & x\geqslant 0\\
    0, & x < 0
\end{cases}
$$

#### Random Variables

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

在这里给出指示函数 (indicator function) 和简单函数 (simple function) 两个随机变量的例子，这两个例子将在后面不带说明地出现。

!!! example "Examples"
    对于集合 $A\in\mathcal{U}$，定义**指示函数** $\bm 1_A$ 为

    $$
        \bm \chi_A(\omega) = 
        \begin{cases}
            1, & \omega\in A\\
            0, & \omega\notin A
        \end{cases}
    $$

    则指示函数可见就是一个随机变量。更一般地，对于 $A_1,A_2,\cdots,A_n\in\mathcal{U}$，且 $\Omega=\bigcup_{k=1}^n A_k$，定义**简单函数** $\bm X$ 为
    
    $$
        \bm X(\omega) = \sum_{k=1}^n a_k\bm \chi_{A_k}(\omega)
    $$

    其中 $a_k\in\mathbb{R}$，简单函数也是一个随机变量。

    > 简单函数就是多个指示函数的线性组合。

通过随机变量 $\bm X$ 可以生成 $\:\sigma$-algebra $\mathcal{U}(\bm X)$，它“包含了所有 $\bm X$ 的相关**信息**”。

!!! info "生成 $\:\sigma$-algebra"
    由 $\bm X$ 生成的 $\:\sigma$-algebra $\:\mathcal{U}(\bm X)$ 定义为

    $$
        \mathcal{U}(\bm X):=\{\bm X^{-1}(B) \mid B\in\mathcal{B}\}
    $$

    如果随机变量 $\bm Y$ 是 $\bm X$ 的函数，即 $\bm Y = \phi (\bm X)$，那就意味着 $\bm Y$ 是 $\:\mathcal{U}(\bm X)$-可测的。
    
    反之，如果 $\bm Y$ 是 $\:\mathcal{U}(\bm X)$-可测的，那么将会存在函数 $\phi$ 使得 $\bm Y = \phi(\bm X)$，即如果确定 $X(\omega)$ 的值，那么 $\bm Y$ 的值也将被确定，尽管我们不一定能实际构造出这个 $\phi$。

#### Stochastic Processes

!!! info "随机过程 (stochastic process) 与采样路径 (sample path)"
    - 随机变量集合 $\{\bm X(t) \mid t\geqslant 0\}$ 被称为**随机过程 (stochastic process)**
    - 给定样本点 $\:\omega\in \Omega$, 映射 $t\to \bm X(\omega, t)$ 被称为**采样路径 (sample path)**

<div style="text-align:center;">
    <img src="../../../imgs/Intro2SDE/sample_paths.png" alt="sample_paths" style="zoom:70%;" />
</div>

### Expected Value, Variance

#### Integration with respect to a Measure

即相对于定义好的概率测度 $P$ 的积分。给定概率空间 $(\Omega,\mathcal{U},P)$，考虑实值**简单**随机变量 $X=\sum_{i=1}^k a_i\bm \chi_{A_i}$，定义其**积分** (integral) 为

$$
\int_{\Omega} X\mathrm{d}P := \sum_{i=1}^k a_i P(A_i)
$$

进一步地，扩展 $X$ 为非负随机变量，可以用简单随机变量的积分逼近去定义它的积分：

$$
\int_{\Omega} X\mathrm{d}P := \sup\left\{\int_{\Omega} Y\mathrm{d}P \;\bigg|\; Y\leqslant X, Y \text{ is simple}\right\}
$$

最终，对于随机变量 $X: \Omega\to \mathbb{R}$，将其积分写作

$$
\int_{\Omega} X\mathrm{d}P := \int_{\Omega} X^+\mathrm{d}P - \int_{\Omega} X^-\mathrm{d}P
$$

只要右侧两个积分至少其一是有限的，那 $X$ 的积分就是一个确定的有限/无限值。这里有

$$
X^+ := \max\{X, 0\},\quad X^- = \max\{-X, 0\}
$$

从而保证了 $X=X^+-X^-$。更进一步地，给出随机向量 $\bm X = (X^1, X^2, \cdots, X^n): \Omega \to \mathbb{R}^n$ 的积分含义：

$$
\int_{\Omega} \bm X\mathrm{d}P := \left(\int_{\Omega} X^1\mathrm{d}P, \int_{\Omega} X^2\mathrm{d}P, \cdots, \int_{\Omega} X^n\mathrm{d}P\right)
$$

完成了积分的定义之后，就可以定义期望值 (expected value)，或称之为均值 (mean value)，以及方差 (variance)：

!!! info "期望和方差"
    随机向量 $\bm X: \Omega\to \mathbb{R}^n$ 的**期望值** (expected value) 定义为

    $$
    \mathbb{E}(\bm X) := \int_{\Omega} \bm X \mathrm{d}P
    $$

    其方差 (variance) 定义为

    $$
    \mathrm{Var}(\bm X) := \int_{\Omega} \left\|\bm X - \mathbb{E}(\bm X)\right\|^2 \mathrm{d}P
    $$

    $\|\cdot \|$ 代表 $\mathbb{R}^n$ 上的欧几里得范数。有方差公式

    $$
    \mathrm{Var}(\bm X) = \mathbb{E}(\|\bm X\|^2) - \|\mathbb{E}(\bm X)\|^2
    $$

#### Distribution Functions 

对于两个同维向量，定义 $x\leqslant y$ 当且仅当对应分量都满足 $x_i\leqslant y_i$。在此约定下，定义随机向量的分布函数和多个随机向量的联合分布函数。

!!! info "分布函数 (distribution function)"
    随机向量 $\bm X: \Omega\to \mathbb{R}^n$ 的**分布函数** (distribution function) $F_{\bm X}: \mathbb{R}^n\to [0, 1]$ 定义为

    $$
    F_{\bm X}(\bm x) := P(\bm X\leqslant \bm x), \quad \forall \bm x\in\mathbb{R}^n
    $$

    更一般地，对于 $n$ 个随机向量 $\bm X_1, \bm X^2, \cdots, \bm X^n$，定义**联合分布函数** (joint distribution function) 为

    $$
    F_{\bm X_1, \bm X_2, \cdots, \bm X_n}(\bm x_1, \bm x_2, \cdots, \bm x_n) := P(\bm X_1\leqslant \bm x_1, \bm X_2\leqslant \bm x_2, \cdots, \bm X_n\leqslant \bm x_n), \quad \forall \bm x_1, \bm x_2, \cdots, \bm x_n\in\mathbb{R}^n
    $$

接下来引入更好用的密度函数。

!!! info "密度函数 (density function)"
    给定随机向量 $\bm X: \Omega\to \mathbb{R}^n$ 和其分布函数 $F=F_{\bm X}$，若存在非负可积 (integrable) 函数 $f: \mathbb{R}^n\to [0, \infty)$ 满足

    $$
    F(\bm x) = F(x_1,\cdots, x_n)=\int_{-\infty}^{x_1}\cdots \int_{-\infty}^{x_n} f(y_1, \cdots, y_n)\mathrm{d}y_1\cdots\mathrm{d}y_n
    $$

    则 $f$ 就称为 $\bm X$ 的密度函数。有时候，上面这个积分也简写为

    $$
    \int_{-\infty}^{\bm x} f(\bm y)\mathrm{d}\bm y
    $$

    作为一个简单的导出结论，对于 $\forall B\in \mathcal{B}$（回顾，$\mathcal{B}$ 是 Borel 集，是 $\mathcal{R}^m$ 上最小的 $\sigma$-algebra，由全部开集构成）有

    $$
    P(\bm X\in B) = \int_{B} f(\bm x)\mathrm{d}\bm x
    $$

!!! tip "导出结论的意义"
    上面的导出结论是计算概率的一种重要方式，因为等式右侧是一个常规的积分，经常能被显式计算。

书中举了一元和多元高斯分布的密度函数作为例子，在此就不再赘述了。

!!! abstract "Lemma"
    令 $X: \Omega\to \mathbb{R}^n$ 为随机向量，假设其分布函数 $F=F_{\bm X}$ 有密度函数 $f$。对于 $g: \mathbb{R}^n\to \mathbb{R}$，如果 $g(\bm X)$ 是可积的，则

    $$
    \mathbb{E}(g(\bm X)) = \int_{\mathbb{R}^n} g(\bm x)f(\bm x)\mathrm{d}\bm x
    $$

    特别地，有

    $$
    \mathbb{E}(\bm X)=\int_{\mathbb{R}^n}xf(x) dx ,\quad \mathrm{Var}(\bm X)=\int_{\mathbb{R}^n}\|x-\mathbb{E}(\bm X)\|^2f(x) dx
    $$

??? general "Proof"
    证明思路为，若 $g$ 是简单函数时成立，则根据近似，$g$ 是任意函数时都成立。（不太严格但是能意会即可）

    则令

    $$
    g = \sum_{i=1}^m b_i\chi_{B_i}
    $$

    于是就有

    $$
    \mathbb{E}(g(\bm X)) = \sum_{i=1}^m b_i \int_{\Omega} \chi_{B_i}(\bm X)\mathrm{d}P = \sum_{i=1}^m b_i P(\bm X\in B_i)
    $$

    另一方面，又有

    $$
    \int_{\mathbb{R}^n} g(\bm x)f(\bm x)\mathrm{d}\bm x
    = \sum_{i=1}^m b_i \int_{B_i} f(\bm x)\mathrm{d}\bm x
    = \sum_{i=1}^m b_i P(\bm X\in B_i)
    $$

    于是得证。

!!! tip "Remark"
    这个引理令我们可以仅用 $\mathbb{R}^n$ 上的积分计算 $\mathbb{E}(\bm X)$ 和 $\mathrm{Var}(\bm X)$。由于我们无法直接观测概率空间，只能观测 $\bm X$ 在 $\mathbb{R}^n$ 上的取值，因此基于 $\mathbb{E}(\bm X)$ 和 $\mathrm{Var}(\bm X)$ 的观测是非常有用的。

### Independence

#### Conditional Probability and Independent Events

首先引入条件概率的概念。

!!! info "条件概率 (conditional probability)"
    考虑概率空间 $(\Omega,\mathcal{U},P)$ 和事件 $A,B\in\mathcal{U}$，定义条件概率 $P(A|B)$ 为：给定 $B$ 发生的条件下，$A$ 发生的概率。容易得知有

    $$
    P(A\mid B) := \frac{P(A\cap B)}{P(B)}
    $$

由此引入事件相互独立的意义。事件 $A$ 独立于 $B$，实际上就是在 $B$ 发生的前提下 $A$ 发生的概率，和不知道 $B$ 是否发生时 $A$ 发生的概率是一样的，即 $P(A\mid B)=P(A)$。根据条件概率的定义，可以得到 $P(A\cap B)=P(A)P(B)$。可以发现，在这个等式中，$A$ 和 $B$ 是完全对称的，所以 $B$ 独立于 $A$ 的要求也是这个式子，可以称之为“相互独立”。

!!! info "事件的相互独立"
    事件 $A$ 和 $B$ 相互独立 (independent)，当且仅当

    $$
    P(A\cap B) = P(A)P(B)
    $$

$A$ 和 $B$ 相互独立，很容易可以得到 $A^c$ 和 $B$ 相互独立，$A^c$ 和 $B^c$ 相互独立等结论。2 个事件相互独立很容易就能推广到 $n$ 个事件相互独立，而更进一步地，从事件推广到 $\;\sigma$-algebra 也是很有必要的。

!!! info "$\sigma$-algebra 的相互独立"
    $\mathcal{U}_i\subseteq \mathcal{U}$ 是一系列 $\;\sigma$-algebra。称 $\{\mathcal{U}_i\}_{i=1}^{\infty}$ 相互独立，当且仅当任选 $1 \leqslant k_1 < k_2 < \cdots < k_m$ 和任意 $A_{k_i}\in \mathcal{U}_{k_i}$，有

    $$
    P(A_{k_1}\cap A_{k_2}\cap \cdots\cap A_{k_m}) = P(A_{k_1})P(A_{k_2})\cdots P(A_{k_m})
    $$

#### Independent Random Variables

!!! info "随机变量的相互独立"
    随机变量 $\bm X_1, \bm X_2, \cdots, \bm X_n$ 相互独立，当且仅当对于 $\;\forall\; 2\leqslant k\leqslant n$, $1\leqslant i_1<\cdots < i_k \leqslant n\;$ 以及任意 Borel 集 $B_1, B_2, \cdots, B_k\in\mathcal{B}$，有

    $$
    P(\bm X_{i_1}\in B_1, \bm X_{i_2}\in B_2, \cdots, \bm X_{i_k}\in B_k) = P(\bm X_{i_1}\in B_1)P(\bm X_{i_2}\in B_2)\cdots P(\bm X_{i_k}\in B_k)
    $$

说随机变量 $\bm X_1, \bm X_2, \cdots, \bm X_n$ 相互独立，等价于说其生成 $\;\sigma$-algebra $\;\mathcal{U}(\bm X_1), \mathcal{U}(\bm X_2), \cdots, \mathcal{U}(\bm X_n)\;$ 相互独立。其中产生联系的关键为 $P(\bm X\in B)$ 即 $P(\bm X^{-1}(B))$。 

> 回顾生成 $\;\sigma$-algebra的定义：$\mathcal{U}(\bm X)$ 是 $\bm X$ 的所有逆像的集合构成的 $\;\sigma$-algebra，即 $\{\bm X^{-1}(B) \mid B\in\mathcal{B}\}$

!!! example "Rademacher functions"
    令 $\Omega=[0, 1)$，$\mathcal{U}$ 是所有 $A\subseteq [0, 1)$ 的 $\;\sigma$-algebra，$P$ 是 Lebesgue 测度。定义随机变量 $\bm X_1, \bm X_2, \cdots$ 为

    $$
    \bm X_n(\omega) = \begin{cases}
        1, & \text{if } \frac{k}{2^n}\leqslant \omega < \frac{k+1}{2^n},\; k\text{ is even}\\
        -1, & \text{if } \frac{k}{2^n}\leqslant \omega < \frac{k+1}{2^n},\; k\text{ is odd}
    \end{cases}
    $$

    则这些被称为拉德马赫函数系 (Rademacher functions)，我们可以证明它们是相互独立的。

    ??? general "Proof"
        只需要证明，对于 $\forall k\geqslant 2, 1\leqslant i_1<\cdots < i_k, \forall e_1, \cdots, e_k\in \{-1, 1\}$ 都有

        $$
        P(\bm X_{i_1}=e_1, \bm X_{i_2}=e_2, \cdots, \bm X_{i_k}=e_k) = P(\bm X_{i_1}=e_1)P(\bm X_{i_2}=e_2)\cdots P(\bm X_{i_k}=e_k)
        $$

        证明两侧都等于 $2^{-k}$ 即可。右侧是显然的（每一项都是 $2^{-1}$），左侧可以通过对 $k$ 进行数学归纳获得。

        > 左侧继续切分的话，必然是在原有的区间基础上再往下区分，所以符合的区间总是刚好是原来的一半

将一簇独立变量分成两簇，然后让这两簇分别任意构建函数，两个函数值是相互独立的，形式化为如下的定理：

!!! abstract "Composition of Independent Random Variables"
    令 $\bm X_1, \cdots, \bm X_{m+n}$ 是相互独立的 $\mathbb{R}^k$-valued 随机变量。对于任意的 $f: (\mathbb{R}^k)^n\to \mathbb{R}$ 和 $g: (\mathbb{R}^k)^m\to \mathbb{R}$，有

    $$
        \bm Y := f(\bm X_1, \cdots, \bm X_n) \text{ and }
        \bm Z := g(\bm X_{n+1}, \cdots, X_{n+m})
    $$

    相互独立。

该定理的证明略。

> 可以参考 [L. Breiman, Probability, Addison-Wesley Publishing Company, 1968](https://epubs.siam.org/doi/book/10.1137/1.9781611971286)

进一步地，随机变量的相互独立可以有其分布函数表示和密度函数表示（当存在密度函数时）。

!!! abstract "随机变量相互独立的其他表示形式"
    对于一簇随机变量 $X_1, \cdots, X_m: \Omega\to \mathbb{R}^n$：
    
    **(1)** 分布函数表示：这些随机变量相互独立，当且仅当 $\forall x_k\in \mathbb{R}^n, k=1, \cdots, m$ 有

    $$
        F_{\bm X_1, \cdots, \bm X_m}(x_1, \cdots, x_m) = F_{\bm X_1}(x_1)\cdots F_{\bm X_m}(x_m)
    $$

    **(2)** 密度函数表示：如果这些随机变量**都有密度函数**，则其相互独立当且仅当 $\forall x_k\in \mathbb{R}^n, k=1, \cdots, m$ 有

    $$
        f_{\bm X_1, \cdots, \bm X_m}(x_1, \cdots, x_m) = f_{\bm X_1}(x_1)\cdots f_{\bm X_m}(x_m)
    $$

??? general "Proof"
    当存在密度函数时，可以得到密度函数表示和分布函数表示的等价性。

    ??? general "Proof"
        $$
        \begin{aligned}
            F_{\bm X_1, \cdots, \bm X_m}(x_1, \cdots, x_m)
            &= P(\bm X_1\leqslant x_1, \cdots, \bm X_m\leqslant x_m)\\
            &= \int_{-\infty}^{x_1}\cdots \int_{-\infty}^{x_m} f_{\bm X_1, \cdots, \bm X_m}(y_1, \cdots, y_m)\mathrm{d}y_1\cdots\mathrm{d}y_m\\
            F_{\bm X_1}(x_1)\cdots F_{\bm X_m}(x_m)
            &= P(\bm X_1\leqslant x_1)P(\bm X_2\leqslant x_2)\cdots P(\bm X_m\leqslant x_m)\\
            &= \int_{-\infty}^{x_1} f_{\bm X_1}(y_1)\mathrm{d}y_1\cdots \int_{-\infty}^{x_m} f_{\bm X_m}(y_m)\mathrm{d}y_m \\
            &= \int_{-\infty}^{x_1}\cdots \int_{-\infty}^{x_m} f_{\bm X_1}(y_1)\cdots f_{\bm X_m}(y_m)\mathrm{d}y_1\cdots\mathrm{d}y_m\\
        \end{aligned}
        $$

        根据密度函数表示推导分布函数表示，显然。从分布函数表示出发，可以得到

        $$
        \begin{aligned}
            & \int_{-\infty}^{x_1}\cdots \int_{-\infty}^{x_m} \left[f_{\bm X_1}(y_1)\cdots f_{\bm X_m}(y_m) - f_{\bm X_1, \cdots, \bm X_m}(y_1, \cdots, y_m)\right] \mathrm{d}y_1\cdots\mathrm{d}y_m \\
            = & F_{\bm X_1}(x_1)\cdots F_{\bm X_m}(x_m) - F_{\bm X_1, \cdots, \bm X_m}(x_1, \cdots, x_m) = 0
        \end{aligned}
        $$

        由于 $x_1, \cdots, x_m$ 是任意的，所以 $f_{\bm X_1}(y_1)\cdots f_{\bm X_m}(y_m) = f_{\bm X_1, \cdots, \bm X_m}(y_1, \cdots, y_m)$。

    如果相互独立，则

    $$
    \begin{aligned}
        F_{\bm X_1, \cdots, \bm X_m}(x_1, \cdots, x_m)
        &= P(\bm X_1\leqslant x_1, \cdots, \bm X_m\leqslant x_m)\\
        &= P(\bm X_1\leqslant x_1)P(\bm X_2\leqslant x_2)\cdots P(\bm X_m\leqslant x_m)\\
        &= F_{\bm X_1}(x_1)\cdots F_{\bm X_m}(x_m)
    \end{aligned}
    $$

    另一方面，若分布函数表示的式子成立，为了便于证明，假设存在密度函数 $f_{\bm X_1, \cdots, \bm X_m}$，则可以从密度函数表示出发去得到随机变量相互独立的定义式。

    任取 $A_i\in \mathcal{U}(\bm X_i), i=1, \cdots, m$。可知有 $A_i=\bm X_i^{-1}(B_i)$，对于某个 $B_i\in \mathcal{B}$。则

    $$
    \begin{aligned}
        P(A_1\cap \cdots \cap A_m)
        &= P(\bm X_1\in B_1, \cdots, \bm X_m\in B_m)\\
        &= \int_{B_1\times \cdots \times B_m} f_{\bm X_1, \cdots, \bm X_m}(x_1, \cdots, x_m)\mathrm{d}x_1\cdots\mathrm{d}x_m\\
        &= \int_{B_1}\cdots \int_{B_m} f_{\bm X_1}(x_1)\cdots f_{\bm X_m}(x_m)\mathrm{d}x_1\cdots\mathrm{d}x_m\\
        &= \left(\int_{B_1} f_{\bm X_1}(x_1)\mathrm{d}x_1\right)\cdots \left(\int_{B_m} f_{\bm X_m}(x_m)\mathrm{d}x_m\right)\\
        &= P(X_1\in B_1)\cdots P(X_m\in B_m) \\
        &= P(A_1)P(A_2)\cdots P(A_m)
    \end{aligned}
    $$

    由此证明了 $\mathcal{U}(\bm X_1), \cdots, \mathcal{U}(\bm X_m)$ 相互独立，也就是 $\bm X_1, \cdots, \bm X_m$ 相互独立。

    > 严谨的证明应当从分布函数表示出发，推导随机变量相互独立的定义式，读者可以自己思考

#### Expectation and Variannce of Independent Random Variables

独立随机变量的期望和方差具有很好的拆解性质。

!!! abstract "独立随机变量的性质"
    对于相互独立的实值随机变量 $X_1, X_2, \cdots, X_m$（此处都是一维的随机“变量”而不是 $n$ 维的随机“向量”），有

    **(1)** 期望的拆解性质：如果 $\mathbb{E}(\left| X_i \right|) < \infty (i=1, \cdots, m)$，则有 $\mathbb{E}(\left| X_1 \cdots X_m \right|)<\infty$，且

    $$
    \mathbb{E}(X_1\cdots X_m) = \mathbb{E}(X_1)\cdots \mathbb{E}(X_m)
    $$

    **(2)** 方差的拆解性质：若 $\mathrm{Var}(X_i)<\infty (i=1, \cdots, m)$，则有

    $$
    \mathrm{Var}(X_1+\cdots + X_m) = \mathrm{Var}(X_1) + \cdots + \mathrm{Var}(X_m)
    $$

??? general "Proof"
    **(1)** 为了方便，不严谨地假定每个 $X_i$ 都有界且存在密度函数，则

    $$
    \begin{aligned}
        \mathbb{E}(X_1\cdots X_m)
        &= \int_{\mathbb{R}^n} x_1\cdots x_m f_{X_1, \cdots, X_m}(x_1, \cdots, x_m)\mathrm{d}x_1\cdots\mathrm{d}x_m\\
        &= \left(\int_{\mathbb{R}^n} x_1 f_{X_1}(x_1)\mathrm{d}x_1\right) \cdots \left(\int_{\mathbb{R}^n} x_m f_{X_m}(x_m)\mathrm{d}x_m\right)\\
        &= \mathbb{E}(X_1)\cdots \mathbb{E}(X_m)
    \end{aligned}
    $$

    > 实际上完全不需要加上有界和存在密度函数的假设，严谨的证明留给读者

    **(2)** 使用归纳法，那么只需要证明 $m=2$ 的情况即可，从 $m=k$ 推到 $m=k+1$ 也只需要 $m=2$ 的情况。则有

    $$
    \begin{aligned}
        \mathrm{Var}(X_1+X_2)
        =& \int_{\Omega} [ X_1+X_2 - \mathbb{E}(X_1) + \mathbb{E}(X_2)]^2\mathrm{d}P \\
        =& \int_{\Omega} \left[X_1-\mathbb{E}(X_1)\right]^2\mathrm{d}P + \int_{\Omega} \left[X_2-\mathbb{E}(X_2)\right]^2\mathrm{d}P \\
        &+ 2\int_{\Omega} [X_1-\mathbb{E}(X_1)][X_2-\mathbb{E}(X_2)]\mathrm{d}P \\
        =& \mathrm{Var}(X_1) + \mathrm{Var}(X_2) + 2\mathbb{E}[X_1-\mathbb{E}(X_1)][X_2-\mathbb{E}(X_2)] \\
        =& \mathrm{Var}(X_1) + \mathrm{Var}(X_2) + 2\underbrace{\mathbb{E}[X_1-\mathbb{E}(X_1)]}_{=0} \cdot \underbrace{\mathbb{E}[X_2-\mathbb{E}(X_2)]}_{=0} \\
    \end{aligned}
    $$

    从而得证。

### Some Probabilistic Methods

#### Chebyshev's Inequality and Borel-Cantelli Lemma

!!! abstract "Chebyshev's Inequality"
    对于随机变量 $\bm X$ 和任意 $1\leqslant p < \infty$，有

    $$
    P(\left| \bm X \right|\geqslant \varepsilon) \leqslant \frac{\mathbb{E}(\left| \bm X \right|^p)}{\varepsilon^p},\quad \forall \varepsilon > 0
    $$

??? general "Proof"
    $$
        \mathbb{E}[\left| \bm X \right|^p]
        = \mathbb{E}[\underbrace{\left| \bm X \right|^p}_{\geqslant \varepsilon^p} \cdot \bm 1_{\left| \bm X \right|\geqslant \varepsilon} + \underbrace{\left| \bm X \right|^p \cdot \bm 1_{\left| \bm X \right|< \varepsilon}}_{\geqslant 0}]
        \geqslant \mathbb{E}[\varepsilon^p \cdot \bm 1_{\left| \bm X \right|\geqslant \varepsilon}]
        = \varepsilon^p P(\left| \bm X \right|\geqslant \varepsilon)
    $$

常见的 Chebyshev 不等式的导出式取 $p=2$，且用 $\bm X - \mathbb{E}(\bm X)$ 替换 $\bm X$，有

$$
P(\left| \bm X - \mathbb{E}(\bm X) \right|\geqslant \varepsilon) \leqslant \frac{\mathrm{Var}(\bm X)}{\varepsilon^2}
$$

在介绍 Borel-Cantelli 引理之前，先介绍一下事件的上极限的概念，实际上就是集合的上极限。

!!! info "事件的上极限"
    对于一系列事件 $A_1, A_2, \cdots$，定义其上极限为

    $$
    \limsup_{n\to\infty} A_n = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k
    := \{\omega \in \Omega \mid \omega \in A_k \text{ for infinitely many } k\}
    $$

    称作 "$A_n$ infinitely often"，简写作 "$A_n\; i.o.$"。
    
注意对于 $\omega\in \limsup\limits_{n\to\infty} A_n$，$\omega$ 需要在无穷多个 $A_k$ 中出现，这无穷多个 $A_k$ 可以是间歇的。

!!! abstract "Borel-Cantelli Lemma"
    对于一系列事件 $A_1, A_2, \cdots$，如果 $\sum_{n=1}^{\infty} P(A_n) < \infty$，则

    $$
    P(A_n\; i.o.) = P(\limsup_{n\to\infty} A_n) = 0
    $$

??? general "Proof"
    $$
        P(\limsup_{n\to\infty} A_n)
        = P\left(\bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k\right)
        \leqslant P\left(\bigcup_{k=n}^{\infty} A_k\right)
        \leqslant \sum_{k=n}^{\infty} P(A_k)
        \to 0 \quad \text{as } n\to\infty
    $$

    $\sum_{n=1}^{\infty} P(A_n) < \infty$，即该级数收敛，所以可以得到上面的余项和趋向于 0。

> 如果 $\sum_{n=1}^{\infty} P(A_n) = \infty$ 且 $A_n$ 两两独立 (pairwise independent)，则有 Borel-Cantelli 第二引理结论：$P(A_n\; i.o.) = 1$

Borel-Cantelli 引理可以简单地应用于对于随机变量依概率收敛的阐释，首先介绍依概率收敛的概念。

!!! info "依概率收敛 (convergence in probability)"
    对于一系列随机变量 $X_1, X_2, \cdots$ 和随机变量 $X$，如果对于 $\forall \varepsilon > 0$ 有

    $$
    \lim_{n\to\infty} P(\left| X_n - X \right| \geqslant \varepsilon) = 0
    $$

    则称 $X_n$ 依概率收敛 (converges in probability) 到 $X$，记作 $X_n \xrightarrow{P} X$

Borel-Cantelli 引理可以用于证明如下和依概率收敛有关的定理。

!!! abstract "依概率收敛的性质"
    对于一系列随机变量 $X_1, X_2, \cdots$ 和随机变量 $X$，如果 $X_k \xrightarrow{P} X$，则存在子序列 $\{X_{k_j}\}_{j=1}^{\infty}\subseteq \{X_k\}_{k=1}^{\infty}$ 使得 $X_{k_j}$ 几乎处处收敛到 $X$，即

    $$
        X_{k_j} \to X, \quad \text{a.s.}
    $$

    或者说，

    $$
        P(\lim_{j\to\infty} X_{k_j} = X) = 1
    $$

??? general "Proof"
    每给定正整数 $j$，总能选到一个足够大的 $k_j$ 使得

    $$
    P\left(\left| X_{k_j} - X \right| > \frac{1}{j}\right) \leqslant \frac{1}{2^j}
    $$

    从 $j=1$ 开始选择 $k_j$，使得 $k_1 < k_2 < \cdots$，因此 $k_j\to \infty (j\to \infty)$。随后定义事件

    $$
    A_j := \left\{\omega \in \Omega :\; \left| X_{k_j}(\omega) - X(\omega) \right| > \frac{1}{j}\right\}
    $$ 

    由于 $\sum P(A_j) \leqslant \sum \frac{1}{2^j} < \infty$，根据 Borel-Cantelli 引理，有 $P(A_j\; i.o.) = 0$。因此，对于 $\forall \omega \in \Omega$，存在一个 $j_0$ 使得 $\omega \notin A_j$ 对于 $\forall j\geqslant j_0$ 都成立，即

    $$
    \left| X_{k_j}(\omega) - X(\omega) \right| \leqslant \frac{1}{j}, \quad \forall j\geqslant j_0
    $$

    从而得证。

#### Characteristic Functions

特征函数是概率论中一个非常重要的工具，对于连续随机变量（存在密度函数）而言，它是密度函数的共轭 Fourier 变换（或者也可以认为进行了逆 Fourier 变换）。

!!! info "特征函数 (characteristic functions)"
    对于 $\mathbb{R}^n$-valued 随机变量 $\bm X$，其特征函数定义为

    $$
    \phi_{\bm X}(\lambda) = \mathbb{E}[e^{i\lambda\bm X}], \quad \lambda\in \mathbb{R}
    $$

!!! example "一元高斯分布随机变量的特征函数"
    对于 $X\sim N(\mu, \sigma^2)$，其特征函数为

    $$
    \phi_X(\lambda) = e^{i\mu\lambda - \frac{1}{2}\sigma^2\lambda^2}
    $$

??? general "Proof"
    首先有

    $$
        \phi_X(\lambda)
        = \int_{-\infty}^{\infty} e^{i\lambda x} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}\mathrm{d}x
        \xlongequal{y=\frac{x-\mu}{\sigma}} \frac{e^{i\mu \lambda}}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{i(\sigma\lambda) y} e^{-\frac{y^2}{2}}\mathrm{d}y
    $$

    容易得到有

    $$
    \int_{-\infty}^{\infty} e^{i\lambda y} e^{-\frac{y^2}{2}}\mathrm{d}y = e^{-\frac{\lambda^2}{2}}\int_{-\infty}^{\infty} e^{-\frac{(y-i\lambda)^2}{2}}\mathrm{d}y
    $$

    将复平面上的积分路径从 $\{\operatorname{Im}(z)=-\lambda\}$ 改成实轴，得到有

    $$
    \int_{-\infty}^{\infty} e^{-\frac{(y-i\lambda)^2}{2}}\mathrm{d}y = \int_{-\infty}^{\infty} e^{-\frac{y^2}{2}}\mathrm{d}y = \sqrt{2\pi}
    $$

    因此可以得到

    $$
    \phi_X(\lambda) = \frac{e^{i\mu \lambda}}{\sqrt{2\pi}} \cdot e^{-\frac{(\sigma\lambda)^2}{2}} \cdot \sqrt{2\pi}
    = e^{i\mu\lambda - \frac{1}{2}\sigma^2\lambda^2}
    $$

    > 这里直接计算了重要积分 $\displaystyle \int_{-\infty}^{\infty} e^{-\frac{x^2}{2}}\mathrm{d}x = \sqrt{2\pi}$
    
    ??? general "重要积分的计算"
        $$
        \begin{aligned}
        \left(\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\mathrm dx\right)^2&=\int_{-\infty}^{+\infty}e^{-\frac{y^2}{2}}\mathrm dy\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\mathrm dx\\
        &=\iint\limits_{R^2}e^{-\frac{x^2+y^2}{2}}\mathrm dx\mathrm dy\\
        &=\iint\limits_{R^2}e^{-\frac{\rho^2}{2}}\rho\mathrm d\rho\mathrm d\theta\\
        &=\int_{0}^{2\pi}\mathrm d\theta\int_0^{+\infty}e^{-\frac{\rho^2}{2}}\rho\mathrm d\rho\\
        &=\int_{0}^{2\pi}\mathrm d\theta\int_0^{+\infty}-e^{-\frac{\rho^2}{2}}\mathrm d(-\frac{\rho^2}{2})\\
        &=2\pi
        \end{aligned}
        $$

        可得 $\displaystyle \int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\mathrm dx=\sqrt{2\pi}$

- 如果对特征函数进行泰勒展开，会发现特征函数每一阶的系数其实就是原随机变量的各阶矩
- 因此特征函数可以看成一个将随机变量的各阶矩串联起来的工具，包含了随机变量的大量特征（期望，方差，偏度，峰度等）
- 同时，特征函数与函数的分布函数紧密联系，特征函数相同便意味着分布函数相同

特征函数的以上特性将由如下形式化的性质进行表达：

!!! abstract "特征函数的性质"
    **(1)** 如果（多元）随机变量 $\bm X_1, \cdots, \bm X_n$ 相互独立，则对 $\forall \lambda \in \mathbb{R}^n$ 有

    $$
    \phi_{\bm X_1+\cdots+\bm X_n}(\lambda) = \phi_{\bm X_1}(\lambda_1)\cdots \phi_{\bm X_n}(\lambda_n)
    $$

    **(2)** 对于实值一元随机变量 $X$ 有

    $$
    \phi^{(k)}(0) = i^k \mathbb{E}(X^k)\quad \text{for } k=0, 1, 2, \cdots
    $$

    **(3)** 如果（多元）随机变量 $\bm X$ 和 $\bm Y$ 有相同的特征函数，则 $X$ 和 $Y$ 有相同的分布，即

    $$
    \phi_{\bm X}(\lambda) = \phi_{\bm Y}(\lambda), \forall \lambda \quad\Rightarrow\quad F_{\bm X}(x) = F_{\bm Y}(x), \forall X
    $$

??? general "Proof"
    **(1)**

    $$
    \begin{aligned}
        \phi_{\bm X_1 + \cdots + \bm X_n}(\lambda)
        &= \mathbb{E}[e^{i\lambda(\bm X_1 + \cdots + \bm X_n)}] \\
        &= \mathbb{E}[e^{i\lambda_1\bm X_1} \cdots e^{i\lambda_n\bm X_n}] \\
        &= \mathbb{E}[e^{i\lambda_1\bm X_1}] \cdots \mathbb{E}[e^{i\lambda_n\bm X_n}] \\
        &= \phi_{\bm X_1}(\lambda_1) \cdots \phi_{\bm X_n}(\lambda_n)
    \end{aligned}
    $$

    **(2)** 

    $$
    \begin{aligned}
        \phi^{(k)}(0)
        &= \left.\frac{\mathrm{d}^k}{\mathrm{d}\lambda^k}\phi(\lambda)\right|_{\lambda=0} \\
        &= \left.\frac{\mathrm{d}^k}{\mathrm{d}\lambda^k}\mathbb{E}[e^{i\lambda X}]\right|_{\lambda=0} \\
        &= \left.\frac{\mathrm{d}^k}{\mathrm{d}\lambda^k}\int_{\mathbb{R}} e^{i\lambda x} \mathrm{d}F_{X}\right|_{\lambda=0} \\
        &= \left.\int_{\mathbb{R}} \frac{\mathrm{d}^k}{\mathrm{d}\lambda^k} e^{i\lambda x} \mathrm{d}F_{X}\right|_{\lambda=0} \\
        &= \int_{\mathbb{R}} i^k x^k \mathrm{d}F_{X} \\
        &= i^k \mathbb{E}(X^k)
    \end{aligned}
    $$

    **(3)** 由特征函数的定义，假定密度函数存在，有

    $$
    \begin{aligned}
        \phi_{\bm X}(\lambda) = \phi_{\bm Y}(\lambda)
        &\Rightarrow \mathbb{E}[e^{i\lambda\bm X}] = \mathbb{E}[e^{i\lambda\bm Y}] \\
        &\Rightarrow \int_{\mathbb{R}^n} e^{i\lambda\bm x} f_{\bm X}(\bm x)\mathrm{d}\bm x = \int_{\mathbb{R}^n} e^{i\lambda\bm y} f_{\bm Y}(\bm y)\mathrm{d}\bm y \\
        &\Rightarrow \int_{\mathbb{R}^n} e^{i\lambda\bm x} [f_{\bm X}(\bm x) - f_{\bm Y}(\bm x)]\mathrm{d}\bm x = 0
    \end{aligned}
    $$

    对 $\forall \lambda$ 都成立，可以感觉到 $f_{\bm X}(\bm x) - f_{\bm Y}(\bm x)=0$（不太严谨）

    > 严谨的证明可以参考 [L. Breiman, Probability, Addison-Wesley Publishing Company, 1968](https://epubs.siam.org/doi/book/10.1137/1.9781611971286)

特征函数的性质还有很多，比如特征函数的共轭性质，特征函数的收敛性质等等，这里不再一一列举。

!!! example "特征函数的应用"
    可以用于证明 $X\sim N(\mu_1, \sigma_1^2)$ 和 $Y\sim N(\mu_2, \sigma_2^2)$ 可以得到

    $$
    X+Y \sim N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)
    $$

    只需要计算其特征函数就可以证明。

    $$
    \phi_{X+Y}(\lambda) = \phi_X(\lambda)\phi_Y(\lambda) = e^{i\mu_1\lambda - \frac{1}{2}\sigma_1^2\lambda^2} e^{i\mu_2\lambda - \frac{1}{2}\sigma_2^2\lambda^2} = e^{i(\mu_1+\mu_2)\lambda - \frac{1}{2}(\sigma_1^2+\sigma_2^2)\lambda^2}
    $$

### Law of Large Numbers, Central Limit Theorem

如果一系列随机变量具有相同的分布函数，称其同分布 (identically distributed)；如果这些随机变量还是相互独立的，称其独立同分布 (independent and identically distributed, i.i.d.)。

> 同分布说明这些随机变量含有相同的概率信息。独立同分布，则说明可以用这些随机变量表示**重复独立实验**的结果。

#### Strong Law of Large Numbers

强大数律说明，随着重复独立实验的不断进行，所有实验结果的均值将 almost surely 趋向于期望。也就是说，重复独立实验的次数足够多时，将能够近似得到期望的值。

!!! abstract "强大数律"
    对于一系列独立同分布的 Lebesgue 可积随机变量 $X_1, X_2, \cdots$，如果 $m:=\mathbb{E}(\left| X_i \right|) < \infty$，则有

    $$
    P\left(\lim_{n\to\infty} \frac{X_1 + \cdots + X_n}{n} = m\right) = 1
    $$

??? general "Proof"
    首先建立所需要的几个假设：

    1. 假设这些随机变量都是实值的，即 $X_i: \Omega\to \mathbb{R}$
    2. 为了简化，假设 $\mathbb{E}(X_i^4)<\infty$, $i=1, \cdots$
    3. 假设 $m=0$，如果非零，只需要用 $X_i - m$ 替换 $X_i$ 即可

    考虑

    $$
        \mathbb{E}\left[
            \left( \sum_{i=1}^n X_i \right)^4
        \right]
        = \sum_{i, j, k, l=1}^n \mathbb{E}(X_iX_jX_kX_l)
    $$

    在交叉项中，只要有一项漏出来，就会导致值变为 0，即若存在 $i$ 同时不等于 $j, k, l$，根据独立性就有

    $$
    \mathbb{E}(X_iX_jX_kX_l) = \mathbb{E}(X_i)\mathbb{E}(X_jX_kX_l) = 0
    $$

    因此就有

    $$
    \begin{aligned}
        \mathbb{E}\left[
            \left( \sum_{i=1}^n X_i \right)^4
        \right]
        &= \sum_{i=1}^n \mathbb{E}(X_i^4) + 3\sum_{\substack{i, j=1 \\ i\neq j}}^n \mathbb{E}(X_i^2X_j^2) \\
        &= n\mathbb{E}(X_1^4) + 3(n^2-n)\mathbb{E}(X_1^2)^2 = O(n^2)
        &\leqslant n^2 C \quad \text{for some } C>0
    \end{aligned}
    $$

    > 系数 3 可以从组合的角度想：给定 $i$，从 $j, k, l$ 中选择一个与之相同，剩下两个再组对相同

    对给定的 $\varepsilon >0$，有

    $$
    \begin{aligned}
        P\left(\left| \frac{X_1 + \cdots + X_n}{n} \right| \geqslant \varepsilon\right)
        &= P\left(\left| \sum_{i=1}^n X_i \right| \geqslant n\varepsilon\right) \\
        &\leqslant \frac{1}{(n\varepsilon)^4} \mathbb{E}\left[
            \left( \sum_{i=1}^n X_i \right)^4
        \right] & \text{(Chebyshev's Inequality)}\\
        &\leqslant \frac{C}{\varepsilon^4n^2}
    \end{aligned}
    $$

    设 $A_n=\{\omega \in \Omega :\; |(X_1(\omega) + \cdots + X_n(\omega)) / n|\geqslant \varepsilon\}$，于是就有

    $$
        \sum P(A_n) \leqslant \sum \frac{C}{\varepsilon^4n^2} < \infty
    $$

    根据 Borel-Cantelli 引理，有 $P(A_n\; i.o.) = 0$。再设

    $$
        B_k := \left\{\omega \in \Omega :\; \limsup_{n\to\infty} \frac{X_1(\omega) + \cdots + X_n(\omega)}{n} \geqslant \frac{1}{k}\right\}
    $$

    其实就是令 $\varepsilon = 1/k$，总有 $P(B_k)=0$。记 $B=\lim\limits_{k\to\infty} B_k=\bigcup\limits_{k=1}^{\infty} B_k$，则有 $P(B)=0$ 且

    $$
    \lim_{n\to \infty} \frac{X_1(\omega) + \cdots + X_n(\omega)}{n} = 0,\quad \forall \omega \notin B
    $$

    由此得证。

    > 由于 $\omega \in B_k$ 可以推出 $\omega \in B_{k+p}$，因此有 $\limsup B_k = \liminf B_k = \bigcup\limits_{k=1}^{\infty} B_k$，即存在 $\lim B_k$

#### Central Limit Theorem

Laplace, Demovire 曾对二项分布独立同分布随机变量的中心极限定理进行了研究，从比较形象的角度去看，可以解释在给定的一个 bound 之内所有实验结果的和相对于均值的一个波动。在这里略去 Laplace-Demovire 定理这一中心极限定理的特殊情形，直接给出更强的 Lindeberg–Lévy 中心极限定理形式。

!!! abstract "Lindeberg–Lévy 中心极限定理"
    对于一系列独立同分布的实值随机变量 $X_1, X_2, \cdots$，设

    $$
        E(X_i) = \mu, \quad \mathrm{Var}(X_i) = \sigma^2 < \infty,\quad \text{for } i=1, 2, \cdots
    $$

    令 $S_n=X_1+\cdots+X_n$，则对于任意实数 $-\infty < a < b < +\infty$ 有

    $$
        \lim_{n\to \infty} P(a\leqslant \frac{S_n - n\mu}{\sqrt{n}\sigma}\leqslant b)
        = \frac{1}{\sqrt{2\pi}} \int_a^b e^{-\frac{x^2}{2}} \mathrm{d}x
    $$

??? general "Outline of Proof"
    简单地假设 $\mu=0, \sigma=1$，如果不是如此则可以先缩放。这样就会有特征函数

    $$
    \phi_{\frac{S_n}{\sqrt{n}}}(\lambda) = \prod_{i=1}^n\phi_{\frac{X_i}{\sqrt{n}}}(\lambda)
    =\left[\phi_{\frac{X_1}{\sqrt{n}}}(\lambda)\right]^n
    =\left[\phi_{X_1}\left(\frac{\lambda}{\sqrt{n}}\right)\right]^n
    ,\quad \forall \lambda\in \mathbb{R}
    $$

    > $\phi_{\frac{X_i}{\sqrt{n}}}(\lambda) = \mathbb{E}[e^{i\lambda\frac{X_i}{\sqrt{n}}}] = \mathbb{E}[e^{i\frac{\lambda}{\sqrt{n}} X_i}] = \phi_{X_i}(\frac{\lambda}{\sqrt{n}})$

    简写 $\phi = \phi_{X_1}$，对其进行泰勒展开到二阶小项。

    $$
    \phi(\mu) = \phi(0) + \phi'(0)\mu + \frac{1}{2}\phi''(0)\mu^2 + o(\mu^2),\quad \mu \to 0^+
    $$

    由于 $\phi(0)=1$, $\phi'(0)=i\mathbb{E}(X_1)=0$, $\phi''(0)=i^2\mathbb{E}(X_1^2)=-(\mathrm{Var}(X_1) + [E(X_1)]^2)=-1$，令 $\mu=\frac{\lambda}{\sqrt{n}}$ 有

    $$
        \phi_{X_1}\left( \frac{\lambda}{\sqrt{n}} \right)
        = 1 - \frac{\lambda^2}{2n} + o\left( \frac{\lambda^2}{n} \right)
    $$

    这样就

    $$
    \begin{aligned}
        \phi_{\frac{S_n}{\sqrt{n}}}(\lambda)
        &= \left[ 1 - \frac{\lambda^2}{2n} + o\left( \frac{\lambda^2}{n} \right) \right]^n \\
        &= e^{n\ln\left[1 - \frac{\lambda^2}{2n} + o\left( \frac{\lambda^2}{n} \right)\right]} \\
        &\xlongequal{x=\frac{1}{n} \to 0^+} \exp\left\{\frac{\ln\left[1 - \frac{1}{2}\lambda^2x + o\left( \lambda^2x \right)\right]}{x}\right\} \\
        &= \exp\left\{\frac{\left(-\frac{1}{2}\lambda^2x + o\left( \lambda^2x \right)\right)+o(x)}{x}\right\} \to e^{-\frac{\lambda^2}{2}}
    \end{aligned}
    $$

    由此可知 $\frac{S_n}{\sqrt{n}} \xrightarrow{d} N(0, 1)$，$\xrightarrow{d}$ 表示依分布收敛。

可以注意到，对于所构建的变量 $\displaystyle \frac{S_n - n\mu}{\sqrt{n}{\sigma}}$，当 $n$ 足够大时，其区间内的分布概率趋向于单位高斯分布在同一区间内的分布概率，即该变量**依分布收敛于单位高斯分布**。

> 中心极限定理 (CLT) 还有许多更强或可能更弱的形式，比如比较有名的 Lyapunov CLT，Lindeberg CLT 等等，可以参考 [Central limit theorem - Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem) 了解更多。

### Conditional Expectation

在这里，我们希望关注的是以**随机变量** $Y$ 为条件，随机变量 $X$ 的期望 $\mathbb{E}(X \mid Y)$。这样的期望是相对比较抽象的，因为大家比较熟悉的期望是以事件 $B$ 为条件的期望 $\mathbb{E}(X \mid B)$：

$$
\mathbb{E}(X \mid B) = \frac{1}{P(B)} \int_B X\mathrm{d} P
$$

但是 $\mathbb{E}(X\mid Y)$ 的定义方式不是显然的，因此首先需要寻找定义 $\mathbb{E}(X\mid Y)$ 的方式，然后用直观的方式进行解释。

#### Approaches to Conditional Expectation

从一个简单的例子出发，可以更好地理解为什么要按后面的方法定义 $\mathbb{E}(X\mid Y)$。

!!! example "Simple Example"
    在概率空间 $(\Omega, \mathcal{U}, P)$ 上定义简单随机变量 $Y=\sum_{i=1}^m a_i\chi_{A_i}$（请读者回忆前面提过的简单函数 simple function 的定义），并且让 $A_1, \cdots, A_m$ 构成 $\Omega$ 的一个划分（即 $\cup A_i = \Omega$ 且 $A_i\cap A_j = \emptyset$），最后再让 $a_i$ 各不相同，则有

    $$
        Y(\omega) = \begin{cases}
            a_1, &        &\omega \in A_1 \\
            a_2, &        &\omega \in A_2 \\
                 & \vdots & \\
            a_m, &        &\omega \in A_m
        \end{cases}
    $$

    由于 $a_i$ 各不相同，根据 $Y(\omega)$ 的值可以推知 $\omega$ 在哪一个 $A_i$ 之中，这样我们对 $X(\omega)$ 的估计自然就是 $\mathbb{E}(X\mid A_i)$ 了。于是有

    $$
    \mathbb{E}(X\mid Y) = \sum_{i=1}^m \mathbb{E}(X\mid A_i)\cdot \chi_{A_i} = 
    \begin{cases}
        \mathbb{E}(X\mid A_1), &        &\omega \in A_1 \\
        \mathbb{E}(X\mid A_2), &        &\omega \in A_2 \\
                               & \vdots & \\
        \mathbb{E}(X\mid A_m), &        &\omega \in A_m
    \end{cases}
    $$

在这个例子中，我们需要注意以下三点：

- $\mathbb{E}(X\mid Y)$ 是一个随机变量，而不是一个常数，这和 $\mathbb{E}(X\mid B)$ 不同
- $\mathbb{E}(X\mid Y)$ 是 $\mathcal{U}(Y)$-measurable 的，即在 $Y$ 的逆像集上定义
- $\int_A X\mathrm{d}P = \int_A \mathbb{E}(X\mid Y)\mathrm{d}P$ 对于任意 $A\in \mathcal{U}(Y)$ 都成立

> 理解第三条性质，在任取的 $Y$ 的某个逆像事件 $A$ 之下做概率积分，可以理解为 $\mathbb{E}(X\mid Y)$ 相对 $X$ 更“平缓”了，但是最后积分累积起来的结果是一样的，也就是期望所具有的“均值”的概念

于是，将注意到的性质作为对 $\mathbb{E}(X\mid Y)$ 的定义：

!!! info "以随机变量为条件的条件期望"
    令 $X, Y$ 都定义于同一概率空间，则给定 $Y$ 的条件下 $X$ 的条件期望是满足以下条件的所有 $\:\mathcal{U}(Y)$-measurable 的随机变量 $Z$：

    $$
    \int_A X\mathrm{d}P = \int_A Z\mathrm{d}P, \quad \forall A\in \mathcal{U}(Y)
    $$

> 可以证明，除去一系列概率测度为 0 的集合外，$Z$ 具有存在唯一性。在后面 $\mathbb{E}(X \mid \mathcal{V})$ 的定义下，由于有 $\mathbb{E}(X \mid Y) = \mathbb{E}(X \mid \mathcal{U}(Y))$，可以通过 $\mathcal{E}(X \mid \mathcal{V})$ 的存在唯一性证明这一点。然而遗憾的是 $\mathcal{E}(X \mid \mathcal{V})$ 的存在唯一性的证明需要用到一些进阶的测度论概念，在书中被略去了，因此这里的详细证明如果读者感兴趣可以自己探索。

在理解条件期望 $\mathbb{E}(X\mid Y)$ 的过程中，可以采用代数和几何的两个视角。

**从代数视角出发**，我们首先将关注点从 $\mathbb{E}(X\mid Y)$ 转移到 $\mathbb{E}(X\mid\mathcal{V})$，$\mathcal{V}=\mathcal{U}(Y)$ 是由 $Y$ 生成的 $\sigma$-algebra。将 $\mathbb{E}(X\mid\mathcal{V})$ 定义如下.

!!! info "以 $\sigma$-algebra 为条件的条件期望"
    给定概率空间 $(\Omega, \mathcal{U}, P)$，对于任意 $\sigma$-algebra $\mathcal{V}\subseteq \mathcal{U}$ 和可积随机变量 $X$，定义 $\mathbb{E}(X\mid\mathcal{V})$ 为任何满足如下两个条件的 $\Omega$ 上的随机变量：

    - $\mathbb{E}(X\mid\mathcal{V})$ 是 $\mathcal{V}$-measurable 的
    - $\int_A X\mathrm{d}P=\int_A \mathbb{E}(X\mid\mathcal{V})\mathrm{d}P$, $\forall A\in \mathcal{V}$

> 第一条要求 $\mathbb{E}(X\mid\mathcal{V})$ 必须利用 $\mathcal{V}$ 的信息构建，第二条则要求 $\mathbb{E}(X\mid\mathcal{V})$ 与 $X$ 在关于 $\mathcal{V}$ 上的事件的积分上是一致的。

$\mathbb{E}(X\mid\mathcal{V})$ 可以用来代表 $\mathbb{E}(X\mid Y)$，容易验证如下事实：

- $\mathbb{E}(X\mid Y)=\mathbb{E}(X\mid\mathcal{V})$
- $\mathbb{E}(\mathbb{E}(X\mid\mathcal{V}))=\mathbb{E}(X)$
- $\mathbb{E}(X)=\mathbb{E}(X\mid\{\emptyset, \Omega\})$, 

<div style="text-align:center;">
    <img src="../../../imgs/Intro2SDE/conditional_expectation_proj.png" alt="conditional_expectation_proj" style="zoom:30%;" />
</div>

**从几何视角出发**，可以证明 $\mathbb{E}(X\mid\mathcal{V})$ 是 $X$ 在 $V:=L^2(\Omega, \mathcal{V})$ 这一线性空间中的**投影**就是 $\mathbb{E}(X\mid\mathcal{V})$，即

$$
\mathbb{E}(X\mid\mathcal{V}) = \mathop{\arg\min}\limits_{Y\in V}\| Y - X \|^2
$$

$L^2(\Omega, \mathcal{V})$ 意为包含所有 2-范数有限的实值 $\mathcal{V}$-measurable 随机变量 $Y$ 的线性空间，其中 2-范数定义为

$$
\|Y\| := \left(\int_{\Omega} Y^2 \mathrm{d}P \right)^{\frac{1}{2}} < \infty
$$

该 2-范数是相对于如下 $L^2(\Omega, \mathcal{V})$ 上的内积而言的：$\forall X, Y\in L^2(\Omega, \mathcal{V})$，有

$$
(X, Y) := \int_{\Omega} XY \mathrm{d}P = \mathbb{E}(XY)
$$

可以注意到 $V$ 只是在 $\mathcal{V}$ 的基础上附加了度量而已，基本可以等同起来看。

#### Properties

!!! abstract "条件期望的性质"
    **(1)** 对于常数 $a, b$，

    $$
        E(aX+bY\mid\mathcal{V})=aE(X\mid\mathcal{V})+bE(Y\mid\mathcal{V}) \quad a.s.
    $$

    **(2)** 若 $X$ 是 $\mathcal{V}$-measurable 的，则
    
    $$
        E(X\mid\mathcal{V})=X \quad a.s.
    $$
    
    **(3)** 若 $X$ 是 $\mathcal{V}$-measurable 的且 $XY$ 可积，则
    
    $$
        E(XY\mid\mathcal{V})=XE(Y\mid\mathcal{V}) \quad a.s.
    $$
    
    **(4)** 若 $X$ 独立于 $\mathcal{V}$，则
    
    $$
        E(X\mid\mathcal{V})=E(X) \quad a.s.
    $$
    
    **(5)** 若 $\mathcal{W}\subseteq\mathcal{V}$，则

    $$
        E(X\mid\mathcal{V})\leq E(Y\mid\mathcal{V}) \quad a.s.
    $$

    **(6)** $X\leqslant Y\; a.s. \Rightarrow$

    $$
        E(X\mid\mathcal{W})=E(E(X\mid\mathcal{V})\mid\mathcal{W})=E(E(X\mid\mathcal{W})\mid\mathcal{V}) \quad a.s.
    $$

!!! warning "留作习题证明略"

另外，原始的期望存在琴生不等式，对于条件期望也存在琴生不等式。

!!! abstract "条件琴生不等式 (Conditional Jensen Inequality)"
    给定凸函数 $\Phi: \mathbb{R}\to \mathbb{R}$，且 $\mathbb{E}(|\Phi(X)|)<\infty$，有

    $$
    \Phi (\mathbb{E} (X\mid \mathcal{V})) = \mathbb{E} ( \Phi (X) \mid \mathcal{V})
    $$

!!! warning "留作习题证明略"

### Martingales

设 $Y_1, Y_2, \cdots$ 是一列独立实值随机变量（不一定同分布），满足

$$
\mathbb{E}(Y_i) = 0,\quad i = 1, 2, \cdots
$$

定义 $S_n = Y_1 + \cdots + Y_n$，给定 $S_1, \cdots, S_n$，现在希望预测 $S_{n+k}$，有条件期望

$$
\begin{aligned}
    \mathbb{E}(S_{n+k}\mid S_1, \cdots, S_n)
    &= \underbrace{\mathbb{E}(S_n\mid S_1, \cdots, S_n)}_{\text{given }S_1, \cdots, S_n}
        + \underbrace{\mathbb{E}(Y_{n+1}+\cdots+Y_{n+k}\mid S_1, \cdots, S_n)}_{Y_{n+t} \text{ independent of }S_1, \cdots, S_n} \\
    &= S_n + \mathbb{E}(Y_{n+1} + \cdots + Y_{n+k}) \\
    &= S_n
\end{aligned}
$$

可知对于 $\forall k\geqslant 1$，对 $S_{n+k}$ 的最佳估计都是 $S_n$。这里可以认为描述了一个“公平” (fair) 的赌博游戏，$Y_i$ 是每局的收益，从此刻 ($n$) 望未来，未来的收益期望始终等于现在的收益。这里的 $\{S_n\}$ 就是一种离散鞅，描述的未来期望如直线一般前进。

!!! info "离散鞅 (discrete martingale)"
    设 $X_1, X_2, \cdots$ 是一列实值随机变量，有 $\mathbb{E}(|X_i|)<\infty (i=1, 2, \cdots)$，如果有

    $$
    \mathbb{E}(X_{n+1}\mid X_1, \cdots, X_n) = X_n \quad a.s., \quad n=1, 2, \cdots
    $$

    我们就称 $\{X_i\}_{i=1}^{\infty}$ 是一个（离散）鞅，即 (discrete) martingale。

引入连续时间 $t$，就可以在连续的随机过程的意义上定义连续的鞅。

!!! info "history"
    令 $X(\cdot)$ 为实值随机过程，则不正式地定义生成 $\sigma$-algebra

    $$
    \mathcal{U}(t)L=\mathcal{U}(X(s)\mid 0\leqslant s\leqslant t)
    $$

    为直到时间 $t$ 的历史信息 (history)。

!!! info "鞅 (martingale)"
    设 $X(\cdot)$ 是连续时间 $t\geqslant 0$ 的实值随机过程，且满足 $\mathbb{E}(|X(t)|)<\infty$, $\forall t\geqslant 0$。
    
    **(1)** 如果有

    $$
    X(s) = \mathbb{E}(X(t)\mid \mathcal{U}(s)) \quad a.s., \quad \forall t\geqslant s \geqslant 0
    $$

    则称 $X(\cdot)$ 是一个鞅 (martingale)。

    **(2)** 如果有

    $$
    X(s) \leqslant \mathbb{E}(X(t)\mid \mathcal{U}(s)) \quad a.s., \quad \forall t\geqslant s \geqslant 0
    $$

    则称 $X(\cdot)$ 是一个下鞅 (submartingale)。

    > 同理可知上鞅 (supmartingale) 只需要把下鞅定义式中的 $\leqslant$ 改成 $\geqslant$ 就行。

!!! example "一维布朗运动"
    一维布朗运动 $W(\cdot)$ 就是一种鞅。记 $\mathcal{W}(t) := \mathcal{U}(W(s)\mid 0\leqslant s\leqslant t)$，则 对 $t\geqslant s$ 有

    $$
    \begin{aligned}
        \mathbb{E}(W(t)\mid \mathcal{W}(s))
        &= \mathbb{E}(W(t)-W(s)\mid \mathcal{W}(s))+\mathbb{E}(W(s)\mid \mathcal{W}(s)) \\
        &= \mathbb{E}(W(t)-W(s)) + W(s) \\
        &= W(s)\quad a.s.
    \end{aligned}
    $$

    注意根据布朗运动的定义，$W(t)-W(s)\sim N(0, t-s)$，与 history $\mathcal{W}(s)$ 无关。

!!! warning "本节还在施工中"