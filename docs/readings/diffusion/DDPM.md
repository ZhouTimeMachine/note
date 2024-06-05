<link rel="stylesheet" href="../../../css/counter.css" />

# Denoising Diffusion Probabilistic Models

!!! info "Reference"
	本文参考自博客 [What are Diffusion Models? | Lil'Log](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) 和知乎[由浅入深了解 Diffusion Model](https://zhuanlan.zhihu.com/p/525106459?utm_source=zhihu)

!!! warning "该页面还在建设中"

Diffusion 的关键就是两个步骤：**前向加噪 (Forward Diffusion Process)**和**反向去噪 (Reverse Diffusion Process)**

## Forward Diffusion Process

原始的真实数据为 $x_0\sim q(x)$，对其进行 $T$ 步的逐渐加噪，得到 $x_1,\cdots, x_T$。令 $T\to\infty$，$x_T$ 就服从各向同性的高斯分布 (isotropic Gaussian distribution)，或球形高斯分布。

在 DDPM(denoising diffusion probabilistic models) 中，加噪过程为**马尔可夫过程**，即后一步的分布仅依赖于前一步，有

$$
q(x_t|x_{t-1})=\mathcal{N}(\sqrt{1-\beta_t}x_{t-1},\beta_tI)
$$

在这里，$I$ 就是单位矩阵，$\beta_t$ 就是**方差**(即 $\sqrt{\beta_t}$ 是标准差)，为**超参**序列。实际加噪过程中，会设置 $\beta_1<\beta_2\cdots<\beta_T$，即随着样本被加噪越来越无序，一次可以加噪的幅度越大。

**均值在** $x_{t-1}$ **前面加一个系数是为了保证** $x_T$ **趋向分布** $\mathcal{N}(0, 1)$。在这里推导时，使用代换 $\alpha_t=1-\beta_t$，由 $x_t-\sqrt{\alpha_t}x_{t-1}\sim \mathcal{N}(0, (1-\alpha_t) I)$，有

$$
\begin{aligned}
	x_t
	&= \sqrt{\alpha_t}x_{t-1} + \sqrt{1-\alpha_t}\varepsilon_{t-1}\\
	&= \sqrt{\alpha_t}(\sqrt{\alpha_{t-1}}x_{t-2} + \sqrt{1-\alpha_{t-1}}\varepsilon_{t-2}) + \sqrt{1-\alpha_t}\varepsilon_{t-1}\\
	&= \sqrt{\alpha_t\alpha_{t-1}}x_{t-2}+\sqrt{\alpha_t(1-\alpha_{t-1})}\varepsilon_{t-2}+\sqrt{1-\alpha_t}\varepsilon_{t-1}
\end{aligned}
$$

这里有 $\varepsilon_i\sim \mathcal{N}(0, 1)$。根据方差的性质

$$
\begin{gathered}
	Var(c\xi+d)=c^2Var\xi\\
	Var\left(\sum_i\xi_i\right)=\sum_iVar\xi_i+2\sum_{i<j}Cov(\xi_i,\xi_j)
\end{gathered}
$$

可知

$$
\begin{aligned}
	&Var(\sqrt{\alpha_t(1-\alpha_{t-1})}\varepsilon_{t-2}+\sqrt{1-\alpha_t}\varepsilon_{t-1})\\
	=\;& Var(\sqrt{\alpha_t(1-\alpha_{t-1})}\varepsilon_{t-2})+Var(\sqrt{1-\alpha_t}\varepsilon_{t-1})\\
	=\;& \alpha_t(1-\alpha_{t-1}) Var(\varepsilon_{t-2}) + (1-\alpha_t)Var(\varepsilon_{t-1})\\
	=\;& \alpha_t(1-\alpha_{t-1}) + (1-\alpha_t)
	= 1-\alpha_t\alpha_{t-1}
\end{aligned}
$$

因此有

$$
x_t=\sqrt{\alpha_t\alpha_{t-1}}x_{t-2}+\sqrt{1-\alpha_t\alpha_{t-1}}\overline{\varepsilon}_{t-2},\quad \overline{\varepsilon}_{t-2}\sim \mathcal{N}(0, 1)
$$

以此类推就会有

$$
x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon
$$

其中 $\overline{\alpha}_t=\prod_{i=1}^t\alpha_i$, $\varepsilon\sim \mathcal{N}(0, 1)$。由于 $\alpha_i\in(0, 1)$，则 $t\to \infty$ 时有 $\overline{\alpha}_t\to 0$，即 $x_t\to \varepsilon\sim \mathcal{N}(0, 1)$。

## Reverse Diffusion Process

$\beta_t$ **足够小时，**$q(x_{t-1}|x_t)$ **也满足 Gaussian 分布。**（Feller, William. "On the theory of stochastic processes, with particular reference to applications." Proceedings of the [First] Berkeley Symposium on Mathematical Statistics and Probability. University of California Press, 1949.）

如果能从 $q(x_{t-1}|x_t)$ 中采样，就可以从纯 $\mathcal{N}(0, 1)$ 高斯噪声中恢复(生成)样本。因此目标是求取 $q(x_{t-1}|x_t)$ ，但是这并不容易，因此需要建立模型用预测分布 $p_\theta$。

$$
\begin{gathered}
	p_{\theta}(X_{0:T})=p(x_T)\prod_{t=1}^Tp_\theta(x_{t-1}|x_t)\\
	p_{\theta}(x_{t-1}|x_t)=\mathcal{N}(\mu_\theta(x_t, t), \Sigma_\theta(x_t, t))
\end{gathered}
$$

如果知道 $x_0$（监督学习），就可以通过 **Bayes 公式**得到

$$
q(x_{t-1}|x_t, x_0)=\mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_tI)
$$

推导如下。首先由 Bayes 公式有

$$
	q(x_{t-1}, x_t| x_0) = 
	q(x_{t-1}|x_t, x_0) q(x_t|x_0) = 
	q(x_t|x_{t-1}, x_0) q(x_{t-1}|x_0)
$$

根据 Markov 过程有 $q(x_t|x_{t-1}, x_0)=q(x_t|x_{t-1})$，因此就有

$$
\begin{aligned}
	q(x_{t-1}|x_t, x_0)
	&= \underbrace{q(x_t|x_{t-1})}
	_{\mathcal{N}(\sqrt{\alpha_t}x_{t-1},(1-\alpha_t)I)} \cdot
		\underbrace{\frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}}_
		{\mathcal{N}(\sqrt{\overline{\alpha}_{t-1}}x_0,(1-\overline{\alpha}_{t-1})I), \;
		\mathcal{N}(\sqrt{\overline{\alpha}_{t}}x_0,(1-\overline{\alpha}_{t})I)}\\
	&\propto \exp\left(-\frac{1}{2}\left(
		\frac{(x_t-\sqrt{\alpha_t}x_{t-1})^2}{1-\alpha_t} +
		\frac{(x_{t-1}-\sqrt{\overline{\alpha}_{t-1}}x_0)^2}{1-\overline{\alpha}_{t-1}} -
		\frac{(x_t-\sqrt{\overline{\alpha}_{t}}x_0)^2}{1-\overline{\alpha}_{t}}\right)\right)
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
	&=\frac{\sqrt{\alpha_t}(1-\overline{\alpha}_{t-1})}{1-\overline{\alpha}_t}x_t + \frac{\sqrt{\overline{\alpha}_{t-1}}\beta_t}{1-\overline{\alpha}_{t}}x_0
\end{aligned}
$$

这里再对一对常数项系数就能验证是否是 Gaussian 分布了，由于前面已经引用了 $\beta_t$ 足够小时近似 Gaussian 分布的结论，这里就不管了。根据前面前向的结论，有 $x_t=\sqrt{\overline{\alpha}_t}x_0 + \sqrt{1-\overline{\alpha}_t}\varepsilon \Rightarrow x_0=\frac{1}{\sqrt{\overline{\alpha}_t}}(x_t-\sqrt{1-\overline{\alpha}_t}\varepsilon)$，代入上式有

$$
\begin{aligned}
	\tilde{\mu}_t
	&=\frac{\sqrt{\alpha_t}(1-\overline{\alpha}_{t-1})}{1-\overline{\alpha}_t}x_t + \frac{\sqrt{\overline{\alpha}_{t-1}}\beta_t}{1-\overline{\alpha}_{t}}\cdot\frac{1}{\sqrt{\overline{\alpha}_t}}(x_t-\sqrt{1-\overline{\alpha}_t}\varepsilon)\\
	&=\frac{1}{\sqrt{\alpha}_t}\left(x_t-\frac{1-\alpha_t}{\sqrt{1-\overline{\alpha}_t}}\varepsilon_t\right)
\end{aligned}
$$ 

