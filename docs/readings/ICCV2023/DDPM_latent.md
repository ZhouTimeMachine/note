<link rel="stylesheet" href="../../../css/counter.css" />

# A Latent Space of Stochastic Diffusion Models for Zero-Shot Image Editing and Guidance

!!! info "Link: [arxiv](https://arxiv.org/abs/2210.05559), [paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wu_A_Latent_Space_of_Stochastic_Diffusion_Models_for_Zero-Shot_Image_ICCV_2023_paper.pdf), [gh-page](https://chenwu.io/stochastic-latent-space/), [code](https://github.com/humansensinglab/cycle-diffusion)"

!!! abstract "Abstract"
    - Claim: Define a **Latent Space** of Stochastic Diffusion Models(**DDPM**)
    - **Zero-shot Image Editing** with DDPM latents
    - **Guidance** with DDPM latents

## Deterministic/Stochastic Denoising

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDPM_latent_1.png" alt="DDPM_latent_1" style="zoom:67%;" />
</div>

!!! info "Latent Space of Diffusion Models"
    - **Deterministic** Diffusion Models(DDIM): ODE-based, size of latent is same as image 
    - **Stochastic** Diffusion Models(DDPM): SDE-based, add noises to latent

In Diffusion Models, when denoising, we have

> Equation (12) in [*Denoising Diffusion Implicit Models*](https://arxiv.org/abs/2010.02502)

$$
    x_{t-1} = \sqrt{\overline{\alpha}_{t-1}}
    \underbrace{\left( \frac{x_t-\sqrt{1-\overline{\alpha}_t}\varepsilon_{\theta}^{(t)}(x_t)}{\sqrt{\overline{\alpha}_t}} \right)}_{\text{“ predicted x0”}}
    + \underbrace{\sqrt{1-\overline{\alpha}_{t-1}-\sigma_t^2}\varepsilon_{\theta}^{(t)}(x_t)}_{\text{“direction pointing to xt”}}
    + \underbrace{\sigma_t \varepsilon_t}_{\text{random noise}}
$$

$\sigma_t^2$ is defined as $\eta \tilde{\beta}_t$。

- When $\eta=1$, that is DDPM
- When $\eta=0$, that is DDIM

!!! tip "Notations in [Lil'Log](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)"
    $$
    \begin{gathered}
        \overline{\alpha}_t=\prod_{i=1}^t\alpha_i=\prod_{i=1}^t(1-\beta_i)\\
        \tilde{\beta}_t=\frac{1-\overline{\alpha}_{t-1}}{1-\overline{\alpha}_t}\beta_t
    \end{gathered}
    $$

Use $z$ to denote latent. In DDIM, we have

$$
\begin{gathered}
    {\color{blue} z := x_T} \sim \mathcal{N}(0, I)\\
    x_{t-1} = \mu_T(x_t, t),\quad t=T,\cdots,1
\end{gathered}
$$

In DDPM, define new latent space:

$$
\begin{gathered}
    {\color{blue} z := x_T\oplus \varepsilon_T \oplus \cdots \oplus \varepsilon_1} \sim \mathcal{N}(0, I)\\
    x_{t-1} = \mu_T(x_t, t) + \sigma_t\odot{\color{blue} \varepsilon_t},\quad t=T,\cdots,1
\end{gathered}
$$

## Application

### Unpaired Image-to-Image Translation

- **Forward Process**: Input $x$ (image of cat), with $t$ condition ("cat")
- **Reverse Process**: Output $\hat{x}$ (image of dog), with $\hat{t}$ condition ("dog")

$$
    {\color{blue} z} \sim 
    \operatorname{DPMEnc}({\color{blue} z}|{\color{red} x},\; G_t),\quad
    {\color{red} \hat{x}} = G_{\hat{t}}({\color{blue} z}).
$$

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDPM_latent_2.png" alt="DDPM_latent_2" style="zoom:80%;" />
</div>

!!! tip "Metrics"
    - FID, KID: Distance between generated images and real images
    - PSNR: Quality
    - SSIM: Similarity

    Details in [Metrics](../miscs/metrics.md).

### Zero-shot Image Editing

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDPM_latent_3.png" alt="DDPM_latent_3" style="zoom:80%;" />
</div>

In DDIM, noise $\varepsilon_{\theta}(x_t, t)$ is predicted by network, but here in DDPM $x_{t-1}$ is firstly sampled, then noise is calculated and denoising continues.

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDPM_latent_4.png" alt="DDPM_latent_4" style="zoom:80%;" />
</div>

$$
\begin{gathered}
    \mathcal{S}_{\text{CLIP}}=\cos\langle \operatorname{CLIP}_{\text{img}}(\hat{x}),\; \operatorname{CLIP}_{\text{text}}(\hat{t}) \rangle\\
    \mathcal{S}_{\text{D-CLIP}}=\cos\langle \operatorname{CLIP}_{\text{img}}(\hat{x}) - \operatorname{CLIP}_{\text{img}}(x),\; \operatorname{CLIP}_{\text{text}}(\hat{t}) - \operatorname{CLIP}_{\text{text}}(t) \rangle
\end{gathered}
$$

!!! tip "Metrics"
    - CLIPScore: Similarity between text and image
    - PSNR: Quality
    - SSIM: Similarity between real image and generated image

    Details in [Metrics](../miscs/metrics.md).

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDPM_latent_5.png" alt="DDPM_latent_5" style="zoom:80%;" />
</div>

### Plug-and-Play Guidance

Given a condition $\mathcal{C}$, define the guided image distribution as energy-based model(EBM):

$$
    p({\color{red} x}|\mathcal{C})\propto p_{\color{red} x}({\color{red} x})e^{-\lambda E({\color{red} x}|\mathcal{C})}
$$

Sampling for ${\color{red} x}\sim p_{\color{red} x}({\color{red} x} | \mathcal{C})$ is equivalent to 

$$
    {\color{blue} z}\sim p_{\color{blue} z}({\color{blue} z} | \mathcal{C}),\quad
    {\color{red} x}=G({\color{blue} z})
$$

Can use any model-agnostic sampler to sample ${\color{blue} z}\sim p_{\color{blue} z}({\color{blue} z} | \mathcal{C})$, the author uses Langevin dynamics:

$$
\begin{gathered}
    {\color{blue} z^{\langle 0 \rangle}}\sim \mathcal{N}(0, I),\quad {\color{blue} z} := {\color{blue} z}^{\langle n \rangle}\\
    {\color{blue} z^{\langle k+1 \rangle}} = {\color{blue} z^{\langle k \rangle}} + 
    \frac{\sigma}{2}\nabla_{\color{blue} z}\left(
        \log_{p_{\color{blue} z}}({\color{blue} z^{\langle k \rangle}}) -
        E(G({\color{blue} z^{\langle k \rangle}}) | \mathcal{C})
    \right) +
    \sqrt{\sigma}\omega^{\langle k \rangle}\\
    \omega^{\langle k \rangle}\sim \mathcal{N}(0, I)
\end{gathered}
$$

The author uses $n=200$, $\sigma=0.05$, and defines a $E_{\text{CLIP}}({\color{red} x}|t)$ for $E({\color{red} x}|\mathcal{C})$: 

$$
    E_{\text{CLIP}}({\color{red} x}|t) = \frac{1}{L}\sum_{l=1}^L \left(
        1-\cos\langle
            \operatorname{CLIP}_{\text{img}}(\operatorname{DiffAug}_l({\color{red} x})),
            \operatorname{CLIP}_{\text{text}}(t)
        \rangle
    \right)
$$

> $\operatorname{DiffAug}_l$ stands for differentiable augmentation that mitigates the adversarial effect

<div style="text-align:center;">
    <img src="../../imgs/ICCV2023/DDPM_latent_6.png" alt="DDPM_latent_6" style="zoom:80%;" />
</div>