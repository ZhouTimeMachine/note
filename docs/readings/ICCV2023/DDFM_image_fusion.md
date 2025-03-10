<link rel="stylesheet" href="../../../css/counter.css" />

# DDFM: Denoising Diffusion Model for Multi-Modality Image Fusion

!!! info "Link: [arxiv](https://arxiv.org/abs/2303.06840), [paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Zhao_DDFM_Denoising_Diffusion_Model_for_Multi-Modality_Image_Fusion_ICCV_2023_paper.pdf), [code](https://github.com/Zhaozixiang1228/MMIF-DDFM)"

!!! abstract "Abstract"
    - Claim: Use **DDPM** for Multi-Modality Image Fusion
    - Image fusion $\to$ **conditional generation**, divided into 2 subproblems
        - **Unconditional generation** problem
        - Maximum likelihood problem
            - modeled in a **hierarchical Bayesian** manner with latent variables
            - inferred by the **expectation-maximization (EM)** algorithm
    - **Training-free**: all we required is an unconditional pre-trained generative model, and no fine-tuning is needed

## Baseline

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_1.png" alt="DDFM_1" style="zoom:67%;" />
</div>

## Get Subproblems

!!! question "Problem"
    The author lists *Infrared-Visible image Fusion* (IVF) and *Medical Image Fusion* (MIF) as application scenarios for this image fusion. Take IVF as an example:

    - $\boldsymbol{i}$: infrared image
    - $\boldsymbol{v}$: visible image
    - $\boldsymbol{f}$: fused image

    The target is to fuse $\boldsymbol{i}$ and $\boldsymbol{v}$ to get $\boldsymbol{f}$ with high quality. 

Recall the reverse SDE of diffusion process:

$$
\mathrm{d} \boldsymbol{f}=\left[-\frac{\beta(t)}{2} \boldsymbol{f}-\beta(t) \nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{f}_t \mid \boldsymbol{i}, \boldsymbol{v}\right)\right] \mathrm{d} t+\sqrt{\beta(t)} \mathrm{d} \overline{\boldsymbol{w}}
$$

and the score function, i.e., $\nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{f}_t \mid \boldsymbol{i}, \boldsymbol{v}\right)$, can be calculated by:

$$
\begin{aligned}
\nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{f}_t \mid \boldsymbol{i}, \boldsymbol{v}\right) 
& =\nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{f}_t\right)+\nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{i}, \boldsymbol{v} \mid \boldsymbol{f}_t\right) \\
& \approx \nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{f}_t\right) + \nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{i}, \boldsymbol{v} \mid \tilde{\boldsymbol{f}}_{0 \mid t}\right)
\end{aligned}
$$

- Equality uses Bayes theorem
- Approximate equality is proved in [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://arxiv.org/abs/2209.14687)

$\nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{f}_t\right)$ represents the score function of unconditional diffusion sampling, which can be readily derived by the **pre-trained DDPM**. In the next section, we explicate the methodology for obtaining 

$$
    \nabla_{\boldsymbol{f}_t} \log p_t\left(\boldsymbol{i}, \boldsymbol{v} \mid \tilde{\boldsymbol{f}}_{0 \mid t}\right)
$$

## Likelihood Rectification

> Use $\boldsymbol{f}$ as an abbr. for $\tilde{\boldsymbol{f}}_{0 \mid t}$

Commonly-used loss function for the image fusion task:

$$
    \min_{\boldsymbol{f}} \|\boldsymbol{f} - \boldsymbol{i}\|_1 + \phi \|\boldsymbol{f} - \boldsymbol{v}\|_1
$$

Use $\boldsymbol{x} = \boldsymbol{f} - \boldsymbol{v}$ and $\boldsymbol{y} = \boldsymbol{i} - \boldsymbol{v}$

$$
    \min_{\boldsymbol{x}}\|\boldsymbol{y} - \boldsymbol{x}\|_1 + \phi\|\boldsymbol{x}\|_1
$$

!!! tip "Optimization Form of Regression"
    Corresponding to the regression model: $\boldsymbol{y} = \boldsymbol{k}\boldsymbol{x} + \boldsymbol{\varepsilon}$, with $\boldsymbol{k}$ fixed to $\boldsymbol{1}$.

The author says, "Accoding to the relationship between **regularization term** and **noise prior distribution**", $\boldsymbol{\varepsilon}$ and $\boldsymbol{x}$ are governed by **Laplacian distribution** ($\mathcal{LAP}$).

$$
\begin{aligned}
p(\boldsymbol{x}) & =\mathcal{L} \mathcal{A} \mathcal{P}(\boldsymbol{x} ; 0, \rho)=\prod_{i, j} \frac{1}{2 \rho} \exp \left(-\frac{\left|x_{i j}\right|}{\rho}\right), \\
p(\boldsymbol{y} \mid \boldsymbol{x}) & =\mathcal{L} \mathcal{A} \mathcal{P}(\boldsymbol{y} ; \boldsymbol{x}, \gamma)=\prod_{i, j} \frac{1}{2 \gamma} \exp \left(-\frac{\left|y_{i j}-x_{i j}\right|}{\gamma}\right),
\end{aligned}
$$

!!! tip "Remark"
    The author wants to transform $\ell_1$-norm optimization into an $\ell_2$-norm optimization with latent variables, avoiding potential non-differentiable points in $\ell_1$-norm.

!!! info "Proposition 1"
    For a random variable $(R V) \xi$ which obeys a **Laplace distribution**, it can be regarded as the coupling of a **normally distributed** $R V$ and an **exponentially distributed** $R V$, which in formula:

    $$
    \mathcal{L} \mathcal{A} \mathcal{P}(\xi ; \mu, \sqrt{b / 2})=\int_0^{\infty} \mathcal{N}(\xi ; \mu, a) \mathcal{EXP} (a ; b) \mathrm{d} a
    $$

Therefore, $p(\boldsymbol{x})$ and $p(\boldsymbol{y} \mid \boldsymbol{x})$ can be rewritten as the following hierarchical Bayesian framework: where $i=1, \ldots, H$ and $j=1, \ldots, W$. 

$$
\begin{cases}
    y_{i j} \mid x_{i j}, m_{i j} \sim \mathcal{N} (y_{i j} ; x_{i j}, m_{i j})\\
    m_{i j} \sim \mathcal{EXP} (m_{i j}; \gamma)\\
    x_{i j} \mid n_{i j} \sim \mathcal{N} (x_{i j} ; 0, n_{i j})\\
    n_{i j} \sim \mathcal{EXP} (n_{i j}; \rho)
\end{cases}
$$

> Through the above probabilistic analysis, the original optimization problem can be transformed into a maximum likelihood inference problem.

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_2.png" alt="DDFM_2" style="zoom:67%;" />
</div>

Ultimately, the **log-likelihood functio**n of the probabilistic inference issue is:

$$
\begin{aligned}
\ell(\boldsymbol{x}) & =\log p(\boldsymbol{x}, \boldsymbol{y})-r(\boldsymbol{x}) \\
& = -\sum_{i, j}\left[\frac{\left(x_{i j}-y_{i j}\right)^2}{2 m_{i j}}+\frac{x_{i j}^2}{2 n_{i j}}\right]-\frac{\psi}{2}\|\nabla \boldsymbol{x}\|_2^2,
\end{aligned}
$$

> Total **variation penalty item** $r(\boldsymbol{x})=\|\nabla \boldsymbol{x}\|_2^2$ is added to make the fusion image $f$ better preserve the texture information from $v$, where $\nabla$ denotes the gradient operator.

## Inference via EM Algorithm

!!! abstract "An Overview of EM Algorithm"

    **E-step**: calculates the conditional expectation of log-likelihood function

    $$
        \mathcal{Q}(\boldsymbol{x} | \boldsymbol{x}^{(t)}) = 
        \mathbb{E}_{\boldsymbol{m}, \boldsymbol{n}\mid \boldsymbol{x}^{(t)}, \boldsymbol{y}}
        [\ell (\boldsymbol{x})]
    $$

    **M-step**: optimizes $\mathcal{Q}$-function

    $$
        \boldsymbol{x}^{(t + 1)} = \mathop{\arg\max}_{\boldsymbol{x}}
        \mathcal{Q}(\boldsymbol{x} | \boldsymbol{x}^{(t)})
    $$

### E-step

!!! info "Proposition 2"
    The conditional expectation of the latent variable $1 / m_{i j}$ and $1 / n_{i j}$ are:

    $$
    \begin{aligned}
    \bar{m}_{i j} = \mathbb{E}_{m_{i j} \mid x_{i j}^{(t)}, y_{i j}}\left[\frac{1}{m_{i j}}\right]
    & =\sqrt{\frac{2\left(y_{i j}-x_{i j}^{(t)}\right)^2}{\gamma}}\\
    \bar{n}_{i j} = \mathbb{E}_{n_{i j} \mid x_{i j}^{(t)}}\left[\frac{1}{n_{i j}}\right] 
    & =\sqrt{\frac{2\left[x_{i j}^{(t)}\right]^2}{\rho}}
    \end{aligned}
    $$

Finally we have

$$
\begin{aligned}
\mathcal{Q} & =-\sum_{i, j}\left[\frac{m_{i j}}{2}\left(x_{i j}-y_{i j}\right)^2+\frac{n_{i j}}{2} x_{i j}^2\right]-\frac{\psi}{2}\|\nabla \boldsymbol{x}\|_2^2 \\
& \propto-\|\boldsymbol{m} \odot(\boldsymbol{x}-\boldsymbol{y})\|_2^2-\|\boldsymbol{n} \odot \boldsymbol{x}\|_2^2-\psi\|\nabla \boldsymbol{x}\|_2^2,
\end{aligned}
$$

> $\odot$ is the elementwise multiplication. $\boldsymbol{m}$ and $\boldsymbol{n}$ are matrices with each element being $\sqrt{\pi_{i j}}$ and $\sqrt{n_{i j}}$, respectively.

### M-step

Here, we need to minimize the negative $Q$-function with respect to $\boldsymbol{x}$. The **half-quadratic splitting algorithm** is employed to deal with this problem, i.e.,

$$
\begin{aligned}
& \min _{\boldsymbol{x}, \boldsymbol{u}, \boldsymbol{k}}\|\boldsymbol{m} \odot(\boldsymbol{x}-\boldsymbol{y})\|_2^2+\|\boldsymbol{n} \odot \boldsymbol{x}\|_2^2+\psi\|\boldsymbol{u}\|_2^2, \\
& \text { s.t. } \boldsymbol{u}=\nabla \boldsymbol{k}, \boldsymbol{k}=\boldsymbol{x} .
\end{aligned}
$$

It can be further cast into the following **unconstraint optimization problem**,

$$
\begin{gathered}
\min _{\boldsymbol{x}, \boldsymbol{u}, \boldsymbol{k}}\|\boldsymbol{m} \odot(\boldsymbol{x}-\boldsymbol{y})\|_2^2+\|\boldsymbol{n} \odot \boldsymbol{x}\|_2^2+\psi\|\boldsymbol{u}\|_2^2 \\
+\frac{\eta}{2}\left(\|\boldsymbol{u}-\nabla \boldsymbol{k}\|_2^2+\|\boldsymbol{k}-\boldsymbol{x}\|_2^2\right) .
\end{gathered}
$$

The unknown variables $\boldsymbol{k}, \boldsymbol{u}, \boldsymbol{x}$ can be solved iteratively in the coordinate descent fashion.

??? general "Details about updates of $\boldsymbol{k}$ and $\boldsymbol{u}$"
    Update $\boldsymbol{k}$ : It is a deconvolution issue,

    $$
    \min _{\boldsymbol{k}} \mathcal{L}_{\boldsymbol{k}}=\|\boldsymbol{k}-\boldsymbol{x}\|_2^2+\|\boldsymbol{u}-\nabla \boldsymbol{k}\|_2^2 .
    $$

    It can be efficiently solved by the **fast Fourier transform (fft)** and **inverse fft (ifft)** operators, and the solution of $k$ is

    $$
    \boldsymbol{k}=\operatorname{ifft}\left\{\frac{\mathrm{fft}(\boldsymbol{x})+\overline{\mathrm{ftt}(\nabla)} \odot \mathrm{fft}(\boldsymbol{u})}{1+\overline{\mathrm{ftt}(\nabla)} \odot \mathrm{fft}(\nabla)}\right\},
    $$

    > $\bar{\cdot}$ is the complex conjugation.

    Update $\boldsymbol{u}$ : It is an $\ell_2$-norm penalized regression issue,

    $$
    \min _u \mathcal{L}_u=\psi\|\boldsymbol{u}\|_2^2+\frac{\eta}{2}\|\boldsymbol{u}-\nabla \boldsymbol{k}\|_2^2 .
    $$

    The solution of $\boldsymbol{u}$ is

    $$
    \boldsymbol{u}=\frac{\eta}{2 \psi+\eta} \nabla \boldsymbol{k} .
    $$

Update $\boldsymbol{x}$ : It is a least squares issue,

$$
\min _{\boldsymbol{x}} \mathcal{L}_{\boldsymbol{x}}=\|\boldsymbol{m} \odot(\boldsymbol{x}-\boldsymbol{y})\|_2^2+\|\boldsymbol{n} \odot \boldsymbol{x}\|_2^2+\frac{\eta}{2}\|\boldsymbol{k}-\boldsymbol{x}\|_2^2 .
$$

The solution of $\boldsymbol{x}$ is

$$
\boldsymbol{x}=\left(2 \boldsymbol{m}^2 \odot \boldsymbol{y}+\eta \boldsymbol{k}\right) \oslash\left(2 \boldsymbol{m}^2+2 \boldsymbol{n}^2+\eta\right),
$$

> $\oslash$ denotes the element-wise division, 

Final estimation of $\boldsymbol{f}$ is

$$
\hat{\boldsymbol{f}}=\boldsymbol{x}+\boldsymbol{v}
$$

Additionally, hyper-parameter $\gamma$ and $\rho$ can be also updated after the sampling from $\boldsymbol{x}$ by

$$
\gamma=\frac{1}{h w} \sum_{i, j} \mathbb{E}\left[m_{i j}\right], \quad
\rho=\frac{1}{h w} \sum_{i, j} \mathbb{E}\left[n_{i j}\right]
$$

## DDFM Algorithm

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_3.png" alt="DDFM_3" style="zoom:67%;" />
</div>

## Experiment on IVF Task

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_4.png" alt="DDFM_4" style="zoom:80%;" />
</div>

??? info "Metrics"
    - EN: entropy
    
    $$
        EN = -\sum_{i=0}^{L-1} p_l\log_2 p_l
    $$

    > $L$ denotes the number of gray levels, $p_l$ is the normalized histogram of the corresponding gray level in the fused image.
    
    - SD: standard deviation

    $$
        SD=\sqrt{\sum_{i=1}^M \sum_{j=1}^N(F(i, j)-\mu)^2}
    $$
    
    > $\mu$ denotes the mean value of the fused image.

    - MI: mutual information
    
    $$
    \begin{gathered}
        MI = MI_{A, F} + MI_{B, F}\\
        MI_{X, F} = \sum_{x, f}p_{X, F}(x, f) \log\frac{p_{X, F}(x, f)}{p_X(f)p_F(f)}
    \end{gathered}
    $$

    > $p_X(x)$ and $p_F(f)$ denote the marginal histograms of source image $X$ and fused image $F$, respectively. 
    > $p_{X, F}(x, f)$ denotes the joint histogram of source image $X$ and fused image $F$

    - VIF: visual information fidelity
    - $Q^{AB/F}$
    
    $$
        Q^{A B / F}=\frac{\sum_{i=1}^N \sum_{j=1}^M Q^{A F}(i, j) w^A(i, j)+Q^{B F}(i, j) w^B(i, j)}{\sum_{i=1}^N \sum_{j=1}^M\left(w^A(i, j)+w^B(i, j)\right)}
    $$

    > $Q^{X F}(i, j)=Q_g^{X F}(i, j) Q_a^{X F}(i, j), Q_g^{X F}(i, j)$ and $Q_a^{X F}(i, j)$ denote the edge strength and orientation values at location $(i, j)$, respectively.
    > $w^X$ denotes the weight that expresses the importance of each source image to the fused image. 
    
    A large $Q^{A B / F}$ means that considerable edge information is transferred to the fused image.
    
    - SSIM: structural similarity index measure

    $$
        SSIM = SSIM(A, F) + SSIM(B, F)
    $$

    Details in *Infrared and visible image fusion methods and applications: A survey*.

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_5.png" alt="DDFM_5" style="zoom:80%;" />
</div>

### Ablation Experiment

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_6.png" alt="DDFM_6" style="zoom:67%;" />
</div>

## Experiment on MIF Task

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_7.png" alt="DDFM_7" style="zoom:67%;" />
</div>

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDFM_8.png" alt="DDFM_8" style="zoom:80%;" />
</div>