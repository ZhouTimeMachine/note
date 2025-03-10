<link rel="stylesheet" href="../../../css/counter.css" />

# 数据特征基础

!!! info "Part of note taken on ZJU *Probability Theory (H)*, 2021 Fall & Winter"

## 数学期望

### 离散型随机变量的数学期望

!!! info "数学期望 (离散型)"
    设离散型随机变量 $\xi\sim$

    $$
    \left[
    \begin{matrix}
    x_1&x_2&\cdots&x_n&\cdots\\
    p(x_1)&p(x_2)&\cdots&p(x_n)&\cdots
    \end{matrix}
    \right]
    $$

    如果满足前提条件 $\sum_k x_k p_k$ 绝对收敛 ($\sum_kx_kp_k<\infty$)，则定义**数学期望 (mathematical expectation)** 或**均值 (mean)** 为

    $$
    E\xi=\sum_kx_kp_k
    $$

这里的前提条件为了保证 $E\xi$ 的和不受求和次序的影响。

!!! question "习题"
    计算泊松分布 ($\xi\sim\mathcal{P}(\lambda)$) 的数学期望

??? general "Answer"
    $E\xi=\lambda$

### 连续型随机变量的数学期望

!!! info "数学期望 (连续型)"
    设连续型随机变量 $\xi$ 有密度函数 $p(x)$，且满足前提条件

    $$
    \int_{-\infty}^{+\infty}|x|p(x)\mathrm{d}x<\infty
    $$

    （即 $\displaystyle\int_{-\infty}^{+\infty}xp(x)\mathrm{d}x$ 绝对收敛）则称

    $$
    E\xi=\int_{-\infty}^{+\infty}xp(x)\mathrm{d}x
    $$

    为 $\xi$ 的数学期望。

无论是连续型还是离散型随机变量，如果前提条件(绝对收敛)不满足，都称数学期望不存在。

!!! question "习题"
    计算指数分布 ($\xi\sim\exp(\lambda)$) 的数学期望

??? general "Answer"
    $E\xi=\frac 1\lambda$

!!! question "习题"
    计算正态分布($\xi\sim N(a,\sigma^2)$)的数学期望

??? general "Answer"
    $E\xi=a$，过程可见[正态分布](normal_distr.md)

### 一般随机变量的数学期望

!!! info "数学期望 (一般)"
    设随机变量 $\xi$ 有分布函数 $F(x)$，且满足前提条件

    $$
    \int_{-\infty}^{+\infty}|x|\mathrm{d}Fx<\infty
    $$

    则称

    $$
    E\xi=\int_{-\infty}^{+\infty}x\mathrm{d}F(x)
    $$

    为 $\xi$ 的数学期望。前提条件若不满足，则数学期望不存在。

!!! tip "Remark"
    需要注意的是，这里的积分不是黎曼 (Riemann) 积分，而是新定义的一种积分，名为斯梯尔吉斯 (Stieltjes) 积分，在此不加赘述。所以在此处可以稍稍看一看它的形式，而不必直接计算，因为容易把黎曼积分的思想套在这个积分上，而这是有可能出错的。

### 数学期望的性质

!!! abstract "期望性质 1"
    **性质 1**：$a\leqslant\xi\leqslant b\Rightarrow$
    
    $$
        \exists\; E\xi,a\leqslant E\xi\leqslant b
    $$

    特别地，$\xi=c\Rightarrow E\xi=Ec=c$

    **性质 1'**：$|\xi|<\eta,\exists \;E\eta\Rightarrow$
    
    $$
        \exists \;E\xi,|E\xi|\leqslant E|\xi|\leqslant E\eta
    $$

!!! abstract "期望性质 2"
    **性质2**：$\exists\; E \xi_{1}, \cdots, E \xi_{n}\Rightarrow$ $\forall$ constant $c_{1}, \cdots, c_{n},b,$

    $$
    \exists\; E\left(\sum_{i=1}^{n} c_{i} \xi_{i}+b\right)
    $$

    且

    $$
    E\left(\sum_{i=1}^{n} c_{i} \xi_{i}+b\right)=\sum_{i=1}^{n}c_{i}E \xi_{i}+b
    $$

    特别地, 

    $$
        E\left(\sum_{i=1}^{n} \xi_{i}\right)=\sum_{i=1}^{n} E \xi_{i}, \quad E(c \xi)=c E \xi
    $$

!!! abstract "期望性质 3"
    **性质 3**：$\xi_{1}, \cdots, \xi_{n}$ 相互独立, $\exists\; E \xi_{i}, i=1, \cdots, n$ , 则
    
    $$
    E\left(\xi_{1} \cdots \xi_{n}\right)=E \xi_{1} \cdots E \xi_{n}
    $$

!!! abstract "期望性质 4"
    **性质 4**(有界收敛定理)
    
    - 假设对 $\forall\;\omega \in \Omega$ 有 $\lim _{n \rightarrow \infty} \xi_{n}(\omega)=\xi(\omega)$
    - 并且对一切 $n \geqslant 1$, $\left|\xi_{n}\right| \leqslant M$, 其中 $M$ 为常数

    则

    $$
    \lim _{n \rightarrow \infty} E \xi_{n}=E \xi
    $$

读者可以自证。在这里象征性地证明一下最常用的性质 2：

??? general "性质 2 的证明"
    $$
    \begin{aligned}
    E\left(\sum_{i=1}^{n} c_{i} \xi_{i}+b\right)
    &=E(\xi +b)\cdots\cdots\xi=\sum_{i=1}^{n} c_{i}\xi_i\\
    &=\int_{-\infty}^{+_\infty}(x+b)p_{\xi}(x)\mathrm dx\\
    &=\int_{-\infty}^{+_\infty}xp_{\xi}(x)\mathrm dx+b\cdots\cdots\int_{-\infty}^{+_\infty}p_{\xi}(x)\mathrm dx=1\\
    &=\int\limits_{R^n}\left(\sum_{i=1}^{n} c_{i}x_i\right)p_{\xi_1,\xi_2,\cdots,\xi_n}(x_1,x_2,\cdots,x_n)
    \mathrm{d}x_1\mathrm{d}x_2\cdots\mathrm{d}x_n+b\\
    &=\sum_{i=1}^{n} \left(c_{i}\int\limits_{R^n}x_ip_{\xi_1,\xi_2,\cdots,\xi_n}(x_1,x_2,\cdots,x_n)
    \mathrm{d}x_1\mathrm{d}x_2\cdots\mathrm{d}x_n\right)+b\\
    &=\sum_{i=1}^{n} \left(c_{i}\int_{-\infty}^{+\infty}x_ip_{\xi_i}(x_i)
    \mathrm{d}x_i\right)+b\\
    &=\sum_{i=1}^{n} c_{i}E \xi_{i}+b
    \end{aligned}
    $$

    以上证明是针对连续型随机变量。下面对离散型随机变量进行证明：

    $$
    \begin{aligned}
    E\left(\sum_{i=1}^{n} c_{i} \xi_{i}+b\right)
    &=E(\xi +b)\cdots\cdots\xi=\sum_{i=1}^{n} c_{i}\xi_i\\
    &=\sum_k(x_k+b)p_k\\
    &=\sum_kx_kp_k+b\cdots\cdots\sum_kp_k=1\\
    &=\sum_k\left(\sum_{i=1}^nc_ix_{ik}\right)p_k+b\\
    &=\sum_{i=1}^nc_i\sum_kx_{ik}p_k+b\\
    &=\sum_{i=1}^{n} c_{i}E \xi_{i}+b
    \end{aligned}
    $$

注意到，性质 2 其实就是线性性质。那么我们浮想联翩，线性代数的 DNA 动了。建立一个线性空间 $V$，$V$ 包括所有存在数学期望的一元随机变量。那么 $E:V\to R$ 就是一个线性变换。

进一步地，我们定义一个内积：$\forall \alpha, \beta\in V$, $(\alpha, \beta)=E\alpha\beta$

首先根据内积的公理化定义验证它是内积。

??? general "Proof: $(\alpha, \beta)=E\alpha\beta$ 是一个内积"
    $\forall \alpha,\beta,\gamma\in V, \forall \lambda\in \mathbb{R}$

    (1) 正定性：$E\alpha^2\geqslant 0$，当且仅当 $\alpha$ 服从 $P(\alpha=0)=1$ 的退化分布时（定义这种随机变量为这个线性空间的零元），有 $E\alpha^2= 0$

    (2) 对称性：显然有 $E\alpha\beta=E\beta\alpha$

    (3) 加性：$E(\alpha+\beta)\gamma=E\alpha\gamma+E\beta\gamma$

    (4) 齐性：$E(\lambda\alpha)\beta=\lambda E\alpha\beta$

    加性和齐性由数学期望的性质 2 证得。

因此 $E\alpha\beta$ 可以成为线性空间 $V$ 上的一个内积，那么就有 Cauchy-Schwarz 不等式:

$$
(E\alpha\beta)^2\leqslant E\alpha^2\cdot E\beta^2
$$

特别地，$\forall X,Y\in V$，有 $\exists EX,EY$，则 $\exists E(X-EX),E(Y-EY)$，则 $X-EX,Y-EY\in V$，有

$$
E(X-E X)(Y-E Y) \leq\left(E(X-E X)^{2} E(Y-E Y)^{2}\right)^{1 / 2}
$$

这将是下一节 Pearson 相关系数一个重要性质的依据。

### 条件期望

进入二元关联的考虑，给定不同的 $\eta=y$，$\xi=x$ 的后验概率有所不同，因而会影响其期望。这种情况下的期望就成为条件期望。

当然，需要注意这里是用离散型随机变量举例进行的一个理解，并不严格。如连续型随机变量的期望还需定义。

一般地，若 $\eta=y$ 时，$\xi$ 有条件分布函数 $F_{\xi|\eta}(x|y)$，那么定义随机变量 $\xi$ 的此时的条件期望为

$$
E(\xi|\eta=y)=\int_{-\infty}^{+\infty}x\mathrm dF_{\xi|\eta}(x|y)
$$

针对常见的离散型和连续型随机变量，可以导出其条件期望。

!!! info "离散型随机变量的条件期望"
    $$
    E(\xi|\eta=y)=\sum_ix_ip_{\xi|\eta}(x|y)=\sum_ix_iP(\xi=x|\eta=y)
    $$

!!! info "连续型随机变量的条件期望"
    $$
    E(\xi|\eta=y)=\int_{-\infty}^{+\infty}xp_{\xi|\eta}(x|y)\mathrm dx
    $$

### 全期望公式

全期望公式是一个很有趣的公式，它可以写成

!!! abstract "全期望公式"
    $$
    E(\xi)=E[E(\xi|\eta)]
    $$

在连续型/离散型随机变量的情况下，可以如下做一个简单的推导。

??? general "连续型/离散型随机变量下全期望公式的证明"
    在连续型随机变量的情况下，

    $$
    \begin{aligned}
    E[E(\xi|\eta)]&=
    \int_{-\infty}^{+\infty}E(\xi|\eta)p_Y(y)\mathrm{d}y\\
    &=\int_{-\infty}^{+\infty}\left(\int_{-\infty}^{+\infty}xp_{\xi|\eta}(x|y)\mathrm dx\right)p_Y(y)\mathrm{d}y\\
    &=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x\frac{p(x,y)}{p_Y(y)}\cdot p_Y(y)\mathrm dx\mathrm{d}y\\
    &=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xp(x,y)\mathrm dx\mathrm{d}y\\
    &=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xp(x,y)\mathrm dy\mathrm{d}x\\
    &=\int_{-\infty}^{+\infty}xp_X(x)\mathrm{d}x=E(\xi)
    \end{aligned}
    $$

    在离散型随机变量的情况下，

    $$
    \begin{aligned}
    E[E(\xi|\eta)]&=\sum_jE(\xi|\eta)P(\eta=y_j)\\
    &=\sum_j(\sum_ix_iP(\xi=x_i|\eta=y_j))P(\eta=y_j)\\
    &=\sum_j\sum_ix_iP(\xi=x_i|\eta=y_j)P(\eta=y_j)\\
    &=\sum_ix_i\left(\sum_jP(\xi=x_i|\eta=y_j)P(\eta=y_j)\right)\\
    &=\sum_ix_iP(\xi=x_i)=E(\xi)
    \end{aligned}
    $$

条件期望也有一系列性质，在此不再列举，只举其比较有趣的性质：Cauchy-Schwarz 不等式。

$$
E(XY|Z)\leqslant \sqrt{E(X^2|Z)}\sqrt{E(Y^2|Z)}
$$

条件期望是具有线性的（显然，可以自己写写），那么内积的齐性和加性就满足了。对称性和正定性当然也满足。那么定义二元运算

$$
(X,Y)=E(XY|Z)
$$

就成为一种 $V$ 上的内积。（$V$ 就是上一小节末尾定义的线性空间）所以根据内积的 Cauchy-Schwarz 不等式就可以得证。

## 方差及其性质

### 方差

> 一切为了描述数据的离散程度！

!!! info "离差 (deviation)"
    $\xi-E\xi$

**离差**取期望时，只要 $E\xi$ 存在，那么将会正负相消。因此考虑定义**方差**来描述期望的离散程度。

!!! info "方差 (variance)"
    $E(\xi-E\xi)^2$，即

    $$
    Var\xi(D\xi)=E(\xi-E\xi)^2
    $$

    当然，方差也只有当它存在且为有限值时有意义。

为统一量纲，有时使用**标准差 (standard deviation)**：$\sqrt{Var\xi}$

计算方差可以直接使用定义，也可以使用重要的**方差公式**：

!!! abstract "方差公式"
    $$
    Var\xi=E\xi^2-(E\xi)^2
    $$

??? general "Proof"
    $$
    \begin{aligned}
    E(\xi-E\xi)^2&=E(\xi^2-2\xi E\xi+(E\xi)^2)\\
    &=E\xi^2-2E\xi\cdot E\xi+(E\xi)^2\\
    &=E\xi^2-(E\xi)^2
    \end{aligned}
    $$

### 切比雪夫不等式

!!! abstract "切比雪夫 (Chebyshev) 不等式"
    若随机变量 $\xi$ 的方差存在, 则 $\forall \varepsilon>0$ 有

    $$
    P(|\xi-E \xi| \geq \varepsilon) \leq \frac{Var\xi}{\varepsilon^{2}}
    $$

??? general "Proof" 
    设 $\xi$ 的分布函数为 $F(x)$, 则

    $$
    \begin{aligned}
    P(|\xi-E \xi| \geq \varepsilon) &=\int_{|x-E \xi| \geq \varepsilon} d F(x) \\
    & \leq \int_{|x-E \xi| \geq \varepsilon} \frac{(x-E \xi)^{2}}{\varepsilon^{2}} d F(x) \\
    & \leq \frac{1}{\varepsilon^{2}} \int_{-\infty}^{\infty}(x-E \xi)^{2} d F(x) \\
    &=\frac{Var\xi}{\varepsilon^{2}}
    \end{aligned}
    $$

根据切比雪夫不等式，可以利用方差粗糙估计随机变量落在偏离均值一定范围内的概率。

### 方差的性质

!!! abstract "方差性质 1"
    $Var\xi=0$ 的充要条件是 $P(\xi=c)=1$, 其中 $c$ 是常数.

??? general "Proof"
    显然条件充分。反之，如果 $Var\xi=0$, 记 $E \xi=c$, 由切贝雪夫不等式

    $$
    P(|\xi-E \xi| \geq \varepsilon)=0
    $$

    对 $\forall\varepsilon>0$ 成立。从而
    
    $$
    \begin{aligned}
        P(\xi=c) &=1-P(|\xi-c|>0) \\
        &=1-\lim _{n \rightarrow \infty} P\left(|\xi-c|>\frac{1}{n}\right)=1
    \end{aligned}
    $$

!!! abstract "方差性质 2"
    设 $c, b$ 都是常数, 则

    $$
    Var(c \xi+b)=c^{2}Var\xi
    $$

??? general "Proof"
    $$
    \begin{aligned}
        Var(c \xi+b) &=E(c \xi+b-E(c \xi+b))^{2} \\
        &=E(c \xi+b-c E \xi-b)^{2} \\
        &=c^{2} E(\xi-E \xi)^{2}=c^{2} Var\xi
    \end{aligned}
    $$

!!! abstract "方差性质 3"
    若 $c \neq E \xi$, 则 $Var\xi<E(\xi-c)^{2}$.

??? general "Proof"

    $$
    Var\xi=E \xi^{2}-(E \xi)^{2}
    $$

    和

    $$
    E(\xi-c)^{2}=E \xi^{2}-2 c E \xi+c^{2}
    $$

    两边相减得

    $$
    Var\xi-E(\xi-c)^{2}=-(E \xi-c)^{2}<0
    $$

这个性质说明随机变量 $\xi$ 对数学期望 $E \xi$ 的离散度最小.

!!! abstract "方差性质 4"
    $$
    Var\left(\sum_{i=1}^{n} \xi_{i}\right)=\sum_{i=1}^{n} Var \xi_{i}+2 \sum_{1 \leq i<j \leq n} E\left(\xi_{i}-E \xi_{i}\right)\left(\xi_{j}-E \xi_{j}\right)
    $$

    特别地, 若 $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$ 两两独立, 则
    
    $$
    Var\left(\sum_{i=1}^{n} \xi_{i}\right)=\sum_{i=1}^{n} Var \xi_{i}
    $$

??? general "Proof"
    $$
    \begin{aligned}
    Var\left(\sum_{i=1}^{n} \xi_{i}\right) &=E\left(\sum_{i=1}^{n} \xi_{i}-E \sum_{i=1}^{n} \xi_{i}\right)^{2}=E\left(\sum_{i=1}^{n}\left(\xi_{i}-E \xi\right)\right)^{2} \\
    &=E\left[\sum_{i=1}^{n}\left(\xi_{i}-E \xi_{i}\right)^{2}+2 \sum_{1 \leq i<j \leq n}\left(\xi_{i}-E \xi_{i}\right)\left(\xi_{j}-E \xi_{j}\right)\right] \\
    &=\sum_{i=1}^{n}Var \xi_{i}+2 \sum_{1 \leq i<j \leq n} E\left(\xi_{i}-E \xi_{i}\right)\left(\xi_{j}-E \xi_{j}\right)
    \end{aligned}
    $$

    当 $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$ 两两独立时, 易证 $\xi_{1}-E \xi_{1}, \cdots, \xi_{n}-E \xi_{n}$ 也两两独立, 故

    $$
    E\left(\xi_{i}-E \xi_{i}\right)\left(\xi_{j}-E \xi_{j}\right)=E\left(\xi_{i}-E \xi_{i}\right) \cdot E\left(\xi_{j}-E \xi_{j}\right)=0
    $$

    交叉项为0，则成立
    
    $$
    Var\left(\sum_{i=1}^{n} \xi_{i}\right)=\sum_{i=1}^{n} Var \xi_{i}
    $$

!!! question "习题"
    求二项分布($\xi\sim B(n,p)$)的方差

!!! tip "Tip"
    $\xi=\sum_{i=1}^n\xi_i,\xi_i$ 服从两点分布且相互独立

??? general "Answer"
    $Var\xi=npq$

!!! question "习题"
    求一元正态分布($\xi\sim N(a,\sigma^2)$)的方差

??? general "Answer"
    $Var\xi=\sigma^2$，详细过程见[正态分布](normal_distr.md)

## 协方差及其性质

### 协方差

对于随机向量，需要研究各分量之间的关系。

!!! info "协方差"
    设 $\xi_{i}$ 和 $\xi_{j}$ 的联合分布函数为 $F_{i j}(x, y)$. 若 $E\left|\left(\xi_{i}-E \xi_{i}\right)\left(\xi_{j}-E \xi_{j}\right)\right|<\infty$, 称

    $$
    E\left(\xi_{i}-E \xi_{i}\right)\left(\xi_{j}-E \xi_{j}\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(x-E \xi_{i}\right)\left(y-E \xi_{j}\right) d F_{i j}(x, y)
    $$

    为 $\xi_{i}$ 和 $\xi_{j}$ 的**协方差 (covariance)**, 记作 $Cov\left(\xi_{i}, \xi_{j}\right)$.

因此协方差就是方差性质 4 当中的交叉项，因此方差性质 4 可以改写为

$$
Var\left(\sum_{i=1}^{n} \xi_{i}\right)=\sum_{i=1}^{n} Var \xi_{i}+2 \sum_{1 \leq i<j \leq n} Cov\left(\xi_{i}, \xi_{j}\right)
$$

### 协方差的性质

!!! abstract "协方差性质 1"
    $Cov(\xi, \eta)=Cov(\eta, \xi)=E \xi \eta-E \xi E \eta$

!!! abstract "协方差性质 2"
    设 $a, b$ 是常数, 则
    
    $$
    Cov(a \xi, b \eta)=a b Cov(\xi, \eta)
    $$

!!! abstract "协方差性质 3"
    $\displaystyle Cov\left(\sum_{i=1}^{n} \xi_{i}, \eta\right)=\sum_{i=1}^{n} Cov\left(\xi_{i}, \eta\right)$.

!!! info "协方差阵"

    对于 $n$ 维随机向量 $\boldsymbol{\xi}=\left(\xi_{1}, \cdots, \xi_{n}\right)^{\prime}$, 可定义它的协方差阵如

    $$
    \boldsymbol{B}=E(\boldsymbol{\xi}-E \boldsymbol{\xi})(\boldsymbol{\xi}-E \boldsymbol{\xi})^{\top}
    =\left[\begin{array}{cccc}
    b_{11} & b_{12} & \cdots & b_{1 n} \\
    b_{21} & b_{22} & \cdots & b_{2 n} \\
    \vdots & \vdots & \vdots & \vdots \\
    b_{n 1} & b_{n 2} & \cdots & b_{n n}
    \end{array}\right]
    $$

    其中 

    $$
    b_{i j}=
    \begin{cases}
    Cov\left(\xi_{i}, \xi_{j}\right), & i\neq j\\
    Var(\xi_i),&i=j
    \end{cases}
    $$

由上面的性质可知 $\boldsymbol{B}$ 是一个对称阵, 且对任何实数 $t_{j}, j=1,2, \cdots, n$, 二次型

$$
\left[t_1,t_2,\cdots,t_n\right]
\left[\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 n} \\
b_{21} & b_{22} & \cdots & b_{2 n} \\
\vdots & \vdots & \vdots & \vdots \\
b_{n 1} & b_{n 2} & \cdots & b_{n n}
\end{array}\right]\left[\begin{matrix}
t_1\\
t_2\\
\vdots\\
t_n
\end{matrix}\right]=\sum_{j, k} b_{j k} t_{j} t_{k}
$$

$$
\begin{aligned}
\sum_{j, k} b_{j k} t_{j} t_{k} &=\sum_{j, k} t_{j} t_{k} E\left(\xi_{j}-E \xi_{j}\right)\left(\xi_{k}-E \xi_{k}\right) \\
&=E\left(\sum_{j=1}^{n} t_{j}\left(\xi_{j}-E \xi_{j}\right)\right)^{2} \geq 0
\end{aligned}
$$

即随机向量 $\xi$ 的协方差阵 $\boldsymbol{B}$ 是非负定的.

!!! abstract "协方差性质 4"
    设

    $$
    \xi=\left(\xi_{1}, \xi_{2}, \cdots, \xi_{n}\right)^{\top}, \quad \boldsymbol{C}=\left[\begin{array}{cccc}
    C_{11} & C_{12} & \cdots & C_{1 n} \\
    C_{21} & C_{22} & \cdots & C_{2 n} \\
    \vdots & \vdots & \vdots & \vdots \\
    C_{n 1} & C_{n 2} & \cdots & C_{n n}
    \end{array}\right]
    $$

    则 $C \xi$ 的协方差阵为 $C B C^{\top}$, 其中 $B$ 是 $\xi$ 的协方差阵。因为
    
    $$
    E C(\xi-E \xi)(C(\xi-E \xi))^{\top}=C B C^{\top}
    $$

!!! abstract "协方差性质 5"
    设 $\xi=\left(\xi_{1}, \xi_{2}, \cdots, \xi_{n}\right)^{\top}\sim N(\mu, B)$, 其中 $\mu$ 为 $n$ 维向量, $B$ 为 $n \times n$ 正定对称矩阵。
    
    则 $\xi$ 的数学期望为 $\mu$, 协方差矩阵为 $B$。

特别地, 当 $\mu=0, B=I$ 时, $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$ 为相互独立的标准正态随机变量,

有 $E \xi_{i}=0$, $Var\left(\xi_{i}\right)=1, Cov\left(\xi_{i}, \xi_{j}\right)=0, i \neq j$。即 $E\xi=0_{n\times 1}$, 协方差矩阵为 $I$。

一般地，设 $T:V\to V, \mathcal{M}(T)=B$，$V$ 是所有 $n$ 元服从正态分布的随机向量构成的线性空间。由于 $B$ 为正定对称矩阵，$\exists$ 正的实特征值 $\lambda_1,\lambda_2,\cdots, \lambda_n$ 和正交矩阵 $Q$ 使得

$$
\begin{aligned}
B&=Q^{\top}\mathrm{diag}\{\lambda_1,\lambda_2,\cdots, \lambda_n\}Q
&(\text{Orthogonal Diagonalization})
\\
&=Q^{\top}D^2Q
&(D=\mathrm{diag}\{\sqrt{\lambda_1},\sqrt{\lambda_2},\cdots, \sqrt{\lambda_n}\})
\\
&=Q^{\top}D(QQ^{\top})DQ
&(QQ^{\top}=I)
\\
&=(Q^{\top}DQ)(Q^{\top}DQ)
&(\text{Associative Law})
\end{aligned}
$$

令 $L=Q^{\top}DQ$，则 $B=L^2$。考虑 $L$ 的特征多项式 $f(\lambda)$：

$$
f(\lambda)=|\lambda E-L|=|\lambda Q^{\top}Q-Q^{\top}DQ|=|Q^{\top}|\cdot|\lambda E-D|\cdot|Q|
=\prod_{i=1}^n(\lambda-\sqrt{\lambda_i})
$$

因此 $\sqrt{\lambda_1},\sqrt{\lambda_2},\cdots, \sqrt{\lambda_n}$ 是 $L$ 的 $n$ 个正的实特征值，可知 $L$ 也是正交对称矩阵。

所以 $B=L^2=LL^{\top}=LIL^{\top}$。令 $\eta=L^{-1}(\xi-\mu)$，则 $\xi$ 可以分解为 $\xi=L \eta+\mu$。 

可以证明，这样分解得到的 $\eta$ 服从标准正态分布，即 $\eta=L^{-1}(\xi-\mu) \sim N(0, I)$，$E\eta=0$，协方差矩阵为单位矩阵 $I$。

## Pearson 相关系数及其性质

### Pearson 相关系数

!!! info "Pearson 相关系数"
    令 $\xi^{*}=\displaystyle\frac{\xi-E \xi}{\sqrt{Var \xi}}, \eta^{*}=\frac{\eta-E \eta}{\sqrt{Var\eta}}$。称

    $$
    r_{\xi \eta}=Cov\left(\xi^{*}, \eta^{*}\right)=\frac{E(\xi-E \xi)(\eta-E \eta)}{\sqrt{Var \xi Var \eta}}
    $$

    为 $\xi, \eta$ 的 Pearson 相关系数 (correlation coefficient)。

### Pearson 相关系数的性质

上一节的末尾，已经证明得到

$$
E(X-E X)(Y-E Y) \leq\left(E(X-E X)^{2} E(Y-E Y)^{2}\right)^{1 / 2}
$$

因此显然可以得到性质1。

!!! abstract "Pearson 相关系数性质 1"
    对 Pearson 相关系数 $r_{\xi n}$ 有

    $$
    \left|r_{\xi \eta}\right| \leq 1
    $$

结合空间向量几何相关知识，$r_{\xi n}=1$ 当且仅当

$$
P\left(\frac{\xi-E \xi}{\sqrt{\operatorname{Var} \xi}}=\frac{\eta-E \eta}{\sqrt{\operatorname{Var} \eta}}\right)=1
$$

$r_{\xi n}=-1$ 当且仅当

$$
P\left(\frac{\xi-E \xi}{\sqrt{\operatorname{Var} \xi}}=-\frac{\eta-E \eta}{\sqrt{\operatorname{Var} \eta}}\right)=1
$$

由性质 1，$r_{\xi \eta}=\pm 1$ 时, $\xi$ 与 $\eta$ 存在线性关系。

另一个极端情形，定义 $r_{\xi \eta}=0$ 时，$\xi$ 与 $\eta$ **不相关 (uncorrelated)**.

!!! abstract "Pearson 相关系数性质 2"
    对随机变量 $\xi$ 和 $\eta$, 如果它们的方差有限, 则下列事实等价:

    (1) $\operatorname{Cov}(\xi, \eta)=0$;

    (2) $\xi$ 与 $\eta$ 不相关;

    (3) $E \xi \eta=E \xi E \eta$;

    (4) $\operatorname{Var}(\xi+\eta)=\operatorname{Var} \xi+\operatorname{Var} \eta$.

??? general "Proof"

    显然 (1) 与 (2) 等价. 又由协方差的性质 1 得 (1) 与 (3) 等价。

    $Var(\xi +\eta)=Var(\xi)+Var(\eta) +Cov(\xi,\eta)$ (方差性质4)，得 (1) 与 (4) 等价。

!!! abstract "Pearson 相关系数性质 3"
    若 $\xi$ 与 $\eta$ 独立，且它们的方差有限，则 $\xi$ 与 $\eta$ 不相关。

??? general "Proof"
    显然，由 $\xi$ 与 $\eta$ 独立知 (3) 成立，从而 $\xi$ 与 $\eta$ 不相关。但其逆不真。

!!! example "不相关但是不独立的例子"
    设随机变量 $\theta$ 服从均匀分布 $U(0,2 \pi) . \xi=\cos \theta, \eta=\sin \theta$。显然 $\xi^{2}+\eta^{2}=1$，故 $\xi$ 与 $\eta$ 不独立。但

    $$
    \begin{gathered}
    E \xi=E \cos \theta=\int_{0}^{2 \pi} \frac{1}{2 \pi} \cos \varphi d \varphi=0 \\
    E \eta=E \sin \theta=\int_{0}^{2 \pi} \frac{1}{2 \pi} \sin \varphi d \varphi=0 \\
    E \xi \eta=E \sin \theta \cos \theta=\int_{0}^{2 \pi} \frac{1}{2 \pi} \sin \varphi \cos \varphi d \varphi=0
    \end{gathered}
    $$

    即 $E\xi\eta=E\xi E\eta$，$\xi$ 与 $\eta$ 不相关。
    
    因此独立条件强于不相关，独立一定不相关，不相关不一定独立。

!!! abstract "Pearson 相关系数性质 4"
    对二元正态随机向量, 两个分量不相关与独立是等价的

!!! question "习题"
    证明性质 4。详解可见[正态分布](normal_distr.md)。