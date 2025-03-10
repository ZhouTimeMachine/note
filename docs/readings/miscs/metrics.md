# Metrics

!!! info "Some metrics used in papers"

!!! tip "Take [A Study on the Evaluation of Generative Models](https://arxiv.org/abs/2206.10935) as reference"

## KL Divergence
> KL, abbr. for Kullback-Leibler

KL Divergence 衡量了概率分布 $p$ 到概率分布 $q$ 的距离，也称为相对熵，实际上是一种特殊的 Bregman Divergence。有

$$
    \operatorname{KL} (p\; ||\; q) = \mathbb{E}_{x\sim p}\left[ \log\frac{p(x)}{q(x)} \right]
$$

!!! warning "关于 Divergence 的更多内容 TBD"

## FID
> FID, abbr. for Frechet Inception Distance. 

基于假设：真实图片的特征服从高斯分布 $\mathcal{N}(\mu_r, \Sigma_r)$，生成图片的特征服从高斯分布 $\mathcal{N}(\mu_g, \Sigma_g)$。使用 Inception Network 作为特征提取器。

$$
    \operatorname{FID} = \|\mu_r - \mu_g\|^2 + \operatorname{Tr}(\Sigma_r+\Sigma_g-2(\Sigma_r\Sigma_g)^{1/2})
$$

描绘了真实图片和生成图片在 feature 层面的距离。

## KID
> KID, abbr. for Kernel Inception Distance

KID 通过放松对高斯分布的假设，试图改善 FID。

> KID measures the squared Maximum Mean Discrepancy (MMD) between the Inception representations of the real and generated samples using a polynomial kernel.

根据 [PyTorch-Metrics Doc](https://torchmetrics.readthedocs.io/en/stable/image/kernel_inception_distance.html)，可知有

$$
    \operatorname{KID}=\operatorname{MMD}(f_{\text{real}}, f_{\text{fake}})^2
$$

计算 KID 时需要估计一个多项式核函数 $k$

$$
    k(x, y) = (\gamma * x^{\top}y+coef)^{degree}
$$

## SSIM
> SSIM, abbr. for Structural Similarity Index Measure

SSIM 即结构相似性指数，仿照人类视觉系统 (Human Visual System, HVS)，从亮度、对比度以及结构量化图像的属性。$x$ 和 $y$ 两张图片之间，

- 用**均值**估计**亮度** $l(x, y)$ (照明度，luminance)
- **方差**估计**对比度** $c(x, y)$ (contrast)
- **协方差**估计**结构相似程度** $s(x, y)$ (structure) 

$$
    l(x, y) = \frac{2\mu_x\mu_y + c_1}{\mu_x^2 + \mu_y^2 + c_1},\quad
    c(x, y) = \frac{2\sigma_x\sigma_y + c_2}{\sigma_x^2 + \sigma_y^2 + c_2},\quad
    s(x, y) = \frac{\sigma_{xy} + c_3}{\sigma_x \sigma_y + c_3}
$$

定义

$$
    \operatorname{SSIM}(x, y)=
    l(x, y)^{\alpha} \cdot c(x, y)^{\beta} \cdot s(x, y)^{\gamma}
$$

设定 $\alpha, \beta, \gamma=1$，则

$$
    \operatorname{SSIM}(x, y)=
    \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}
    {(\mu_x^2 + \mu_x^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}
$$

其中，

- $\mu_x, \mu_y$ 是 $x, y$ 的平均值
- $\sigma_x, \sigma_y$ 是 $x, y$ 的标准差
- $\sigma_{xy}$ 是 $x$ 和 $y$ 的协方差
- $c_1=(k_1L)^2, c_2=(k_2L)^2$ 是两个用于维持稳定的常数，避免出现除零的情况
- $L$ 和 PSNR 中的 $\operatorname{MAX}_I$ 意义相同
- 一般情况下，$k_1=0.01$，$k_2=0.03$

## PSNR
> PSNR, abbr. for Peak Signal to Noise Ratio

PSNR 即峰值信噪比，是一种评价图像质量的度量标准。

> 因为 PSNR 值具有局限性，所以它只是衡量最大值信号和背景噪音之间的图像质量参考值。PSNR 的单位为 dB，其值越大，图像失真越少。一般来说，PSNR 高于 40dB 说明图像质量几乎与原图一样好；在 30-40dB 之间通常表示图像质量的失真损失在可接受范围内；在 20-30dB 之间说明图像质量比较差；PSNR 低于 20dB 说明图像失真严重。——[知乎](https://zhuanlan.zhihu.com/p/309892873)

> 有损图像和视频压缩中 PSNR 的典型值在 30 到 50 dB 之间，前提是位深度为 8 位，越高越好。当 PSNR 值为 60 dB 或更高时，12 位图像的处理质量被认为是高的。对于 16 位数据，PSNR 的典型值介于 60 和 80 dB 之间。无线传输质量损失的可接受值约为 20 dB 至 25 dB。——[wikipedia](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)

PSNR 最容易通过均方误差（MSE）定义。给定无噪声 $m\times n$ 单色图像 $I$ 及其噪声近似值 $K$，MSE 定义为

$$
    \operatorname{MSE}=\frac{1}{mn} \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} [I(i, j)- K(i, j)]^{2}
$$

PSNR（单位：dB）定义为

$$
\begin{aligned}
\operatorname{PSNR}
&=10\cdot \log _{10}\left({\frac {{\operatorname{MAX}}_{I}^{2}}{\operatorname{MSE}}}\right)\\
&=20\cdot \log _{10}\left({\frac {{\operatorname{MAX}}_{I}}{\sqrt {\operatorname{MSE}}}}\right)\\
&=20\cdot \log _{10}({\operatorname{MAX}}_{I})-10\cdot \log _{10}({\operatorname{MSE}})
\end{aligned}
$$

这里，${\operatorname{MAX}}_{I}$ 是图像的最大可能像素值。当每个样本使用 8 位表示像素时，即 255。更一般地说，当使用线性 PCM 表示样本时，每个样本有 $B$ 位，${\operatorname{MAX}}_{I}$ 为 $2B-1$。针对浮点型数据，最大像素值为1。

有三种方法来计算彩色 RGB 图像的 PSNR：

1. 分别计算 RGB 三个通道的 PSNR，然后取平均值；
2. 或者计算 RGB 各个通道的均方差的均值，然后统一求 PSNR；
3. 或者把 RGB 转化为 YCbCr，然后只计算 Y (亮度)分量的PSNR。

第二三种方法较为常用。

## CLIP Score

> 出自 [CLIPScore: A Reference-free Evaluation Metric for Image Captioning](https://arxiv.org/abs/2104.08718)

特征提取器选用 ViT-B/32。原始的 CLIP Score，$v$ 为 visual CLIP embedding, $c$ 为 textual CLIP embedding，则

$$
    \operatorname{CLIP-S}(c,\; v) = w*\max(\cos(c,\; v),\;0)
$$

还有一种 RefCLIPScore，在此略去。