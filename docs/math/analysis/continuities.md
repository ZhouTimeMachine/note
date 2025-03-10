<link rel="stylesheet" href="../../../css/counter.css" />

# Continuities

根据 [Lipschitz continuity - Wikipedia](https://en.wikipedia.org/wiki/Lipschitz_continuity) 和 [Hölder condition - Wikipedia](https://en.wikipedia.org/wiki/H%C3%B6lder_condition)，在实轴的闭区间 $I=[a, b]$ 上，有如下的连续性包含关系：

- [continuiously differentiable](#continuiously-differentiable) $\subset$ [Lipschitz continuous](#lipschitz-continuous) $\subset$ [$\alpha$-Hölder continuous](#alpha-holder-continuous) $\subset$ [uniformly continuous](#uniformly-continuous) $=$ **continuous**

> 这里要求 $0 < \alpha \leqslant 1$

特别地，对于 absolutely continuous，有

- [Lipschitz continuous](#lipschitz-continuous) $\subset$ [absolutely continuous](#absolutely-continuous) $\subset$ [uniformly continuous](#uniformly-continuous)

## Continuiously Differentiable

**连续可微 (continuiously differentiable)** 指 $f$ 的导数 $f'$ **存在**且**连续**。

!!! general "continuiously differentiable $\Rightarrow$ Lipschitz continuous"
    $f'$ 在闭区间 $I$ 上连续，可以得到其在 $I$ 上有界，那么对于 $x, y\in I$ 有

    $$
    |f(x) - f(y)| = \left| \int_x^y f'(t)\mathrm{d}t\right| \leqslant \int_x^y |f'(t)|\mathrm{d}t \leqslant L |x - y| 
    $$ 

## Lipschitz Continuous

**Lipschitz 连续**指存在一个常数 $L\geqslant 0$ 使得对于所有 $x, y$ 有

$$
|f(x) - f(y)| \leqslant L |x - y|
$$

## $\alpha$-Hölder Continuous

**$\alpha$-Hölder 连续**指对于给定的 $\alpha>0$，存在一个常数 $C\geqslant 0$ 使得对于所有 $x, y$ 有

$$
|f(x) - f(y)| \leqslant C |x - y|^\alpha
$$

Lipschitz 连续是 $\alpha$-Hölder 连续的特例，即 $\alpha=1$。

## Uniformly Continuous

**一致连续 (uniformly continuous)** 指对于任意 $\varepsilon>0$，存在 $\delta>0$ 使得对于所有 $x, y$ 有

$$
|x - y| < \delta \Rightarrow |f(x) - f(y)| < \varepsilon
$$

$\alpha$-Hölder 连续已经让 $|f(x) - f(y)|$ 被 $C\delta^\alpha$ 控制，因此只需要让 $\varepsilon > C[\delta(\varepsilon)]^\alpha$ 即可

> $\delta(\varepsilon)$ 代表 $\delta$ 由 $\varepsilon$ 决定

根据 [Heine-Cantor theorem - Wikipedia](https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem)，一致连续的函数在闭区间上一定是连续的。

## Absolutely Continuous

绝对连续要求对 $\forall \varepsilon > 0$，存在 $\delta > 0$，使得对于任意有限个互不相交的满足 $\sum\limits_{k=1}^N(y_k - x_k) < \delta$ 的子区间 $(x_k, y_k)\subseteq I$，有

$$
\sum_{k=1}^N|f(y_k) - f(x_k)| < \varepsilon
$$

所有 $I$ 上的绝对连续函数的集合记为 $\operatorname{AC}(I)$。

!!! general "Lipschitz continuous $\Rightarrow$ Absolutely continuous"
    直接取 $\delta < \varepsilon / L$ 即可。

取 $N=1$，会发现绝对连续是一致连续的强化版。

## Bounded Variation

实分析中还有一个常见的相关概念有界变差 (bounded variation)，存在强弱关系：

- [uniformly continuous](#uniformly-continuous) $\subset$ [bounded variation](#bounded-variation) $\subset$ differentiable almost everywhere

> 变差也常常翻译作变分，在这里遵循周性伟、孙文昌编著的《实变函数》第三版；有界变差也称为有限变差

首先介绍变差的概念，$f$ 是 $I=[a, b]$ 上的实值函数，$X=\{x_k\}_{0\leqslant k \leqslant n}$ 是 $I$ 上的一个划分 (partition)，即 $a=x_0<x_1<\cdots<x_n=b$，定义 $f$ 在 $X$ 上的变差 (variation) 为

$$
V(X) = \sum_{k=1}^n |f(x_k) - f(x_{k-1})|
$$

而 $f$ 在 $I$ 上的全变差 (total variation) 为

$$
T_a^b(f) = \sup_{X} V(X)
$$

如果 $T_a^b(f) < \infty$，则称 $f$ 在 $I$ 上有界变差 (bounded variation)。

!!! general "uniformly continuous $\Rightarrow$ bounded variation"
    取 $n$ 足够大，使得 $x_{i+1} - x_i$ 都小于 $\delta$，则可以得到 $T_a^b(f) \leqslant n\varepsilon$。
    
    > 也可以使用反证法去证明。

!!! general "bounded variation $\Rightarrow$ differentiable almost everywhere"
    为了得到这个结论，只需要证明以下两个定理：

    1. (Lebesgue) 若 $f$ 是 $[a, b]$ 上的单增实值函数，则 $f$ 在 $[a, b]$ 上几乎处处可导
    2. $f$ 在 $[a, b]$ 上有界变差，等价于 $f$ 可以表示为两个单增实值函数的差

    第一个定理的证明较为复杂，涉及到 Vitali 覆盖定理（参见 [Vitali Covering Lemma - Wikipedia](https://en.wikipedia.org/wiki/Vitali_covering_lemma#Vitali's_covering_theorem_for_the_Lebesgue_measure) 中关于 Lebesgue 测度下的 Vitali 覆盖定理）与一些实分析的技术，感兴趣的读者可以查阅周性伟、孙文昌编著的《实变函数》第三版 5.1 节。
    
    ??? general "第二个定理的证明"
        单增实值函数显然是有限变差的，两个单增实值函数的差也是有限变差的，因此反推显然，只证明正推的过程。

        设 $f$ 是有界变差的，当 $a \leqslant x_1 < x_2 \leqslant b$ 时，由于

        $$
            f(x_2) - f(x_1) \leqslant T_{x_1}^{x_2}(f) = T_a^{x_2}(f) - T_a^{x_1}(f)
        $$

        可以得到 $T_a^{x_1}(f) - f(x_1) \leqslant T_a^{x_2}(f) - f(x_2)$，即 $T_a^{x}(f) - f(x)$ 是单增的。这样，我们就可以将 $f$ 表示为

        $$
            f(x) = T_a^x(f) - [T_a^x(f) - f(x)]
        $$

        即两个单增实值函数的差。