<link rel="stylesheet" href="../../../css/counter.css" />

# 概率极限定理

!!! info "Part of note taken on ZJU *Probability Theory (H)*, 2021 Fall & Winter"

!!! warning "本页面还在建设中"

## 概率极限定理

### Bernoulli 大数律

$p\in(0,1)$，$S_n\sim B(n,p)$，则

$$
\frac{S_n}{n}\to p,\quad n\to \infty
$$

即

$$
    P\left(\omega:\left|\frac{S_n(\omega)}{n}-p\right|>\varepsilon\right)\to 0,\quad n\to \infty
$$

若引入依概率收敛的概念，那么其实就是

$$
\frac{S_n}{n}\stackrel{P}{\longrightarrow}p,\quad n\to \infty
$$


### De Moivre-Laplace 中心极限定理

$p\in(0,1)$，$S_n\sim B(n,p)$，则

$$
\frac{S_n-np}{\sqrt{np(1-p)}}
\stackrel{d}{\longrightarrow}N(0,1)
$$

这里是依分布收敛的概念。

### Poisson极限定理
$p_n\in(0,1)$，$S_n\sim B(n,p_n),np_n\to\lambda,\lambda\in(0,1)$，则

$$
P(S_n=k)\to\frac{\lambda^k}{k!},\quad
k=0,1,2,\cdots,\quad n\to \infty
$$

我猜想这里应该是依概率收敛。不过我也猜想这里不是重点。

### Chebyschev 大数律

#### 内容

$\xi_k$ 是一列随机变量。$E\xi_k=\mu$，$S_n=\displaystyle\sum_{k=1}^n\xi_k$，如果有

$$
\frac{Var(S_n)}{n^2}\to 0,\quad n\to\infty
$$

那么

$$
\frac{S_n}{n}
\stackrel{P}{\longrightarrow}\mu
,n\to \infty
$$

#### 推广
$E\xi_k=\mu_k$，则满足方差条件后有

$$
\frac{S_n}{n}-\frac{\sum_{k=1}^n\mu_k}{n}
\stackrel{P}{\longrightarrow}
,n\to \infty
$$

#### 回忆 Chebyschev 不等式

$\exists\; EX,EX^2$，则 $\forall \varepsilon>0$

$$
P(|X-EX|>\varepsilon)\leqslant\frac{Var(X)}{\varepsilon^2}
$$

可以用以证明 Bernoulli 大数律

$$
\begin{aligned}
P\left(\left|\frac{S_n}{n}-p\right|>\varepsilon\right)&
\leqslant\frac{Var(\frac{S_n}{n})}{\varepsilon^2}\\
&=\frac{Var(\sum_{k=1}^n\xi_k)}{n^2\varepsilon^2}\\
&=\frac{\sum_{k=1}^nVar(\xi_k)}{n^2\varepsilon^2}\\
&=\frac{p(1-p)}{n\varepsilon^2}\to 0,\quad n\to\infty
\end{aligned}
$$

## Khinchine 大数律

$\xi_k$ 独立同分布，$E\xi_k=\mu$，则

$$
\frac{S_n}{n}\to \mu,\quad n\to\infty
$$

### Levy-Feller 中心极限定理
#### 内容
$\xi_k,k\geqslant 1$ 是一列**独立同分布**随机变量，$E\xi_k=\mu,Var(\xi_k)=\sigma^2$。记 $S_n=\sum_{k=1}^n\xi_k$，则 $\forall x$,

$$
    P\left(\frac{S_n-n\mu}{\sigma\sqrt{n}}\leqslant x\right)\to \varphi(x)
$$

即

$$
\frac{S_n-n\mu}{\sigma\sqrt{n}}
\stackrel{d}{\longrightarrow}
N(0,1)
$$

#### 意义

(1) 应用于**一般**随机变量，是de Moivre-Laplace 中心极限定理的**推广**

(2) 说明测量误差可用**正态分布**描述

随机测量值 $X_i$，均值 $\mu$，每次误差为 $X_i-\mu$，$n$ 次观测叠加误差(注意是离差不是方差，可以相消)为 $\displaystyle\sum_{i=1}^n(X_i-\mu)$，则

$$
\sum_{i=1}^n(X_i-\mu)\sim N(0, n\sigma^2),\quad n\gg 1
$$

#### 证明
组合计算失效，使用特征函数方法。

### Lyapunov 中心极限定理

$\xi_k,k\geqslant 1$ 是一列**独立**随机变量(不一定同分布)，$E\xi_k=\mu_k,Var(\xi_k)=\sigma_k^2$。记 $S_n=\sum_{k=1}^n\xi_k,B_k=\sum_{k=1}^n\sigma_k^2$，如果

(1)$B_n\to\infty$

(2)$E(|X_k|^3)<\infty$，且

$$
\frac{\displaystyle\sum_{k=1}^nE|X_k|^3}{B_n^\frac{3}{2}}\to0,
\quad n\to\infty
$$

则 $\forall x$，

$$
P\left(\frac{\displaystyle\sum_{k=1}^n(\xi_k-\mu_k)}{\sqrt{B_n}}\leqslant x\right)
\to\phi(x)
$$

则

$$
\frac{\displaystyle\sum_{k=1}^n(\xi_k-\mu_k)}{\sqrt{B_n}}\stackrel{d}{\longrightarrow}N(0,1)
$$

## 概率论的收敛

### 依概率收敛

!!! warning "该部分仍在施工中"

#### 定义

在概率空间 $(\Omega,\Sigma,P)$ 中，

#### 敛散性判别法则

#### 性质

4.连续映射保持依概率收敛性

设 $f:\mathbf{R}\to \mathbf{R}$ 是连续映射，则

$$
X_n\stackrel{P}{\longrightarrow}X\Rightarrow 
f(X_n)\stackrel{P}{\longrightarrow}f(X)
$$

### 依分布收敛

#### 定义
$X,X_n,n\geqslant 1$ 是一列随机变量，其分布函数分别为 $F,F_n,n\geqslant 1$。若对 $\forall F$ 的连续点 $x$，

$$
F_n(x)\to F(x),\quad n\to \infty
$$

则有

$$
X_n\stackrel{d}{\longrightarrow} X
$$

(1) 回顾 $F$ 的基本条件：左极限存在，右连续

(2) $F$ 若在 $\mathbf{R}$ 上连续，则 $F_n$ 处处收敛于 $F$

(3) 如果 $F$ 单调有界，则不连续点最多可数个。

$$
D_F=\{x:F(x)-F(x-0)>0\}=\cup_{n=1}^\infty
\{x:F(x)-F(x-0)\geqslant \frac{1}{n}\}
$$

因为有界，$\{x:F(x)-F(x-0)\geqslant \frac{1}{n}\}$ 就是有限集；$n$ 从 1 数到 $\infty$，则可数。

(4) $F$ 的连续点集在 $\mathbf{R}$ 上稠密

#### 依概率收敛强于依分布收敛

!!! info "依概率收敛 $\Rightarrow$ 依分布收敛"
    $$
    X_n\stackrel{P}{\longrightarrow}X
    \Rightarrow
    X_n\stackrel{d}{\longrightarrow}X
    $$

??? general "Proof"
    $\forall x\in \mathbf{R},\varepsilon >0,$

    $$
    P(X_n\leqslant x)=P(X_n\leqslant x,X_n-X\geqslant -\varepsilon)+
    P(X_n\leqslant x,X_n-X<-\varepsilon)
    $$

    然而，

    $$
    P(X_n\leqslant x,X_n-X<-\varepsilon)\leqslant P(X_n-X<-\varepsilon)\to 0
    $$

    则

    $$\begin{aligned}
    \lim_{n\to \infty}\sup P(X_n\leqslant x)
    =&P(X_n\leqslant x,X_n-X\geqslant -\varepsilon)\\
    =&P(-\varepsilon\leqslant X_n-X\leqslant x-X)\\
    \leqslant &P(X\leqslant x+\varepsilon)\to P(X\leqslant x),\varepsilon\to 0
    \end{aligned}$$

    因为分布函数右连续所以可以直接这么趋向。然而分布函数只是左极限存在，并不一定左连续，所以有同理，

    $$
    \lim_{n\to \infty}\inf P(X_n\leqslant x)\geqslant P(X\leqslant x-\varepsilon)\to P(X<x),\varepsilon\to 0
    $$

    但是在连续点，就也左连续了，那么就可以得到

    $$
    \lim_{n\to \infty}P(X_n\leqslant x)=P(X\leqslant x)
    $$

    也就得到了依分布收敛。

!!! info "依概率收敛 $\Rightarrow$ 依分布收敛"

??? general "Counterexample"

    设 $Y$ 为非退化对称随机变量，则显然有

    $$
    Y\stackrel{d}{=}-Y
    $$

    那么令 $X_n=Y,X=Y$，则 $X,X_n,n\geqslant 1$ 分布相同，有

    $$
    X_n\stackrel{d}{\longrightarrow}X
    $$

    然而

    $$
    P(|X_n-X|-\varepsilon)=P(2|Y|>\varepsilon)
    $$

    $Y$ 不恒等于 0（否则就是退化分布了），那么 $X_n$ 不依概率收敛到 $X$

对于退化分布，特别地，有

$$
X_n\stackrel{d}{\longrightarrow}c
\Rightarrow
X_n\stackrel{P}{\longrightarrow}c
$$

即退化分布情况下，依概率收敛和依分布收敛是等价的。

证明：

!!! warning "施工中"

#### 证明 Levy 连续性定理

$X,X_n,n\geqslant 1$ 是一列随机变量，其特征函数分别为 $\phi,\phi_n,n\geqslant 1$，则

$$
X_n\stackrel{d}{\longrightarrow}X
\Rightarrow
\phi_n(t)\to \phi(t),\quad t\in \mathbf{R}
$$

另一种形式，如果

$$
\phi_n(t)\to\phi(t),\quad t\in\mathbf{R}
$$

且 $\phi$ 在 0 处连续，那么 $\phi$ 一定是特征函数，其对应的随机变量 $X$ 满足

$$
X_n\stackrel{d}{\longrightarrow}X
$$

可以认为是等价条件。

#### 证明 Khinchine 大数律

!!! tip "分析"
    频数除以次数依概率收敛于期望，由于期望可以看成退化分布的随机变量，所以和按分布收敛于期望是等价的。

$\xi_k,k\geqslant 1$ 独立同分布，$E\xi_k=\mu$ 时，令 $X_n=\displaystyle \frac{1}{n}\sum_{k=1}^n\xi_n$，由独立性有

$$
\begin{aligned}
\phi_n(t)&=E\exp\left\{i\frac{1}{n}\sum_{k=1}^n\xi_nt\right\}\\
&=\prod_{k=1}^n\left[E\exp\left\{i\frac{1}{n}\xi_kt\right\}\right](\text{独立性})\\
&=\left[E\exp\left\{i\frac{1}{n}\xi_1t\right\}\right]^n(\text{同分布})
\end{aligned}
$$

对 $\displaystyle E\exp\left\{i\frac{1}{n}\xi_1t\right\}$ 进行泰勒展开，有

$$
E\exp\left\{i\frac{1}{n}\xi_1t\right\}=1+i\frac{t}{n}\mu+o(\frac{t}{n})
$$

那么，$\forall t\in\mathbf{R}$，

$$
\phi_n(t)=\left[1+\frac{it\mu}{n}+o(\frac{t}{n})\right]^n\to e^{it\mu}
$$

显然 $e^{it\mu}$ 在 0 处连续，且对应常数为 $\mu$ 的退化分布，那么得证依分布收敛

#### 证明 Levy-Feller 中心极限定理

$\xi_k,k\geqslant 1$ 独立同分布，$E\xi_k=\mu,Var(\xi_k)=\sigma^2$，那么

$$
X_n=\frac{1}{\sigma\sqrt{n}}\sum_{k=1}^n(\xi_k-\mu)
\stackrel{d}{\longrightarrow}N(0,1)
$$

??? general "Proof"
    只需证

    $$
    \phi_n(t)=E\exp\left\{itX_n\right\}\to exp\{-\frac{t^2}{2}\}
    $$

    易得
    
    $$
    \phi_n(t)=\left[E\exp\left\{it\frac{\xi_1-\mu}{\sigma\sqrt{n}}\right\}\right]^n
    $$

    泰勒展开，有
    
    $$
    \begin{aligned}
    E\exp\left\{i\frac{t}{\sigma\sqrt{n}}(\xi_1-\mu)\right\}
    =&1+i\frac{t}{\sigma\sqrt{n}}E(\xi_1-\mu)
    -\frac{t^2}{\sigma^2n}E(\xi_1-\mu)^2+o(\frac{1}{n})\\
    \end{aligned}
    $$