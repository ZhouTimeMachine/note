<link rel="stylesheet" href="../../../css/counter.css" />

# 概念与基础公式

!!! info "Part of note taken on ZJU *Probability Theory (H)*, 2021 Fall & Winter"

## 两种概型与概率空间的简单介绍

### 古典概型

!!! info "古典概型的特征"
    1. 样本空间中样本点有限，$\Omega=\{\omega_1,\omega_2, \cdots, \omega_n\}$
    2. 各基本事件等可能，即 $P(\omega)=\frac 1n$

古典概型的计算：

$$
    P(A)=\frac m n=\frac{A\text{ 包含的样本点数}}{\text{样本空间中样本点总数}}
$$

### 几何概型

!!! info "几何概型的特征"
    1. 样本空间中样本点无限
    2. 样本点落在等测度(长度、面积、体积...)区域的概率相等

几何概型的计算：

$$
    P(A_g)=\frac{g\text{ 的测度}}{\Omega\text{ 的测度}}
$$

$A_g=\{\text{任取样本点，位于区域 }g\in\Omega\text{ 的概率}\}$

### 概率空间

!!! info "概率空间"
    一个概率空间可以表示为 $(\Omega, \mathcal{F}, P)$，其中

    $\Omega:$样本空间，即样本点$\omega$的全体。有
    $\Omega=\{\omega_1,\omega_2,\cdots\}$。

    $\mathcal{F}:$事件域，包括所有的事件。

    $P:$定义的概率。
    
定义的概率 $P$ 需要满足概率的公理化定义。

!!! info "概率的公理化定义"

    1. 非负性：$\forall A\in \mathcal{F},P(A)\geqslant 0$

    2. 规范性：$P(\Omega)=1$

    2. 可列可加性：$A_i\cap A_j=\emptyset, i\neq j$ (即 $A_1,\cdots, A_n, \cdots$ 为两两不相容的事件)

    $$
        P\left(\sum_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty P(A_n)
    $$

## 条件概率和链式法则

!!! info "条件概率 $P(A|B)$"
    事件 $B$ 发生条件下事件 $A$ 发生的概率，称为事件 $A$ 关于事件 $B$ 的**条件概率 (conditional probability)**

有基本公式:

$$
    P(A|B)=\frac{P(AB)}{P(B)}
$$

也可以表示为**链式法则(乘法公式)**的形式：

$$
    P(AB)=P(A|B)P(B)
$$

??? general "推广到 $n$ 个事件"
    推广到 $n$ 个事件，有链式法则：

    $$
        P\left(\prod_{i=i}^nA_i\right)=\prod_{i=1}^n P\left(A_i\bigg|\prod_{j=1}^{i-1}A_j\right)
    $$

    特别定义 $a>b$ 时，$\prod_{i=a}^bA_i$ 为必然事件。或者这样写可能更容易看懂：

    $$
        P\left(A_{1} A_{2} \cdots A_{n}\right) =
        P\left(A_{1}\right) \cdot P\left(A_{2} \mid A_{1}\right) \cdot P\left(A_{3} \mid A_{1} A_{2}\right) \cdots P\left(A_{n} \mid A_{1} A_{2} \cdots A_{n-1}\right)
    $$

## 全概率公式

!!! info "分割(完备事件组)"
    在概率空间 ($\Omega, \mathcal{F}, P$) 中，若事件 $\{A_1, A_2, \cdots, A_n\}$($n<\infty$ 或 $n=\infty$) 满足：

    1. $A_i$ 两两互不相容(不可能同时发生)，且 $P(A_i)>0$
    2. $\sum_{i=1}^\infty A_i=\Omega$

    则称 $\{A_1, A_2, \cdots, A_n\}$ 构成 $\Omega$ 的一个**分割(完备事件组)**

!!! abstract "全概率 (total probability) 公式"

    在概率空间 ($\Omega, \mathcal{F}, P$) 中，若 $\{A_1, A_2, \cdots, A_n\}$($n<\infty$ 或 $n=\infty$) 构成 $\Omega$ 的一个**分割(完备事件组)**，
    
    则有**全概率公式**成立：$\forall B\in \mathcal{F}$，有

    $$
        P(B)=\sum_{i=1}^nP(A_i)P(B|A_i)
    $$

??? general "Proof"

    $$
    \begin{aligned}
        P(B)&=P(B\Omega)\\
        &=P\left(B\sum_{i=1}^nA_i\right)\\
        &=P\left(\sum_{i=1}^nBA_i\right)\\
        &=\sum_{i=1}^nP(BA_i)\\
        &=\sum_{i=1}^nP(A_i)P(B|A_i)
    \end{aligned}
    $$

## 贝叶斯公式

!!! abstract "贝叶斯 (Bayes) 公式"
    $$
    P(A_i|B)=\frac{P(A_i)P(B|A_i)}
    {\sum_{k=1}^\infty P(A_k)P(B|A_k)}
    $$

**hint for proof**: $P(A_i|B)=\dfrac{P(A_iB)}{P(B)}$，分子用链式法则展开，分母用全概率公式展开。

!!! tip "深入了解条件概率的意义"
    $P(A_i)$：不知 $B$ 是否发生，称为**先验 (priori) 概率**

    $P(A_i|B)$：以 $B$ 发生为已知条件，称为**后验 (posteriori) 概率**

## 事件独立性

### 两个事件的独立性

!!! info "$A$ 与 $B$ 相互独立（统计独立）"
    称事件 $A$ 与事件 $B$ **相互独立（统计独立，statistical independence）**，如果满足

    $$
        P(AB)=P(A)\cdot P(B)
    $$

因为此时有

$$
    P(A|B)=\frac{P(AB)}{P(B)}=P(A)
$$

且

$$
    P(B|A)=\frac{P(AB)}{P(A)}=P(B)
$$

如果 $A$ 与 $B$ 不相互独立，也称为**统计相依 (statistical dependence)**

### 多个事件的独立性

对于一组事件 $A_1,A_2,\cdots,A_n$，存在两两独立和整体的相互独立两种概念。

不妨先以三个事件 $A,B,C$ 为例进行研究。

- 两两独立：即 $A$ 与 $B$ 相互独立，$B$ 与 $C$ 相互独立，$C$ 与 $A$ 相互独立
    
    $$
    \left\{\begin{array}{l}
        P(A B)=P(A) \cdot P(B) \\
        P(A C)=P(A) \cdot P(C) \\
        P(B C)=P(B) \cdot P(C)
        \end{array}\right.
    $$

- 整体相互独立：即满足

    $$
    P(ABC)=P(A)\cdot P(B)\cdot P(C)
    $$

同时满足两两独立和整体的相互独立，才能说 $A, B, C$ 相互独立。

??? general "推广到 $n$ 个事件"
    推广到 $n$ 个事件，$A_1,A_2,\cdots,A_n$ 相互独立需要满足：$\forall r<n$，$A_1,A_2,\cdots,A_n$ 中任意 $r$ 个事件都相互独立，且

    $$
        P\left(\prod_{i=1}^nA_i\right)=\prod_{i=1}^n P(A_i)
    $$

    或者可以直接这么定义：$A_1,A_2,\cdots,A_n$ 相互独立，如果

    $$
    \forall r\leqslant n(r\in \mathbb N_+),\;
    P\left(\prod_{i=1}^rA_{n_i}\right)=\prod_{i=1}^r P(A_{n_i}),\;
    1\leqslant n_1<n_2<\cdots<n_r\leqslant n
    $$
