<link rel="stylesheet" href="../../../../css/counter.css" />

# 基础：复数和旋转

!!! info "notes of https://github.com/Krasjet/quaternion, chapter 1 & 2"

## 复数和 2D 旋转

### 复数乘法矩阵形式

对于复数 $z_1 = a + bi$ 和 $z_2 = c + di$，它们最基础的乘法形式为：

$$
z_1 z_2 = (a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i
$$

实际上，我们可以将复数看作是一个 $2 \times 2$ 的反对称矩阵。

!!! info "复数的反对称矩阵表示"
    对于复数 $z=a + bi$，可以表示为如下的反对称矩阵：

    $$
    z=\begin{bmatrix}
        a & -b \\
        b & a
    \end{bmatrix}
    $$

只将 $z_1$ 视为矩阵，就足够将复数乘法表示为**矩阵和向量的乘法**：

$$
z_1z_2 = \begin{bmatrix}
    a & -b \\
    b & a
\end{bmatrix}
\begin{bmatrix}
    c \\
    d
\end{bmatrix} = 
\begin{bmatrix} 
    ac - bd \\ 
    ad + bc 
\end{bmatrix}
$$

或者，将 $z_1$ 和 $z_2$ 都视为矩阵，那最终的结果也得是反对称矩阵表示，那么复数乘法可以表示为**矩阵乘法**：

$$
z_1z_2 = \begin{bmatrix}
    a & -b \\
    b & a
\end{bmatrix}
\begin{bmatrix}
    c & -d \\
    d & c
\end{bmatrix} =
\begin{bmatrix}
    ac - bd & -ad - bc \\
    ad + bc & ac - bd
\end{bmatrix}
$$

> 从可以表示为矩阵乘法也可以看出复数乘法是**可交换**的

### 复数乘法极坐标形式

只把 $z_1$ 视为矩阵，可以认为是对向量 $z_2$ 进行了 $z_1$ 矩阵形式对应的变换。而 $z_1$ 的矩阵形式既可以简单地看作是把 $(1, 0)^{\top}$ 变换到 $(a, b)^{\top}$、$(0, 1)^{\top}$ 变换到 $(-b, a)^{\top}$ 的变换，也可以将其拆解为一个缩放变换和一个旋转变换的复合：

$$
\begin{aligned}
    \begin{bmatrix}
        a & -b \\
        b & a
    \end{bmatrix}
    &= 
        \begin{bmatrix}
            \sqrt{a^2 + b^2} & 0 \\
            0 & \sqrt{a^2 + b^2}
        \end{bmatrix}
        \begin{bmatrix}
            \frac{a}{\sqrt{a^2 + b^2}} & -\frac{b}{\sqrt{a^2 + b^2}} \\
            \frac{b}{\sqrt{a^2 + b^2}} & \frac{a}{\sqrt{a^2 + b^2}}
        \end{bmatrix}
    &= 
        \underbrace{\begin{bmatrix}
            \|z_1\| & 0 \\
            0 & \|z_1\|
        \end{bmatrix}}_{\text{scaling}}
        \underbrace{\begin{bmatrix}
            \cos \theta & -\sin \theta \\
            \sin \theta & \cos \theta
        \end{bmatrix}}_{\text{rotation}}
\end{aligned}
$$

这是否十分熟悉？利用欧拉公式 $e_{i\theta} = cos \theta + i \sin \theta$，可以很容易地导出复数的极坐标形式：

$$
z_1 = \|z_1\|\begin{bmatrix}
    \cos \theta _1 & -\sin \theta _1 \\
    \sin \theta _1 & \cos \theta _1
\end{bmatrix}
= \|z_1\|(\cos \theta _1 + i \sin \theta _1) = \|z_1\|e^{i\theta _1}
$$

也就有我们十分熟悉的极坐标形式下的复数乘法了

$$
z_1z_2 = \|z_1\|\|z_2\|e^{i(\theta _1 + \theta _2)}
$$

可以认为先将复数乘法视为矩阵乘法，再将 $z_1, z_2$ 对应的矩阵都视为缩放和旋转的复合变换，最后交换变换顺序让两个缩放变换相复合、两个旋转变换相复合，最后就得到了极坐标形式下的复数乘法。

!!! tip "复数乘法形式总结"
    - 原始形式

    $$
    z_1 z_2 = (a + bi)(c + di) = (ac - bd) + (ad + bc)i
    $$

    - 矩阵和向量乘法形式

    $$
        z_1z_2 = \begin{bmatrix}
            a & -b \\
            b & a
        \end{bmatrix}
        \begin{bmatrix}
            c \\
            d
        \end{bmatrix} = 
        \begin{bmatrix} 
            ac - bd \\ 
            ad + bc 
        \end{bmatrix}
    $$

    - 矩阵乘法形式

    $$
        z_1z_2 = \begin{bmatrix}
            a & -b \\
            b & a
        \end{bmatrix}
        \begin{bmatrix}
            c & -d \\
            d & c
        \end{bmatrix} =
        \begin{bmatrix}
            ac - bd & -ad - bc \\
            ad + bc & ac - bd
        \end{bmatrix}
    $$

    - 极坐标形式

    $$
        z_1z_2 = \|z_1\|\|z_2\|e^{i(\theta _1 + \theta _2)}
    $$

### 2D 旋转

由此，2D 旋转可以有如下三种表示形式（将 2D 向量 $v$ 旋转到 $v'$）：

!!! abstract "2D 旋转的表示形式" 

    - 矩阵形式

    $$
    v' = Rv
    = \begin{bmatrix}
        \cos \theta & -\sin \theta \\
        \sin \theta & \cos \theta
    \end{bmatrix}v
    $$

    - 复数积形式

    $$
    v' = zv = (\cos \theta + i \sin \theta)v
    $$

    - 极坐标形式

    $$
    v' = e^{i\theta}v
    $$

## 3D 旋转

### 轴角式表示

将主要讨论轴角 (axis-angle) 式的 3D 旋转表示，即以旋转轴和围绕旋转轴进行旋转的角度确定旋转：

- 旋转轴由其在 3D 空间中的方向向量 $\mathbf{u}=(u_x, u_y, u_z)^{\top}\in \mathbb{R}^3$ 确定
- 旋转角 $\theta$ 为一个实数，取正时的方向默认由右手定则确定

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/basics-axis-angle-rotation.svg" alt="basics-axis-angle-rotation" style="width: 40%;">
</div>

看似变量一共为 4 个实数，实际上由于方向向量满足约束 $\|\mathbf{u}\|=\sqrt{u_x^2 + u_y^2 + u_z^2}=1$，实际自由度为 3。

除了轴角式，欧拉角也常用来表示 3D 旋转，但是欧拉角存在死锁问题 (**Gimbal Lock**)，而且依赖于三个坐标轴的标定，使用轴角式表示就可以解决这个问题。

> 关于 Gimbal Lock 的部分，将专门开一块进行讨论；对于采取左手定则确定旋转角正方向的情况，也将开一块进行讨论

### 旋转分解

把即将进行旋转的向量 $\mathbf{v}$ 分解为

$$
\mathbf{v} = \mathbf{v}_{\parallel} + \mathbf{v}_{\perp}
$$

其中 $\mathbf{v}_{\perp}$ 正交于 $\mathbf{u}$，$\mathbf{v}_{\parallel}$ 平行于 $\mathbf{u}$，如下图所示，可以看出 $\mathbf{v}_{\parallel}$ 就是 $\mathbf{v}$ 在旋转轴 $\mathbf{u}$ 上的正交投影。

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/basics-orthogonal-decomposition.svg" alt="basics-orthogonal-decomposition" style="width: 50%;">
</div>

这样，我们可以通过 $\mathbf{v}' = \mathbf{v}_{\parallel}' + \mathbf{v}_{\perp}'$ 计算旋转后得到的向量 $\mathbf{v}'$，由于平行分量不会被旋转，即 $\mathbf{v}_{\parallel}'=\mathbf{v}_{\parallel}$，所以实际上只需要进行如下步骤：

!!! tip "利用向量正交分解进行 3D 旋转变换的步骤"
    1. 计算分解 $\mathbf{v}_{\parallel}$ 和 $\mathbf{v}_{\perp}$
    2. 旋转 $\mathbf{v}_{\perp}$ 得到 $\mathbf{v}_{\perp}'$
    3. 计算 $\mathbf{v}'=\mathbf{v}_{\perp}' + \mathbf{v}_{\parallel}$

### 3D 旋转

#### 计算分解

根据 $v_{\parallel}$ 是 $\mathbf{v}$ 的正交投影，可以得到

$$
\begin{aligned}
    \mathbf{v}_{\parallel}
    &= \operatorname{proj}_{\mathbf{u}}\mathbf{v} \\
    &= \frac{\mathbf{u}\cdot \mathbf{v}}{\|\mathbf{u}\|} \cdot \frac{\mathbf{u}}{\|\mathbf{u}\|} \\
    &= (\mathbf{u}\cdot \mathbf{v}) \mathbf{u}
\end{aligned}
$$

这样，就有 $\mathbf{v}_{\perp} = \mathbf{v} - \mathbf{v} _{\parallel} = \mathbf{v} - (\mathbf{u}\cdot \mathbf{v}) \mathbf{u}$。

#### 旋转正交分量

接下来旋转 $\mathbf{v}$ 的正交分量 $\mathbf{v}_{\perp}$ 得到 $\mathbf{v}_{\perp}'$。这实际上是在垂直于旋转轴 $\mathbf{u}$ 的平面上的一个 2D 旋转，将这个平面视为一个 x-y 平面，我们就可以使用我们前面已经得到的 2D 旋转公式。但我们首先需要 x 方向和 y 方向来表征这个平面，或者说，用实轴方向和虚轴方向来表征复平面。

将 $\frac{\mathbf{v}_{\perp}}{\|\mathbf{v}_{\perp}\|}$ 视为 x 方向是很自然的，我们还需要构造一个这个平面上的和 $\mathbf{v}_{\perp}$ 正交的向量作为 y 方向，由于它同时和 $\mathbf{v}_{\perp}$ 以及 $\mathbf{u}$ 正交，我们很自然地想到可以通过**叉积**的方式构造这样一个正交于由 $\mathbf{v}_{\perp}$ 和 $\mathbf{u}$ 所确定的平面的向量：

$$
\mathbf{w} = \mathbf{u}\times \mathbf{v}_{\perp}
$$

然后将 $\frac{\mathbf{w}}{\|\mathbf{w}\|}$ 作为 y 方向。注意到：

1. $\|\mathbf{w}\| = \| \mathbf{u}\|\cdot \| \mathbf{v_{\perp}}\| \sin\frac{\pi}{2}= \| \mathbf{v_{\perp}}\|$，$\mathbf{w}$ 和 $\mathbf{v}_{\perp}$ 实际上位于同一个圆周上
2. 叉积的方向由 $\mathbf{u}$ 到 $\mathbf{v}_{\perp}$ 的右手定则确定，我们一开始规定正旋转角方向由以 $\mathbf{u}$ 为轴的右手定则确定，容易得知以这种方式确定的 x-y 平面上的旋转角仍遵循 x 方向到 y 方向 $\frac{\pi}{2}$ 以内的旋转为正旋转角（即逆时针旋转）

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/basics-perp-rotation.svg" alt="basics-perp-rotation" style="width: 70%;">
</div>

所以，将 x 轴视为实轴，y 轴视为虚轴，$\mathbf{v}_{\perp}$ 可以表示为 $\|\mathbf{v}_{\perp}\|$，$\mathbf{w}$ 可以表示为 $\|\mathbf{v}_{\perp}\|i$，然后我们有

$$
\mathbf{v}_{\perp}' = (\cos\theta + i\sin\theta)\|\mathbf{v}_{\perp}\|
=\underbrace{\|\mathbf{v}_{\perp}\|\cos\theta}_{\in \mathbb{R}} + i\underbrace{\|\mathbf{v}_{\perp}\|\sin\theta}_{\in \mathbb{R}}
$$

重新将复数表示转换为向量表示，就有

$$
\begin{aligned}
    \mathbf{v}_{\perp}'
    &= \|\mathbf{v}_{\perp}\|\cos\theta \cdot \frac{\mathbf{v}_{\perp}}{\|\mathbf{v}_{\perp}\|} + \|\mathbf{v}_{\perp}\|\sin\theta \cdot \frac{\mathbf{w}}{\|\mathbf{w}\|} \\
    &= \mathbf{v}_{\perp} \cos\theta + (\mathbf{u}\times \mathbf{v}_{\perp})\sin\theta \\
    &= [\mathbf{v} - (\mathbf{u}\cdot \mathbf{v}) \mathbf{u}]\cos\theta + \{\mathbf{u}\times [\mathbf{v} - (\mathbf{u}\cdot \mathbf{v}) \mathbf{u}]\}\sin\theta \\
    &= \mathbf{v}\cos\theta - (\mathbf{u}\cdot \mathbf{v}) \mathbf{u}\cos\theta + (\mathbf{u}\times \mathbf{v})\sin\theta
\end{aligned}
$$

> 注意 $\mathbf{u}\times \mathbf{u}=0$

#### 组合两个分量

由于 $\mathbf{v}' = \mathbf{v}_{\perp}' + \mathbf{v}_{\parallel}$，我们有

$$
\begin{aligned}
    \mathbf{v}'
    &= \underbrace{\mathbf{v}\cos\theta - (\mathbf{u}\cdot \mathbf{v}) \mathbf{u}\cos\theta + (\mathbf{u}\times \mathbf{v})\sin\theta}_{\mathbf{v}_{\perp}'} 
    + \underbrace{(\mathbf{u}\cdot \mathbf{v}) \mathbf{u}}_{\mathbf{v}_{\parallel}} \\
    &= \mathbf{v}\cos\theta + \mathbf{u}[(\mathbf{u}\cdot \mathbf{v})(1-\cos\theta)] + (\mathbf{u}\times \mathbf{v})\sin\theta
\end{aligned}
$$

由此我们就得到了著名的罗德里格斯旋转公式 (Rodrigues' rotation formula)：

!!! abstract "罗德里格斯旋转公式 (Rodrigues' rotation formula)"
    在 3D 空间中，将任意向量 $\mathbf{v}$ 绕着旋转轴 $\mathbf{u}$ 进行右手定则正方向下 $\theta$ 的旋转 ($\|\mathbf{u}\|=1$)，旋转后得到的向量 $\mathbf{v}'$ 为

    $$
    \mathbf{v}'= \mathbf{v}\cos\theta + \mathbf{u}(\mathbf{u}\cdot \mathbf{v})(1-\cos\theta) + (\mathbf{u}\times \mathbf{v})\sin\theta
    $$