<link rel="stylesheet" href="../../../css/counter.css" />

# Guidance

!!! info "References"
    [Understanding Diffusion Models: A Unified Perspective](http://arxiv.org/abs/2208.11970)

我们前面都在讨论对 $p(x)$ 的建模，但仅仅基于此的生成是无条件的、不可控的。为了实现可控的条件生成，我们需要对 $p(x\mid y)$ 进行建模。条件引导 (Conditional Guidance) 提供了条件 $y$ 嵌入 $x$ 生成的方式，牺牲生成多样性、控制样本向条件靠拢。

## Classifier & Classifier-Free Guidance

Classifier Guidance 和 Classifier-Free Guidance (CFG) 是谈论 Diffusion Guidance 时绕不开的两种基础条件引导方式。

### Classifier Guidance

我们考虑

$$
\begin{aligned}
    \nabla _{x_t} \log p(x_t\mid y)
    &= \nabla _{x_t} \log\left(
        \frac {p(y\mid x_t)p(x_t)} {p(y)}
    \right) & (\text{Bayes rule})\\
    &= \underbrace{
        \nabla _{x_t} \log p(x_t)
    }_{\text{unconditioned score}}
    + \underbrace{
        \nabla _{x_t} \log p(y\mid x_t)
    }_{\text{adversarial gradient}}
    & (\nabla _{x_t} \log p(y) = 0)\\
\end{aligned}
$$

> 为了细粒度控制条件强度，可以令 $\nabla _{x_t} \log p(x_t\mid y) = \nabla _{x_t} \log p(x_t) + \gamma \nabla _{x_t} \log p(y\mid x_t)$，其中 $\gamma$ 是一个超参数。

按照这种 guidance 方案，我们训练的时候要同时训练无条件生成模型 $p(x_t)$ 和条件分类器 (classifier) $p(y\mid x_t)$。这种方式对 classifier 的依赖很重，classifier 必须要能处理任意噪声输入，现在已经不是主流的 guidance 方式了。

### Classifier-Free Guidance

Classifier-Free Guidance (CFG) 是当前最常用的条件引导方式，在我们前面强加了 $\gamma$ 控制条件引导强度的基础上

$$
\nabla _{x_t} \log p(x_t\mid y) = \nabla _{x_t} \log p(x_t) + \gamma \nabla _{x_t} \log p(y\mid x_t)
$$

我们再把 $\nabla _{x_t} \log p(y\mid x_t)= \nabla _{x_t} \log p(x_t\mid y) - \nabla_{x_t} \log p(x_t)$ 回代回去：

$$
\begin{aligned}
    \nabla _{x_t} \log p(x_t\mid y)
    &= \nabla _{x_t} \log p(x_t) + \gamma (\nabla _{x_t} \log p(x_t\mid y) - \nabla_{x_t} \log p(x_t)) \\
    &= (1-\gamma) \nabla _{x_t} \log p(x_t) + \gamma \nabla _{x_t} \log p(x_t\mid y) \\
\end{aligned}
$$

即，条件生成的 score 可以通过无条件生成的 score 和条件生成的 score 的线性组合得到。

- 只需要训练无条件生成模型 $p(x_t)$ 和条件生成模型 $p(x_t\mid y)$，而不需要训练分类器 $p(y\mid x_t)$
- 实践中，无条件生成模型一般直接处理为 $p(x_t \mid \empty)$
- 训练时既看到无条件的 sample，也看到带条件的 sample，按比例混合

!!! abstract "Classifier & Classifier-Free Guidance"
    - **Classifier Guidance**: 训练无条件生成模型 $p(x_t)$ 和条件分类器 $p(y\mid x_t)$，依赖于分类器的能力。

    $$
    \nabla _{x_t} \log p(x_t\mid y) = \nabla _{x_t} \log p(x_t) + \gamma\nabla_{x_t} \log p(y\mid x_t)
    $$

    - **Classifier-Free Guidance**: 训练无条件生成模型 $p(x_t)$ 和条件生成模型 $p(x_t\mid y)$，通过线性组合得到条件生成的 score，当前主流方式。

    $$
    \nabla _{x_t} \log p(x_t\mid y) = (1-\gamma) \nabla _{x_t} \log p(x_t) + \gamma \nabla_{x_t} \log p(x_t\mid y)
    $$

> SD2.1 T2I 推理常用 $w_{CFG}=7.5$，即 $1-\gamma=-6.5$，$\gamma=7.5$，向条件生成的外侧较远处进行了外插

## Guidance in Practice

### Text & Image joint as Condition

> Reference: [InstructPix2Pix: Learning to Follow Image Editing Instructions](https://arxiv.org/abs/2211.09800), CVPR2023 Highlight

图像编辑场景下，针对文本 $c_T$ 和图像 $c_I$ 两个模态的条件，进行了特殊的 CFG 设计：

$$
\begin{aligned}
    \tilde{\varepsilon}_{\theta}(z_t, c_I, c_T)
    =& \varepsilon_{\theta}(z_t, \emptyset, \emptyset) \\
    &+ s_I \cdot (\varepsilon_{\theta}(z_t, c_I, \emptyset) - \varepsilon_{\theta}(z_t, \emptyset, \emptyset)) \\
    &+ s_T \cdot (\varepsilon_{\theta}(z_t, c_I, c_T) - \varepsilon_{\theta}(z_t, c_I, \emptyset)) \\
\end{aligned}
$$

- 至少需要训练 $\varepsilon_{\theta}(z_t, \emptyset, \emptyset)$、$\varepsilon_{\theta}(z_t, c_I, \emptyset)$、$\varepsilon_{\theta}(z_t, c_I, c_T)$ 三种情形
- 训练过程中，作者随机设置
    - $\varepsilon_{\theta}(z_t, \emptyset, c_T)$: only $c_I=\emptyset$ for 5% of examples
    - $\varepsilon_{\theta}(z_t, c_I, \emptyset)$: only $c_T=\emptyset$ for 5% of examples
    - $\varepsilon_{\theta}(z_t, \emptyset, \emptyset)$: both $c_I=\emptyset$ and $c_T=\emptyset$ for 5% of examples.
    - (85% both not empty)
- 代码中，默认有$s_I=1.5$, $s_T=7.5$

### History Guidance for Video Generation

> [History-Guided Video Diffusion](http://arxiv.org/abs/2502.06764), ICML2025

<figure style="text-align:center;">
    <img src="../../imgs/diffusion/history-guidance-light.png#only-light" alt="history-guidance-light" style="zoom:100%;" />
    <img src="../../imgs/diffusion/history-guidance-dark.png#only-dark" alt="history-guidance-dark" style="zoom:100%;" />
    <figcaption><small>
        Sampling with Diffusion Forcing Transformer (DFoT) and History Guidance.
    </small></figcaption>
</figure>

> A DFoT can be used to estimate scores conditioned on differently masked histories using noise as masking. This includes clean (full history), fully masked (unconditional), subset masked (shorter history), or partially masked (low-frequency history). These scores can be composed when sampling to obtain a family of History Guidance methods.

按照视频扩散模型 (video diffusion model) 目前的设计，单次对特定长度的视频 latent 去噪，能单次直接生成的视频长度是有限的。想要生成长视频，就需要在前面生成的视频序列的基础上“续写”，此时原来已经生成的视频序列可以认为是 history，在 history 的引导下进行生成——此时 history 也可以视为一种 conditional guidance，也可以直接应用 CFG。

- 令 $x_{\mathcal{T}}$ 代表 $T$ 帧的视频片段
- 各帧下标为 $\mathcal{T} = \{1, 2, \cdots , T \}$
- 历史帧下标 $\mathcal{H} \subset \mathcal{T}$，待生成的帧下标 $\mathcal{G} = \mathcal{T} \setminus \mathcal{H}$

提出了 Vanilla, Temporal 和 Fractional 三种 History Guidance 形式，并表示即使是最平凡的 Vanilla HG 也能提升

#### Vanilla History Guidance (HG-v)

$$
    \nabla \log p_k(x_{\mathcal{G}}^k) + \omega[\nabla\log p_k(x_{\mathcal{G}}^k\mid x_{\mathcal{H}}) - \nabla\log p_k(x_{\mathcal{G}}^k)]
$$

即原始 CFG 的平凡扩展，$k$ 代表第 $k$ 次推理，和原始的区别在于：

1. $x_{\mathcal{H}}, x_{\mathcal{G}}$ 都属于 $x_{\mathcal{T}}$。进一步地，$k$ 的 $x_{\mathcal{G}}$ 可以作为 $k+1$ 的 $x_{\mathcal{H}}$，从而能够生成长视频
2. $\mathcal{H}$ 可以是 $\mathcal{T}$ 的任意子集，因此可以历史帧可以变长、可以在所有帧中零散分布

#### History Guidance across Time and Frequency

$$
    \nabla \log p_k(x_{\mathcal{G}}^k) + \sum_{i}\omega_{i}[\nabla\log p_k(x_{\mathcal{G}}^k\mid x_{\mathcal{H_i}}^{k_{\mathcal{H_i}}}) - \nabla\log p_k(x_{\mathcal{G}}^k)]
$$

#### Temporal History Guidance (HG-t)

令 $k_{\mathcal{H_i}}=0$，则得到 Temporal History Guidance。

$$
    \nabla \log p_k(x_{\mathcal{G}}^k) + \sum_{i}\omega_{i}[\nabla\log p_k(x_{\mathcal{G}}^k\mid x_{\mathcal{H_i}}^{k_{\mathcal{H_i}}}) - \nabla\log p_k(x_{\mathcal{G}}^k)]
$$
