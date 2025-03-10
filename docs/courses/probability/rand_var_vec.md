<link rel="stylesheet" href="../../../css/counter.css" />

# 随机变量与随机向量

!!! info "Part of note taken on ZJU *Probability Theory (H)*, 2021 Fall & Winter"

!!! warning "本页面还在建设中"

## 随机变量

### 随机变量的概念

!!! info "随机变量"
    定义概率空间 $(\Omega, \mathcal{F}, P)$ 上的单值实函数 $\xi(\omega)$，即

    $$
    \xi: \Omega\to \mathbb R
    $$

    还要求 $\xi(\omega)$ 的任意取值组合对应的样本点集合构成的事件在事件域 $\mathcal{F}$ 中，这样就可以称 $\xi(\omega)$ 为**随机变量 (random variable)**

实在太过抽象，暂且可以认为随机变量就是一个随机值。

### 离散型随机变量

离散型随机变量：随机变量 $\xi$ 可取的值至多可列个。

!!! info "分布列 (distribution sequence)"
    $$
    \left[
    \begin{matrix}
    x_1&x_2&\cdots&x_n&\cdots\\
    p(x_1)&p(x_2)&\cdots&p(x_n)&\cdots
    \end{matrix}
    \right]
    $$

第一行是 $\xi$ 可能取的值，第二行是 $\xi$ 取这些值的概率。

!!! abstract "分布列的性质"
    - 正性，即

    $$
    p(x_i)>0,i=1,2\cdots
    $$

    - 规范性，即

    $$
    \sum_{i=1}^\infty p(x_i)=1
    $$

!!! example "Examples"
    对一些常见离散型随机变量举例如下：

    === "退化分布"
        即 degenerate distribution

        $$
        \left[
        \begin{matrix}
        c\\
        1
        \end{matrix}
        \right]
        $$

    === "两点分布"
        即**伯努利分布**，Bernoulli distribution

        $$
        \left[
        \begin{matrix}
        1&0\\
        p&1-p
        \end{matrix}
        \right],p\in (0,1)
        $$

    === "二项分布"
        即 binomial distribution

        $$
        P(\xi=k)=\begin{pmatrix}
            n\\k
        \end{pmatrix}
        p^k(1-p)^{n-k},p\in (0,1),k=0,1,\cdots,n
        $$

        记为 $\xi\sim B(n,p)$

    === "泊松分布"
        即 Poisson distribution

        $$
        P(\xi=k)=\frac{\lambda^k}{k!}e^{-\lambda}
        ,\lambda>0,k\in \mathbb N
        $$

        记为 $\xi\sim\mathcal{P}(\lambda)$

    === "几何分布"
        即 geometry distribution

        $$
        P(\xi=k)=p(1-p)^{k-1},p\in (0,1),k\in \mathbb{N}_+
        $$

    === "超几何分布"
        即 hypergeometry distribution

        $$
        P(\xi=k)=\frac{\displaystyle
        \begin{pmatrix}
            M\\k
        \end{pmatrix}
        \begin{pmatrix}
            N-M\\n-k
        \end{pmatrix}
            }{\displaystyle
        \begin{pmatrix}
            N\\n
        \end{pmatrix}}
        ,n\leqslant N,M\leqslant N,k=0,1,\cdots, \min\{n,M\}
        $$

### 分布函数与连续型随机向量
#### 分布函数

!!! info "分布函数 (distribution function)"
    定义随机变量 $\xi(\omega)$ 的**分布函数**为

    $$
        F(x) = P(\xi\leqslant x),\quad -\infty<x<+\infty
    $$

!!! info "分布函数公理化定义"
    (1) 单调递增(不要求严格)：$a<b$, $F(a)\leqslant F(b)$

    (2) $\displaystyle\lim_{x\to -\infty}F(x)=0,\lim_{x\to +\infty}F(x)=1$

    (3) 处处左极限存在，右连续。即
    
    $$
    \exists F(x-0)=\lim_{h\to 0^+}F(x-h)
    $$
    
    $$
    F(x+0)=\lim_{h\to 0^+}F(x+h)=F(x)
    $$

注意，如果修改分布函数定义为

$$
F(x)=P(\xi<x),-\infty<x<+\infty
$$

那么 (3) 应该修改为处处右极限存在，左连续。

#### 连续型随机变量

!!! info "连续型随机变量"
    若 $\exists$ 一个非负的可积函数 $p(x)$ s.t. 分布函数 $F(x)$ 满足

    $$
    F(x)=\int_{-\infty}^xp(y)\mathrm{d}y,-\infty<x<+\infty
    $$

    则以 $F(X)$ 为分布函数的 $\xi$ 称为**连续型** (continuous) 随机变量。

其中，$p(x)$ 称为 $\xi$ 的概率密度函数，简称**密度函数 (density function)**

$F(x)$ 是一个变上限积分，可以证明，在 $p(x)$ 的连续点处，有

$$
F'(x)=p(x)
$$

$\xi$ 落于 $(a,b]$ 的概率为

$$
\begin{aligned}
P(a<\xi\leqslant b)
&=F(b)-F(a)\\
&=\int_{-\infty}^b p(y)\mathrm{d}y-\int_{-\infty}^a p(y)\mathrm{d}y\\
&=\int_a^b p(y)\mathrm{d}y
\end{aligned}
$$

然而需注意，联系几何概型有类似结论：

$$
\begin{aligned}
P(\xi=c)&=F(c)-\lim_{h\to 0^+}F(c-h)\\
&=\lim_{h\to 0^+}\int_{c-h}^cp(y)\mathrm dy=0
\end{aligned}
$$

类似离散型随机变量分布列的性质，连续性随机变量的密度函数有如下性质。

!!! abstract "密度函数的性质"
    - 非负性，即

    $$
    p(x)\geqslant 0
    $$

    - 规范性，即

    $$
    \int_{-\infty}^{+\infty}p(x)\mathrm dx=1
    $$

注意，随机变量包括连续型随机变量和离散型随机变量，但随机变量并不总是连续性随机变量或离散型随机变量。如

$$
F(x)= 
\begin{cases}
    0, & x<0 \\ 
    \dfrac{1+x}{2}, & 0 \leq x<1 \\
    1, & x \geq 1
\end{cases}
$$

根据分布函数的公理化定义可以判断它确实是一个分布函数。但是对应的随机变量取值在 $[\frac12,1)$，取值并不可列，因此不是离散型随机变量。它也不是连续型随机变量，因为 $F(x)$ 不连续，比如可以看出应有 $P(\xi=0)=\frac12$，与连续性随机变量 $P(\xi=c)=0$ 的性质矛盾。

!!! example "Examples"
    对常见连续性随机变量举例如下：

    === "均匀 (uniform) 分布"
        $$
        p(x)=\begin{cases}
            \dfrac{1}{b-a},
            & a \leqslant x \leqslant b \\
            0, & \text { 其他. }
        \end{cases}
        $$

        记作 $\xi\sim U(a,b)$

    === "一元正态 (normal) 分布"
        $$
        p(x)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-\displaystyle\frac{(x-\mu)^{2}}{2 \sigma^{2}}}, \quad-\infty<x<\infty
        ,\quad\sigma>0
        $$

        记作 $\xi\sim N(\mu,\sigma^2)$

    === "指数 (exponential) 分布"
        $$
        p(x)=\left\{\begin{array}{ll}
            \lambda e^{-\lambda x}, & x \geq 0, \\
            0, & x<0
            \end{array} \quad \lambda>0\right.
        $$

        记作 $\xi\sim \exp(\lambda)$

## 随机向量
### 随机向量

!!! info "随机向量"
    在同一概率空间 $(\Omega,\mathcal{F}, P)$ 上，有随机变量 $\xi_1(\omega),\xi_2(\omega),\cdots,\xi_n(\omega)$，称

    $$
    \mathbf{\xi}(\omega)=\left(\xi_1(\omega), \xi_2(\omega), \cdots, \xi_n(\omega)\right)
    $$

    为 $n$ **维随机向量**。

### 离散型随机向量

考虑离散型随机向量 $(\xi,\eta)$，其**联合分布**为：

$$
    P(\xi=x_i,\eta=y_j)=p_{ij}
$$

其**边际分布**为：

$$
    P(\xi=x_i)=p_{i\cdot}=\sum_j p_{ij}
$$

$$
    P(\eta=y_j)=p_{\cdot j}=\sum_i p_{ij}
$$

其分布列可以这么画：

$$
\begin{array}{c|ccccc|c}
\hline
\xi\backslash\eta & y_{1} & y_{2} & \cdots & y_{n} & \cdots & p_{i\cdot} \\
\hline
x_{1} & p_{11} & p_{11} & \cdots & p_{1 n} & \cdots &p_{1\cdot}\\
x_{2} & p_{21} & p_{22} & \cdots & p_{2 n} & \cdots &p_{2\cdot}\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots &\vdots\\
x_{m} & p_{m 1} & p_{m 2} & \cdots & p_{m n} & \cdots &p_{m\cdot}\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots &\vdots\\
\hline
p_{\cdot j}& p_{\cdot 1} & p_{\cdot 2} & \cdots & p_{\cdot n} & \cdots\\
\hline
\end{array}
$$

给出一道练习用的例题：

!!! question "例题"
    口袋中有 2 个白球 3 个黑球，连取两次，每次任取一球。设 $\xi$ 为第一次得白球数，$\eta$ 为第二次得白球数。对 **(1) 有放回**，**(2) 无放回**两种情况，分别求 $(\xi, \eta)$ 的联合分布。

??? general "Answer"
    **(1)**

    $$
        P(\xi=0, \eta=0)=P(\xi=0) P(\eta=0)=\frac{3}{5} \cdot \frac{3}{5}
    $$

    同理

    $$
    \begin{aligned}
        &P(\xi=0, \eta=1)=\frac{3}{5} \cdot \frac{2}{5} \\
        &P(\xi=1, \eta=0)=\frac{2}{5} \cdot \frac{3}{5} \\
        &P(\xi=1, \eta=1)=\frac{2}{5} \cdot \frac{2}{5}
    \end{aligned}
    $$

    得

    $$
    \begin{array}{c|cc|c}
    \hline
    \xi\backslash\eta& 0 & 1 & p_{i\cdot} \\
    \hline
    0 & 3/5 \cdot 3/5 & 3/5 \cdot 2/5 & 3/5 \\
    1 & 2/5 \cdot 3/5 & 2/5 \cdot 2/5 & 2/5 \\
    \hline
    p_{\cdot j} & 3/5 & 2/5 &
    \end{array}
    $$

    **(2)**

    $$
    \begin{array}{c|cc|c}
    \hline
    \xi\backslash\eta & 0 & 1 & p_{i\cdot} \\
    \hline
    0 & 3/5 \cdot 2/4 & 3/5 \cdot 2/4 & 3/5 \\
    1 & 2/5 \cdot 3/4 & 2/5 \cdot 1/4 & 2/5 \\
    \hline
    p_{\cdot j} & 3/5 & 2/5 &
    \end{array}
    $$

### n 元分布函数

!!! info "随机向量的联合分布函数"
    $\forall\left(x_{1}, \cdots, x_{n}\right) \in \mathbf{R}^{n}$，称 $n$ 元函数

    $$
    F\left(x_{1}, \cdots, x_{n}\right)=P\left(\xi_{1}(\omega) \leq x_{1}, \xi_{2}(\omega) \leq x_{2}, \cdots, \xi_{n}(\omega) \leq x_{n}\right)
    $$

    为随机向量 $\xi(\omega)=\left(\xi_{1}(\omega), \xi_{2}(\omega), \cdots, \xi_{n}(\omega)\right)$ 的
    **(联合)分布函数**。

以二元联合分布函数为例，其有性质（对标一元分布函数的公理化定义）：

!!! abstract "二元联合分布函数性质"
    (1) 对每个变量单调递增(不严格)

    (2) 对每个变量右连续，左极限存在

    (3) $\forall (x,y)$
    
    $$
    F(x,-\infty)=0,\quad F(-\infty, y)=0,\quad F(\infty, \infty)=1
    $$

    (4) $\forall a_1,a_2,b_1,b_2\in R,a_1<b_1,a_2<b_2$
    
    $$
    F(b_1,b_2)-F(a_1,b_2)-F(b_1,a_2)+F(a_1,a_2)\geqslant 0
    $$

考虑边际分布函数 $F_{\xi}(x)$ 与 $F_{\eta}(y)$

$$
\begin{aligned}
F_{\xi}(x)
&=P(\xi<x)\\
&=P(\xi<x,-\infty<y<+\infty)\\
&=F(x, +\infty)
\end{aligned}
$$

同理 $F_{\eta}(y)=F(+\infty, y)$

### 连续型随机向量

若存在 $n$ 元可积的非负函数 $p\left(x_{1}, \cdots, x_{n}\right)$, 使 $n$ 元分布函数可表示为

$$
F\left(x_{1}, \cdots, x_{n}\right)=\int_{-\infty}^{x_{1}} \cdots \int_{-\infty}^{x_{n}} p\left(y_{1}, \cdots, y_{n}\right) d y_{1} \cdots d y_{n}
$$

则称它是连续型分布，并称 $p\left(x_{1}, \cdots, x_{n}\right)$ 为 (联合) 密度函数。显然，密度函数满足如下条件:

!!! info "联合密度函数的性质"
    (1) $p\left(x_{1}, \cdots, x_{n}\right) \geq 0$

    (2)

    $$
    \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} p\left(y_{1}, \cdots, y_{n}\right) d y_{1} \cdots d y_{n}=1
    $$

在这里不多加赘述，只是需要提及一下 $n$ 维正态分布的形式。

!!! info "n 维正态分布"
    设 $\boldsymbol{B}=\left(b_{i j}\right)$ 为 $n$ 维正定对称矩阵, $|\boldsymbol{B}|$ 为其行列式, $\boldsymbol{B}^{-1}$ 为其逆,

    又设 $\boldsymbol{x}=$ $\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\top}$, $\boldsymbol{a}=\left(a_{1}, a_{2}, \cdots, a_{n}\right)^{\top}$, 则称

    $$
    p(\boldsymbol{x})=\frac{1}{(2 \pi)^{n / 2}|\boldsymbol{B}|^{1 / 2}} \exp \left\{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{a})^{\top} \boldsymbol{B}^{-1}(\boldsymbol{x}-\boldsymbol{a})\right\}
    $$

    为 $n$ 维正态密度函数。若随机向量 $\xi$ 具有此密度函数，则称 $\xi$ 服从 $n$ 维正态分布，记作 $\xi \sim N(\boldsymbol{a}, \boldsymbol{B})$

对 $n=1$ 和 $n=2$ 时的正态分布进行额外的讨论：

=== "$n=1$"
    $n=1$ 时，$\boldsymbol{B}=\sigma^2,\boldsymbol{a}=\mu$，得

    $$
    p(x)=\frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
    $$

=== "$n=2$"
    $n=2$ 时，记

    $$
    \boldsymbol{B}=\left(\begin{array}{cc}
    \sigma_{1}^{2} & r \sigma_{1} \sigma_{2} \\
    r \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
    \end{array}\right)
    $$

    其中 $\sigma_{1}, \sigma_{2}>0,|r|<1 . \boldsymbol{x}=(x, y)^{\prime}, \boldsymbol{a}=(a, b)^{\prime}$. 则

    $$
    \boldsymbol{B}^{-1}=\frac{1}{|\boldsymbol{B}|}\left(\begin{array}{cc}
    \sigma_{2}^{2} & -r \sigma_{1} \sigma_{2} \\
    -r \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
    \end{array}\right)
    $$

    故可得

    $$
    \begin{aligned}
    p(x, y)=& \frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-r^{2}}} \exp \left\{-\frac{1}{2\left(1-r^{2}\right)}\left[\frac{(x-a)^{2}}{\sigma_{1}^{2}}-\frac{2 r(x-a)(y-b)}{\sigma_{1} \sigma_{2}}+\frac{(y-b)^{2}}{\sigma_{2}^{2}}\right]\right\}
    \end{aligned}
    $$

    简记作 $(\xi, \eta) \sim N\left(a, b, \sigma_{1}^{2}, \sigma_{2}^{2}, r\right)$。

关于正态分布的更多详细内容见[正态分布](normal_distr.md)。

## 随机变量的独立性
设 $F(x, y), F_{\xi}(x)$ 和 $F_{\eta}(y)$ 分别为 $(\xi, \eta)$ 的联合分布函数及其边际分布函数, 如 果对一切 $x, y$ 都有

$$
    F(x, y)=F_{\xi}(x) F_{\eta}(y)
$$

成立，则称 $\xi$ 与 $\eta$ 相互独立。

### 离散型随机变量的独立性

!!! info "离散型随机变量的独立性"
    如果离散型随机向量 $(\xi, \eta)$ 的联合分布列满足

    $$
    P\left(\xi=x_{i}, \eta=y_{j}\right)=P\left(\xi=x_{i}\right) P\left(\eta=y_{j}\right), \quad i, j=1,2, \cdots,
    $$

    即

    $$
    p_{ij}=p_{i\cdot}\cdot p_{\cdot j}
    $$

    则称 $\xi$ 与 $\eta$ **相互独立(independent)**。否则，称 $\xi$ 与 $\eta$ **相依(dependent)**。

可以这么推导：

??? general "Proof"
    $$
    F(x,y)=P(\xi \leq x, \eta \leq y)=\sum_{x_{i} \leqslant x} \sum_{y_{j} \leqslant y} P\left(\xi=x_{i}, \eta=y_{j}\right)
    $$

    $$
    F_{\xi}(x) F_{\eta}(y)=\sum_{x_{i} \leqslant x} P\left(\xi=x_{i}\right) \sum_{y_{j} \leqslant y} P\left(\eta=y_{j}\right)
    $$

    根据

    $$
        F(x, y)=F_{\xi}(x) F_{\eta}(y)
    $$

    令 $x_1<x_2<\cdots,y_1<y_2<\cdots$，有

    $$
        F(x_1, y_1)=F_{\xi}(x_1) F_{\eta}(y_1)
    $$

    即

    $$
        p_{11}=p_{1\cdot}\cdot p_{\cdot 1}
    $$

    考虑数学归纳，如果 $p_{ij}=p_{i\cdot}\cdot p_{\cdot j}$ 对 $\forall i\leqslant m,j\leqslant n(i,j\in \mathbb{N}_+)$ 成立，那么根据

    $$
        F(x_{m+1}, y_n)=F_{\xi}(x_{m+1}) F_{\eta}(y_n)
    $$

    有

    $$
    \sum_{i \leqslant m+1} \sum_{j \leqslant n} p_{ij}
    =\sum_{i \leqslant m+1} p_{i\cdot} \sum_{j \leqslant n} p_{\cdot j}
    $$

    根据已有条件，除去相等项，可以得到

    $$
    p_{m+1,n}=p_{m+1,\cdot}\cdot p_{\cdot, n}
    $$

    同理，根据

    $$
        F(x_m, y_{n+1})=F_{\xi}(x_m) F_{\eta}(y_{n+1})
    $$

    可以得到

    $$
    p_{m,n+1}=p_{m,\cdot}\cdot p_{\cdot, n+1}
    $$

    因此对于离散型随机变量，用分布函数定义的随机变量的独立性条件

    $$
        F(x, y)=F_{\xi}(x) F_{\eta}(y)
    $$

    可以通过数学归纳推出其特有独立性条件

    $$
        p_{ij}=p_{i\cdot}\cdot p_{\cdot j}
    $$

    同理，很方便地可以用后者反推出前者。因此在离散型随机变量中，这两种定义是等价的。

### 连续型随机变量的独立性

!!! info "连续型随机变量的独立性"
    设 $p(x, y)$ 与 $p_{\xi}(x), p_{\eta}(y)$ 分别为连续型随机向量 $(\xi, \eta)$ 的联合密度和边际密度, 则 $\xi, \eta$ 相互独立的充要条件是

    $$
        p(x, y)=p_{\xi}(x) p_{\eta}(y)
    $$

??? general "Proof"
    $\forall x, y$,

    $$
    \begin{aligned}
    &F(x, y) =F_{\xi}(x) F_{\eta}(y) \\
    & \Longleftrightarrow \int_{-\infty}^{x} \int_{-\infty}^{y} p(u, v) d u d v=\int_{-\infty}^{x} p_{\xi}(u) d u \int_{-\infty}^{y} p_{\eta}(v) d v \\
    & \Longleftrightarrow \int_{-\infty}^{x} \int_{-\infty}^{y} p(u, v) d u d v=\int_{-\infty}^{x} \int_{-\infty}^{y} p_{\xi}(u) p_{\eta}(v) d u d v \\
    & \Longleftrightarrow p(x, y)=p_{\xi}(x) p_{\eta}(y)
    \end{aligned}
    $$

## 随机变量的条件分布

### 离散型随机变量的条件分布

设 $(\xi, \eta)$ 的联合分布列为 $P\left(\xi=x_{i}, \eta=y_{j}\right)=p_{i j}, i, j=1,2, \cdots$。

若已知 $\xi=x_{i}(P(\xi=$ $\left.x_{i}>0\right)$, 则

$$
P\left(\eta=y_{j} \mid \xi=x_{i}\right)=\frac{P\left(\xi=x_{i}, \eta=y_{j}\right)}{P\left(\xi=x_{i}\right)}=\frac{p_{i j}}{p_{i\cdot}}, \quad j=1,2, \cdots
$$

即

$$
p_{\eta|\xi}(y_j|x_i)=\frac{p_{i j}}{p_{i\cdot}}
$$

如果令事件 $A=\{\eta=y_j\}$，$B=\{\xi=x_i\}$，由乘法公式可知这是很自然的。

可见，$\xi$ 和 $\eta$ 相互独立的等价条件是

$$
P(\eta=y_{j} \mid \xi=x_{i})=P(\eta=y_j)
$$

定义 $\xi=x_i$ 的条件下 $\eta$ 的**条件分布函数**：

$$
P(\eta\leqslant y|\xi = x_i)=\sum_{j:y_j\leqslant y}p_{\eta|\xi}(y_j|x_i)
$$

### 连续性随机变量的条件分布

首先获得条件分布函数，通过条件分布函数求导获得概率密度函数。

$$
\begin{aligned}
    P(Y\leqslant y|X=x)&=\lim_{\epsilon\to0}P(Y\leqslant y|x-\epsilon<X\leqslant x+\epsilon)\\
    &=\lim_{\epsilon\to0}\frac{P(Y\leqslant y,x-\epsilon<X\leqslant x+\epsilon)}{P(x-\epsilon<X\leqslant x+\epsilon)}\\
    &=\lim_{\epsilon\to0}\frac{\displaystyle\frac{1}{2\epsilon}\int_{x-\epsilon}^{x+\epsilon}\int_{-\infty}^yp(u,v)\mathrm{d}u\mathrm{d}v}{\displaystyle \frac{1}{2\epsilon}\int_{x-\epsilon}^{x+\epsilon}p_X(u)\mathrm{d}u}\\
    &=\frac{\int_{-\infty}^{y}p(x,v)\mathrm dv}{p_X(x)}
\end{aligned}
$$

求导得到

$$
p_{Y|X}(y|x)=\frac{p(x,y)}{p_X(x)}
$$

同理可以得到

$$
    p_{X|Y}(x|y)=\frac{p(x,y)}{p_Y(y)}
$$
