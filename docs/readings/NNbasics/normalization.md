<link rel="stylesheet" href="../../../css/counter.css" />

# Normalization

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/normalizations.png" alt="normalizations" style="zoom: 100%;" />
</div>

## Batch Normalization

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

> 有趣的是，每一层的偏置项 (bias) 和 $\beta$ 是重复的，所以可以去掉偏置项。

于是，使用了 Batch Normalization 之后，只是把某一层的直接输出 $z^{(i)}$ 替换为 $\tilde{z}^{(i)}$，然后再应用激活函数后得到 $a^{(i)}$，再输入下一层。

> 这里先 BN 还是先应用激活函数是一个问题，吴恩达认为经常先 BN 再使用激活函数。

## Layer Normalization

Layer Normalization 和 Batch Normalization 的不同之处只在于 $\mu$ 和 $\sigma^2$ 的计算方法。 Batch Normalization 是沿着 mini batch 这一维计算均值 $\mu$ 和方差 $\sigma^2$，而 Layer Normalization 则是单个样本内部进行 $\mu$ 和 $\sigma^2$ 的计算。

!!! warning "该页面还在建设中"

$$
\mu = \frac{1}{b}\sum_{i=1}^{b}z^{(i)}, \quad \sigma^2 = \frac{1}{b}\sum_{i=1}^{b}(z^{(i)}-\mu)^2
$$

可以从下图简单看到计算维度的差别：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/bn_vs_ln.png" alt="bn_vs_ln" style="zoom: 100%;" />
</div>

将 Batch Normalization 和 Layer Normalization 举例如下：

\begin{figure}[H]
    \centering
    \includegraphics[scale=0.4]{graph/6.2.png}
    \includegraphics[scale=0.4]{graph/6.3.png}
    \caption{examples of Batch Normalization(left) and Layer Normalization(right)}
\end{figure}

## Instance Normalization

## Group Normalization