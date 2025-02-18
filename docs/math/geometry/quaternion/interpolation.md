<link rel="stylesheet" href="../../../../css/counter.css" />

# 四元数插值

!!! info "notes of https://github.com/Krasjet/quaternion, chapter 4 & 5 & 6"

对 $q_0=[\cos(\theta_0), \mathbf{u}_0\sin(\theta_0)]$、$q_1=[\cos(\theta_1), \mathbf{u}_1\sin(\theta_1)]$，我们希望找出一些中间变换 $q_t$，让 $q_0$ 能够平滑地过渡到 $q_1$，其中 $t=[0, 1]$。

对于特定的向量 $\mathbf{v}$ 而言，$q_0$、$q_t$、$q_1$ 会分别将 $\mathbf{v}$ 旋转到 $\mathbf{v}_0$、$\mathbf{v}_t$、$\mathbf{v}_1$。如下图所示，会有固定的 $\mathbf{u}_t$，使得当 $\mathbf{v}_0$、$\mathbf{v}_t$、$\mathbf{v}_1$ 的起点都在 $\mathbf{u}_t$ 上时，他们三者的终点会位于以 $\mathbf{u}_t$ 上某点为圆心的圆上——这个圆上 $\mathbf{v}_0$ 和 $\mathbf{v}_1$ 之间的夹角是 $\varphi$，而 $\mathbf{v}_t$ 和 $\mathbf{v}_0$ 构成的夹角恰为 $t\varphi$。

> 事实上这样对应的插值就是球面线性插值（Slerp），Lerp、Nlerp 都是尝试对 Slerp 进行近似。

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/interpolation-find-vt.svg" alt="interpolation-find-vt" style="width: 40%;">
</div>

## 从四元数差分到 3D 向量旋转差分

从 $\mathbf{v}$ 到 $\mathbf{v}_1$，我们可以认为先经历了 $q_0$ 对应的旋转成为 $\mathbf{v}_0$，然后经历了一个 $\Delta q$ 的旋转从 $\mathbf{v}_0$ 到 $\mathbf{v}_1$，这样就有：

$$
q_1 = \Delta q q_0
$$

$q_0$ 是单位四元数，有 $q_0^{-1} = q_0^*$，所以

$$
\Delta q = q_1 q_0^* = [\cos\theta_1\cos\theta_0 + (\mathbf{u}_1\sin\theta_1)\cdot (\mathbf{u}_0\sin\theta_0), ...]
$$

注意到，将四元数 $q_1, q_0$ 视为 $\mathbb{R}^4$ 向量，$\Delta q$ 的实部恰为 $q_1\cdot q_0$

- 由于 $\|q_0\|=\|q_1\|=1$，于是设 $q_0$ 和 $q_1$ 在 $\mathbb{R}^4$ 中的夹角为 $\theta$，有 $\Delta q = [\cos\theta, ...]$
- 从 $\mathbf{v}_0$ 到 $\mathbf{v}_1$，我们前面定义其绕 $\mathbf{u}_t$ 的旋转角为 $\varphi$，则 $\Delta q = [\cos\frac{\varphi}{2}, ...]$
- 因此有 $\cos\frac{\varphi}{2} = \cos\theta$，考虑到 $\frac{\varphi}{2}, \theta\in [0, \pi]$，有 $\varphi = 2\theta$

<div style="display: flex; justify-content: space-between;">
    <img src="../../../imgs/quaternion/interpolation-quat-to-vec-rot-1.svg" alt="interpolation-quat-to-vec-rot-1" style="width: 48%;">
    <img src="../../../imgs/quaternion/interpolation-quat-to-vec-rot-2.svg" alt="interpolation-quat-to-vec-rot-2" style="width: 48%;">
</div>

因此，对于 $q_t$，我们会希望它旋转了 $t\varphi = 2t\theta$，对应的 $q_t$ 和 $q_0$ 的夹角为 $t\theta$。这样，我们可以初步得到 Slerp 的一个实践上不好用的公式：将四元数差分 $\Delta q$ 改成 $(\Delta q)^t$

$$
q_t = (\Delta q)^tq_0 = (q_1q_0^*)^tq_0
$$

## Lerp & Nlerp

Slerp 的以上公式并不好算，我们考虑

$$
q_t = \alpha q_0 + \beta q_1
$$

最简单的插值方式就是线性插值 (**L**inear In**terp**olation, Lterp)：

$$
\mathbf{v}_t = (1-t)\mathbf{v}_0 + t\mathbf{v}_1
$$

如下图所示，$\mathbf{v}_0$、$\mathbf{v}_t$、$\mathbf{v}_1$ 的终点会位于一条直线上，$\mathbf{v}_t$ 构成 $\mathbf{v}_0$、$\mathbf{v}_1$ 的凸组合。

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/interpolation-lerp.svg" alt="interpolation-lerp" style="width: 40%;">
</div>

直接迁移，我们能得到 Lerp 插值公式：

!!! abstract "Lerp"
    $$
    q_t = t q_0 + (1-t) q_1
    $$

然而 Lerp 存在的问题是它插出来的 $q_t$ 一般不是一个单位四元数，因此进行正规化 (Normalization) 修正，得到 Nlerp (**N**ormalized **L**inear Int**erp**olation)公式：

!!! abstract "Nlerp"
    $$
    q_t = \frac{t q_0 + (1-t) q_1}{\|t q_0 + (1-t) q_1\|}
    $$

Nlerp 的问题是当需要插值的弧比较大时，$\mathbf{v}_t$ 的角速度会有明显的变化。如下图所示，$t=0$ 到 $t=0.25$ 的弧就比 $t=0.25$ 到 $t=0.5$ 的弧短很多。$0$ 到 $0.5$，角速度会逐渐增大；$0.5$ 到 $1$，角速度会逐渐减小。

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/interpolation-Nlerp-problem.svg" alt="interpolation-Nlerp-problem" style="width: 40%;">
</div>

## Slerp

球面线性插值 (**S**pherical **L**inear Int**erp**olation, Slerp) 能够保证插值的四元数是单位四元数，且角速度是恒定的。

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/interpolation-Slerp.svg" alt="interpolation-Slerp" style="width: 40%;">
</div>

我们想要把 $\mathbf{v}_t$ 表示为 $\mathbf{v}_1$ 和 $\mathbf{v}_0$ 的线性组合，即

$$
\mathbf{v}_t = \alpha \mathbf{v}_0 + \beta \mathbf{v}_1
$$

因此 $\mathbf{v}_t$, $\alpha \mathbf{v}_0$ 和 $\beta \mathbf{v}_1$ 构成一个三角形

<div style="text-align:center;">
    <img src="../../../imgs/quaternion/interpolation-Slerp-triangle.svg" alt="interpolation-Slerp-triangle" style="width: 50%;">
</div>

设 $\|\mathbf{v}_t\|= \|\mathbf{v}_1\| = \|\mathbf{v}_0\| = r$，根据正弦定理有

$$
\frac{r}{\sin \theta} = \frac{\beta r}{\sin(t\theta)} = \frac{\alpha r}{\sin((1-t)\theta)}
\Rightarrow \alpha = \frac{\sin((1-t)\theta)}{\sin\theta}, \beta = \frac{\sin(t\theta)}{\sin\theta}
$$

将 $\mathbf{v}$ 换成 $q$，可以得到 Slerp 公式：

!!! abstract "Slerp"

    $$
    q_t = \frac{\sin((1-t)\theta)}{\sin\theta}q_0 + \frac{\sin(t\theta)}{\sin\theta}q_1,\quad \theta = \cos^{-1}(q_0\cdot q_1)
    $$

在运算效率方面，这个公式会比之前利用幂运算的公式要高效很多，但是仍然涉及到三个三角函数以及一个反三角函数的运算，所以还是会比 Nlerp 要慢一点。如果要插值的角度比较小的话，Nlerp 其实相对于 Slerp 的误差并没有那么大，为了提高效率，我们经常会使用 Nlerp 来代替 Slerp。

> 也能用一些数值分析的方法来近似并优化四元数的 Slerp，可以在一些图形引擎的源代码中找到一些例子

具体实现中，我们还需要注意以下两个问题：

!!! warning "小心除零"
    除了效率问题之外，我们在实现 Slerp 时要注意，如果单位四元数之间的夹角 $\theta$ 非常小，那么 $\sin\theta$ 可能会由于浮点数的误差被近似为 0.0，从而导致除以 0 的错误。
    
    因此我们在实施 Slerp 之前，需要检查两个四元数的夹角是否过小（或者完全相同），如果过小我们就必须改用 Nlerp 对两个四元数进行插值，这时候 Nlerp 的误差非常小所以基本不会与真正的 Slerp 有什么区别。

!!! warning "双倍覆盖带来的问题"
    插值时应当寻找弧面最短路径，由于双倍覆盖的存在，如果 $q_0$ 和 $q_1$ 成钝角，那么 $q_0$ 和 $q_1$ 的 等效四元数 $-q_1$ 成锐角，更符合弧面最短路径。

    <div style="text-align:center;">
        <img src="../../../imgs/quaternion/interpolation-Slerp-double-cover.svg" alt="interpolation-Slerp-double-cover" style="width: 40%;">
    </div>

    因此，首先检查若 $q_0\cdot q_1 < 0$，则将 $q_1$ 取为 $-q_1$，再算夹角 $\theta$ 进行插值。

    > 当然，取 $q_0$ 为 $-q_0$ 也是可以的

## Squad

Slerp 虽然实现了 $q_0$ 到 $q_1$ 的固定角速度的插值，但是如果依次在 $q_0, q_1, q_2, q_3$ 之间插值，在切换点会出现角速度的突变。我们希望以**牺牲固定角速度**为条件，让插值的曲线不仅是连续的（$C^0$ 连续），其一阶甚至更高阶导数也能是连续的（$C^1$ 甚至 $C^n$ 连续）。

球面四边形插值 (**S**pherical and **quad**rangle, Squad) 是一种解决方案，据说它由 Ken Shoemake 在 1987 年提出（这篇 paper 已经找不到了）。

### 三次 Bézier 曲线

对于一系列向量 $\mathbf{v}_0, \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_n$，我们分段对 $\mathbf{v}_i, \mathbf{v}_{i+1}$ 进行插值，将会涉及三次 Bézier 曲线 (Cube Bézier Curve) 。这个算法需要生成中间的两个控制点 $\mathbf{s}_{i-(i+1)-0}$ 和 $\mathbf{s}_{i-(i+1)-1}$，这两个控制点的生成需要借助 $\mathbf{v}_{i-1}$ 和 $\mathbf{v}_{i+2}$ 的信息。

为了让曲线是 $C^1$ 的，每个中间点的两个控制点将会分列其左右两侧，而端点的控制点可以直接取其本身。这样，我们将 $\mathbf{v}_i$, $\mathbf{s}_{i-(i+1)-0}$, $\mathbf{s}_{i-(i+1)-1}$, $\mathbf{v}_{i+1}$ 重新编号为 $\mathbf{v}_0, \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$，思考从 $\mathbf{v}_0$ 到 $\mathbf{v}_3$ 的插值。

这里我们略去包括 **de Casteljau 算法**在内的推理过程，直接给出

$$
\operatorname{Bézier}(\mathbf{v}_0, \mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3; t) = (1-t)^3\mathbf{v}_0 + 3(1-t)^2t\mathbf{v}_1 + 3(1-t)t^2\mathbf{v}_2 + t^3\mathbf{v}_3
$$

将 Slerp 简写为 S，则对应的 SBézier 插值为

$$
\operatorname{SBézier}(q_0, q_1, q_2, q_3; t) = S(S(S(q_0, q_1; t), S(q_1, q_2; t); t), S(S(q_1, q_2; t), S(q_2, q_3; t); t); t)
$$

一次 Slerp 需要使用 4 次三角函数，这样两个点之间插值就需要 7 个 Slerp，性能影响过大。Squad 是对其的一种近似，这里依然省略其推导，有

!!! abstract "Squad"
    $$
    \operatorname{Squad}(q_0, q_1, q_2, q_3; t) = \operatorname{Slerp}(\operatorname{Slerp}(q_0, q_3; t), \operatorname{Slerp}(q_1, q_2; t); 2t(1-t))
    $$


可以写作指数形式，方便一些分析

$$
\operatorname{Squad}(q_0, q_1, q_2, q_3; t) = \left\{\operatorname{Slerp}(q_1, q_2; t)[\operatorname{Slerp}(q_0, q_3; t)]^*\right\}^{2t(1-t)}\operatorname{Slerp}(q_1, q_2; t)
$$

### Quad 应用

一个关键问题是如何生成控制点。我们希望 $q_{i-1}$ 和 $q_i$ 插值在 $t=1$ 处的导数，和 $q_i$ 和 $q_{i+1}$ 插值在 $t=0$ 处的导数相等。省略一系列推导，我们有

$$
s_i = q_i\exp\left(-\frac{\log(q_i^*q_{i-1}) + \log(q_i^*q_{i+1})}{4}\right)
$$

注意，和三次 Bézier 曲线不同，这里 $q_i$ 对应的控制点不管在左侧还是右侧都是 $s_i$。

与两个四元数之间的插值一样，Squad 同样会受到双重覆盖的影响。我们在计算中间控制点和插值之前，需要先选中一个四元数，比如说 $q_i$，检测它与其它三个四元数之间的夹角，如果是钝角就翻转，将插值的路线减到最小。