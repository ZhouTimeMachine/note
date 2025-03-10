<link rel="stylesheet" href="../../../css/counter.css" />

# LSTM & GRU

!!! info "References"
    [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/), 本篇中的图直接取自这篇博客

## Notations

- $x_t$: input
- $h_t$: hidden state (short-term memory)
- $c_t$: cell state (long-term memory)

$x_t$ 和 $h_t$ 已经是 RNN 中的基本概念了，回顾 RNN 的结构：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/RNN-unrolled.png" alt="RNN-unrolled" style="zoom: 50%;background-color: white" />
</div>

但是 RNN 存在 hidden state 难以捕捉长时序依赖的缺陷，因此 $h_t$ 被解释为短时记忆；LSTM 在 $h_t$ 的基础上引入 $c_t$ 作为长时记忆，使得网络能够同时捕捉长短时记忆。

## Long-Short Term Memory (LSTM)

首先从一个简单的例子解释长时记忆的必要性：

> 进入教育界是 yhwu_is 的理想，尽管遇到了许多挫折，但他还是实现理想成为了一位<del>教授</del>。Frightenedfox 则喜欢创业，我们劝他进入教育界，但他最后还是回归初心成为了一位<del>企业家</del>。

- 删除线所删除的“教授”和“企业家”是希望语言模型能够根据前文猜出来的，显然要猜出这两个词分别**需要**“教育界”“理想”“喜欢创业”这些在填空处前方**较长时序的上文**
- 在猜测“企业家”时，既要避免“教育界”“理想”这些**原有无关长时信息的遗留**，也要继续避免“劝他进入教育界”这样的**短时信息的干扰**

因此可见 LSTM 引入长时记忆是必要的，而 LSTM 在处理每个词的时候，对长时记忆 (cell state) 的处理思路是 **先遗忘**已经价值不高的长时信息，**再更新**新的有价值的信息，其中遗忘和更新都需要一个**价值评估**。

### Gate

为了进行“价值评估”，引入了一种门 (gate) 结构：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-gate.png" alt="LSTM3-gate" style="zoom: 50%;background-color: white" />
</div>

$\sigma$ 常取 Sigmoid 激活函数，因此其输出倾向于 0 或 1，起到一个门控信号的作用（保持原信号或变为 0）。注意，在 LSTM 中采用了 $\sigma$ 和 tanh 两种激活函数，前者用于门控信号，后者用于数据信息。

LSTM 中有三大门控信号：

- **遗忘门 (forget gate)**: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$，控制 cell state 的遗忘
- **输入门 (input gate)**: $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$，控制 cell state 的更新
- **输出门 (output gate)**: $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$，控制 cell state 经 tanh 变换后到最后的输出（既作为输出，也作为新的 hidden state）

### Cell State

首先通过长时记忆这一让 LSTM 区别于 RNN 的 memory 结构 (cell state)，介绍遗忘门和输入门的作用机制。

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-C-line.png" alt="LSTM3-C-line" style="zoom: 50%;background-color: white" />
</div>

可见从 $c_{t-1}$ 到 $c_t$，首先进行了一次门控乘法（遗忘门），然后进行了一次加法更新（来自输入门的更新信号）

- RNN 将网络输出的一部分**直接作为 hidden state**，因此只能储存短时信息
- LSTM 仅将此时网络输出的一部分作为 **cell state 的加法更新量**，因此长时信息有机会在 cell state 中保留
- 输入门的存在使这个**更新量可以是 0**，因此在机器学习的过程中它能够逐渐对抗短时上文的干扰

### Forget Gate

无论遗忘门、输入门还是输出门，都是将 $h_{t-1}$ 和 $x_t$ 拼接输出一层线性层，然后再应用激活函数。

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-focus-f.png" alt="LSTM3-focus-f" style="zoom: 50%;background-color: white" />
</div>

遗忘门的输出 $f_t$ 是 $c_{t-1}$ 首先受到的控制，用几乎 0/1 的信号控制截断和保留。如果 $c_{t-1}$ 被保留，说明遗忘门认为之前的长时记忆仍有价值，反之则进行遗忘。

> 在前面的例子中，在处理第一句话时，关于“教育界”“理想”的长时记忆应该保留，直到用于预测“教授”；到处理第二句话的时候就应该逐渐被遗忘门遗忘了，处理到“喜欢创业”时让遗忘门首先截断“教育界”“理想”的长时记忆，然后让输入门将“喜欢创业”的信息输入到长时记忆，并在后续的处理中保留，直到用于预测“企业家”

### Input Gate

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-focus-i.png" alt="LSTM3-focus-i" style="zoom: 50%;background-color: white" />
</div>

将 $x_t$ 和 $h_{t-1}$ 拼接后过线性层、tanh 得到数据信息 $\tilde{c}_t$（注意，tanh 说明我们希望它是一个数据信息而不是一个门控信号），同时与遗忘门完全类似地得到输入门控信息 $i_t$，在 $i_t$ 的控制下 $\tilde{c}_t$ 被保留或截断，然后作为 $c_t$ 的更新。如果 $\tilde{c}_t$ 被保留，说明捕捉到了有价值的信息需要进入长时记忆，反之则说明当前输入不是关键词，可以跳过（例如一些带信息极少的语助词）。

> 在前面的例子中，“教育界”“理想”“喜欢创业”是预测“教授”“企业家”所需要的关键词，因此在处理到这些词的时候需要输入门给出 1 的信号让长时记忆保留，处理到其他无关的词时给出 0 的信号让长时记忆不受影响，这样就能让长时记忆存且仅存储关键词。

### Output Gate

回顾前面的过程，经过遗忘门对原先长时记忆 ($c_{t-1}$) 的过滤和输入门控制的短时信息 ($\tilde{c}_t$) 的更新，可以得到新的长时记忆 $c_t$:

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-focus-C.png" alt="LSTM3-focus-C" style="zoom: 50%;background-color: white" />
</div>

但长时记忆 cell state 并不直接作为输出，而且下一时刻的 $h_t$ 的值也需要确定，其处理就是将长时记忆经过 tanh 转化为数据信息，然后使用输出门控制输出：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-focus-o.png" alt="LSTM3-focus-o" style="zoom: 50%;background-color: white" />
</div>

此时的输出就是 $h_t$，也可以再接一下 Softmax 用于得到分类结果 $y_t$ 等等。

### Compared with RNN

将 RNN 也用这种风格的图表示，会是如下图所示：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-SimpleRNN.png" alt="LSTM3-SimpleRNN" style="zoom: 50%;background-color: white" />
</div>

而 LSTM 的结构则是：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-chain.png" alt="LSTM3-chain" style="zoom: 50%;background-color: white" />
</div>

由此可以观察到，关键的变化就是 cell state 长时记忆的存在，以及遗忘门、输入门、输出门的引入。

## Gated Recurrent Unit (GRU)

### LSTM Variants

添加 "peephole connections", 即门控信号的生成能看到 cell state 的信息，如下图所示：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-var-peepholes.png" alt="LSTM3-var-peepholes" style="zoom: 50%;background-color: white" />
</div>

还有一种简单的变体是将遗忘门和输入门合并为一个更新门，想法很简单，要么遗忘要么更新，给两个门控信号添加 $f_t + i_t = 1$ 的约束，如下图所示：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-var-tied.png" alt="LSTM3-var-tied" style="zoom: 50%;background-color: white" />
</div>

### GRU Structure

GRU 是 LSTM 最流行的变体之一，省去了显式的长时记忆 cell state，让 hidden state 同时储存长时短时记忆。其结构如下：

<div style="text-align:center;">
    <img src="../../imgs/NNbasics/LSTM3-var-GRU.png" alt="LSTM3-var-GRU" style="zoom: 50%;background-color: white" />
</div>

最上面这条线还是用于让 GRU 具有长时记忆的能力，一次门控乘法、一次加法更新；而计算 $\tilde{h}_t$ 的过程（呈 U 形的线）则可以理解为提取短时记忆的过程，最后通过更新门 $z_t$ 控制长短时记忆的融合。

- $r_t$ 代表**重置门 (reset gate)**，控制是否在 $\tilde{h}_t$ 的计算中忽略过去的 hidden state，起到了类似遗忘门的作用
- $z_t$ 代表**更新门 (update gate)**，控制是否在 $h_{t-1}$ 和 $\tilde{h}_t$ 之间进行加权平均，起到了类似输入门（对应 $z_t*\tilde{h}_t$）和输出门（对应 $(1-z_t) * h_{t-1}$）的作用

### PyTorch Interface

在 [PyTorch 官方文档](https://pytorch.org/docs/stable/generated/torch.nn.GRU.html) 可以看到 `torch.nn.GRU` 所实现的 GRU 内部公式：

$$
\begin{aligned}
&c_t=\sigma(W_{ir}x_t+b_{ir}+W_{hr}h_{(t-1)}+b_{hr}) \\
&z_t=\sigma(W_{iz}x_t+b_{iz}+W_{hz}h_{(t-1)}+b_{hz}) \\
&n_{t}=\mathrm{tanh}(W_{in}x_{t}+b_{in}+r_{t}\odot(W_{hn}h_{(t-1)}+b_{hn})) \\
&h_t=(1-z_t)\odot n_t+z_t\odot h_{(t-1)}
\end{aligned}
$$

> $n_t$ 对标的是 $\tilde{h}_t$，上面的图解中 $h_{t-1}$ 先被 $r_t$ 门控再过线性层生成 $\tilde{h}_t$，而这里的实现是 $h_t$ 先过线性层再被 $r_t$ 门控，用于生成 $n_t$，两种处理方式基本等价。

可以注意到，线性层的 bias 被默认添加了，而且从官网的接口可以看出，实现中可能会用到双向 GRU、多层 GRU 这些变种，但是最基本的原理还是基本一致的。

### ConvGRU in RAFT

在 [RAFT](https://arxiv.org/abs/2003.12039) 中，作者使用了 ConvGRU 作为迭代更新光流的关键模型架构，其[实现](https://github.com/princeton-vl/RAFT/blob/3fa0bb0a9c633ea0a9bb8a79c576b6785d4e6a02/core/update.py#L16-L31)为：

```python
class ConvGRU(nn.Module):
    def __init__(self, hidden_dim=128, input_dim=192+128):
        super(ConvGRU, self).__init__()
        self.convz = nn.Conv2d(hidden_dim+input_dim, hidden_dim, 3, padding=1)
        self.convr = nn.Conv2d(hidden_dim+input_dim, hidden_dim, 3, padding=1)
        self.convq = nn.Conv2d(hidden_dim+input_dim, hidden_dim, 3, padding=1)

    def forward(self, h, x):
        hx = torch.cat([h, x], dim=1)

        z = torch.sigmoid(self.convz(hx))
        r = torch.sigmoid(self.convr(hx))
        q = torch.tanh(self.convq(torch.cat([r*h, x], dim=1)))

        h = (1-z) * h + z * q
        return h
```

可以看出，除了把线性层换成了卷积层，和原始的 GRU 是一样的。不过实际 RAFT 中使用的是 [SeqConvGRU](https://github.com/princeton-vl/RAFT/blob/3fa0bb0a9c633ea0a9bb8a79c576b6785d4e6a02/core/update.py#L33-L60)，先在水平方向上进行 ConvGRU，再在竖直方向上进行 ConvGRU。

> We also experiment with a separable ConvGRU unit, where we replace the 3 × 3 convolution with two GRUs: one with a 1 × 5 convolution and one with a 5 × 1 convolution to **increase the receptive field without significantly increasing the size of the model**.

