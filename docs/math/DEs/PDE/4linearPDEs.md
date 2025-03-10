<link rel="stylesheet" href="../../../../css/counter.css" />

# Four Important Linear Partial Differential Equations

!!! info "Part of note of *Partial Differential Equations*, Lawrence C. Evans"

!!! warning "本页面还在施工中"

## Transport Equation

（常系数）运输方程 (transport equation) 是最简单的 PDE 之一。

!!! info "transport equation"
    其一般形式为

    $$
        u_t + b \cdot \nabla_x u = 0
    $$

    其中，$b \in \mathbb{R}^n$ 是常向量，$u = u(x, t): \mathbb{R}^n\times [0, +\infty)\to \mathbb{R}$ 是未知函数，并且有

    $$
        u_t = \frac{\partial u}{\partial t}, \quad
        \nabla_x u = \left(\frac{\partial u}{\partial x_1}, \frac{\partial u}{\partial x_2}, \cdots, \frac{\partial u}{\partial x_n}\right)^T
    $$

    在实际问题中，$x$ 具有典型的位置含义，$t$ 具有典型的时间含义，$b$ 则具有速度含义。

要解决 transport equation，首先要注意到它的一个重要性质：$u$ 在某个方向（直线）上保持为常数。可以证明，这个方向就是 $(b, 1)\in\mathbb{R}^{n+1}$。

??? general "Proof"
    令
    
    $$
        z(s)=u(x+sb, t+s), \quad s\in\mathbb{R}
    $$

    则

    $$
        \frac{\mathrm{d}z}{\mathrm{d}s} = b\cdot \nabla_x u(x+sb, t+s) + u_t(x+sb, t+s) = 0
    $$

    由此可知 $z(s)$ 关于 $s$ 为常数。

### Initial Value Problem

!!! info "Initial Value Problem"
    令 $u_0(x) = u(x, 0)$，则

    $$
        \begin{cases}
            u_t + b \cdot \nabla_x u = 0, & x\in\mathbb{R}^n, t>0 \\
            u(x, 0) = u_0(x), & x\in\mathbb{R}^n
        \end{cases}
    $$

    是 transport equation 的初值问题。

简单地利用前面得到的性质，就有

$$
    u(x, t) = u(x-bt, 0) = u_0(x-bt)
$$

需要注意，这里只是证明了若方程有足够好（合法）的解 $u$，那么这个解一定形如 $u_0(x-bt)$；但并没有证明这个形式的解总是合法。

如果额外提供条件 $g\in C^1$，那么就能证明 $u(x, t) = u_0(x-bt)$ 也满足方程，这样就成为了一个充要解。

- 机械运动认识：$u_0(x)$ 是 $u(x, t)$ 在 $t=0$ 时刻的刻画，$u_0(x)$ 沿着 $(b, 1)$ 运动得到 $u(x, t)$
- 几何认识：$u_0(x)$ 是 $u(x, t)$ 在 $\mathbb{R}^n\times \{t=0\}$ 的截面，过 $(x, t)$ 方向为 $(b, 1)$ 的直线与平面交于 $(x-tb, 0)$

!!! tip "weak solutions"
    如果 $g\notin C^1$，那么显然方程就没有 $C^1$ 解了，此时可以非正式地称 $u(x, t) = u_0(x-bt)$ 为方程的弱解（weak solution）

### Nonhomogeneous Problem

其实就是将 transport equation 改成

$$
    u_t + b \cdot \nabla_x u = f
$$

同样定义 $z(s)$，有

$$
    \frac{\mathrm{d}z}{\mathrm{d}s} = b\cdot \nabla_x u(x+sb, t+s) + u_t(x+sb, t+s) = f(x+sb, t+s)
$$

这样就有

$$
\begin{aligned}
    u(x, t)
    &= u_0(x-bt) + z(0) - z(-t)\\
    &= u_0(x-bt) + \int_{-t}^0 \frac{\mathrm{d}z}{\mathrm{d}s}\mathrm{d}s\\
    &= u_0(x-bt) + \int_{-t}^0 f(x+sb, t+s) \mathrm{d}s\\
    &= u_0(x-bt) + \int_{0}^t f(x+(s-t)b, s) \mathrm{d}s
\end{aligned}
$$

这个公式也将被应用于 wave equation 的求解。

!!! tip "method of characteristics"
    这种将 PDE 转换成 ODE 求解的方法，是特征线法 (method of characteristics) 的一个特例。

!!! question "Problem 2.1"
    解

    $$
    \begin{cases}
        u_t + b \cdot \nabla_x u + cu = 0, & x\in\mathbb{R}^n, t>0 \\
        u(x, 0) = g(x), & x\in\mathbb{R}^n
    \end{cases}
    $$

    $c\in \mathbb{R}$, $b\in\mathbb{R}^n$ 为常数

!!! general "Solution"
    令 $z(s)=u(x+sb, t+s)$，则

    $$
        \frac{\mathrm{d}z}{\mathrm{d}s} = b\cdot \nabla_x u(x+sb, t+s) + u_t(x+sb, t+s) = -cu(x+sb, t+s) = -cz(s)
    $$

    解该 ODE 得到

    $$
        z(s) = u(x, t)e^{-cs}
    $$

    因此有

    $$
        u(x, t)e^{-cs} = u(x+sb, t+s)
    $$
    
    令 $s=-t$，有

    $$
        u(x, t) = u(x-bt, t-t)e^{-ct} = g(x-tb)e^{-ct}
    $$

## Laplace's Equation

首先回忆一下散度 (divergence) 和拉普拉斯算子 (Laplace operator) 的定义。

??? info "Divergence"
    对于 $u\in\mathbb{R}^n$，其散度 (divergence) $\operatorname{div} u$ 定义为

    $$
        \operatorname{div} u = \nabla \cdot u = \sum_{i=1}^n \frac{\partial u_i}{\partial x_i}
    $$

    考虑其“发散程度”的物理意义，它还有一种定义：

    $$
        \operatorname{div} u = \lim_{V\to 0} \frac{1}{|V|} \oiint_{\partial V} u\cdot \hat{n} \mathrm{d}S
    $$

??? info "Laplace operator"
    Laplace operator $\Delta$ 定义为梯度的散度，即

    $$
        \Delta u = \nabla \cdot \nabla u = \sum_{i=1}^n \frac{\partial^2 u}{\partial x_i^2}
    $$

同时介绍 Laplace's equation 和 Poisson's equation 方程，因为只有齐次和非齐次的区别。

!!! info "Laplace's equation and Poisson's equation"
    Laplace's equation 形式为

    $$
        \Delta u = 0
    $$

    Poisson's equation 形式为

    $$
        -\Delta u = f
    $$

    其中，$x\in U\subset \mathbb{R}^n$，$U$ 是给定的开集。$u: \overline{U}\to \mathbb{R}$ 是未知函数，$f: U\to \mathbb{R}$ 是已知函数。（$\overline{U}$ 表示 $U$ 的闭包）

## Heat Equation

## Wave Equation