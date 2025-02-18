<link rel="stylesheet" href="../../../../css/counter.css" />

# 四元数

!!! info "notes of https://github.com/Krasjet/quaternion, chapter 3"

四元数和复数十分类似，只是复数只有 1 个虚部，而四元数有 3 个虚部。所有四元数 $q\in \mathbb{H}$ 都可以表示为：

$$
q = a + bi + cj + dk, \quad a, b, c, d \in \mathbb{R}
$$

> $\mathbb{H}$ 代表全体四元素，用来纪念四元数的发现者 William Rowan Hamilton

其中 $i^2=j^2=k^2=ijk=-1$。

与复数类似，四元数也可以表示为 $\mathbb{R}^4$ 的向量，或者将实部和虚部分开，表示为单个实数和向量 $\mathbb{R}^3$ 的有序对：

$$
q = [s, \mathbf{v}],\quad \mathbf{v} = (x, y, z)^{\top}\in \mathbb{R}^3
$$

## 概念和运算

### 模长

$$
\|q\| = \sqrt{a^2 + b^2 + c^2 + d^2}
= \sqrt{s^2 + \|\mathbf{v}\|^2}
$$

### 加减法

和复数完全类似，即对应实部、虚部相加减。对于 $q_1 = a_1 + b_1i + c_1j + d_1k = [s, \mathbf{v}]$，$q_2 = a_2 + b_2i + c_2j + d_2k = [t, \mathbf{u}]$，有

$$
\begin{aligned}
    q_1 \pm q_2 
    &= (a_1 \pm a_2) + (b_1 \pm b_2)i + (c_1\pm c_2)j + (d_1\pm d_2)k \\
    &= [s\pm t, \mathbf{v}\pm \mathbf{u}]
\end{aligned}
$$

### 乘法

#### 数乘

和复数完全类似，直接进行一个 scale：

$$
sq = s(a + bi + cj + dk) = sa + sbi + scj + sdk
$$

数乘满足交换律，有 $sq=qs$

#### 相互乘法

##### 基本形式

- 四元数之间的乘法**不满足交换律**，即左乘 $q_1q_2$ 并不一定等于右乘 $q_2q_1$
- **结合律、分配律依然成立**

两个四元数的乘法是十分凌乱的，有

$$
\begin{aligned}
    q_1q_2
    =& (a_1 + b_1i + c_1j + d_1k) (a_2 + b_2i + c_2j + d_2k) \\
    =& (a_1a_2 + a_1b_2i + a_1c_2j + a_1d_2k) + \\
    & (b_1a_2i + b_1b_2i^2 + b_1c_2ij + b_1d_2ik) + \\
    & (c_1a_2j + c_1b_2ji + c_1c_2j^2 + c_1d_2jk) + \\
    & (d_1a_2k + d_1b_2ki + d_1c_2kj + d_1k^2) \\
\end{aligned}
$$

根据 $i^2=j^2=k^2=ijk=-1$，有

$$
\begin{aligned}
    -jk=i^2(jk)=i(ijk)=-i &\quad\Rightarrow\quad  jk=i \\
    -ij=(ij)k^2=(ijk)k=-k &\quad\Rightarrow\quad ij=k \\
    kj=(ij)j=ij^2=-i &\quad\Rightarrow\quad kj=-i \\
    -ki=k(kj)=k^2j=-j &\quad\Rightarrow\quad ki=j \\
    ji=(ki)i=ki^2=-k &\quad\Rightarrow\quad ji=-k \\
    ik=i(ij)=i^2j=-j &\quad\Rightarrow\quad ik=-j
\end{aligned}
$$

> 从这里就可以注意到四元数乘法不满足交换律

用一个表格表示基 $(1, i, j, k)^{\top}$ 两两相乘的结果：

!!! info "四元数基底相乘表"

    <div class="center" markdown="1">

    | $\times$ |   1   |  $i$  |  $j$  |  $k$  |
    | :------: | :---: | :---: | :---: | :---: |
    |     1    |   1   |  $i$  |  $j$  |  $k$  |
    |    $i$   |  $i$  |  $-1$ |  $k$  |  $-j$ |
    |    $j$   |  $j$  |  $-k$ |  $-1$ |  $i$  |
    |    $k$   |  $k$  |  $j$  |  $-i$ |  $-1$ |

    </div>

利用表格中的结果，我们可以把四元数相互乘法的形式简化为

$$
\begin{aligned}
    q_1q_2
    =& (a_1a_2 +a_1b_2i + a_1c_2j + a_1d_2k) + \\
    & (b_1a_2i - b_1b_2 + b_1c_2k - b_1d_2j) + \\
    & (c_1a_2j - c_1b_2k - c_1c_2 + c_1d_2i) + \\
    & (d_1a_2k + d_1b_2j - d_1c_2i - d_1d_2)\\
    =& (a_1{\color{red} a_2} - b_1{\color{cyan} b_2} - c_1{\color{green} c_2} - d_1{\color{yellow} d_2}) + \\
    & (b_1{\color{red} a_2} + a_1{\color{cyan} b_2} - d_1{\color{green} c_2} + c_1{\color{yellow} d_2})i + \\
    & (c_1{\color{red} a_2} + d_1{\color{cyan} b_2} + a_1{\color{green} c_2} - b_1{\color{yellow} d_2})j + \\
    & (d_1{\color{red} a_2} - c_1{\color{cyan} b_2} + b_1{\color{green} c_2} + a_1{\color{yellow} d_2})k
\end{aligned}
$$

!!! info "四元数乘法基本形式"
    对 $q_1=a_1 + b_1i + c_1j + d_1k$ 和 $q_2={\color{red} a_2} + {\color{cyan} b_2}i + {\color{green} c_2}j + {\color{yellow} d_2}k$，有

    $$
    \begin{aligned}
        q_1q_2 
        =& (a_1{\color{red} a_2} - b_1{\color{cyan} b_2} - c_1{\color{green} c_2} - d_1{\color{yellow} d_2}) + \\
        & (b_1{\color{red} a_2} + a_1{\color{cyan} b_2} - d_1{\color{green} c_2} + c_1{\color{yellow} d_2})i + \\
        & (c_1{\color{red} a_2} + d_1{\color{cyan} b_2} + a_1{\color{green} c_2} - b_1{\color{yellow} d_2})j + \\
        & (d_1{\color{red} a_2} - c_1{\color{cyan} b_2} + b_1{\color{green} c_2} + a_1{\color{yellow} d_2})k
    \end{aligned}
    $$

##### 矩阵形式

在向量表示四元数下，可以把四元数相互乘法表示为矩阵乘向量的形式，即

!!! info "四元数乘法矩阵形式"
    对 $q_1=a_1 + b_1i + c_1j + d_1k$ 和 $q_2={\color{red} a_2} + {\color{cyan} b_2}i + {\color{green} c_2}j + {\color{yellow} d_2}k$，有

    $$
        q_1q_2 = 
        \begin{bmatrix}
            a_1 & -b_1 & -c_1 & -d_1 \\
            b_1 &  a_1 & -d_1 &  c_1 \\
            c_1 &  d_1 &  a_1 & -b_1 \\
            d_1 & -c_1 &  b_1 &  a_1
        \end{bmatrix} \begin{bmatrix}
            {\color{red} a_2} \\
            {\color{cyan} b_2} \\
            {\color{green} c_2} \\
            {\color{yellow} d_2}
        \end{bmatrix}
    $$

我们发现，这实际上把 $q_1$ 看作一个 $\mathbb{R}^{4\times 4}$ 的反对称矩阵，$q_2$ 看作一个 $\mathbb{R}^4$ 的向量。所以，类似复数地，四元数也有其反对称矩阵表示。

##### Grassmann 积形式

我们还希望在 $q=[s, \mathbf{v}]$ 的表示下能够方便地进行四元数乘法，于是就有了 Grassmann 积的结果形式。将 $q_1, q_2$ 表示为 $q_1=[a_1, [b_1, c_1, d_1]^{\top}]=[a_1, \mathbf{v}]$ 和 $q_2=[a_2, [b_2, c_2, d_2]^{\top}]=[a_2, \mathbf{u}]$，整理前面得到的乘法结果：

$$
\begin{aligned}
    q_1q_2
    =& (a_1a_2 - (b_1b_2 + c_1c_2 + d_1d_2)) + \\
    & (b_1{\color{red} a_2} + {\color{cyan} a_1}b_2 + c_1d_2 - d_1c_2)i + \\
    & (c_1{\color{red} a_2} + {\color{cyan} a_1}c_2 + d_1b_2 - b_1d_2)j + \\
    & (d_1{\color{red} a_2} + {\color{cyan} a_1}d_2 + b_1c_2 - c_1b_2)k
\end{aligned}
$$

又**注意到**

$$
\begin{gathered}
    \mathbf{v}\cdot \mathbf{u} = b_1b_2 + c_1c_2 + d_1d_2 \\
    \mathbf{v}\times \mathbf{u} = \begin{bmatrix}
        \mathbf{i} & \mathbf{j} & \mathbf{k} \\
        b_1 & c_1 & d_1 \\
        b_2 & c_2 & d_2
    \end{bmatrix} = (c_1d_2 - d_1c_2)\mathbf{i} + (d_1b_2 - b_1d_2)\mathbf{j} + (b_1c_2 - c_1b_2)\mathbf{k}
\end{gathered}
$$

所以我们发现 $q_1q_2$ 可以用向量点乘和叉乘的方式表示出来，即

!!! info "Grassmann 积"
    对四元数 $q_1=[a_1, \mathbf{v}]$ 和 $q_2=[a_2, \mathbf{u}]$，有

    $$
    q_1q_2 = [a_1a_2 - \mathbf{v}\cdot \mathbf{u}, a_1\mathbf{u} + a_2\mathbf{v} + \mathbf{v}\times \mathbf{u}]
    $$

回忆前面推导过的 3D 旋转公式，也是由 $\mathbf{u}\times \mathbf{v}$ 和 $\mathbf{u}\cdot \mathbf{v}$ 构成的，只是 $\mathbf{u}$ 是旋转轴的方向，而 $\mathbf{v}$ 是受到旋转变换的向量。事实上，Grassmann 积形式的四元数乘法也正是连接四元数和旋转的纽带，这会在后面进行展示。

!!! abstract "四元数乘法的表示形式"
    四元数 $q_1=a_1 + b_1i + c_1j + d_1k = [a_1, \mathbf{v}]$ 和 $q_2=a_2 + b_2i + c_2j + d_2k = [a_2, \mathbf{u}]$ 的乘法有如下表示形式：

    - 基本形式：
    
    $$
    \begin{aligned}
        q_1q_2 
        =& (a_1{\color{red} a_2} - b_1{\color{cyan} b_2} - c_1{\color{green} c_2} - d_1{\color{yellow} d_2}) + \\
        & (b_1{\color{red} a_2} + a_1{\color{cyan} b_2} - d_1{\color{green} c_2} + c_1{\color{yellow} d_2})i + \\
        & (c_1{\color{red} a_2} + d_1{\color{cyan} b_2} + a_1{\color{green} c_2} - b_1{\color{yellow} d_2})j + \\
        & (d_1{\color{red} a_2} - c_1{\color{cyan} b_2} + b_1{\color{green} c_2} + a_1{\color{yellow} d_2})k
    \end{aligned}
    $$

    - 矩阵形式

    $$
    q_1q_2 =
    \begin{bmatrix}
        a_1 & -b_1 & -c_1 & -d_1 \\
        b_1 &  a_1 & -d_1 &  c_1 \\
        c_1 &  d_1 &  a_1 & -b_1 \\
        d_1 & -c_1 &  b_1 &  a_1
    \end{bmatrix} \begin{bmatrix}
        {\color{red} a_2} \\
        {\color{cyan} b_2} \\
        {\color{green} c_2} \\
        {\color{yellow} d_2}
    \end{bmatrix}
    $$

    - Grassmann 积形式

    $$
    q_1q_2 = [a_1a_2 - \mathbf{v}\cdot \mathbf{u}, a_1\mathbf{u} + a_2\mathbf{v} + \mathbf{v}\times \mathbf{u}]
    $$

### 纯四元数、逆和共轭

#### 纯四元数

与复数类似，纯四元数指实部为 0 的四元数。对于纯四元数 $q_v=[0, \mathbf{v}]$ 和 $q_u=[0, \mathbf{u}]$，有

$$
q_vq_u = [- \mathbf{v}\cdot \mathbf{u}, \mathbf{v}\times \mathbf{u}]
$$

#### （乘法）逆和共轭

事实上，我们容易验证四元数集合 $\mathbb{H}$ 和其加法和乘法构成的代数系统为环 (ring) 而不是域 (field)。这一点和复数是不一致的，因为复数与其加法、乘法运算构成了一个数域。

> 事实上所构成的环是含幺环，但不是交换环

??? tip "对群、环、域的回顾"
    !!! info "群 (group)"
        代数系统 $<G: \circ>$ 是一个群，如果满足以下条件：
        
        1. 结合律：对于任意 $a, b, c\in G$，有 $a\circ (b\circ c) = (a\circ b)\circ c$
        2. 单位元：存在运算单位元，即存在一个元素 $e\in G$，使得对于任意 $a\in G$，有 $a\circ e = e\circ a = a$
        3. 逆元：任意元素可逆，即对于任意 $a\in G$，存在一个元素 $a^{-1}\in G$，使得 $a\circ a^{-1} = a^{-1}\circ a = e$

    群需要满足 3 个条件，如果满足的条件数量不同，有如下常见情形：
    
    - (1) 如果仅满足条件 1（结合律），则称为**半群**
    - (2) 如果满足条件 1 和 2，则称为**含幺半群**
    - (4) 如果在条件 1、2、3 的基础上，运算 $\circ$ 还满足交换律，则称**交换群**或 **Abel 群**

    环和域都含有一个加法运算 $+$ 和一个乘法运算 $\circ$。

    !!! info "环 (ring)"
        代数系统 $<R: +, \circ>$ 是一个环，如果满足以下条件：
        
        1. $<R: +>$ 是一个交换群
        2. $<R: \circ>$ 是一个半群（仅需满足结合律）
        3. 乘法运算 $\circ$ 对加法运算 $+$ 满足分配律

    如果环中的乘法满足交换律，则称为**交换环**；如果环中的乘法有单位元，则称为**含幺环**。

    > 环的加法单位元记作 $0$，如果是含幺环，其乘法单位元记作 $1$

    !!! info "域 (field)"
        代数系统 $<F: +, \circ>$ 是一个域，如果满足以下条件：
        
        1. $<F: +, \circ>$ 是一个含有至少两个元的交换环
        2. $<F\backslash \{0\}: \circ>$ 是一个交换群

    可见，域所必须含有的两个元就是加法单位元 0 和乘法单位元 1。

四元数 $q$ 的加法逆是很自然的 $-q$，但是乘法逆就需要小心构造了。使用 $q^*=[s, -\mathbf{v}]$ 表示 $q=[s, \mathbf{v}]$ 的共轭，则有

$$
\begin{aligned}
    qq^* 
    &= [s, \mathbf{v}][s, -\mathbf{v}] = [s^2 - \mathbf{v}\cdot (-\mathbf{v}), s(-\mathbf{v}) + s\mathbf{v} + \mathbf{v}\times (-\mathbf{v})] \\
    &= [s^2 + \|\mathbf{v}\|^2, 0] = [s, -\mathbf{v}][s, \mathbf{v}] = q^*q \\
    &= \|q\|^2 (+0i+0j+0k)
\end{aligned}
$$

从而我们发现

!!! info "四元数的乘法逆"
    对于四元数 $q=[s, \mathbf{v}]$，其乘法逆为 $q^{-1} = q^*/\|q\|^2$，$q^*=[s, -\mathbf{v}]$ 为 $q$ 的共轭，我们有

    $$
    qq^* = q^*q = \|q\|^2
    $$

## 3D 旋转的四元数基本形式

### 3D 向量的四元数表示

首先我们需要将相关的 3D 向量转换为四元数表示。回顾利用向量正交分解进行 3D 旋转变换的步骤：

1. 计算分解 $\mathbf{v}_{\parallel}$ 和 $\mathbf{v}_{\perp}$
2. 旋转 $\mathbf{v}_{\perp}$ 得到 $\mathbf{v}_{\perp}'$
3. 计算 $\mathbf{v}'=\mathbf{v}_{\perp}' + \mathbf{v}_{\parallel}$

我们将所涉及的向量用**纯四元数**表示如下：

$$
\begin{aligned}
    & v = [0, \mathbf{v}], & v' = [0, \mathbf{v}'],\\
    & v_{\perp} = [0, \mathbf{v}_{\perp}], & v_{\perp}' = [0, \mathbf{v}_{\perp}'],\\
    & v_{\parallel} = [0, \mathbf{v}_{\parallel}], & u = [0, \mathbf{u}]
\end{aligned}
$$

那么依然有 $v=v_{\parallel}+v_{\perp}$, $v'=v_{\parallel}+v_{\perp}'$。

### 旋转正交向量

根据前面对 3D 旋转的讨论，我们有

$$
\mathbf{v}_{\perp}' = \mathbf{v}_{\perp}\cos\theta + (\mathbf{u}\times \mathbf{v}_{\perp})\sin\theta
$$

$\mathbf{v}_{\perp}'$ 和 $\mathbf{v}_{\perp}$ 很容易替换成对应的纯四元数，但是叉乘 $\mathbf{u}\times \mathbf{v}_{\perp}$ 比较难以表示。回忆起纯四元数乘法可以干净地用点乘和叉乘表示，所以我们可以用纯四元数乘法得到这个叉乘值：

$$
    uv_{\perp} 
    = [0, \mathbf{u}][0, \mathbf{v}_{\perp}]
    = [-\underbrace{\mathbf{u}\cdot \mathbf{v}_{\perp}}_{=0, \mathbf{u}\perp \mathbf{v}_{\perp}}, \mathbf{u}\times \mathbf{v}_{\perp}]
    = [0, \mathbf{u}\times \mathbf{v}_{\perp}]
$$

因此我们有

$$
v_{\perp}' = v_{\perp}\cos\theta + uv_{\perp}\sin\theta = (\cos\theta + u\sin\theta)v_{\perp}
$$

由此我们成功把 $v_{\perp}'$ 表示为一个四元数和 $v_{\perp}$ 的乘积，特别地，这个四元数 $q=\cos\theta + u\sin\theta=[\cos\theta, \mathbf{u}\sin\theta]$ 满足

$$
\|q\| = \sqrt{\cos^2\theta + \|\mathbf{u}\|^2\sin^2\theta} = 1
$$

### 组合两个分量

现在我们有

$$
v' = v_{\perp}' + v_{\parallel} = qv_{\perp} + v_{\parallel}
$$

其中 $q=[\cos\theta, \mathbf{u}\sin\theta]$。当然，像前面讨论 3D 旋转一样，我们可以分别计算 $v_{\perp}$ 和 $v_{\parallel}$，但是这里我们将使用新的方法：构造一个半角旋转四元数 $p$，使得 $p^2=q$。我们采取简单的构造 $p=[\cos\frac{\theta}{2}, \mathbf{u}\sin\frac{\theta}{2}]$，这个构造的合理性将由一个引理的形式说明：

!!! abstract "旋转四元数二倍角"
    如果 $q=[\cos\theta, \mathbf{u}\sin\theta]$，其中 $\|\mathbf{u}\|=1$，那么有 $q^2=[\cos 2\theta, \mathbf{u}\sin 2\theta]$。

??? general "Proof"
    $$
    \begin{aligned}
        q^2 
        &= [\cos\theta, \mathbf{u}\sin\theta][\cos\theta, \mathbf{u}\sin\theta] \\
        &= [\cos^2\theta - \mathbf{u}\cdot \mathbf{u}\sin^2\theta, \mathbf{u}\sin\theta\cos\theta + \cos\theta\mathbf{u}\sin\theta + \mathbf{u}\times \mathbf{u}\sin^2\theta] \\
        &= [\cos^2\theta - \sin^2\theta, 2\mathbf{u}\sin\theta\cos\theta] \\
        &= [\cos 2\theta, \mathbf{u}\sin 2\theta]
    \end{aligned}
    $$

这样，我们就有

$$
    v' 
    = qv_{\perp} + v_{\parallel}
    = p^2v_{\perp} + pp^{-1}v_{\parallel}
    = p (pv_{\perp} + p^{-1}v_{\parallel})
    = p (pv_{\perp} + p^*v_{\parallel})
$$

> 容易得到 $\|p\|=1$，所以 $p^*=p^{-1}$

即将进行的进一步化简为：

$$
v' = p (pv_{\perp} + p^*v_{\parallel})
\xlongequal{?} p (v_{\perp}p^* + v_{\parallel}p^*)
= p (v_{\perp} + v_{\parallel})p^*
= pv p^*
$$

这里需要我们证明两个事情：$pv_{\perp}=v_{\perp}p^*$ 和 $p^*v_{\parallel}=v_{\parallel}p^*$。将证明折叠如下：

> 关键在于，Grassmann 积由点乘和叉乘构成，垂直会让点乘为 0，平行会让叉乘为 0

??? general "Proof"
    简记 $p=[\cos\frac{\theta}{2}, \mathbf{u}\sin\frac{\theta}{2}]=[\alpha, \beta\mathbf{u}]$

    - 对于 $pv_{\perp}=v_{\perp}p^*$，我们有

    $$
    \begin{aligned}
        LHS
        &= [\alpha, \beta\mathbf{u}][0, \mathbf{v}_{\perp}] \\
        &= [0 - \beta\mathbf{u}\cdot \mathbf{v}_{\perp}, \alpha \mathbf{v}_{\perp} + 0 + \beta\mathbf{u}\times \mathbf{v}_{\perp}] \\
        &= [0, \alpha \mathbf{v}_{\perp} + \beta\mathbf{u}\times \mathbf{v}_{\perp}] & (\mathbf{u}\perp\mathbf{v}_{\perp} \Rightarrow \mathbf{u}\cdot \mathbf{v}_{\perp}=0 ) 
    \end{aligned}
    $$

    $$
    \begin{aligned}
        RHS
        &= [0, \mathbf{v}_{\perp}][\alpha, -\beta\mathbf{u}] \\
        &= [0 + \beta\mathbf{u}\cdot \mathbf{v}_{\perp}, 0 + \mathbf{v}_{\perp}\alpha + \mathbf{v}_{\perp}\times (-\beta\mathbf{u})] \\
        &= [0, \alpha \mathbf{v}_{\perp} + \beta\mathbf{u}\times \mathbf{v}_{\perp}] & (a\times b = - b\times a)
    \end{aligned}
    $$

    - 对于 $p^*v_{\parallel}=v_{\parallel}p^*$，我们有

    $$
    \begin{aligned}
        LHS
        &= [\alpha, -\beta\mathbf{u}][0, \mathbf{v}_{\parallel}] \\
        &= [0 - \beta\mathbf{u}\cdot \mathbf{v}_{\parallel}, \alpha \mathbf{v}_{\parallel} + 0 - \beta\mathbf{u}\times \mathbf{v}_{\parallel}] \\
        &= [- \beta\mathbf{u}\cdot \mathbf{v}_{\parallel}, \alpha \mathbf{v}_{\parallel}] & (\mathbf{u}\parallel\mathbf{v}_{\parallel} \Rightarrow \mathbf{u}\times \mathbf{v}_{\parallel}=0 )
    \end{aligned}
    $$

    $$
    \begin{aligned}
        RHS
        &= [0, \mathbf{v}_{\parallel}][\alpha, -\beta\mathbf{u}] \\
        &= [0 - \beta\mathbf{v}_{\parallel}\cdot \mathbf{u}, 0 + \mathbf{v}_{\parallel}\alpha + \mathbf{v}_{\parallel}\times (-\beta\mathbf{u})] \\
        &= [- \beta\mathbf{u}\cdot \mathbf{v}_{\parallel}, \alpha \mathbf{v}_{\parallel}]
    \end{aligned}
    $$

因此我们就有

!!! abstract "3D 旋转的四元数基本形式"
    对于 3D 向量 $\mathbf{v}$，其绕旋转轴方向向量 $\mathbf{u}$ 进行的角度为 $\theta$ 的旋转变换可以表示为

    $$
    v' = qv q^*
    $$

    其中 $q=[\cos\frac{\theta}{2}, \mathbf{u}\sin\frac{\theta}{2}]$。

这个公式和我们之前推导的 Rodrigues 旋转公式是相容的，容易验证：

$$
qvq^* = [0, \mathbf{v}\cos\theta + \mathbf{u}((\mathbf{u}\cdot \mathbf{v})(1-\cos\theta)) + (\mathbf{u}\times \mathbf{v})\sin\theta]
$$

??? general "Proof"
    $$
    \begin{aligned}
        qvq^* 
        =& \left[
            \cos\frac{\theta}{2}, 
            \mathbf{u}\sin\frac{\theta}{2}
        \right]
        [0, \mathbf{v}]
        \left[
            \cos\frac{\theta}{2},
            -\mathbf{u}\sin\frac{\theta}{2}
        \right] \\
        =& \left[
            0 - \mathbf{u}\cdot \mathbf{v}\sin\frac{\theta}{2}, 
            \mathbf{v}\cos\frac{\theta}{2}
            + 0
            + (\mathbf{u}\times \mathbf{v})\sin\frac{\theta}{2}
        \right]\left[
            \cos\frac{\theta}{2},
            -\mathbf{u}\sin\frac{\theta}{2}
        \right] \\
        =& \left[
            - \mathbf{u}\cdot \mathbf{v}\sin\frac{\theta}{2}, 
            \mathbf{v}\cos\frac{\theta}{2}
            + (\mathbf{u}\times \mathbf{v})\sin\frac{\theta}{2}
        \right]\left[
            \cos\frac{\theta}{2},
            -\mathbf{u}\sin\frac{\theta}{2}
        \right] \\
        =& \left[
            -\mathbf{u}\cdot \mathbf{v}\sin\frac{\theta}{2}\cos\frac{\theta}{2}
            + \left(
                \mathbf{u}\cdot \mathbf{v}\sin\frac{\theta}{2}\cos\frac{\theta}{2}
                + \underbrace{\mathbf{u}\cdot (\mathbf{u}\times \mathbf{v})}_{=0, \mathbf{u}\perp (\mathbf{u}\times \mathbf{v})}\sin^2\frac{\theta}{2}
            \right)
        \right., \\
        &   \mathbf{u}(\mathbf{u}\cdot \mathbf{v})\sin^2\frac{\theta}{2}
            + \mathbf{v}\cos^2\frac{\theta}{2}
            + (\mathbf{u}\times \mathbf{v})\sin\frac{\theta}{2}\cos\frac{\theta}{2} \\
        &\left.
            - \mathbf{v}\times \mathbf{u}\sin\frac{\theta}{2}\cos\frac{\theta}{2}
            - \underbrace{(\mathbf{u}\times \mathbf{v})\times \mathbf{u}}_{=-(\mathbf{u}\cdot \mathbf{v})\mathbf{u} + \|\mathbf{u}\|^2\mathbf{v}}\sin^2\frac{\theta}{2}
        \right] \\
        =& \left[
            0, 
            2\mathbf{u}(\mathbf{u}\cdot \mathbf{v})\sin^2\frac{\theta}{2}
            + \mathbf{v}\left(\cos^2\frac{\theta}{2} - \sin^2\frac{\theta}{2}\right)
            + 2(\mathbf{u}\times \mathbf{v})\sin\frac{\theta}{2}\cos\frac{\theta}{2}
        \right] \\
        =& [0, \mathbf{u}(\mathbf{u}\cdot \mathbf{v})(1-\cos\theta) + \mathbf{v}\cos\theta + (\mathbf{u}\times \mathbf{v})\sin\theta]
    \end{aligned}
    $$

    注意有公式 $\mathbf{a}\times (\mathbf{b}\times \mathbf{c}) = (\mathbf{a}\cdot \mathbf{c})\mathbf{b} - (\mathbf{a}\cdot \mathbf{b})\mathbf{c}$

如果想要从旋转四元数 $q=[a, \mathbf{b}]$ 恢复旋转轴方向 $\mathbf{u}$ 和旋转角 $\theta$，根据 $q=[\cos\frac{\theta}{2}, \mathbf{u}\sin\frac{\theta}{2}]$，只需要

$$
    \theta = 2\arccos a, \quad
    \mathbf{u} = \frac{\mathbf{b}}{\sin(\arccos a)}
$$

## 3D 旋转的矩阵形式（利用四元数元素）

前面讨论过，对四元数左乘一个四元数 $q=a+bi+cj+dk$，相当于对这个四元数向量左乘一个 $L(q)$:

$$
L(q) = \begin{bmatrix}
    a & -b & -c & -d \\
    b &  a & -d &  c \\
    c &  d &  a & -b \\
    d & -c &  b &  a
\end{bmatrix}
$$

用和之前类似的方法，可以得知对四元数右乘 $q$，等价于对这个四元数向量左乘一个 $R(q)$:

$$
R(q) = \begin{bmatrix}
    a & -b & -c & -d \\
    b &  a &  d & -c \\
    c & -d &  a &  b \\
    d &  c & -b &  a
\end{bmatrix}
$$

因此我们通过计算 $L(q)R(q^*)$ 可以有

$$
v' = qvq^* = L(q)R(q^*)v = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1-2c^2-2d^2 & 2bc-2ad & 2ac+2bd \\
    0 & 2ad+2bc & 1-2b^2-2d^2 & 2cd-2ab \\
    0 & 2bd-2ac & 2ab+2cd & 1-2b^2-2c^2
\end{bmatrix}v
$$

> $L(q)R(q^*)$ 的计算过程略，读者可以自行验证

因为是纯四元数的变换，实部没有意义，所以我们可以简单地有

!!! info "3D 旋转的矩阵形式（利用四元数元素）"
    对 3D 向量 $\mathbf{v}$ 进行旋转，其旋转四元数为 $q=a+bi+cj+dk$，则有

    $$
    \mathbf{v}' = \begin{bmatrix}
        1-2(c^2+d^2) & 2(bc-ad) & 2(ac+bd) \\
        2(ad+bc) & 1-2(b^2+d^2) & 2(cd-ab) \\
        2(bd-ac) & 2(ab+cd) & 1-2(b^2+c^2)
    \end{bmatrix}\mathbf{v}
    $$

矩阵形式的好处在于，对大批量的向量进行相同的旋转变换时，可以预先计算变换矩阵，而不需要一个一个地计算四元数乘法。

## 3D 旋转的四元数指数形式

类似复数的欧拉公式，旋转四元数也可以表示为指数形式，考虑四元数 $u=[0, \mathbf{u}]$，$\mathbf{u}$ 为单位向量，我们有

$$
e^{u\theta} = \cos\theta + u\sin\theta = \cos\theta + \mathbf{u}\sin\theta
$$

也就是说，旋转四元数 $q=[\cos\theta, \mathbf{u}\sin\theta]$ 可以表示为 $e^{u\theta}$。类似欧拉公式，使用级数展开可以证明这个公式。

??? general "Proof"
    注意到 $e^x$, $\sin x$, $\cos x$ 的泰勒展开式为

    $$
    \begin{aligned}
        e^x &= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \\
        \sin x &= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \\
        \cos x &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots
    \end{aligned}
    $$

    从而有

    $$
    \begin{aligned}
        e^{u\theta}
        &= \sum_{n=0}^{\infty} \frac{(u\theta)^n}{n!} \\
        &= 1 + u\theta + \frac{(u\theta)^2}{2!} + \frac{(u\theta)^3}{3!} + \frac{(u\theta)^4}{4!} + \frac{(u\theta)^5}{5!} + \cdots \\
        &= 1 + u\theta - \frac{\theta^2}{2!} - \frac{u\theta^3}{3!} + \frac{\theta^4}{4!} + \frac{u\theta^5}{5!} - \cdots & (u^2=-1) \\
    \end{aligned}
    $$

    结合

    $$
    \begin{aligned}
        \sin \theta &= \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!}\theta^{2n+1} = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots \\
        \cos \theta &= \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!}\theta^{2n} = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots
    \end{aligned}
    $$

    有
    
    $$
        \cos\theta + u\sin\theta
        = 1 + u\theta - \frac{\theta^2}{2!} - \frac{u\theta^3}{3!} + \frac{\theta^4}{4!} + \frac{u\theta^5}{5!} - \cdots
        = e^{u\theta}
    $$

    > 实际上证明了李代数 $\mathfrak{su}(2)$ 到李群 $SU(2)$ 的指数映射

> 注意到有 $u^2 = [-\mathbf{u}\cdot \mathbf{u}, 0] = -1$，这和欧拉公式中的 $i$ 是非常类似的。

有了四元数的指数形式，就可以改写前面的 3D 旋转的四元数表示：

!!! info "3D 旋转的四元数指数形式"
    对 3D 向量 $\mathbf{v}$ 绕着旋转轴方向向量 $\mathbf{u}$ 进行的角度为 $\theta$ 的旋转变换，令 $v=[0, \mathbf{v}]$，$u=[0, \mathbf{u}]$，有

    $$
    v' = e^{u\frac{\theta}{2}} v e^{-u\frac{\theta}{2}}
    $$

在旋转四元数的指数形式下，其自然对数运算和幂运算也就可以定义了。

!!! info "旋转四元数的自然对数、幂运算"
    对旋转四元数 $q=[\cos\theta, \mathbf{u}\sin\theta]$，有

    $$
    \ln q = [0, \mathbf{u}\theta], \quad
    q^t = (e^{u\theta})^t = e^{u(t\theta)}=[\cos (t\theta), \mathbf{u}\sin (t\theta)]
    $$

    可以看到，一个单位四元数的 $t$ 次幂等价于将它的旋转角缩放至 $t$ 倍，且不会改变旋转轴 $\mathbf{u}$。

旋转四元数的自然对数和幂运算会在之后讨论四元数插值时非常有用。

## 旋转四元数的复合

先进行旋转四元数 $q_1$ 对应的旋转，再进行旋转四元数 $q_2$ 对应的旋转，则可以一次性进行 $q_1q_2$ 对应的旋转：

$$
v''=q_2(q_1vq_1^*)q_2^*=(q_2q_1)v(q_1^*q_2*)
$$

这里需要证明的有 2 个关键：

1. $q_2q_1$ 仍是旋转四元数
2. $(q_2q_1)^*=q_1^*q_2^*$

### 复合四元数仍是旋转四元数

$q_1=[\cos\theta_1, \mathbf{u}_1\sin\theta_1]$，$q_2=[\cos\theta_2, \mathbf{u}_2\sin\theta_2]$，我们有

$$
    q_2q_1 = [\cos\theta_2\cos\theta_1 - \mathbf{u}_2\cdot \mathbf{u}_1\sin\theta_2\sin\theta_1, \mathbf{u}_2\sin\theta_2\cos\theta_1 + \cos\theta_2\mathbf{u}_1\sin\theta_1 + \mathbf{u}_2\times \mathbf{u}_1\sin\theta_2\sin\theta_1]
$$

需要有

$$
\begin{aligned}
    \theta &= \arccos(\cos\theta_2\cos\theta_1 - \mathbf{u}_2\cdot \mathbf{u}_1\sin\theta_2\sin\theta_1) \\
    \mathbf{u} &= \pm \frac{\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1 + (\mathbf{u}_2\times \mathbf{u}_1)\sin\theta_2\sin\theta_1}{\|\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1 + (\mathbf{u}_2\times \mathbf{u}_1)\sin\theta_2\sin\theta_1\|}
\end{aligned}
$$

只需证明

$$
|\sin\theta| = \|\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1 + (\mathbf{u}_2\times \mathbf{u}_1)\sin\theta_2\sin\theta_1\|
$$

??? general "Proof"
    由于 $\mathbf{u}_2\times \mathbf{u}_1$ 与 $\mathbf{u}_1$、$\mathbf{u}_2$ 都正交，设 $\mathbf{u}_1$ 和 $\mathbf{u}_2$ 之间的夹角为 $\varphi$，有

    $$
    \begin{aligned}
        &\|\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1 + (\mathbf{u}_2\times \mathbf{u}_1)\sin\theta_2\sin\theta_1\| \\
        =& \sqrt{(\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1)^2 + (\mathbf{u}_2\times \mathbf{u}_1\sin\theta_2\sin\theta_1)^2} \\
        =& \sqrt{\sin^2\theta_1\cos^2\theta_2 + \sin^2\theta_2\cos^2\theta_1 + 2\sin\theta_1\cos\theta_2\sin\theta_2\cos\theta_1\cos\varphi + \sin^2\theta_2\sin^2\theta_1\sin^2\varphi} \\
    \end{aligned}
    $$

    所以有

    $$
    \begin{aligned}
        &\|\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1 + (\mathbf{u}_2\times \mathbf{u}_1)\sin\theta_2\sin\theta_1\|^2 + \cos^2\theta \\
        =& \sin^2\theta_1\cos^2\theta_2 + \sin^2\theta_2\cos^2\theta_1 + \bcancel{2\sin\theta_1\cos\theta_2\sin\theta_2\cos\theta_1\cos\varphi} + \sin^2\theta_2\sin^2\theta_1{\color{cyan} \sin^2\varphi} \\
        &+ \cos^2\theta_2\cos^2\theta_1 + \sin^2\theta_2\sin^2\theta_1{\color{cyan}\cos^2\varphi} - \bcancel{2  \cos\theta_2\cos\theta_1\sin\theta_2\sin\theta_1\cos\varphi}\\
        =& ({\color{yellow} \sin^2\theta_1}\cos^2\theta_2 + \cos^2\theta_2{\color{yellow} \cos^2\theta_1}) + (\sin^2\theta_2{\color{red} \sin^2\theta_1} + \sin^2\theta_2{\color{red} \cos^2\theta_1}) \\
        =& \cos^2\theta_2 + \sin^2\theta_2 = 1
    \end{aligned}
    $$

    则证得

    $$
    |\sin \theta| = \|\mathbf{u}_1\sin\theta_1\cos\theta_2 + \mathbf{u}_2\sin\theta_2\cos\theta_1 + (\mathbf{u}_2\times \mathbf{u}_1)\sin\theta_2\sin\theta_1\|
    $$

### 复合共轭计算

$q_1=[s, \mathbf{v}]$，$q_2=[t, \mathbf{u}]$，我们有

$$
\begin{aligned}
    (q_2q_1)^*
    &= [t, \mathbf{u}][s, \mathbf{v}]^* \\
    &= [ts - \mathbf{u}\cdot \mathbf{v}, t\mathbf{v} + s\mathbf{u} + \mathbf{u}\times \mathbf{v}]^* \\
    &= [st - \mathbf{v}\cdot \mathbf{u}, - s\mathbf{u} - t\mathbf{v} + \mathbf{v}\times \mathbf{u}] \\
\end{aligned}
$$

而

$$
\begin{aligned}
    q_1^*q_2^*
    &= [s, -\mathbf{v}][t, -\mathbf{u}] \\
    &= [st - \mathbf{v}\cdot \mathbf{u}, -s\mathbf{u} - t\mathbf{v} + \mathbf{v}\times \mathbf{u}]
\end{aligned}
$$

从而证得 $(q_2q_1)^*=q_1^*q_2^*$。

## 四元数表示 3D 旋转的问题：双倍覆盖

即对于 $q=[\cos\frac{\theta}{2}, \mathbf{u}\sin\frac{\theta}{2}]$，$q$ 和 $-q$ 表示的旋转是相同的，因为

$$
-q = \left[-\cos\frac{\theta}{2}, -\mathbf{u}\sin\frac{\theta}{2}\right] = \left[\cos\left(\pi-\frac{\theta}{2}\right), \sin\left(\pi-\frac{\theta}{2}\right)(-\mathbf{u})\right]
$$

> 从 $(-q)v(-q)^*=(-1)^2qvq^*=qvq^*$ 也可以看出来

如下图所示，左图为 $q$ 代表的旋转，中图为 $-q$ 代表的旋转，两者其实是一样的。

<div style="display: flex; justify-content: space-between;">
    <img src="../../../imgs/quaternion/quaternion-double-cover-a.svg" alt="quaternion-double-cover-a" style="width: 33%;">
    <img src="../../../imgs/quaternion/quaternion-double-cover-b.svg" alt="quaternion-double-cover-b" style="width: 33%;">
    <img src="../../../imgs/quaternion/quaternion-double-cover-c.svg" alt="quaternion-double-cover-c" style="width: 30%;">
</div>

所以，事实上单位四元数（旋转四元数）到 3D 旋转构成了一个 **2 对 1 满射同态** (2-1 surjective homomorphism)，也就是说单位四元数**双倍覆盖** (double cover) 了 3D 旋转。

> 虽然 $q$ 和 $-q$ 是两个不同的四元数，但是它们对应的旋转矩阵是一样的，因此旋转矩阵不会出现双倍覆盖的问题。

