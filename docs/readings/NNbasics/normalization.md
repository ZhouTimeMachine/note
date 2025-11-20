<link rel="stylesheet" href="../../../css/counter.css" />

# Normalization

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/normalizations.png" alt="normalizations" style="zoom: 100%;" />
</div>

## Batch Normalization

### Basic Formulation

对每个 mini batch $(z^{(1)}, \cdots, z^{(b)})$, $b$ 是 batch size。计算各个样本特征向量的均值 $\mu$ 和方差 $\sigma^2$

$$
\mu = \frac{1}{b}\sum_{i=1}^{b}z^{(i)}, \quad \sigma^2 = \frac{1}{b}\sum_{i=1}^{b}(z^{(i)}-\mu)^2
$$

随后有（为了数值稳定性引入一个很小的 $\varepsilon>0$）

$$
z^{(i)}_{\text{norm}}=\frac{z^{(i)}-\mu}{\sqrt{\sigma^2+\varepsilon}}
$$

用以替换 $z^{(i)}$ 的 $\tilde{z}^{(i)}$ 还需要对标准化得到的 $z^{(i)}_{\text{norm}}$ 进行线性(仿射)变换

$$
\tilde{z}^{(i)} = \gamma z^{(i)}_{\text{norm}} + \beta
$$

这里线性变换的参数 $\gamma$ 和 $\beta$ 也相当于网络参数 $w$，参与前向传播和反向传播的参数更新过程。线性变换的意义在于让每层的直接输出的分布更加多元化，而不总是被标准化所限制。

于是，使用了 Batch Normalization 之后，只是把某一层的直接输出 $z^{(i)}$ 替换为 $\tilde{z}^{(i)}$，然后再应用激活函数后得到 $a^{(i)}$，再输入下一层。

!!! tips "Remark"
    - 有趣的是，每一层的偏置项 (bias) 和 $\beta$ 是重复的，所以可以去掉偏置项。
    - 先 BN 还是先应用激活函数是一个问题，吴恩达认为经常先 BN 再使用激活函数。

### Implementation in PyTorch

PyTorch 中，`torch.nn.BatchNorm1d`、`torch.nn.BatchNorm2d` 和 `torch.nn.BatchNorm3d` 分别用于一维、二维和三维数据的 Batch Normalization，它们都继承自 `_BatchNorm`。代码和数学公式的映射为：

- `self.weight`: $\gamma$，可学习参数
- `self.bias`: $\beta$，可学习参数
- `self.eps`: $\varepsilon$，数值稳定性参数

如果直接在 mini batch 内部计算均值 $\mu_b$ 和方差 $\sigma^2_b$，那么就可以直接计算了，但实际上经常会维护一个全局均值估计 $\mu_g$ 和全局方差估计 $\sigma^2_g$，通过动量 (momentum) $p$ 来持续更新，描述尽可能多的样本的均值和方差：

$$
\begin{aligned}
\mu_g &\leftarrow (1-p)\mu_g + p\mu_b \\
\sigma^2_g &\leftarrow (1-p)\sigma^2_g + p\sigma^2_b\cdot \frac{b}{b-1}
\end{aligned}
$$

> 这里方差的更新中多乘了一个 $\frac{b}{b-1}$，是因为在 mini batch 内计算的方差是有偏估计 (biased estimate)，而全局方差需要无偏估计 (unbiased estimate)，因此需要进行贝塞尔校正 (Bessel's correction)

对应的代码和数学公式映射为

- `self.running_mean`: $\mu_g$，全局均值估计
- `self.running_var`: $\sigma^2_g$，全局方差估计
- `self.momentum`: $p$，动量参数

下面展示一下 `_BatchNorm` 的关键代码。为了简化代码，我们默认同时启用 `affine=True` 和 `track_running_stats=True`，即学习 $\gamma$ 和 $\beta$，并且用动量维护全局均值和方差估计。

- 训练时，动量默认选用 $1.0 / B$，$B$ 是已经处理过的 mini batch 数量。如果手动指定了动量 `momentum`，则使用指定的动量。
- 推理时，动量不再有作用。

```python
class _BatchNorm(_NormBase):
    def __init__(
        self,
        num_features: int,
        eps: float = 1e-5,
        momentum: Optional[float] = 0.1,
        ...
    ) -> None:
        ...

    def forward(self, input: Tensor) -> Tensor:
        self._check_input_dim(input)

        exponential_average_factor = self.momentum
        if self.training:  # when training, and tracking mu and sigma^2
            if self.num_batches_tracked is not None:  # type: ignore[has-type]
                self.num_batches_tracked.add_(1)  # type: ignore[has-type]
                if self.momentum is None:  # use cumulative moving average
                    exponential_average_factor = 1.0 / float(self.num_batches_tracked)
                else:  # use exponential moving average
                    exponential_average_factor = self.momentum

        return F.batch_norm(
            input,
            self.running_mean if not self.training else None,
            self.running_var if not self.training else None,
            self.weight,
            self.bias,
            self.training,
            exponential_average_factor,
            self.eps,
        )
```

## Layer Normalization

### Basic Formulation

Layer Normalization 和 Batch Normalization 的关键区别在于 $\mu$ 和 $\sigma^2$ 的计算方法。 Batch Normalization 是沿着 mini batch 这一维（样本维度）计算均值 $\mu$ 和方差 $\sigma^2$，而 Layer Normalization 则是单个样本内部进行 $\mu$ 和 $\sigma^2$ 的计算。

可以从下图简单看到计算维度的差别：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/bn_vs_ln.png" alt="bn_vs_ln" style="zoom: 100%;" />
</div>

!!! tip "因此，LayerNorm 在实现上比 BatchNorm 更简单，BatchNorm 会考虑全局均值/方差估计的问题，而 LayerNorm 则始终在样本内部计算均值和方差。"

设样本维度为 $d$，对于二维情况，就是 $d=h\times w$，这样就有

$$
\mu = \frac{1}{d}\sum_{j=1}^{d}z_{j}, \quad \sigma^2 = \frac{1}{d}\sum_{j=1}^{d}(z_{j}-\mu)^2
$$

### Implementation in PyTorch

PyTorch 中，LayerNorm 代码和数学公式的映射为：

- `self.weight`: $\gamma$，可学习参数
- `self.bias`: $\beta$，可学习参数
- `self.eps`: $\varepsilon$，数值稳定性参数

同样，我们默认启用 `self.weight` 和 `self.bias`，即 `elementwise_affine=True` 且 `bias=True`，会发现把底层实现丢给 Functional 之后，代码变得非常简洁：

```python
class LayerNorm(Module):
    __constants__ = ["normalized_shape", "eps", ...]
    normalized_shape: Tuple[int, ...]
    eps: float
    ...

    def __init__(
        self,
        normalized_shape: _shape_t,
        eps: float = 1e-5,
        ...
    ) -> None:
        ...
        self.weight = Parameter(torch.empty(self.normalized_shape))
        self.bias = Parameter(torch.empty(self.normalized_shape))

        self.reset_parameters()

    def reset_parameters(self) -> None:
        init.ones_(self.weight)
        init.zeros_(self.bias)

    def forward(self, input: Tensor) -> Tensor:
        return F.layer_norm(
            input, self.normalized_shape, self.weight, self.bias, self.eps
        )
```

!!! note "Instance Normalization 和 Group Normalization 略，相对不太常用，基本思想看图即可。"

## Root Mean Square Layer Normalization (RMSNorm)

RMSNorm 是对 LayerNorm 的一个简化，即不再计算均值 $\mu$ 进行中心化。

> 如果样本的均值为 0，则 RMSNorm 和 LayerNorm 的表现是一样的。

RMSNorm 相比 LayerNorm 在内存占用上更节省，计算效率也更高，但可能模型表现会较差一些。比较闻名的，[LLaMA](https://github.com/meta-llama/llama/blob/main/llama/model.py#L34-L77) 就使用了 RMSNorm：

```python
class RMSNorm(torch.nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        output = self._norm(x.float()).type_as(x)
        return output * self.weight
```

## Adaptive Layer Normalization (AdaLN)

DiT (Diffusion Transformer) 的基本块大量使用了 AdaLN (Adaptive Layer Normalization)。根据 DiT 论文，AdaLN 的基本思想之前在 FiLM 中提出，是一种有效的让条件嵌入 $c$ 调制网络主干输出 $x$ 的方式：

$$
FiLM(F_{i,c}\mid \gamma_{i,c}, \beta_{i,c}) = \gamma_{i,c}F_{i,c} + \beta_{i,c}
$$

其中 $\gamma_{i,c}=f_c(x_i)$, $\beta_{i,c}=h_c(x_i)$。

> - [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748), ICCV 2022
> - [FiLM: Visual Reasoning with a General Conditioning Layer](https://arxiv.org/abs/1709.07871), AAAI 2018

### Prototype in U-Net

在 FiLM 中，$\gamma$ 和 $\beta$ 直接作为可学习参数，至少在 ADM 的时候，[代码](https://github.com/openai/guided-diffusion/blob/22e0df8183507e13a7813f8d38d51b072ca1e67c/guided_diffusion/unet.py#L250-L251)中就已经出现了利用条件嵌入通过激活函数和线性层后回归生成 $\gamma$ 和 $\beta$ 的做法，尽管当时的网络结构还是 U-Net：

> ADM: [Diffusion Models Beat GANs on Image Synthesis](https://arxiv.org/abs/2105.05233), NeurIPS 2021

```python hl_lines="37 38"
class ResBlock(TimestepBlock):
    def __init__(
        self,
        channels,
        emb_channels,
        dropout,
        out_channels=None,
        use_scale_shift_norm=False,
        dims=2,
        ...
    ):
        ...
        self.emb_layers = nn.Sequential(
            nn.SiLU(),
            linear(
                emb_channels,
                2 * self.out_channels if use_scale_shift_norm else self.out_channels,
            ),
        )
        self.out_layers = nn.Sequential(
            normalization(self.out_channels),
            nn.SiLU(),
            nn.Dropout(p=dropout),
            zero_module(
                conv_nd(dims, self.out_channels, self.out_channels, 3, padding=1)
            ),
        )
        ...

    def _forward(self, x, emb):
        ...
        emb_out = self.emb_layers(emb).type(h.dtype)
        while len(emb_out.shape) < len(h.shape):
            emb_out = emb_out[..., None]
        if self.use_scale_shift_norm:
            out_norm, out_rest = self.out_layers[0], self.out_layers[1:]
            scale, shift = th.chunk(emb_out, 2, dim=1)
            h = out_norm(h) * (1 + scale) + shift
            h = out_rest(h)
        else:
            h = h + emb_out
            h = self.out_layers(h)
        return self.skip_connection(x) + h
```

可见 modulate 的基本形式就是 

$$
\mathrm{modulate}(x, \beta, \gamma) = x \cdot (1 + \gamma) + \beta
$$

### AdaLN in DiT

- 不同于 U-Net 中只对 `out_norm` 进行调制，DiT 中对注意力层 (Multi-head Self Attention, MSA)和 MLP 层的输入都进行了调制，因此需要两份 $\gamma, \beta$
- 引入了门控机制 (gating mechanism) 进一步调制，又需要两份 gate，一共需要六份调制参数
- 输入的条件 $c=t+y$
- 最终形成的 [DiT Block 代码](https://github.com/facebookresearch/DiT/blob/ed81ce2229091fd4ecc9a223645f95cf379d582b/models.py#L101-L122)就如下所示

```python
def modulate(x, shift, scale):
    return x * (1 + scale.unsqueeze(1)) + shift.unsqueeze(1)

class DiTBlock(nn.Module):
    """
    A DiT block with adaptive layer norm zero (adaLN-Zero) conditioning.
    """
    def __init__(self, hidden_size, num_heads, mlp_ratio=4.0, **block_kwargs):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_size, elementwise_affine=False, eps=1e-6)
        self.attn = Attention(hidden_size, num_heads=num_heads, qkv_bias=True, **block_kwargs)
        self.norm2 = nn.LayerNorm(hidden_size, elementwise_affine=False, eps=1e-6)
        mlp_hidden_dim = int(hidden_size * mlp_ratio)
        approx_gelu = lambda: nn.GELU(approximate="tanh")
        self.mlp = Mlp(in_features=hidden_size, hidden_features=mlp_hidden_dim, act_layer=approx_gelu, drop=0)
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(hidden_size, 6 * hidden_size, bias=True)
        )

    def forward(self, x, c):
        shift_msa, scale_msa, gate_msa, shift_mlp, scale_mlp, gate_mlp = self.adaLN_modulation(c).chunk(6, dim=1)
        x = x + gate_msa.unsqueeze(1) * self.attn(
            modulate(self.norm1(x), shift_msa, scale_msa)
        )
        x = x + gate_mlp.unsqueeze(1) * self.mlp(
            modulate(self.norm2(x), shift_mlp, scale_mlp)
        )
        return x
```

!!! note "Remark"
    - AdaLN 称为 Adaptive LN，是因为 $\gamma$ 和 $\beta$ 从直接的可学习参数变成了从条件嵌入回归生成的参数，注意到代码中 LayerNorm 的 `elementwise_affine=False`，即是不包括 $\gamma$ 和 $\beta$ 的
    - DiT 对 AdaLN 进行了[零初始化](https://github.com/facebookresearch/DiT/blob/ed81ce2229091fd4ecc9a223645f95cf379d582b/models.py#L208-L210)，论文中称为 AdaLN-Zero，即把最后一层线性层的权重和偏置都初始化为零，这样一开始网络的行为就和没有 AdaLN 一样，避免一开始训练不稳定的问题