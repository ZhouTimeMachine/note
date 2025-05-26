<link rel="stylesheet" href="../../../css/counter.css" />

# Denoising Diffusion Probabilistic Models

!!! info "References"
	- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
	- [What are Diffusion Models? | Lil'Log](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
	- [Understanding Diffusion Models: A Unified Perspective](http://arxiv.org/abs/2208.11970)

Diffusion 的关键就是两个步骤：**前向加噪 (Forward Diffusion Process)**和**反向去噪 (Reverse Diffusion Process)**

<div style="text-align:center;">
	<img src="../../imgs/diffusion/ddpm-modeling.svg" alt="ddpm-modeling" style="zoom:67%;" />
</div>

> 该图来自于 [DDPM 原论文](https://arxiv.org/abs/2006.11239)，进行了重绘

## Forward Diffusion Process

原始的真实数据为 $x_0\sim p(x)$，对其进行 $T$ 步的逐渐加噪，得到 $x_1,\cdots, x_T$。

$$
x_0 \xrightarrow{\text{add noise }t=0} x_1 \xrightarrow{\text{add noise }t=1} \cdots \xrightarrow{\text{add noise }t=T-1} x_T
$$

令 $T\to\infty$，$x_T$ 就服从各向同性的高斯分布 (isotropic Gaussian distribution)，或球形高斯分布。

在 DDPM(denoising diffusion probabilistic models) 中，加噪过程为**马尔可夫过程**，即后一步的分布仅依赖于前一步，有

$$
q(x_t \mid x_{t-1})=\mathcal{N}(\sqrt{1-\beta_t}x_{t-1},\beta_tI)
$$

$I$: 单位矩阵 (identity matrix); $\beta_t$: **方差** (variance)，即 $\sqrt{\beta_t}$ 是标准差 (standard deviation)。

!!! tip "$\{\beta_t\}_T$ 的设置"
	$\{\beta_t\}_T$ 为**超参** (hyperparameter) 序列，是预先设定的。实际加噪过程中，会设置 $\beta_1<\beta_2\cdots<\beta_T$，即随着样本被加噪越来越无序，一次可以加噪的幅度越大。

	> DDPM 原论文中，给 $\{\beta_t\}_T$ 由 $0.0001$ 到 $0.02$ 线性插值——这完全可以改进，即 denoising scheduler 的设计

直观感觉的 $x_t$ 的均值应该为 $x_{t-1}$，而实际在前面加了一个系数 $\sqrt{1-\beta_t}$。这是为了保证 $T\to\infty$ 时，$x_T$ 趋向于服从标准正态分布 $\mathcal{N}(0, 1)$。

接下来的推导中将使用代换 $\alpha_t=1-\beta_t$，$\alpha$ 将会是更常见的加噪公式中的符号，即更常见的加噪公式可能是

$$
x_t = \sqrt{\alpha _t}x_{t-1} + \sqrt{1-\alpha _t}\epsilon_{t-1}
$$

> $x_t-\sqrt{\alpha _t}x_{t-1}\sim \mathcal{N}(0, \beta _t I)$

递推有

$$
x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon_t
$$

> 我们将在符号上，使用 $\epsilon$ 表示 $x_0$ 到 $x_1$, $x_1$ 到 $x_2$, ... 的噪声，使用 $\varepsilon$ 表示从 $x_0$ 到 $x_t$ 的噪声

??? general "推导：$x_T$ 趋向于服从标准正态分布"
	$$
	\begin{aligned}
		x_t
		&= \sqrt{\alpha_t}x_{t-1} + \sqrt{1-\alpha_t}\epsilon_{t-1}\\
		&= \sqrt{\alpha_t}(\sqrt{\alpha_{t-1}}x_{t-2} + \sqrt{1-\alpha_{t-1}}\epsilon_{t-2}) + \sqrt{1-\alpha_t}\epsilon_{t-1}\\
		&= \sqrt{\alpha_t\alpha_{t-1}}x_{t-2}+\sqrt{\alpha_t(1-\alpha_{t-1})}\epsilon_{t-2}+\sqrt{1-\alpha_t}\epsilon_{t-1}
	\end{aligned}
	$$

	这里有 $\epsilon_i\sim \mathcal{N}(0, 1)$。根据方差的性质

	$$
	\begin{gathered}
		Var(c\xi+d)=c^2Var\xi\\
		Var\left(\sum_i\xi_i\right)=\sum_iVar\xi_i+2\sum_{i<j}Cov(\xi_i,\xi_j)
	\end{gathered}
	$$

	可知

	$$
	\begin{aligned}
		&Var(\sqrt{\alpha_t(1-\alpha_{t-1})}\epsilon_{t-2}+\sqrt{1-\alpha_t}\epsilon_{t-1})\\
		=\;& Var(\sqrt{\alpha_t(1-\alpha_{t-1})}\epsilon_{t-2})+Var(\sqrt{1-\alpha_t}\epsilon_{t-1})\\
		=\;& \alpha_t(1-\alpha_{t-1}) Var(\epsilon_{t-2}) + (1-\alpha_t)Var(\epsilon_{t-1})\\
		=\;& \alpha_t(1-\alpha_{t-1}) + (1-\alpha_t)
		= 1-\alpha_t\alpha_{t-1}
	\end{aligned}
	$$

	因此有

	$$
	x_t=\sqrt{\alpha_t\alpha_{t-1}}x_{t-2}+\sqrt{1-\alpha_t\alpha_{t-1}}\overline{\epsilon}_{t-2},\quad \overline{\epsilon}_{t-2}\sim \mathcal{N}(0, 1)
	$$

	以此类推就会有

	$$
	x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon_t
	$$

	其中 $\overline{\alpha}_t=\prod_{i=1}^t\alpha_i$, $\varepsilon_t\sim \mathcal{N}(0, 1)$。由于 $\alpha_i\in(0, 1)$，则 $t\to \infty$ 时有 $\overline{\alpha}_t\to 0$，即 $x_t\to \varepsilon_t\sim \mathcal{N}(0, 1)$。

## Reverse Diffusion Process

如果能从 $p(x_{t-1}\mid x_t)$ 中采样，就可以从纯 $\mathcal{N}(0, 1)$ 高斯噪声中恢复(生成)样本，即

$$
x_T\sim \mathcal{N}(0, 1) \xrightarrow{\text{sample from }p(x_{T-1}\mid x_{T})} x_{T-1} \xrightarrow{\text{sample from }p(x_{T-2}\mid x_{T-1})} \cdots \xrightarrow{\text{sample from }p(x_{0}\mid x_{1})} x_0
$$

因此目标是求取 $p(x_{t-1}\mid x_t)$ ，但是这并不容易，因此需要建立模型来预测分布 $p_\theta(x_{t-1} \mid x_t)\to p(x_{t-1} \mid x_t)$。

$$
\begin{gathered}
	p_{\theta}(x_{0:T})=p(x_T)\prod_{t=1}^Tp_\theta(x_{t-1} \mid x_t)\\
	p_{\theta}(x_{t-1} \mid x_t)=\mathcal{N}(\mu_\theta(x_t, t), \Sigma_\theta(x_t, t))
\end{gathered}
$$

引入条件 $x_0$，我们将 $p_{\theta}(x_{t-1} \mid x_t)$ 建模为 $p(x_{t-1} \mid x_t, x_0)$。注意到有一个数学结论：$\beta_t$ 足够小时，$p(x_{t-1}\mid x_t)$ 也近似满足 Gaussian 分布。

> 在此不仔细检查提供其推导，详见 Feller, William. "On the theory of stochastic processes, with particular reference to applications." Proceedings of the [First] Berkeley Symposium on Mathematical Statistics and Probability. University of California Press, 1949.

在这个数学结论的支持下，我们就可以求解：

$$
p(x_{t-1} \mid x_t, x_0)=\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)
$$

其中

$$
\begin{aligned}
	\tilde{\mu}_t
	&=\tilde{\mu}_t(x_t, x_0)=\frac{\sqrt{\alpha_t}(1-\overline{\alpha}_{t-1})}{1-\overline{\alpha}_t}x_t + \frac{\sqrt{\overline{\alpha}_{t-1}}(1-\alpha_t)}{1-\overline{\alpha}_{t}}x_0 \\
	&=\tilde{\mu}_t(x_t, \varepsilon_t)=\frac{1}{\sqrt{\alpha}_t}\left(x_t-\frac{1-\alpha_t}{\sqrt{1-\overline{\alpha}_t}}\varepsilon_t\right)\\
	\tilde{\beta}_t
	&=\frac{1-\overline{\alpha}_{t-1}}{1-\overline{\alpha}_{t}}\beta_t
\end{aligned}
$$

??? general "推导：$p(x_{t-1} \mid x_t, x_0)=\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)$"
	首先由 Bayes 公式有

	$$
		q(x_{t-1}, x_t \mid  x_0) = 
		p(x_{t-1} \mid x_t, x_0) q(x_t \mid x_0) = 
		q(x_t \mid x_{t-1}, x_0) q(x_{t-1} \mid x_0)
	$$

	根据 Markov 过程有 $p(x_t \mid x_{t-1}, x_0)=p(x_t \mid x_{t-1})$，因此就有

	$$
	\begin{aligned}
		p(x_{t-1} \mid x_t, x_0)
		&= \underbrace{
				p(x_t \mid x_{t-1})
			}_{
				\mathcal{N}(
					\sqrt{\alpha_t}x_{t-1},
					(1-\alpha_t)I
				)
			}
			\cdot
			\underbrace{
				\frac{q(x_{t-1} \mid x_0)}{q(x_t \mid x_0)}
			}_{
				\mathcal{N}(
					\sqrt{\overline{\alpha}_{t-1}}x_0,
					(1-\overline{\alpha}_{t-1})I
				)
				\; / \;
				\mathcal{N}(
					\sqrt{\overline{\alpha}_{t}}x_0,
					(1-\overline{\alpha}_{t})I
				)
			}\\
		&\propto \exp\left(
			-\frac{1}{2} \left(
				\frac{
					(x_t-\sqrt{\alpha_t}x_{t-1})^2
				} {
					1-\alpha_t
				} +
				\frac{
					(x_{t-1}-\sqrt{\overline{\alpha}_{t-1}}x_0)^2
				} {
					1-\overline{\alpha}_{t-1}
				} -
				\frac{
					(x_t-\sqrt{\overline{\alpha}_{t}}x_0)^2
				} {
					1-\overline{\alpha}_{t}
				}
			\right)
		\right)
	\end{aligned}
	$$

	整理 $\exp\left(-\frac{1}{2}(*)\right)$ 中的 $*$，仅关注 $x_{t-1}$，有

	$$
	\left(\frac{\alpha_t}{1-\alpha_t} + \frac{1}{1-\overline{\alpha}_{t-1}}\right)x_{t-1}^2 -
	\left(\frac{2\sqrt{\alpha_t}}{1-\alpha_t}x_t + \frac{2\sqrt{\overline{\alpha}_{t-1}}}{1-\overline{\alpha}_{t-1}}x_0\right)x_{t-1} +
	C(x_t, x_0)
	$$

	想要求出 $\tilde{\mu}_t, \tilde{\beta}_tI$，首先看 Gaussian 分布公式中指数相关有

	$$
	\exp\left(-\frac{(x-\mu)^2}{2\beta}\right) =
	\exp\left(-\frac{1}{2}\left(\frac{1}{\beta}x^2-\frac{2\mu}{\beta}x+\frac{\mu^2}{\beta}\right)\right)
	$$

	根据二次项系数就得到 $\tilde{\beta}_t=\frac{(1-\alpha_t)(1-\overline{\alpha}_{t-1})}{1-\alpha_t\overline{\alpha}_{t-1}}=\frac{1-\overline{\alpha}_{t-1}}{1-\overline{\alpha}_{t}}\beta_t$，再根据一次项系数可以得到

	$$
	\begin{aligned}
		\tilde{\mu}_t
		&=\frac{1}{2}\left(\frac{2\sqrt{\alpha_t}}{1-\alpha_t}x_t + \frac{2\sqrt{\overline{\alpha}_{t-1}}}{1-\overline{\alpha}_{t-1}}x_0\right)\cdot \frac{1-\overline{\alpha}_{t-1}}{1-\overline{\alpha}_{t}}\beta_t\\
		&=\boxed{\frac{\sqrt{\alpha_t}(1-\overline{\alpha}_{t-1})}{1-\overline{\alpha}_t}x_t + \frac{\sqrt{\overline{\alpha}_{t-1}}(1-\alpha_t)}{1-\overline{\alpha}_{t}}x_0}
		\quad \boxed{ \tilde{\mu}_t(x_t, x_0) }
	\end{aligned}
	$$

	> Recall: $\beta_t = 1-\alpha_t$，$\overline{\alpha}_t = \prod_{i=1}^t\alpha_i$

	这里再对一对常数项系数就能验证是否是 Gaussian 分布了，由于前面已经引用了 $\beta_t$ 足够小时近似 Gaussian 分布的结论，这里就不管了。根据前面前向的结论，有 $x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon \Rightarrow x_0=\frac{1}{\sqrt{\overline{\alpha}_t}}(x_t-\sqrt{1-\overline{\alpha}_t}\varepsilon)$，代入上式有

	$$
	\begin{aligned}
		\tilde{\mu}_t
		&=\frac{\sqrt{\alpha_t}(1-\overline{\alpha}_{t-1})}{1-\overline{\alpha}_t}x_t + \frac{\sqrt{\overline{\alpha}_{t-1}}\beta_t}{1-\overline{\alpha}_{t}}\cdot\frac{1}{\sqrt{\overline{\alpha}_t}}(x_t-\sqrt{1-\overline{\alpha}_t}\varepsilon)\\
		&=\boxed{\frac{1}{\sqrt{\alpha}_t}\left(x_t-\frac{1-\alpha_t}{\sqrt{1-\overline{\alpha}_t}}\varepsilon_t\right)}
		\quad \boxed{ \tilde{\mu}_t(x_t, \varepsilon_t) }
	\end{aligned}
	$$ 

$\tilde{\beta}_t$ 是确定的，而模型所预测的噪声 $\varepsilon$ (epsilon-prediction) 或者 $x_0$ (v-prediction 间接预测) 用于构造 $\tilde{\mu}_t$。这样，我们只要首先通过模型的预测构造 $\tilde{\mu}_t$，然后从 $\mathcal{N}(0, 1)$ 中采样一个 $\epsilon_t$，就可以从 $x_t$ 去噪得到

$$
x_{t-1}=\tilde{\mu}_t + \sqrt{\tilde{\beta}_t}\epsilon_t
$$

> 这里应用了重参数化技巧，不直接从 $\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)$ 中采样 $x_{t-1}$，而是从 $\mathcal{N}(0, 1)$ 中采样一个 $\epsilon_t$，然后通过 $\tilde{\mu}_t$ 和 $\tilde{\beta}_t$ 来得到 $x_{t-1}$

事实上，大家后来往往用 $\sigma_t^2$ 来表示去噪时使用的方差 $\tilde{\beta}_t$，一方面是标准差在符号上表示更友好，另一方面则是因为实践中取理论上的 $\tilde{\beta}_t$ 并不一定最优，取 $\beta_t$ 也完全没问题，后来的 denoising scheduler 的设计中对 $\sigma_t^2$ 的设计更是层出不穷，在此就不多加赘述了。

## Interpretation from Maximum Likelihood

在极大似然视角下，DDPM 仍然是经典的通过优化 ELBO (Evidence Lower Bound) 来极大化对数似然函数的：

$$
\log p(x_0) \geqslant \mathbb{E}_{q(x_{1:T}\mid x_0)}\left[\log \frac{p(x_{0:T})}{q(x_{1:T}\mid x_0)} \right]
$$

> $\mathbb{E}_{z\sim q(z \mid x)}$ 常简记为 $\mathbb{E}_{q(z\mid x)}$

??? general "推导：Evidence Lower Bound (ELBO)"
	将数据 $x$ 编码为隐变量 $z$，从 $z$ 解码得到 $x$。有

	$$
	\begin{aligned}
		\log p(x)
		&= \log p(x) \int q_{\phi} (z \mid x) dz\\
		&= \int \log p(x) q_{\phi} (z \mid x) dz\\
		&= \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log p(x)\right] \\
		&= \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log \frac{p(x, z)}{p(z\mid x)}\right] \\
		&= \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log \frac{p(x, z)q_{\phi}(z\mid x)}{p(z\mid x)q_{\phi}(z\mid x)}\right] \\
		&= \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log \frac{p(x, z)}{q_{\phi}(z\mid x)}\right] + \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log \frac{q_{\phi}(z\mid x)}{p(z\mid x)}\right] \\
		&= \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log \frac{p(x, z)}{q_{\phi}(z\mid x)}\right] + D_{\mathrm{KL}}(q_{\phi}(z\mid x) \;\|\; p(z\mid x)) \\
		&\geqslant \mathbb{E}_{z\sim q_{\phi} (z \mid x)}\left[\log \frac{p(x, z)}{q_{\phi}(z\mid x)}\right]
	\end{aligned}
	$$

将前面反向去噪过程中建模的 $p_\theta(x_{0:T})$ 代入 $p(x_{0:T})$，有

$$
\begin{aligned}
	\log p(x_0)
	&\geqslant \mathbb{E}_{q(x_{1:T}\mid x_0)}\left[
		\log \frac {
			p_{\theta}(x_{0:T})
		} {
			q(x_{1:T}\mid x_0)
		} 
	\right]\\
	&=\mathbb{E}_{q(x_{1:T}\mid x_0)}\left[
		\log \frac {
			p(x_T)
			{\color{lime} \prod_{t=1}^T p_\theta(x_{t-1} \mid x_t)}
		} {
			{\color{lime} \prod_{t=1}^T q(x_t \mid x_{t-1})}
		}
	\right]\\
	&=\mathbb{E}_{q(x_{1:T}\mid x_0)}\left[
		\log \frac {
			p(x_T)
			{\color{skyblue} p_\theta(x_0 \mid x_1)}
			{\color{red} \prod_{t=2}^T p_\theta(x_{t-1} \mid x_t)}
		} {
			{\color{skyblue} q(x_1 \mid x_0)}
			{\color{red} \prod_{t=2}^T q(x_t \mid x_{t-1})}
		}
	\right]\\
	&=\mathbb{E}_{q(x_{1:T}\mid x_0)}\left[
		{\color{skyblue}
			\log \frac {
				p(x_T) p_\theta(x_0 \mid x_1)
			} {
				q(x_1 \mid x_0)
			}
		} + 
		\underbrace{ \color{red}
			\sum_{t=2}^T\log \frac {
				p_\theta(x_{t-1} \mid x_t)
			} {
				q(x_t \mid x_{t-1})
			}
		}_{\text{to be processed}}
	\right]
\end{aligned}
$$

针对上面的连加项，由于马尔可夫性质有 $q(x_t \mid x_{t-1})=q(x_t \mid x_{t-1}, x_0)$，因此

$$
\begin{aligned}
	&{\color{red} \sum_{t=2}^T\log \frac {
			p_\theta(x_{t-1} \mid x_t)
		} {
			q(x_t \mid x_{t-1})
	}} \\
	=& \sum_{t=2}^T\log \frac {
			p_\theta(x_{t-1} \mid x_t)
		} {
			q(x_t \mid x_{t-1}, x_0)
	} \quad \boxed{
		q(x_t \mid x_{t-1}, x_0)
		= p(x_{t-1} \mid x_t, x_0) \frac{
			q(x_t \mid x_0)
		} {
			q(x_{t-1} \mid x_0)
		}
	}\\
	=& \sum_{t=2}^T\log \frac {
			p_\theta(x_{t-1} \mid x_t)
		} {
			p(x_{t-1} \mid x_t, x_0)
	} + \sum_{t=2}^T \log \frac{
		q(x_{t-1} \mid x_0)
	} {
		q(x_t \mid x_0)
	} \\
	=& { \color{red}
		\sum_{t=2}^T\log \frac {
			p_\theta(x_{t-1} \mid x_t)
		} {
			p(x_{t-1} \mid x_t, x_0)
		}
	} + { \color{skyblue}
		\log \frac{
			q(x_1 \mid x_0)
		} {
			q(x_T \mid x_0)
		}
	} \\
\end{aligned}
$$

$\log \frac {q(x_1 \mid x_0)} {q(x_T \mid x_0)}$ 与原式中的 $\log \frac { p(x_T) p_\theta(x_0 \mid x_1) } { q(x_1 \mid x_0) }$ 可以合并为 $\log \frac {p(x_T) p_\theta(x_0 \mid x_1)} {q(x_T \mid x_0)}$，因此有

$$
\begin{aligned}
	\log p(x_0)
	&\geqslant \mathbb{E}_{q(x_{1:T}\mid x_0)}\left[
		{ \color{skyblue}
			\log \frac {
				p(x_T) p_\theta(x_0 \mid x_1)
			} {
				q(x_T \mid x_0)
			}
		} + { \color{red}
			\sum_{t=2}^T\log \frac {
				p_\theta(x_{t-1} \mid x_t)
			} {
				p(x_{t-1} \mid x_t, x_0)
			}
		}
	\right]\\
	&=\mathbb{E}_{q(x_1\mid x_0)}\left[
		{\color{skyblue} p_\theta(x_0 \mid x_1)}
	\right] + 
	\mathbb{E}_{q(x_{T}\mid x_0)}\left[
		{ \color{skyblue}
			\log \frac {
				p(x_T)
			} {
				q(x_T \mid x_0)
			}
		}
	\right] \\
	&\quad + \sum_{t=2}^T
	\mathbb{E}_{q(x_t, x_{t-1}\mid x_0)}\left[
		{ \color{red}
			\log \frac {
				p_\theta(x_{t-1} \mid x_t)
			} {
				p(x_{t-1} \mid x_t, x_0)
			}
		}
	\right]\\
	&=\underbrace{\mathbb{E}_{q(x_1\mid x_0)}\left[
		p_\theta(x_0 \mid x_1)
	\right]}_{\text{reconstruction term, }L_0} -
	\underbrace{D_{KL}\left(
		q(x_T \mid x_0) \;\|\; p(x_T)
	\right)}_{\text{prior matching term, }L_T} \\
	&\quad -
	\underbrace{\sum_{t=2}^T
	\mathbb{E}_{q(x_{t}\mid x_0)}\left[
		D_{KL} \left(
			p(x_{t-1} \mid x_t, x_0)
			\;\|\;
			p_\theta(x_{t-1} \mid x_t)
		\right)
	\right]}_{\text{denoising matching term, }L_{1:T-1}}
\end{aligned}
$$

- **重建项 (reconstruction term)** $L_0$: VAE 中也有，DDPM 中视为从连续隐变量到离散图片数据的映射，进行了特殊处理
- **先验匹配项 (prior matching term)** $L_{T}$: 不含可学习参数，在 DDPM 的假设下就是 0
- **去噪匹配项 (denoising matching term)** $L_{1:T-1}$: 最关键的需要学习的部分，可见就是让 $p_\theta(x_{t-1} \mid x_t)$ 逼近 $p(x_{t-1} \mid x_t, x_0)$，也就解释了我们前面为什么如此建模

## Training Objective

即

$$
L_{t-1} = \mathbb{E}_{q(x_t, x_{t-1} \mid x_0)}
\left[
	\log \frac {
		p_\theta(x_{t-1} \mid x_t)
	} {
		p(x_{t-1} \mid x_t, x_0)
	}
\right]
$$

代入 $p(x_{t-1} \mid x_t, x_0)=\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)$，并也将 $p_\theta(x_{t-1} \mid x_t)$ 参数化为 $\mathcal{N}(\mu_\theta(x_t, t), \tilde{\beta}_tI)$，有

$$
\begin{aligned}
	L_{t-1}
	&= \mathbb{E}_{q(x_t \mid x_0)} D_{KL}\left(
		p_\theta(x_{t-1} \mid x_t) \;\|\; p(x_{t-1} \mid x_t, x_0)
	\right)\\
	&= \mathbb{E}_{q(x_t \mid x_0)} \left[
		\frac{1}{2}(\mu_\theta(x_t, t)-\tilde{\mu}_t(x_t, x_0))^{\top}\tilde{\beta}_t^{-1}(\mu_\theta(x_t, t)-\tilde{\mu}_t(x_t, x_0))
	\right] \\
	&= \mathbb{E}_{q(x_t \mid x_0)} \left[
		\frac{1}{2\tilde{\beta}_t}\|\mu_\theta(x_t, t)-\tilde{\mu}_t(x_t, x_0))\|^2
	\right]
\end{aligned}
$$

> 原论文中还要加上一个与 $\theta$ 无关的常数项 $C$，这是有意义的，当 $p_\theta(x_{t-1} \mid x_t)$ 的方差不严格等于 $\tilde{\beta}_tI$ 时就会存在，然而我们最关心的还是均值 $\mu_\theta(x_t, t)$

??? general "两个 $d$ 元正态分布之间的 KL 散度"
	设 $p_1$, $p_2$ 为两个 $d$ 元正态分布，均值分别为 $\mu_1, \mu_2$，协方差矩阵分别为 $\Sigma_1, \Sigma_2$，则有

	$$
	\boxed{
		D_{KL}(p_1 \;\|\; p_2) = \frac{1}{2}\left(
		\log \frac{\det\Sigma_2}{\det\Sigma_1} + \mathrm{Tr}(\Sigma_2^{-1}\Sigma_1) +
		(\mu_2-\mu_1)^{\top}\Sigma_2^{-1}(\mu_2-\mu_1) - d
		\right)
	}
	$$

	证明如下。考虑到

	$$
	p_i(x) = \frac{1}{(2\pi)^{d/2}(\det\Sigma_i)^{1/2}} \exp\left(-\frac{1}{2}(x-\mu_i)^{\top}\Sigma_i^{-1}(x-\mu_i)\right)
	$$

	有

	$$
	\begin{aligned}
	\mathbb{E}_{p_1}[\log p_i(x)]
	&= \mathbb{E}_{p_1}\left[-\frac{d}{2}\log(2\pi) -\frac{1}{2}\log \det\Sigma_i- \frac{1}{2}(x-\mu_i)^{\top}\Sigma_i^{-1}(x-\mu_i)\right]\\
	&= -\frac{1}{2}\left(
		{ \color{skyblue}
			d\log(2\pi) + \log \det\Sigma_i
		}
		+ {\color{red}
			\mathbb{E}_{p_1}[
				(x-\mu_i)^{\top}\Sigma_i^{-1}(x-\mu_i)
			]
		}
	\right)\\
	\end{aligned}
	$$

	其中

	$$
	\begin{aligned}
	{\color{red} \mathbb{E}_{p_1}[
		(x-\mu_i)^{\top} \Sigma_i^{-1} (x-\mu_i)
	]}
	&= \mathbb{E}_{p_1}[\mathrm{Tr}((x-\mu_i)^{\top}\Sigma_i^{-1}(x-\mu_i))]\\
	&= \mathbb{E}_{p_1}[
		\mathrm{Tr}(
			\Sigma_i^{-1} (x-\mu_i)(x-\mu_i)^{\top}
		)
	]\\
	&= \mathrm{Tr}(
		\Sigma_i^{-1} \mathbb{E}_{p_1}[
			(x-\mu_i)(x-\mu_i)^{\top}
		]
	) \\
	&= \mathrm{Tr}(
		\Sigma_i^{-1} \mathbb{E}_{p_1}[
			xx^{\top} + \mu_i\mu_i^{\top} - x\mu_i^{\top} - \mu_ix^{\top}
		]
	) \\
	&= \mathrm{Tr}(
		\Sigma_i^{-1} [
			(\Sigma_1 + \mu_1\mu_1^{\top}) + \mu_i\mu_i^{\top} - \mu_1\mu_i^{\top} - \mu_i\mu_1^{\top}
		]
	) \\
	&= \begin{cases}
		{\color{red} d}, & i = 1\\
		{\color{red} \mathrm{Tr}(\Sigma_2^{-1}\Sigma_1) + (\mu_2 - \mu_1)^{\top}\Sigma_2^{-1}(\mu_2 - \mu_1)}, & i = 2
	\end{cases}
	\end{aligned}
	$$

	> 第一行到第二行应用了迹的恒等式：$\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$

	因此最终有

	$$
	\begin{aligned}
		D_{KL}(p_1 \;\|\; p_2)
		&= \mathbb{E}_{p_1}\left[\log p_1(x) - \log p_2(x)\right]\\
		&= \frac{1}{2}\left(
			{\color{skyblue} \log\frac{\det\Sigma_2}{\det\Sigma_1}}
			+ { \color{red}
				\mathrm{Tr}(\Sigma_2^{-1}\Sigma_1)
				+ (\mu_2 - \mu_1)^{\top}\Sigma_2^{-1}(\mu_2 - \mu_1)
				- d
			}
		\right)\\
	\end{aligned}
	$$

前面我们已经得到了 $\tilde{\mu}_t$ 的 $\tilde{\mu}_t(x_t, \varepsilon_t)$ 表示，也同样将 $\mu_\theta(x_t, t)$ 重参数化为

$$
\mu_\theta(x_t, t) = \mu_t(x_t, \varepsilon_{\theta}(x_t, t)) = \frac{1}{\sqrt{\alpha}_t}\left(x_t - \frac{1-\alpha_t}{\sqrt{1-\overline{\alpha}_t}}\varepsilon_{\theta}(x_t, t)\right)
$$

这样就有

$$
L_{t-1} = \mathbb{E}_{q(x_t \mid x_0), \varepsilon_t}\left[
	\frac{\beta_t^2}{2\tilde{\beta}_t \alpha_t (1-\overline{\alpha}_t)}\|\varepsilon_{\theta}(x_t, t) - \varepsilon_t\|^2
\right]
$$

> Recall $x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon_t$, $\beta_t=1-\alpha_t$

实践中，DDPM 略去了常数乘法系数（不同 $t$ 的损失函数系数一致了），最小化

$$
L_{t-1} = \mathbb{E}_{t\sim \{1, ..., T\}, q(x_t \mid x_0), \varepsilon_t}\|\varepsilon_{\theta}(x_t, t) - \varepsilon_t\|^2
$$

综合观之，有

<div style="text-align:center;">
	<img src="../../imgs/diffusion/ddpm-pseudo-code-light.png#only-light" alt="ddpm-pseudo-code-light" style="zoom:67%;" />
	<img src="../../imgs/diffusion/ddpm-pseudo-code-dark.png#only-dark" alt="ddpm-pseudo-code-dark" style="zoom:67%;" />
</div>