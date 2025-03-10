<link rel="stylesheet" href="../../../css/counter.css" />

# 数据特征进阶

!!! info "Part of note taken on ZJU *Probability Theory (H)*, 2021 Fall & Winter"

## 矩 (moment)

!!! info "$k$ 阶原点矩 (origin moment, or raw moment)"
    $$
    m_k=E\xi^k
    $$

数学期望就是一阶原点矩，另外在方差公式 $Var\xi=E\xi^2-(E\xi)^2$ 中，我们经常用到的 $E\xi^2$ 就是二阶原点矩。

原点矩简称为矩，可以对比力学中计算力矩时参考点选在原点时的情况，不过力学的力矩仅是一阶原点矩，二阶原点矩或许要用能量进行类比。但我们这里并不尝试直接阐明其应用（因为我目前也还不知道），仅先讲清楚这些抽象概念。

相对应地，参考点可以不选在原点，这样参考点和原点就会有偏移。此时就需要定义 $k$ 阶中心距

!!! info "$k$ 阶中心矩 (central moment)"
    $$
    c_k=E(\xi-E\xi)^k
    $$

从定义可以知道，一阶中心距总是 0，二阶中心矩就是方差。其他常用的中心距有三阶中心距和四阶中心距，可以用来表示随机变量分布函数的形状。

!!! info "偏态系数 (Coefficient of Skewness)"
    $$
    Cs=\dfrac{c_3}{c_2^{1.5}}
    $$

    偏态系数 $Cs$ 衡量了随机变量分布的对称性。大于 0 表示正偏态，小于 0 表示负偏态。

!!! info "峰态系数 (Coefficient of Kurtosis)"
    $$
    Ck=\dfrac{c_4}{c_2^2}-3
    $$

    峰态系数衡量了均值处峰值高低，若大于 0 表明比正态分布更尖峭。

对于正态分布 $\xi\sim N(\mu, \sigma^2)$，其偏态系数和峰态系数都是 0。其 $k$ 阶中心矩都存在。

考虑到正态分布 $\xi\sim N(\mu, \sigma^2)$ 的 $k$ 阶中心距其实就是 $\eta\sim N(0, \sigma^2)$ 的 $k$ 阶原点矩，因此有

$$
\begin{aligned}
    &E(\xi-\mu)^{2k}=E\eta^{2k}=(2k-1)!!\sigma^2,\\
    &E(\xi-\mu)^{2k+1}==E\eta^{2k+1}=0
\end{aligned}
$$

## 常见特征函数
### 退化分布
$P(\xi=c)=1$

$$
\varphi(t)=e^{ict}
$$

### 二项分布
$\xi\sim B(n,p)$

$$
\varphi(t)=(pe^{it}+q)^n
$$

??? general "Proof"

    $$
    \begin{aligned}
    \varphi(t)&=\sum_{k=0}^n\begin{pmatrix}
    n\\k
    \end{pmatrix}p^kq^{n-k}e^{itk}\\
    &=\sum_{k=0}^n\begin{pmatrix}
    n\\k
    \end{pmatrix}\left(pe^{it}\right)^kq^{n-k}\\
    &=(pe^{it}+q)^n
    \end{aligned}
    $$

    第二行到第三行使用了二项式定理。

### 泊松分布
$\xi\sim \mathcal{P}(\lambda)$

$$
\varphi(t)=e^{\lambda(e^{it}-1)}
$$

??? general "Proof"
    $$
    \begin{aligned}
    \varphi(t)&=\sum_{k=0}^\infty e^{itk}\frac{\lambda^k}{k!}e^{-\lambda}\\
    &=\sum_{k=0}^\infty \frac{\left(\lambda e^{it}\right)^k}{k!}e^{-\lambda}\\
    &=e^{\lambda e^{it}}\cdot e^{-\lambda}=e^{\lambda(e^{it}-1)}
    \end{aligned}
    $$

### 均匀分布
$\xi\sim U(a,b)$

$$
\varphi(t)=
\frac{e^{ibt}-e^{iat}}{i(b-a)t}
$$

??? general "Proof"
    $$
    \begin{aligned}
    \varphi(t)&=\int_a^be^{itx}\frac{1}{b-a}\mathrm{d}x\\
    &=\frac{1}{i(b-a)t}e^{itx}\bigg|_a^b\\
    &=\frac{e^{ibt}-e^{iat}}{i(b-a)t}
    \end{aligned}
    $$

### 正态分布
$\xi\sim N(\mu, \sigma^2)$

$$
\varphi(t)=e^{it\mu-\frac{\sigma^2t^2}{2}}
$$

??? general "Proof"
    $$
    \begin{aligned}
    \varphi(t)&=\int_{-\infty}^{+\infty}e^{itx}
    e^{-\frac{(x-\mu)^2}{2\sigma^2}}\mathrm{d}x\\
    &\xlongequal{y=\frac{x-\mu}{\sigma}}
    \sigma e^{it\mu}\int_{-\infty}^{+\infty}e^{i(\sigma t)y}
    e^{-\frac{y^2}{2}}\mathrm{d}y
    \end{aligned}
    $$

    考虑标准正态分布需要的积分

    $$
    \begin{aligned}
    \int_{-\infty}^{+\infty}e^{itx}
    e^{-\frac{x^2}{2}}\mathrm{d}x
    &=\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\cos tx\mathrm{d}x
    +i\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\sin tx\mathrm{d}x\\
    &=\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\cos tx\mathrm{d}x
    (\text{第二个积分因奇函数为}0)
    \end{aligned}
    $$

    设 $g(t)=\displaystyle\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\cos tx\mathrm{d}x$，考虑求导

    $$
    \begin{aligned}
    g'(t)&=
    \frac{\mathrm{d}}{\mathrm{d}t}\left(
    \int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\cos tx\mathrm{d}x
    \right)\\
    &=-\int_{-\infty}^{+\infty}xe^{-\frac{x^2}{2}}\sin tx\mathrm{d}x\\
    &=\int_{-\infty}^{+\infty}\sin tx\mathrm{d}e^{-\frac{x^2}{2}}\\
    &=e^{-\frac{x^2}{2}}\sin tx\bigg|_{-\infty}^{+\infty}-
    t\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\cos tx\mathrm{d}x=-tg(t)
    \end{aligned}
    $$

    解微分方程

    $$
    \begin{gathered}
    g'(t)=-tg(t)\\
    \frac{\mathrm{d}g}{g}=-t\mathrm{d}t\\
    g=Ae^{-\frac{t^2}{2}}
    \end{gathered}
    $$

    $g(0)=\displaystyle\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\mathrm{d}x=1$，定得 $A=1$。因此有

    $$
    \int_{-\infty}^{+\infty}e^{itx}
    e^{-\frac{x^2}{2}}\mathrm{d}x=e^{-\frac{t^2}{2}}
    $$

    则原 $\varphi(t)$ 有

    $$
    \varphi(t)=e^{it\mu}\cdot e^{-\frac{\sigma^2t^2}{2}}
    =e^{it\mu-\frac{\sigma^2t^2}{2}}
    $$

## 特征函数可微性

### 预备知识

记

$$
    F(t)=\int_Rf(x,t)p(x)dx
$$

假定其存在，然后以下的 $g\geqslant 0$ 需满足要求

$$
    \int_Rg(x)p(x)dx<\infty
$$

(1)
$\exists g,s.t.\forall x,t$

$$
|f(x,t)|<g(x)
$$

对某个 $x$,若

$$
\lim_{t\to t_0}f(x,t)=f(x,t_0)
$$

则

$$
\lim_{t\to t_0}F(t)=F(t_0)
$$

即 $f$ 连续 $\Rightarrow F$ 关于 $t$ 连续

(2)$\exists g,s.t.\forall x,t$

$$
\bigg|\frac{\partial f(x,t)}
{\partial t}\bigg|<g(x)
$$

则

$$
F'(t)=\int_R\frac{\partial f(x,t)}
{\partial t}p(x)dx
$$

### 可微性

现在令 $g(x)=|x|$，由于预设 $X$ 期望存在，则

$$
\int_{-\infty}^{+\infty}g(x)dF(x)=\int_{-\infty}^{+\infty}|x|dF(x)<\infty
$$

对于特征函数

$$
\varphi(t)=Ee^{itX}=\int_{-\infty}^{+\infty}e^{itx}dF(x)
$$

令 $f(x,t)=e^{itx}$，则

$$
\bigg|\frac{\partial f(x,t)}
{\partial t}\bigg|=
\bigg|ixe^{itx}\bigg|\leqslant|x|=g(x)
$$

那么就有

$$
\varphi'(t)=\int_{-\infty}^{+\infty}\frac{\partial f(x,t)}
{\partial t}dF(x)=i\int_{-\infty}^{+\infty}xe^{itx}dF(x)
$$

特别地，有

$$
\varphi'(0)=i\int_{-\infty}^{+\infty}xdF(x)=i\mu
$$

同理，考虑 $k$ 阶(原点)矩，则若 $E|X|^k<\infty$，则

$$
\varphi^{(k)}(t)=i^k\int_{-\infty}^{+\infty}x^ke^{itx}dF(x)
$$

那么原点处 $\varphi(x)$ 可做 $k$ 次 Taylor 展开

$$
\begin{aligned}
\varphi(x)&=\varphi(0)+\varphi'(0)x+\frac{\varphi''(0)}{2!}x^2+\cdots+\frac{\varphi^{(k)}(0)}{k!}x^n+o(t^k)\\
&=1+iEXt-\frac{1}{2}EX^2t^2+\cdots+i^k\frac{EX^k}{k!}t^k+o(t^k)
\end{aligned}
$$