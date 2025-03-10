<link rel="stylesheet" href="../../../css/counter.css" />

# 电流

!!! info "Part of note taken on ZJU *Physics Ⅱ (H)*, 2021 Fall & Winter"

## Chap27：电流

### 电流密度电子漂移模型

$$
\begin{gathered}
    I=\frac{\mathrm dq}{\mathrm dt}=\frac{n(\Delta S\cdot v\mathrm dt)e}{\mathrm dt}=ne(\Delta S)v\\
    j=\frac{I}{\Delta S}=nev\\
\end{gathered}
$$

考虑电子运动方向，则 $\vec{j}=-ne\vec{v}$

### 欧姆定律微分形式

欧姆定律 (Ohm's Law) 微分形式：$j=\sigma E$

$$
\begin{aligned}
j\mathrm d S=\mathrm dI&=-\frac{\mathrm d U}{\mathrm dR}\\
&=-\frac{\mathrm dU}{\rho\frac{\mathrm d l}{\mathrm d S}}\\
&=(-\frac{\mathrm dU}{\mathrm dl})\cdot\frac{1}{\rho}\cdot\mathrm dS\\
&=\frac{E}{\rho}\mathrm dS
\end{aligned}
$$

那么就有

$$
j = \frac{E}{\rho}=\sigma E \quad (\sigma=\frac{1}{\rho})
$$

### 焦耳定律微分形式

焦耳定律 (Joule's Law) 微分形式：$w=\sigma^2E$

$$
\begin{aligned}
Q&=I^2R\Delta t\\
\mathrm{d}Q&=(j\mathrm{d}S)^2(\rho\frac{\mathrm{d}l}{\mathrm{d}S})\mathrm{d}t\\
&=j^2\rho(\mathrm{d}S\mathrm{d}l)\mathrm{d}t\\
&=(\sigma^2 E^2)\frac{1}{\sigma}\mathrm{d}V\mathrm{d}t\\
&=\sigma E^2\mathrm{d}V\mathrm{d}t
\end{aligned}
$$

那么就有

$$
w = \frac{\mathrm{d}Q}{\mathrm{d}V\mathrm{d}t}=\sigma E^2
$$

### 金属的 Drude 模型

先算速度 $v_i=v_{0i}+at=v_{0i}+\frac{eE}{m}t_i$，而

$$
\begin{aligned}
j&=ne\bar v=\sum_{i=1}^nev_i=\sum_{i=1}^nv_{0i}+\sum_{i=1}^n\frac{e^2E}{m}t_i\\
&=\sum_{i=1}^n\frac{e^2E}{m}t_i\text{ (初始速度任意)}
\end{aligned}
$$

根据平均时间 $\displaystyle \tau = \frac{\sum_{i=1}^nt_i}{n}$，有

$$
j = \frac{ne^2\tau}{m}E=\sigma E\Rightarrow \sigma=\frac{ne^2\tau}{m}
$$

根据麦克斯韦速度分布律

$$
\tau = \frac{\lambda}{\bar v}=\lambda\sqrt{\frac{\pi m}{8kT}}\propto\frac{1}{\sqrt T}
$$

所以有 $\sigma\propto\frac{1}{\sqrt T}\Rightarrow\rho\propto\sqrt T$。该模型与实际符合得不是很好。

## Chap28：电路

### RC 电路（充电）

即 $\epsilon$ 充电。

$$
\begin{aligned}\mathrm{d}
\epsilon-iR-\frac{q}{C}&=0\\
R\mathrm{d}q&=\left(\epsilon-\frac{q}{C}\right)\mathrm{d}t\\
\frac{\mathrm{d}q}{C\epsilon-q}&=\frac{\mathrm dt}{CR}\\
\ln|C\epsilon-q|&=-\frac{t}{CR}+C\\
C\epsilon-q&=Ae^{-\frac{t}{CR}}\\
\text{当 }t=0&,q=0\Rightarrow A=C\epsilon\\
q&=C\epsilon(1-e^{-\frac{t}{CR}})\\
\text{令 }\tau=RC\text{，则 }q(t)&=C\epsilon(1-e^{-\frac{t}{\tau}})\\
i(t)&=\frac{\epsilon}{R}e^{-\frac{t}{\tau}}\\
\Delta V_C(t)&=\frac{q(t)}{C}=\epsilon(1-e^{-\frac{t}{\tau}})\
\end{aligned}
$$

### RC 电路（放电）

$$
\begin{aligned}
\frac{q}{C}&=R\frac{\mathrm dq}{\mathrm dt}\\
\ln q&=\frac{t}{\tau}+C\\
q&=Ae^{\frac{t}{\tau}}\\
\text{当 }t=0&,q=C\epsilon\Rightarrow A=C\epsilon\\
q(t)&=C\epsilon e^{\frac{t}{\tau}}\\
i(t)&=\frac{\epsilon}{R}e^{-\frac{t}{\tau}}\\
\Delta V_C(t)&=\frac{q(t)}{C}=\epsilon(1-e^{-\frac{t}{\tau}})\
\end{aligned}
$$