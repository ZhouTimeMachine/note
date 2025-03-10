<link rel="stylesheet" href="../../../css/counter.css" />

# v-prediction

!!! warning "该页面还在建设中"

!!! info "Based on *Progressive Distillation for Fast Sampling of Diffusion Models* (ICLR 2022 Spotlight). Link: [arxiv](https://arxiv.org/abs/2202.00512), [openreview](https://openreview.net/forum?id=TIdIXIpzhoI), [code](https://github.com/google-research/google-research/tree/master/diffusion_distillation)"

Diffusion Model 中的 v-prediction 是相对于 $\varepsilon$-prediction 方法而言的，从预测一个噪声 $\varepsilon$ 变化到预测速度 $v$，作为一种加速采样的方法在渐进蒸馏这篇论文中提出。

## Angular Reparameterization of Diffusion Process

在 DDPM 中，加噪有

$$
x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon
$$

用 $\alpha$ 表示 $\sqrt{\overline{\alpha}_t}$，$\sigma$ 表示 $\sqrt{1-\overline{\alpha}_t}$（方差），也就有

$$
\alpha^2 + \sigma^2=1
$$

在 DDPM 推导中，这种数量关系的存在是为了让充分加噪之后的 $x_T$ 趋向于标准正态分布。而这里这种优雅的性质使其能够使用角参数化 (angular parameterization) 将其替换：

$$
\begin{gathered}
    \phi=\arctan\frac{\sigma}{\alpha}\\
    \alpha=\cos \phi,\quad \sigma=\sin \phi
\end{gathered}
$$

在论文的附录 D 中给出了这种角参数化的可视化效果：

<div style="text-align:center;">
    <img src="../../imgs/diffusion/v-prediction-visualization.png" alt="v-prediction-visualization" style="zoom:67%;" />
</div>

这里的 $z$ 指的就是 $x_t$，$x$ 就是 $x_0$，有

$$
x_t = x_0\cos\phi + \varepsilon\sin\phi
$$

对 $\phi$ 求导，有

$$
\frac{\mathrm d x_t}{\mathrm d \phi}=-x_0\sin\phi + \varepsilon \cos\phi
$$

速度 $v$ 就定义为 $x_t$ 对 $\phi$ 的导数，所以就有

$$
v=\alpha \varepsilon - \sigma x_0
$$

去噪时考虑使用速度 $v$ 而不是噪声 $\varepsilon$，于是需要把加噪公式中的 $\varepsilon$ 消掉，也就有

$$
x_t = \alpha x_0 + \sigma \cdot \frac{v+\sigma x_0}{\alpha}\Rightarrow x_0=\alpha x_t - \sigma v
$$

同理消掉 $x_0$ 可以得到

$$
\varepsilon = \alpha v + \sigma x_t
$$

> 这个式子在下面改写 DDIM Update Rule 的推导中有用

## Rewrite DDIM Update Rule

DDIM 旨在求解 ODE

$$
\mathrm dx = \left[f(x, t) - \frac{1}{2}g(t)^2\nabla _x\log  p_t(x)\right]\mathrm d t
$$

使用传统的数值方法（例如 Euler 法或者 Runge-Kutta 法）当然也可以分步求解，例如 DDIM 使用的是 Euler 法：

$$
    x_{t-1} = \sqrt{\overline{\alpha}_{t-1}}
    \underbrace{\left( \frac{x_t-\sqrt{1-\overline{\alpha}_t}\varepsilon_{\theta}^{(t)}(x_t)}{\sqrt{\overline{\alpha}_t}} \right)}_{\text{“ predicted }x_0\text{”}}
    + \underbrace{\sqrt{1-\overline{\alpha}_{t-1}}\varepsilon_{\theta}^{(t)}(x_t)}_{\text{“direction pointing to }x_t\text{”}}
$$

> 可以从 [*Denoising Diffusion Implicit Models*](https://arxiv.org/abs/2010.02502) 的 Equation (12) 导出

然而，利用 v-prediction 的角参数化性质，可以重写 DDIM 的更新规则。设 $t$ 时刻角参数化的结果为 $\phi_{t}$，$t-1$ 时刻角参数化的结果为 $\phi_s$，那么有

$$
\begin{aligned}
    x_{t-1}
    & = \cos \phi_s\left( \frac{x_t-\sin\phi_t\varepsilon_{\theta}^{(t)}(x_t)}{\cos\phi_t} \right) + \sin\phi_s\varepsilon_{\theta}^{(t)}(x_t) \\
    & = \frac{\cos \phi_s}{\cos\phi_t}x_t + \frac{\sin \phi_s\cos \phi_t - \sin\phi_t\cos \phi_s}{\cos\phi_t}\varepsilon_{\theta}^{(t)}(x_t) \\
    & = \frac{\cos \phi_s}{\cos\phi_t}x_t + \frac{\sin (\phi_s - \phi_t)}{\cos\phi_t}(v\cos\phi_t + x_t\sin\phi_t) \\
    & = \left[\frac{(1-\sin^2\phi_t)\cos \phi_s}{\cos\phi_t} + \sin \phi_s\sin \phi_t\right]x_t + v\sin (\phi_s - \phi_t)\\
    & = x_t\cos (\phi_s - \phi_t) + v\sin (\phi_s - \phi_t)\\
\end{aligned}
$$

事实上，$\phi_t - \phi_s = \delta > 0$，于是有

$$
x_{t-1} = x_t\cos\delta - v\sin \delta
$$

或者写作

$$
x_{\phi_t - \delta}= x_{\phi_t}\cos\delta - v(x_{\phi_t})\sin\delta
$$

## Implementation in diffusers

然而，考察了稳定的 0.25.0 和考察时最新的 0.29.1 版本的 diffusers 代码，发现并没有直接使用 v-prediction 的角参数化性质进行去噪，事实上仍使用前面最基本的 DDIM 去噪公式，只是将原本使用 $\varepsilon$ 表示的 predicted $x_0$ 改成了 v-prediction 表示的 predicted $x_0$，即

$$
x_0=\alpha x_t - \sigma v_{\theta}^{(t)}(x_t)
$$