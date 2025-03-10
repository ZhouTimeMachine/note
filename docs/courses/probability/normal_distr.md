<link rel="stylesheet" href="../../../css/counter.css" />

# 正态分布

!!! info "Part of note taken on ZJU *Probability Theory (H)*, 2021 Fall & Winter"

## 一元正态分布密度函数的规范性

!!! question "Lemma"
    考虑重要积分 $\displaystyle \int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\mathrm dx$ 的值

??? general "Answer"
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

!!! question "规范性证明"
    证明一元正态分布密度函数 $\displaystyle p(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\}$ 的规范性。

??? general "Proof"
    $$
    \begin{aligned}
    \int_{-\infty}^{+\infty}p(x)\mathrm dx
    &=\int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\}\mathrm dx\\
    &\xlongequal{\displaystyle t=\frac{x-\mu}{\sigma}}\int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}}\exp\left\{-\frac{t^2}{2}\right\}\mathrm dt=1
    \end{aligned}
    $$

得证。

## 二元正态分布的边际分布与线性变换

### 二元正态分布的边际分布

考虑 $(X,Y)\sim N(a,\sigma_1,b,\sigma_2;r)$，求 $p_{X}(x)$, $p_{Y}(y)$

??? general "Answer"

    在二元正态分布的密度函数

    $$
    p(x)=\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-r^2}}\exp\left\{-\frac{1}{2(1-r^2)}\left[\frac{(x-a)^2}{\sigma_1^2}
    -\frac{2\rho(x-a)(y-b)}{\sigma_1\sigma_2}+\frac{(y-b)^2}{\sigma_2^2}\right]\right\}
    $$

    的指数中对 $y$ 配方, 可把 $p(x, y)$ 写成

    $$
    \begin{aligned}
    p(x, y)=\frac{1}{\sqrt{2 \pi} \sigma_{1}} \exp \left\{-\frac{(x-a)^{2}}{2 \sigma_{1}^{2}}\right\}\frac{1}{\sqrt{2 \pi} \sigma_{2} \sqrt{1-r^{2}}} \exp \left\{-\frac{\left[y-b-\frac{r \sigma_{2}}{\sigma_{1}}(x-a)\right]^{2}}{2 \sigma_{2}^{2}\left(1-r^{2}\right)}\right\}
    \end{aligned}
    $$

    令

    $$
    q(x,y)=\frac{1}{\sqrt{2 \pi} \sigma_{2} \sqrt{1-r^{2}}} \exp \left\{-\frac{\left[y-b-\frac{r \sigma_{2}}{\sigma_{1}}(x-a)\right]^{2}}{2 \sigma_{2}^{2}\left(1-r^{2}\right)}\right\}
    $$

    $$
    \begin{aligned}
    \int_{-\infty}^{+\infty}q(x,y)\mathrm dy
    &=\frac{1}{\sqrt{2 \pi} \sigma_{2} \sqrt{1-r^{2}}}\int_{-\infty}^{+\infty}\exp \left\{-\frac{\left[y-b-\frac{r \sigma_{2}}{\sigma_{1}}(x-a)\right]^{2}}{2 \sigma_{2}^{2}\left(1-r^{2}\right)}\right\}\mathrm dy\\
    &=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{+\infty}e^{-\frac{t^2}{2}}\mathrm dt
    \cdots\cdots t=\frac{y-b-\frac{r \sigma_{2}}{\sigma_{1}}(x-a)}{\sigma_2\sqrt{1-r^2}}\\
    &=1\\
    \end{aligned}
    $$

    则

    $$
    \begin{aligned}
    p_X(x)&=\int_{-\infty}^{+\infty}
    \frac{1}{\sqrt{2 \pi} \sigma_{1}} \exp \left\{-\frac{(x-a)^{2}}{2 \sigma_{1}^{2}}\right\}q(x,y)\mathrm{d}y \\
    &=\frac{1}{\sqrt{2 \pi} \sigma_{1}} \exp \left\{-\frac{(x-a)^{2}}{2 \sigma_{1}^{2}}\right\}
    \end{aligned}
    $$

    同理

    $$
    p_Y(y)=\frac{1}{\sqrt{2 \pi} \sigma_{2}} \exp \left\{-\frac{(y-b)^{2}}{2 \sigma_{2}^{2}}\right\}
    $$

### 二元正态分布的线性变换

!!! question "二元正态分布的线性变换"
    假设 $(X, Y) \sim N\left(\mu_{1}, \sigma_{1}^{2}, \mu_{2}, \sigma_{2}^{2}, \rho\right)$ 。定义

    $$
    \left(\begin{array}{l}
    U \\
    V
    \end{array}\right)=A \cdot\left(\begin{array}{l}
    X \\
    Y
    \end{array}\right),\quad A=\left(\begin{array}{ll}
        a & b \\
        c & d
        \end{array}\right)\text{invertible}
    $$

    求 $(U, V)$ 的分布密度

??? general "Answer"
    $A$ 可逆，则

    $$
    \begin{pmatrix}
    X\\Y
    \end{pmatrix}=A^{-1}
    \begin{pmatrix}
    U\\
    V
    \end{pmatrix}
    $$

    $\mathrm{Jacobi}$ 行列式

    $$
    J=|A^{-1}|=|A|^{-1}
    $$

    协方差矩阵 $\Sigma$，随机向量 $\vec x$，期望向量 $\vec \mu$

    $$
    \Sigma=\begin{pmatrix}
    \sigma_1^2&\rho\sigma_1\sigma_2\\
    \rho\sigma_1\sigma_2&\sigma_2^2
    \end{pmatrix},\vec x=\begin{pmatrix}
    x\\y
    \end{pmatrix},
    \vec \mu=\begin{pmatrix}
    \mu_1\\
    \mu_2
    \end{pmatrix}
    $$

    则

    $$
    p_{X,Y}(x,y)=\frac{1}{2\pi|\Sigma|^{\frac12}}\exp\left\{-\frac12(\vec x-\vec\mu)^{T}\Sigma^{-1}(\vec x-\vec \mu)\right\}
    $$

    随机向量 $\vec{u}=\begin{pmatrix}u\\v\end{pmatrix}$

    $$
    \begin{aligned}
    p_{U,V}(u,v)&=\frac{1}{2\pi|\Sigma|^{\frac12}}\exp\left\{-\frac12(A^{-1}\vec u-\vec\mu)^{T}\Sigma^{-1}(A^{-1}\vec u-\vec \mu)\right\}|J|\\
    &=\frac{1}{2\pi|A^{\top}\Sigma A|^{\frac12}}\exp\left\{-\frac12(\vec u-A\vec\mu)^{T}(A\Sigma A^{\top})^{-1}(\vec u-A\vec \mu)\right\}
    \end{aligned}
    $$

    则

    $$
    (U,V)\sim N(A\vec\mu,A\Sigma A^{\top})
    $$

    $$
    A\vec\mu=\begin{pmatrix}
    a&b\\
    c&d
    \end{pmatrix}\cdot
    \begin{pmatrix}
    \mu_1\\
    \mu_2
    \end{pmatrix}=\begin{pmatrix}
    a\mu_1+b\mu_2\\
    c\mu_1+d\mu_2
    \end{pmatrix}
    $$

    $A\Sigma A^{\top}$ 不再展开，那将会是个很长的可怕式子。

## 二元正态分布的条件分布和独立性

### 二元正态分布的条件分布

!!! question "二元正态分布的条件边缘分布"
    考虑 $(X,Y)\sim N(\mu_1,\sigma_1,\mu_2,\sigma_2;\rho)$，求 $p_{X|Y}(x|y)$, $p_{Y|X}(y|x)$

当然，如果直接使用上一节中的配方结果，就不需要下面这么麻烦地化简了。因为上一节中没有给出配方过程，因此在这里稍微写得详细一点。

??? general "Answer"
    $$
    \begin{aligned}
    &p_{X|Y}(x|y)=\frac{p(x,y)}{p_Y(y)}\\
    &=\frac{\displaystyle \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\exp\left\{-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_1)^2}{\sigma_1^2}-\frac{2\rho(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{(y-\mu_2)^2}{\sigma_2^2}\right]\right\}}{\displaystyle \frac{1}{\sqrt{2\pi}\sigma_2}\exp\left\{-\frac{(y-\mu_2)^2}{2\sigma_2^2}\right\}}\\
    &=\frac{\displaystyle \exp\left\{-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_1)^2}{\sigma_1^2}-\frac{2\rho(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{(y-\mu_2)^2}{\sigma_2^2}\right]\right\}}
    {\displaystyle \sqrt{2\pi(1-\rho^2)}\sigma_1\exp\left\{-\frac{(y-\mu_2)^2}{2\sigma_2^2}\right\}}\\
    &=\frac{1}
    {\sqrt{2\pi(1-\rho^2)}\sigma_1}
    \exp\left\{-\frac{(x-\mu_1)^2}{2(1-\rho^2)\sigma_1^2}+\frac{2\rho(x-\mu_1)(y-\mu_2)}{2(1-\rho^2)\sigma_1\sigma_2}-\frac{\rho^2(y-\mu_2)^2}{2(1-\rho^2)\sigma_2^2}\right\}\\
    &=A_1\exp\left\{A_2\left[(x-\mu_1)^2-2k\rho(x-\mu_1)(y-\mu_2)+k^2\rho^2(y-\mu_2)^2\right]\right\}\\
    &(A_1=\frac{1}{\sqrt{2\pi(1-\rho^2)}\sigma_1}, A_2=-\frac{1}{2(1-\rho^2)\sigma_1^2},k=\frac{\sigma_1}{\sigma_2})\\
    &=A_1\exp\{A_2[(x-\mu_1)-\rho k(y-\mu_2)]^2\}\\
    &=\frac{1}{\sqrt{2\pi(1-\rho^2)}\sigma_1}\exp\left\{-\frac{[(x-\mu_1)-\rho \frac{\sigma_1}{\sigma_2}(y-\mu_2)]^2}{2(1-\rho^2)\sigma_1^2}\right\}
    \end{aligned}
    $$

    同理

    $$
    p_{Y|X}(y|x)=\frac{1}{\sqrt{2\pi(1-\rho^2)}\sigma_2}\exp\left\{-\frac{[(y-\mu_2)-\rho \frac{\sigma_2}{\sigma_1}(x-\mu_1)]^2}{2(1-\rho^2)\sigma_2^2}\right\}
    $$


### 二元正态分布的独立性等价条件

!!! question "二元正态分布的独立性等价条件"
    考虑 $(X,Y)\sim N(\mu_1,\sigma_1,\mu_2,\sigma_2;\rho)$，则 $X,Y$ 相互独立（即 $p(x,y)=p_X(x)p_Y(y),\;\forall x,y$ ）等价于

    $$
        \rho=0
    $$

??? general "Proof"

    由于

    $$
    \begin{aligned}
    p_X(x)&=\frac{1}{\sqrt{2\pi}\sigma_1}\exp\left\{-\frac{(x-\mu_1)^2}{2\sigma_1^2}\right\}\\
    p_Y(y)&=\frac{1}{\sqrt{2\pi}\sigma_2}\exp\left\{-\frac{(y-\mu_2)^2}{2\sigma_2^2}\right\}\\
    p(x,y)&=\frac{1}{2\pi\sigma_1\sigma_2(1-\rho^2)}\cdot\\
    &\exp\left\{-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_1)^2}{\sigma_1^2}-\frac{2\rho(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{(y-\mu_2)^2}{\sigma_2^2}\right]\right\}
    \end{aligned}
    $$

    则

    $$
    \begin{aligned}
    &p(x,y)=p_X(x)p_Y(y)\\
    \iff&\frac{1}{(1-\rho^2)}\exp\left\{-\frac{1}{2(1-\rho^2)}\left[\frac{\rho^2(x-\mu_1)^2}{\sigma_1^2}-\frac{2\rho(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{\rho^2(y-\mu_2)^2}{\sigma_2^2}\right]\right\}=1\\
    \iff&\rho^2 a^2-2\rho ab+\rho^2 b^2=-2\sigma_1^2(1-\rho^2)\ln(1-\rho^2),\forall a=(x-\mu_1),b=\frac{\sigma_1}{\sigma_2}(y-\mu_2)
    \end{aligned}
    $$

    $\rho=0$ 时，显然反推成立。则考虑正推，用反证法，若 $\rho\in(-1,0)\cup(0,1)$，有

    $$
        \rho a^2-2ab+\rho b^2=-2\frac{\sigma_1^2}{\rho}(1-\rho^2)\ln(1-\rho^2)=C(\rho,\sigma_1)
    $$

    设 $f(a,b)=\rho a^2-2ab+\rho b^2$，则

    $$
    f(a,b)=C(\rho,\sigma_1)
    \Rightarrow\frac{\partial f}{\partial a}=0,\frac{\partial f}{\partial b}=0
    $$

    $$
    \therefore\left\{\begin{matrix}
    \displaystyle\frac{\partial f}{\partial a}=2\rho a-2b=0\\
    \\
    \displaystyle\frac{\partial f}{\partial b}=2\rho b-2a=0
    \end{matrix}\right.\Rightarrow b=\rho a=\rho(\rho b)=\rho^2b,(1-\rho^2)b=0,b=0
    $$


    同理 $a=0$。这与 $a,b$ 任取，$f\equiv C(\rho, \sigma_1)$ 矛盾，则假设不成立，必有 $\rho=0$，正推得证。

## 一元正态分布的期望与方差

!!! question "一元正态分布的期望与方差"
    考虑 $\xi\sim N(\mu, \sigma^2)$，试求 $E\xi$, $Var\xi$

??? general "Answer"

    $\xi$ 的密度函数为

    $$
    p(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\}\\
    $$

    首先预备求两个积分：$\displaystyle \int_{-\infty}^{+\infty}xe^{-\frac{x^2}{2}}$ 和 $\displaystyle \int_{-\infty}^{+\infty}x^2e^{-\frac{x^2}{2}}\mathrm dx$

    对于第一个积分，由于被积函数是奇函数，有：

    $$
    \int_{-\infty}^{+\infty}xe^{-\frac{x^2}{2}}\mathrm dx=0
    $$

    对于另外一个积分，有：

    $$
    \int_{-\infty}^{+\infty}x^2e^{-\frac{x^2}{2}}\mathrm dx=-\int_{-\infty}^{+\infty}x\mathrm d(e^{-\frac{x^2}{2}})=-xe^{-\frac{x^2}{2}}\bigg|^{+\infty}_{-\infty}+\int_{-\infty}^{+\infty}e^{-\frac{x^2}{2}}\mathrm dx=\sqrt{2\pi}
    $$

    因为

    $$
    \lim_{x\to\infty}xe^{-\frac{x^2}{2}}=\lim_{x\to\infty}\frac{x}{e^{\frac{x^2}{2}}}=\lim_{x\to\infty}\frac{1}{xe^{\frac{x^2}{2}}}=0
    $$

    考虑其期望，有

    $$
    \begin{aligned}
    E\xi&=\int_{-\infty}^{+\infty}x\frac{1}{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\}\mathrm dx\\
    &\xlongequal{t=\dfrac{x-\mu}{\sigma}}\int_{-\infty}^{+\infty}(\sigma t+\mu)\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\mathrm dt\\
    &=\sigma\int_{-\infty}^{+\infty}t\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\mathrm dt+\mu\int_{-\infty}^{+\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\mathrm dt\\
    &=\mu
    \end{aligned}
    $$

    考虑方差，有

    $$
    \begin{aligned}
    E\xi^2&=\int_{-\infty}^{+\infty}x^2\frac{1}{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\}\mathrm dx\\
    &\xlongequal{\displaystyle t=\frac{x-\mu}{\sigma}}\int_{-\infty}^{+\infty}(\sigma t+\mu)^2\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\mathrm dt\\
    &=\frac{1}{\sqrt{2\pi}}\left(\sigma^2\int_{-\infty}^{+\infty}t^2e^{-\frac{t^2}{2}}\mathrm dt+2\sigma\mu\int_{-\infty}^{+\infty}te^{-\frac{t^2}{2}}\mathrm dt+\mu^2\int_{-\infty}^{+\infty}e^{-\frac{t^2}{2}}\mathrm dt\right)\\
    &=\sigma^2+\mu^2
    \end{aligned}
    $$

    则 $Var\xi=E\xi^2-(E\xi)^2=\sigma^2$

## 二元正态分布的协方差、Pearson 相关系数

!!! question "二元正态分布的协方差、Pearson 相关系数"
    $(\xi, \eta)\sim N\left(a, b, \sigma_{1}^{2}, \sigma_{2}^{2}, r\right)$, 求 $Cov(\xi, \eta)$ 和 $r_{\xi, \eta}$.

??? general "Answer"
    $$
    \begin{aligned}
    Cov(\xi, \eta)
    &=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}(x-a)(y-b) p(x, y) \mathrm{d} x \mathrm{d} y \\
    &=\frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-r^{2}}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}(x-a)(y-b) \\
    &\cdot \exp \left\{-\frac{1}{2\left(1-r^{2}\right)}\left(\frac{x-a}{\sigma_{1}}-r \frac{y-b}{\sigma_{2}}\right)^{2}-\frac{(y-b)^{2}}{2 \sigma_{2}^{2}}\right\} \mathrm{d} x \mathrm{d} y \\
    \end{aligned}
    $$

    令

    $$
    z=\frac{x-a}{\sigma_{1}}-r \frac{y-b}{\sigma_{2}}, \quad t=\frac{y-b}{\sigma_{2}}
    $$

    则

    $$
    \frac{x-a}{\sigma_{1}}=z+r t, \quad |J|=\left|\frac{\partial(x, y)}{\partial(z, t)}\right|=\sigma_{1} \sigma_{2}
    $$

    于是

    $$
    \begin{aligned}
    Cov(\xi, \eta)=& \frac{\sigma_{1} \sigma_{2}}{2 \pi \sqrt{1-r^{2}}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(z t+r t^{2}\right) e^{-\frac{z^{2}}{2\left(1-r^{2}\right)}} e^{-\frac{t^{2}}{2}} d z d t \\
    =& \sigma_{1} \sigma_{2} \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} t e^{-\frac{t^{2}}{2}} d t \frac{1}{\sqrt{2 \pi} \sqrt{1-r^{2}}} \int_{-\infty}^{\infty} z e^{-\frac{z^{2}}{2\left(1-r^{2}\right)} d z} \\
    &+\frac{r \sigma_{1} \sigma_{2}}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} t^{2} e^{-\frac{t^{2}}{2}} d t \frac{1}{\sqrt{2 \pi} \sqrt{1-r^{2}}} \int_{-\infty}^{\infty} e^{-\frac{s^{2}}{2\left(1-r^{2}\right)}} d z \\
    =& r \sigma_{1} \sigma_{2}
    \end{aligned}
    $$

    故得

    $$
    r_{\xi \eta}=\frac{Cov(\xi, \eta)}{\sqrt{\operatorname{Var} \xi \operatorname{Var} \eta}}=r
    $$

因此，$\xi$ 与 $\eta$ 不相关等价于 $r=0$，也就等价于 $\xi$ 与 $\eta$ 相互独立。