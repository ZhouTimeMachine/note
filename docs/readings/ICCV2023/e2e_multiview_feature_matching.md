<link rel="stylesheet" href="../../../css/counter.css" />

# End2End Multi-View Feature Matching with Differentiable Pose Optimization

!!! warning "该页面还在建设中"

!!! info "Link: [arxiv](https://arxiv.org/abs/2205.01694), [paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Roessle_End2End_Multi-View_Feature_Matching_with_Differentiable_Pose_Optimization_ICCV_2023_paper.pdf), [gh-page](https://barbararoessle.github.io/e2e_multi_view_matching/), [code](https://github.com/barbararoessle/e2e_multi_view_matching)"

!!! abstract "Abstract"
    - Claim: **Differentiable** Pose Estimation (Eight-Point Algorithm + Bundle Adjustment) and feature matching jointly, End-to-End training
    - Core Problem: reject outliers in feature matching
    - GNN: predict feature matching and confidence weights
    - Pose Estimation: use matching as constraints

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DifferentiablePO_1.png" alt="DifferentiablePO_1" style="zoom:67%;" />
</div>

## Multi-View Graph Attention Network

!!! tip "Notations"
    - $N$ images: $\{I_n\}_{n=1}^N$
    - corresponding poses: $\{p_n\}_{n=1}^N$
    - keypoints $x\in \mathbb{R}^2$ , descriptors $d\in \mathbb{R}^D$, confidence score $c\in [0, 1]$

!!! warning "待续。从代码可以看出用的就是 [SuperGlue](https://arxiv.org/abs/1911.11763)。"

输出 confidence weight $w_{ij}$

## Differentiable Pose Optimization

### Weighted Eight-Point Algorithm

#### Epipolar Geometry Basics

回忆基础矩阵(fundamental matrix) $F$ 和本质矩阵(essential matrix) $E$，它们之间有关系

$$
    E = K_2^{\top}EK_1
$$

其中 $K$ 是相机内参矩阵。给定对应 keypoints 的像素位置 $p_1, p_2$，又或者对应相机坐标系坐标 $x_1, x_2$，有对极约束(epipolar constraint)：

$$
    p_2^\top Fp_1 = 0, \quad x_2^\top Ex_1 = 0
$$

> $p_1=Kx_1$, $p_2=Kx_2$

因此，通过足够多的匹配点像素坐标可以计算基础矩阵，进而结合内参矩阵计算本质矩阵。由于有

$$
    E=t^{\wedge}R
$$

可以证明，$E$ 可以进行如下的 SVD 分解

$$
E=U\Sigma V^{\top},\quad \Sigma=\operatorname{diag}\{\sigma, \sigma, 0\}
$$

??? general "Proof"
    !!! abstract "Lemma"
        设 $A$ 是 $n$ 阶实反对称矩阵 (skew-symmetric matrix)，若 $n$ 为奇数，则 $A$ 必定奇异。
    
    !!! general "Proof"
        
        $$
            \det A = \det A^{\top}=\det (-A) = (-1)^n \det A= -\det A\Rightarrow \det A=0
        $$

    设 $Z=\begin{bmatrix}0 & 1 \\ -1 & 0\end{bmatrix}$，则有结论

    !!! abstract "Lemma"
        设 $A$ 是 $n$ 阶实反对称矩阵，则 $A=UDU^{\top}$，其中 $D$ 为如下的分块对角矩阵

        $$
            D=\operatorname{diag}\{\lambda_1Z, \lambda_2Z, \cdots, \lambda_mZ, 0, \cdots, 0\}
        $$
    
    > 证明见 [pdf](http://scipp.ucsc.edu/~haber/ph218/pfaffian15.pdf)。可以得到推论：反对称矩阵的非零特征值就是 $\pm \lambda_1 i, \cdots, \pm \lambda_m i$，都是纯虚数

    $E=t^{\wedge}R$，由于 $t^{\wedge}\neq 0$ 是反对称矩阵，存在 $\sigma\neq 0$ 使得

    $$
        t^{\wedge}=\sigma UDU^{\top},\quad D=\operatorname{diag}\{Z, 0\}
    $$

    考虑

    $$
    W=\begin{bmatrix}0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1\end{bmatrix}
    $$

    > $W$ 实际上是绕 $z$ 轴逆时针旋转 90 度的旋转矩阵

    则 $D=\operatorname{diag}\{1, 1, 0\} W$。由此就有

    $$
        E=\sigma UDU^{\top}R=U \operatorname{diag}\{\sigma, \sigma, 0\} (WU^{\top}R)
    $$

    从而得证。

以上的证明也同时证明了，完成该 SVD 分解之后，可以解得如下两种可能的 $t^{\wedge}$, $R$：

$$
\begin{aligned}
    &t^{\wedge} = UR_Z\left(\frac{\pi}{2}\right)\Sigma U^{\top},\quad R=UR_Z^{\top}\left(\frac{\pi}{2}\right)V^{\top}\\
    &t^{\wedge} = UR_Z\left(-\frac{\pi}{2}\right)\Sigma U^{\top},\quad R=UR_Z^{\top}\left(-\frac{\pi}{2}\right)V^{\top}
\end{aligned}
$$

> $R_Z(\theta)$ 表示绕 $z$ 轴逆时针旋转 $\theta$ 的旋转矩阵

由于 $E$ 和 $-E$ 等价，对任何一个 $t$ 取负号，结果也是相同的，所以一共可以有 $4$ 种解，需要选择其中最好的解。**在训练时，作者采用了离 ground truth 最近的解；在测试时，作者采用了能让最多的点在两个相机坐标系下都具有正深度的解。**

#### Implementation Details

一般的解出来的 $E$ 奇异值矩阵不一定满足 $\operatorname{diag}\{\sigma, \sigma, 0\}$ 的形式，可以有很多种修正方式：

- 解得奇异值矩阵 $\operatorname{diag}\{\sigma_1, \sigma_2, \sigma_3\}$ 后，取 $\Sigma=\operatorname{diag}\{\frac{\sigma_1+\sigma_2}{2}, \frac{\sigma_1+\sigma_2}{2}, 0\}$
- 由于 $E$ 具有尺度等价性，直接取 $\Sigma=\operatorname{diag}\{1, 1, 0\}$
- ……

这里作者使用的方法比较粗暴，就是简单地将解得的奇异值矩阵 $\operatorname{diag}\{\sigma_1, \sigma_2, \sigma_3\}$ 取为 $\Sigma=\operatorname{diag}\{\sigma_1, \sigma_2, 0\}$，这里没有保证 $\sigma_1=\sigma_2$，我认为是不太对的。也许在作者调的来自 Kornia 的包中进行了处理，有待进一步探索。

### Bundle Adjustment