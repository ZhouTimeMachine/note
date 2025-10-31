<link rel="stylesheet" href="../../../css/counter.css" />

# Mean Flow

!!! info "References"
    [Mean Flows for One-step Generative Modeling](http://arxiv.org/abs/2505.13447)

## Main Idea

为了解决源分布 $p_1$（往往是标准高斯分布）到目标分布 $p_0$（往往是目标数据分布）的转移问题，flow matching 旨在建模一个瞬时速度场 $v(z_t, t)$，使得 $z_1\sim p_1$ 通过解如下 ODE 可以得到 $z_0\sim p_0$：

$$
    \frac{\mathrm{d}}{\mathrm{d}t} z_t = v(z_t, t)\\
$$

为了能够单步生成，Mean Flow 的基本思想很简单：建模平均速度 $u(z_t, r, t)$，使得有

$$
z_t = z_r + (t - r)\cdot u(z_t, r, t) 
$$

这样就可以通过 $u(z_1, 0, 1)$ 从 $z_1$ 得到 $z_0$，注意到实际上就有

$$
    u(z_t, r, t) = \frac{1}{t - r} \int_r^t v(z_{\tau}, \tau) \, \mathrm{d}\tau
$$

<figure style="text-align:center;">
    <img src="../../imgs/diffusion/mean-flow-overview-light.png#only-light" alt="mean-flow-overview-light" style="zoom:40%;" />
    <img src="../../imgs/diffusion/mean-flow-overview-dark.png#only-dark" alt="mean-flow-overview-dark" style="zoom:40%;" />
    <figcaption><small>
        Illustration of Mean Flow. Average velocity u is an integration of the instantaneous velocity v over time. In fact, u is the direction straight from source to target.
    </small></figcaption>
</figure>

## MeanFlow Properties

<figure style="text-align:center;">
    <img src="../../imgs/diffusion/mean-flow-mean-with-t-light.png#only-light" alt="mean-flow-mean-with-t-light" style="zoom:50%;" />
    <img src="../../imgs/diffusion/mean-flow-mean-with-t-dark.png#only-dark" alt="mean-flow-mean-with-t-dark" style="zoom:50%;" />
</figure>

### Consistency

[Consistency Model](http://arxiv.org/abs/2303.01469) 在概率流 ODE 的轨迹解 $\{x_t\}_{t\in[0, 1]}$ 上定义了一致性函数 (consistency function) $f(x_t, t)$，要求其具有自一致性 (self-consistency) 的条件：

$$
f(x_t, t) = f(x_{t'}, t'), \quad \forall\, t, t' \in [0, 1]
$$

Consistency Model 中所建模的 $f_{\theta}(x_t, t)$ 要求有 $f_{\theta}(x_t, t)\equiv x_0$。

<figure style="text-align:center;">
    <img src="../../imgs/diffusion/mean-flow-consistency-model-light.png#only-light" alt="mean-flow-consistency-model-light" style="zoom:20%;" />
    <img src="../../imgs/diffusion/mean-flow-consistency-model-dark.png#only-dark" alt="mean-flow-consistency-model-dark" style="zoom:20%;" />
    <figcaption><small>
        Illustration of Consistency Model.
        <a href="http://arxiv.org/abs/2303.01469">Image Source</a>
    </small></figcaption>
</figure>

我们会发现，建模的平均速度 $u(z_t, r, t)$ 也具有很相似的一致性性质，即

$$
(t - r)\cdot u(z_t, r, t) = (s - r)\cdot u(z_s, r, s) + (t - s)\cdot u(z_t, s, t), \quad \forall\, 0\leqslant r\leqslant s\leqslant t \leqslant 1
$$

这个一致性等式是通过积分可加性，在建模时就定义好的，实际上并不作为学习的目标；但如果学得比较好的话，应当是要满足这个一致性等式的。

### MeanFlow Identity

接下来的推导将是 Mean Flow 训练的关键。

$$
(t - r)\cdot u(z_t, r, t) = \int_r^t v(z_{\tau}, \tau) \, \mathrm{d}\tau
$$

对于上式，考虑 $r$ 与 $t$ 无关，则两边对 $t$ 求导有

$$
u(z_t, r, t) + (t - r) \frac{\mathrm{d}}{\mathrm{d}t} u(z_t, r, t)  = v(z_t, t)
$$

> 如果 $r$ 与 $t$ 有关，则右边会多出一个 $-v(z_r, r)\frac{\mathrm{d}r}{\mathrm{d}t}$ 的项。

由此我们就得到了用于获得 $u(z_t, r, t)$ 训练时监督信号的 MeanFlow Identity：

$$
\boxed{
u(z_t, r, t) = v(z_t, t) - (t - r) \frac{\mathrm{d}}{\mathrm{d}t} u(z_t, r, t)
}
$$

## Algorithm

### Training

我们对 $u(z_t, r, t)$ 进行建模，利用 MeanFlow Identity 获得监督信号。注意到现有 Flow Matching 的实践算法一般会预先定义好轨迹簇，例如 Rectified Flow 直接使用直线轨迹，那么 $v(z_t, t)$ 在给定 $r, t$ 以及 $z_t$ 的采样时是已知的。所以关键问题就是如何给出 $\mathrm{d}u(z_t, r, t)/\mathrm{d}t$ 的监督信号，我们直接有

$$
\frac{\mathrm{d}}{\mathrm{d}t} u(z_t, r, t) = \frac{\mathrm{d}z_t}{\mathrm{d}t} \partial_{z_t} u + \frac{\mathrm{d}r}{\mathrm{d}t} \partial_r u + 1\cdot \partial_t u
$$

依然考虑与 $t$ 无关的 $r$，且注意到其实有 $\mathrm{d}z_t/\mathrm{d}t = v(z_t, t)$，那么就有

$$
\boxed{
\frac{\mathrm{d}}{\mathrm{d}t} u(z_t, r, t) = v(z_t, t)\partial_{z_t} u + \partial_t u
}
$$

实践中，可以直接用 Jacobian-vector product（JVP，在 `torch` 和 `jax` 中已经有了成熟的实现）来计算这个全导数，即

$$
\frac{\mathrm{d}}{\mathrm{d}t} u(z_t, r, t) = [\partial_{z_t} u, \partial_r u, \partial_t u] \cdot [v(z_t, t), 0, 1]^{\top}
$$

> 即计算 Jacobian matrix 和 vector 的向量内积

但是实现细节上，JVP 的结果同样是可以被梯度追踪的，如果同时允许其梯度反向传播有可能会导致显存爆炸、梯度混乱等问题，因此 Mean Flow 利用了 Stop Gradient 算子 $\operatorname{sg}$ 阻止梯度通过 JVP 反向传播：

$$
\min_{\theta}\mathbb{E} \| u_{\theta}(z_t, r, t) - \operatorname{sg}(u_{\mathrm{trg}}) \|^2,\quad u_{\mathrm{trg}} = v(z_t, t) - (t - r) \cdot \frac{\mathrm{d}}{\mathrm{d}t} u(z_t, r, t)
$$

### Sampling

前面已经提到，单步生成可以通过

$$
z_0 = z_1 - u(z_1, 0, 1)
$$

实现，如果希望利用多步提高生存质量，也可以

$$
z_r = z_t - (t - r)\cdot u(z_t, r, t)
$$

在给定的 scheduling 下进行多步迭代生成。