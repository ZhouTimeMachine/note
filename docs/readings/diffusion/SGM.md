<link rel="stylesheet" href="../../../css/counter.css" />

# Score-based Generative Models

!!! info "Reference"
	本文参考自宋飏博客 [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/)

!!! warning "该页面还在建设中"

## Energy-based & Score-based Models

### Introduction to Energy-based Models

论及生成模型，最直接也是以前普遍使用的思路就是使用基于似然的模型 (likelihood-based models)，直接建模目标数据的数据分布，然后在这个数据分布中采样就可以得到生成的新数据。基于这种想法，如果设待建模数据是一个连续型随机变量，那就可以通过建模该随机变量的概率密度函数来进行生成。

> 直接设为连续型随机变量其实包含了对世界的连续性的假设

但是直接建模概率密度函数是难以捉摸的，往往使用 Energy-based Models (EBM) 的框架进行进一步的转化与实现。EBM 是 Yann Lecun 提出的一种希望统括 ML/DL 的模型框架，它认为模型只需要建模一个能量函数 $F(x, y)$ 衡量 $x$ 和 $y$ 的相容性 (compatibility)，从能量函数出发再进一步处理就可以得到最终想要建模的概率密度函数。

能量函数（相容性度量）$F(x, y)$ 中 $x$ 是观测变量，$y$ 是待预测变量。我们希望 $y$ 尽可能地和 $x$ 相容，即能量函数 $F(x, y)$ 尽可能小。

> 举视频生成的例子，若 $x$ 是已有的视频帧，$y$ 就是待生成的视频帧

如果模型很好地学到了这个能量函数，在推断时就可以通过

$$
y^*=\mathop{\arg\min}_{y} F(x, y)
$$

得到和所给数据最相容的预测 $y$。

相容性衡量了 $y$ 出现在 $x$ 的分布中的“概率”。实践中的 EBM 事实上是使用模型，给定 $y$ 能够输出一个 $f_{\theta}(y)$，并通过

$$
p_{\theta}(x)=\frac{e^{-f_{\theta}(x)}}{Z_{\theta}}
$$

去建模实际数据 $x$ 客观的概率密度函数 $p(x)$。其中，$Z_{\theta}$ 就是一个归一化项，使得 $p_{\theta}$ 满足概率密度函数的基本要求：

$$
\int p_{\theta}(x)\mathrm d x=1
$$

因此，这里说的 EBM 也被称为未归一化的概率模型 (unnormalized probabilistic model)。

### Challenges of EBM, and Score-based Models

前面已经描述了 EBM 如何推断，那么 EBM 该如何训练？EBM 仍然在基于似然模型的框架下，所以其实也就是极大似然方法，通过最大化训练集的对数似然以训练 $p_{\theta}(x)$：

$$
\max_{\theta} \log p_{\theta}\left(\prod_{i=1}^{N}x_i\right)
=\max_{\theta} \log \prod_{i=1}^{N} p_{\theta}\left(x_i\right)
=\max_{\theta} \sum_{i=1}^N \log p_{\theta} (x_i)
$$

但在使用 $f_{\theta}$ 表示 $p_{\theta}$ 的过程中，计算 $Z_{\theta}$ 可能是困难的（对于任意的 $f_{\theta}$ 而言）。为了计算 $Z_{\theta}$ 有两种常见的妥协方式：

- 限制网络结构，如自回归 CNN 中的因果卷积 (causal convolution) 和归一化流模型 (normalizing flow models) 中的可逆网络
- 近似计算 $Z_{\theta}$，如 VAE 中的变分推断和对比散度 (contrastive divergence) 中的马尔科夫链蒙特卡洛 (Markov Chain Monte Carlo, MCMC) 采样，往往需要较高的计算量代价

> 详细可见宋飏自己写的 [How to Train Your Energy-Based Models](https://arxiv.org/abs/2101.03288)

为了避免求取 $Z_{\theta}$ 的麻烦，Score-based Model 在和基于似然的模型的同一层次上，将原本的建模 $p(x)$ 转为去建模

$$
\nabla _x \log p(x)
$$

也就是说，不同于 EBM 使用模型预测能量函数 $f(x)$（下一步准备获得 $p(x)$），Score-based Model 则是使用模型预测一个称为 score 的 $s(x)=\nabla _x \log p(x)$。我们可以建立 $s_{\theta}(x)$ 和 $f_{\theta}(x)$ 的一个关系：

$$
\begin{aligned}
	s_{\theta}(x) &= \nabla _x \log p(x)
	= \nabla _x \log\frac{e^{-f_{\theta}(x)}}{Z_{\theta}} \\
	& = -\nabla_x f_{\theta}(x) - \underbrace{\nabla_x \log Z_{\theta}}_{=0} \\
	& = -\nabla_x f_{\theta}(x)
\end{aligned}
$$

由此可知，建模 score 而不是建模概率密度函数的好处就是可以不用处理归一化项 $Z_{\theta}$。