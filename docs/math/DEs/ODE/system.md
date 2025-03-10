<link rel="stylesheet" href="../../../../css/counter.css" />

# 常微分方程组

!!! warning "该页面还在建设中"

## Preliminaries

### 向量/矩阵相关的收敛

!!! info "向量列收敛"
    如果 $\forall \;k\in\{1, 2, \cdots, n\}$，数列 $\{x_{km}\}$ 都收敛，则称向量序列 $X_m=(x_{1,m}, x_{2m}, \cdots, x_{nm})^{\top}$ 收敛

这里 $m$ 是单个数列中的数的下标索引，而 $n$ 则是向量维度（向量列中的数列个数）。

!!! tip "向量函数列一致收敛"
    同理，向量函数列 $X_m(t)=(x_{1m}(t), x_{2m}(t), \cdots, x_{nm}(t))^{\top}$ 中每个函数列都在 $I$ 上一致收敛，那么向量函数列在 $I$ 上一致收敛。

!!! info "向量函数级数一致收敛"
    给定向量函数级数

    $$
    \sum_{m=1}^\infty X_m(t)
    $$

    其部分和是一个向量函数列。如果其部分和在 $I$ 上一致收敛，则称该向量函数级数在 $I$ 上一致收敛。

同理，矩阵序列收敛等价于其每个元素对应的数列都收敛，从而导出将会用到的关键的矩阵级数收敛概念。

!!! info "矩阵级数收敛"
    给定矩阵级数

    $$
    \sum_{m=1}^{\infty} A_m
    $$

    其部分和是一个矩阵序列。如果其部分和收敛，则该矩阵级数收敛。

### 向量函数的线性相关性

考虑一组向量函数 $X_1(t), X_2(t), \cdots, X_m(t)$ 在区间 $I$ 上的线性相关性，定义其线性相关为

!!! info "向量函数线性相关"
    如果存在不全为 $0$ 的常数 $c_1, c_2, \cdots, c_m$，使得

    $$
    \sum_{k=1}^m c_kX_k(t)\equiv 0,\quad t\in I
    $$

    则称这组向量函数在 $I$ 上线性相关。

反之则可称这组向量函数在 $I$ 上线性无关。类似常向量组可以使用行列式判断线性相关性，向量函数组也可以如此判断。

$$
|(X_1, X_2, \cdots, X_m)| = \begin{vmatrix}
X_{11} & X_{12} & \cdots & X_{1m}\\
X_{21} & X_{22} & \cdots & X_{2m}\\
\vdots & \vdots & \ddots & \vdots\\
X_{n1} & X_{n2} & \cdots & X_{nm}\\
\end{vmatrix}
$$

!!! warning "该部分还在建设中"

如上的行列式，其

### 矩阵指数

!!! warning "该部分还在建设中"

## 一阶线性微分方程组

### 形式化

!!! info "一阶线性微分方程组"
    形如

    $$
    \begin{cases}
    \begin{aligned}
        \frac{\mathrm dx_1}{\mathrm dt} &= a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n + f_1(t)\\
        \frac{\mathrm dx_2}{\mathrm dt} &= a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n + f_2(t)\\
        &\cdots\\
        \frac{\mathrm dx_n}{\mathrm dt} &= a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n + f_n(t)\\
    \end{aligned}
    \end{cases}
    $$

引入一些记号

$$
X(t) = \begin{bmatrix}
x_1(t)\\
x_2(t)\\
\vdots\\
x_n(t)
\end{bmatrix},\quad
A(t) = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{bmatrix},\quad
F(t) = \begin{bmatrix}
f_1(t)\\
f_2(t)\\
\vdots\\
f_n(t)
\end{bmatrix}
$$

则一阶线性微分方程组可写为矩阵形式

$$
\frac{\mathrm dX(t)}{\mathrm dt} = A(t)X(t) + F(t)
$$

初始条件为

$$
X(t_0)=\alpha
$$

$\alpha=(\alpha_1,\alpha_2,\cdots,\alpha_n)^{\top}$ 为常向量。

!!! general "高阶线性微分方程的转化"
    $n$ 阶线性微分方程的初值问题

    $$
    \begin{cases}
    \begin{aligned}
        &x^{(n)}+a_1 x^{(n-1)}+\cdots+a_{n-1}x'+a_nx=f(t)\\
        &x(t_0)=\alpha_1,x'(t_0)=\alpha_2,\cdots,x^{(n-1)}(t_0)=\alpha_n
    \end{aligned}
    \end{cases}
    $$

    通过变换

    $$
    x_1=x,x_2=x',\cdots,x_n=x^{(n-1)}
    $$

    可以转化为一阶线性微分方程组

    $$
    \begin{cases}
    \begin{aligned}
        x_1'&=x_2\\
        x_2'&=x_3\\
        &\cdots\\
        x_{n-1}'&=x_n\\
        x_n'&=-a_nx_1-a_{n-1}x_2-\cdots-a_1x_n+f(t)\\
    \end{aligned}
    \end{cases}
    $$

!!! tip "Remark"
    高阶线性微分方程必能转化为一阶线性微分方程组，但是反之不一定。由于这种转化方法的存在，对于线性微分方程组，研究一阶即可。

### 解的理论

!!! info "存在唯一性定理"
    设 $A(t)$ 是 $n\times n$ 矩阵，$F(t)$ 是 $n$ 维列向量，且都在 $I=[a, b]$ 上连续，那么 $\forall \; t_0\in I$, $\alpha\in \mathbb{R}$，初值问题

    $$
    \begin{cases}
        X'(t) = A(t)X(t) + b(t)\\
        X(t_0)=\alpha
    \end{cases}
    $$

    在 $I$ 上存在唯一解。

参考一阶一元线性微分方程的 Picard 存在唯一性定理的证明可以得到。

现在只是证明了解的存在唯一性，为求出其解析解，可以首先考虑其**齐次形式**，即令 $b(t) = 0$。即

$$
X'(t) = A(t)X(t)
$$

其中 $A(t)\in C[a, b]$。首先有一个简单的叠加原理，如果 $X_1(t), \cdots, X_m(t)$ 都是方程的解向量，那么

$$
\sum_{k=1}^m c_kX_k(t)
$$

也是方程的解向量，$c_k$ 是任意常数。只需要把这个解代入方程就会发现叠加原理是十分自然的。


