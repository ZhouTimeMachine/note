# Introduction

!!! info "Lecture 1, 2024.9.10, [Link](https://www.math.pku.edu.cn/teachers/zhzhang/videos/09-10.mp4)"

## Overview

<div style="text-align:center;">
    <img src="../../imgs/prob/high-dim/overview.drawio.png" alt="overview" style="margin: 0 auto; zoom: 80%;"/>
</div>

在高维中，需要刻画两个重要问题：

- 维数灾难 (Curse of Dimensionality)
- 高维特性 (Surprises in High Space)

用来分析的两种常用工具：

- 期望 (Expectation)
- 以高概率存在 (with high probability)

研究对象：向量 -> 矩阵 -> 函数

数据假设：独立同分布 (i.i.d.) -> 鞅差 (Martingale Difference) -> 马尔科夫链 (Markov Chain)

教材：*High-Dimensional Probability* by Roman Vershynin

推荐资料：

- 统计方面：*High-Dimensional Statistics* by Martin Wainwright
- 理论计算机：*The Probabilitic Method* by Alon and Spencer
- 更有趣味，偏向算法设计：*Probability and Computing* by Mitzenmacher and Upfal

比较 $f(n)$ 和 $g(n)$：

- $f(n) = O(g(n))$：$\exists\; c > 0$, $f(n) \leqslant c g(n)$ ($n$ 足够大)
- $f(n) = \Omega(g(n))$：$\exists\; c > 0$, $f(n) \geqslant c g(n)$ ($n$ 足够大)
- $f(n) = \Theta(g(n))$：$\exists\; c_1, c_2 > 0$, $c_1 g(n) \leqslant f(n) \leqslant c_2 g(n)$ ($n$ 足够大)
> 即 $f(n) = O(g(n))$ 且 $f(n) = \Omega(g(n))$
- $f(n) = o(g(n))$：$f(n) / g(n) \to 0$ ($n \to \infty$)
- $f(n) \sim g(n)$：$f(n) / g(n) \to 1$ ($n \to \infty$)

!!! example "Example 1"
    先声明以下基本定义与定理：对于 $z_1, z_2, \ldots, z_n \in \mathbb{R}$

    - 凸组合 (convex combination)：$\sum_{i=1}^n \lambda_i z_i$, $\lambda_i\geqslant 0$, $\sum_{i=1}^n \lambda_i=1$
    - 凸包 (convex hull)：$T\subseteq \mathbb{R}^n$, $\mathrm{conv}(T):=\{\text{convex combinations of }z_1, \cdots, z_m\in T, \forall m\in \mathbb{N}\}$
    - Caratheodory's Theorm: 对于 $T\subseteq \mathbb{R}^n$，任意 $\mathrm{conv}(T)$ 中的点，都可以被表示为 $n+1$ 个 $T$ 中的点的凸组合

    尝试证明如下定理：

    !!! abstract "Theorem"
        考虑 $T\subseteq \mathbb{R}^n$，令 $T$ 的直径和每个点都被 1 bound，即：

        - 直径 (diameter) $\mathrm{diam}(T)=\sup\limits_{x, y\in T} \|x-y\|_2\leqslant 1$
        - $\|x\|_2\leqslant 1$，$\forall x\in T$

        则 $\forall x\in \mathrm{conv}(T)$，$\forall k\in \mathbb{N}^+$, 我们能够找到 $x_1, \cdots, x_k\in T$ s.t.

        $$
        \left\| x - \frac{1}{k}\sum_{i=1}^k x_i \right\|_2 \leqslant \frac{1}{\sqrt{k}}
        $$

    > 使用 $k$ 个点估计 $x$ 的误差不受空间维度 $n$ 影响，仅与 $k$ 有关
    
    证明思路：考虑 $k$ 个随机点 $Z_1, \cdots, Z_k\in T$，通过对这个随机变量的构造，使其满足 $\mathbb{E}\|x - 1/k \sum Z_i\|_2^2 \leqslant 1/k$，则说明存在 $Z_1, \cdots, Z_k$ 的某组采样值 $x_1, \cdots, x_k$ 满足定理要求

    ??? general "Proof"
        根据 Caretheodory's Theorm，$\forall x\in \mathrm{conv}(T)$，$\exists y_1, \cdots, Y_{n+1}\in T$，$\lambda_1, \cdots, \lambda_{n+1}\geqslant 0$，$\sum_{i=1}^{n+1}\lambda_i=1$，s.t.
        
        $$
        x = \sum_{i=1}^{n+1}\lambda_i y_i
        $$

        构造随机变量 $Z$，其概率分布 $P$ 满足 $P(Z=y_i)=\lambda_i$，则

        $$
        \mathbb{E}Z = \sum_{i=1}^{n+1}\lambda_i y_i
        $$

        考虑 $k$ 个与 $Z$ 独立同分布的随机变量 $Z_1, \cdots, Z_k$，则

        $$
        \begin{aligned}
            \mathbb{E}\left\| x - \frac{1}{k}\sum_{i=1}^k Z_i \right\|_2^2
            &= \mathbb{E}\left\| \frac{1}{k} \sum_{i=1}^{k} (x - Z_i) \right\|_2^2 \\
            &= \frac{1}{k^2}\mathbb{E}\left\| \sum_{i=1}^{k} (\mathbb{E}Z_i - Z_i) \right\|_2^2 \\
            &= \frac{1}{k^2}\sum_{i=1}^{k} \mathbb{E}\left\|  Z_i - \mathbb{E}Z_i \right\|_2^2 - \frac{2}{k^2}\sum_{1\leqslant i < j \leqslant n} \underbrace{\mathbb{E}(Z_i - \mathbb{E}Z_i )^{\top} (Z_j - \mathbb{E}Z_j )}_{\mathrm{Cov}(Z_i, Z_j)} \\
            &= \frac{1}{k^2}\sum_{i=1}^{k} \mathbb{E}\left\|  Z_i - \mathbb{E}Z_i \right\|_2^2 \\
        \end{aligned}
        $$

        注意由于 $Z_i, Z_j$ 相互独立，$\mathrm{Cov}(Z_i, Z_j)=0$。而

        $$
            \mathbb{E}\left\|  Z_i - \mathbb{E}Z_i \right\|_2^2
            = \mathbb{E}\|Z\|_2^2 - \|\mathbb{E}Z\|_2^2
            \leqslant \mathbb{E}\|Z\|_2^2
            = \sum_{j=1}^{n+1}\lambda_j \|y_j\|_2^2 
            \leqslant \sum_{j=1}^{n+1}\lambda_j
            = 1
        $$

        因此就有
        
        $$
            \mathbb{E}\left\| x - \frac{1}{k}\sum_{i=1}^k Z_i \right\|_2^2
            \leqslant \frac{1}{k^2} \cdot k
            = \frac{1}{k}
            \Rightarrow
            \exists\: x_1, \cdots, x_k\in T, \text{s.t.} \left\| x - \frac{1}{k}\sum_{i=1}^k x_i \right\|_2 \leqslant \frac{1}{\sqrt{k}}
        $$

!!! question "作业"
    对于 $x_1, \cdots, x_n\in \mathbb{R}^n$, $\|x_i\|_2\leqslant 1$, 考虑任意 $p_1, \cdots, p_n\in [0, 1]$, $w=p_1x_1 + \cdots + p_nx_n$

    > 注意，$\sum p_i$ 不一定为 1 了

    (1) 求证存在 $\epsilon_1, \cdots, \epsilon_n\in \{0, 1\}$ 使得 $v=\epsilon_1x_1 + \cdots \epsilon_nx_n$ 满足

    $$
    \|w-v\|_2 \leqslant \frac{\sqrt{n}}{2}
    $$

    (2) 找到一个复杂度为 $O(n^2)$ （或更低）的确定性算法解出可行的 $\epsilon_1, \cdots, \epsilon_n$


Timestamp: 0:00:00-1:03:47

!!! warning "本页面还在建设中"