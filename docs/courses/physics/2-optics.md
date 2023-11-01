<link rel="stylesheet" href="../../../css/counter.css" />

# 光学

!!! info "Part of note taken on ZJU *Physics Ⅱ (H)*, 2021 Fall & Winter"

!!! warning "本页面还在建设中"

## Chap34：几何光学

费马原理 (Fermat's Principle) 推导反射定律

$$
\begin{gathered}
L=\sqrt{a^2+x^2}+\sqrt{b^2+(d-x)^2}\\
t=\frac{L}{c},\frac{\mathrm dt}{\mathrm dx}=0(Fermat)\Rightarrow\frac{\mathrm dL}{\mathrm dx}=0\\
\therefore \frac{x}{\sqrt{a^2+x^2}}-\frac{d-x}{\sqrt{b^2+(d-x)^2}}=0\\
\therefore\sin\theta_1=\sin\theta_1'\text{, 有 }\theta_1=\theta_1'
\end{gathered}
$$

费马原理推导折射定律

$$
\begin{gathered}
t=\frac{\sqrt{a^2+x^2}}{\dfrac{c}{n_1}}+\frac{\sqrt{b^2+(d-x)^2}}{\dfrac{c}{n_2}}\\
\frac{\mathrm dt}{\mathrm dx}=\frac 1c\left(\frac{n_1x}{\sqrt{a^2+x^2}}-\frac{n_2(d-x)}{\sqrt{b^2+(d-x)^2}}\right)=0\\
n_1\sin\theta_1=n_2\sin\theta_2=C
\end{gathered}
$$

球面镜反射公式

$$
\begin{gathered}
\beta=\alpha+\theta,\gamma=\beta+\theta\\
s\approx u\alpha,s=r\beta,s\approx v\gamma\\
\therefore \frac 1u+\frac 1 v=\frac{\alpha+\gamma}{s}=\frac{2\beta}{s}=\frac{2}{r}=\frac{1}{\dfrac{r}{2}}
\end{gathered}
$$

## Chap36-1：干涉

### 光强与电场

分析光一般主要考虑电场分量。

- 原因1：人眼主要感受光的电场分量
- 原因2：光与物质作用的电场力数量级大于磁场力 $E=cB$，即低速情况下 $\dfrac{v}{c}\ll 1$，故

$$
\vec F=\vec Eq + q\vec v\times \vec B
=\vec E q+q\frac{\vec v}{c}
\times\vec B\approx\vec Eq
$$

本来公式是

$$
I=\overline{S}=\frac{1}{2\mu_0c}E_m^2=\frac{c}{2\mu_0}B_m^2,\quad I\propto E^2\\
$$

光学中常用相对光强 $I=E^2$

### 干涉

干涉 (Interference)

$$
\begin{gathered}
\vec E=\vec E_0\cos(\omega t-kr+\varphi)\\
\text{由 }k=\frac{2\pi}{\lambda}=\frac{2\pi\nu}{\lambda \nu}=\frac{\omega}{c}\\
\vec E_1=\vec E_{01}\cos(\omega_1 t-\frac{\omega_1}{c}r_1+\varphi_1)\\
\vec E_2=\vec E_{02}\cos(\omega_2 t-\frac{\omega_2}{c}r_2+\varphi_2)\\
\vec E_P=\vec E_1+\vec E_2, E_P^2=E_1^2+E_2^2+2E_1\cdot E_2\\
\text{则 }I=E_P^2=E_1^2+E_2^2+2(E_1,E_2)     
\end{gathered}
$$

$(E_1,E_2)=0$ 即正交时，不发生干涉

$(E_1,E_2)\neq 0$，发生干涉

$$
\begin{aligned}
\vec E_1\cdot\vec E_2=&\frac{1}{2}\vec E_{01}\cdot\vec E_{02}\cos(\omega_1t+\varphi_1-kr_1)\cos(\omega_2t+\varphi_2-kr_2)\\
=&\frac{1}{2}\vec E_{01}\cdot\vec E_{02}\{
\cos\left[(\omega_1+\omega_2)t+(\varphi_1+\varphi_2)-\frac{\omega_1r_1+\omega_2r_2}{c}\right]\\
&+\cos\left[(\omega_1-\omega_2)t+(\varphi_1-\varphi_2)\right]-\frac{\omega_1r_1-\omega_2r_2}{c}\}\\
&(k=\frac{2\pi}{\lambda}=\frac{2\pi \nu}{c}=\frac{\omega}{c})
\end{aligned}
$$

我们要考虑一个周期内的有叠加的平均值，即取

$$
\frac{1}{2T}\int_t^{t+2T}\vec E_1\cdot\vec E_2\mathrm dt
$$

### 无干涉情况

1. $\vec E_1\perp \vec E_2$
2. $\omega_1\neq \omega_2$，一个周期叠加平均值=0
3. ($\varphi_1-\varphi_2$) 不是常数

因此相干条件有相同频率、相同偏振(振动)方向、恒定相位差

### 干涉中的光程差计算

光程 $L=nr$，有 $\varphi=2\pi\dfrac{L}{\lambda}$

双缝通过的介质可能有所不同，因此考虑

$$
\begin{aligned}
y_1=E_1=A_1\cos(\omega t-\frac{2\pi}{\lambda_1}r_1+\varphi_1),y_2=A_2\cos(\omega t-\frac{2\pi}{\lambda_2}r_2+\varphi_2)\\
y=y_1+y_2=A\cos(\omega t+\phi)    
\end{aligned}
$$

$$
\begin{aligned}
A&=\sqrt{A_1^2+A_2^2+2A_1A_2\cos\left[(\varphi_1-\varphi_2)-2\pi(\frac{r_1}{\lambda_1}-\frac{r_2}{\lambda_2})\right]}\\
&=\sqrt{A_1^2+A_2^2+2A_1A_2\cos\Delta\varphi}\\
&\phi=\arctan\frac{A_1\sin(\varphi_1-\dfrac{\pi r_1}{\lambda_1})+A_2\sin(\varphi_2-\dfrac{\pi r_2}{\lambda_2})}{A_1\cos(\varphi_1-\dfrac{\pi r_1}{\lambda_1})+A_2\cos(\varphi_2-\dfrac{\pi r_2}{\lambda_2})}
\end{aligned}
$$

考虑初相位相同，则 $\varphi_1=\varphi_2$

考虑同一介质，则 $\lambda_1=\lambda_2$

$$
\begin{aligned}
\Delta\varphi&=\frac{2\pi}{\lambda}(r_2-r_1)\\
\Delta\varphi&=\begin{cases}
\pm 2m\pi,&\to A_{max}\\
\pm(2m+1)\pi,&\to A_{min}
\end{cases}    
\end{aligned}
$$


考虑不同介质，则

$$
\begin{gathered}
\Delta\varphi=\frac{2\pi}{\dfrac{\lambda}{n_2}}r_2-\frac{2\pi}{\dfrac{\lambda}{n_1}}r_1=\frac{2\pi}{\lambda}(n_2r_2-n_1r_1)=\frac{2\pi}{\lambda}\delta\\
\delta=\begin{cases}
\pm m\lambda,&\to A_{max}\\
\pm (2m+1)\dfrac{\lambda}{2},&\to A_{min}
\end{cases}        
\end{gathered}
$$

### 杨氏双缝干涉

$$
\begin{gathered}
\delta=r_2-r_1=d\sin\theta\approx d\tan\theta=\frac{xd}{D}=\begin{cases}
\pm m\lambda,&\to A_{max}\\
\pm (2m+1)\dfrac{\lambda}{2},&\to A_{min}
\end{cases}\\
\Delta x=\frac{D\lambda}{d}        
\end{gathered}
$$

### 干涉光强问题

$$
\begin{gathered}
\varphi_1=\varphi_0-\frac{2\pi r_1}{\lambda},\;
\varphi_2=\varphi_0-\frac{2\pi r_2}{\lambda}\\
I=I_1+I_2+2\sqrt{I_1I_2}\cos(\varphi_2-\varphi_1)\\
\end{gathered}
$$

近轴条件且双缝等宽，有 $I_1=I_2=I_0$，因此

$$
I=2I_0[1+\cos(\varphi_2-\varphi_1)]
=4I_0\cos^2\frac{\varphi_2-\varphi_1}{2}
$$

### 等倾干涉

等倾干涉 (Equal Inclination Interference)，考虑光疏到光密

$$
n_1\sin i=n_2\sin r
$$

$$
\begin{aligned}
\delta=&\frac{n_2\Delta x}{\sin r}-n_1\Delta x\sin i+\frac{\lambda}{2}\\
=&\Delta x\left(\frac {n_2^2}{n_1\sin i}-n_1\sin i\right)+\frac{\lambda}{2}\\
=&\left(2d\frac{\sin r}{\cos r}\right)\frac{n_2^2-n_1^2\sin^2 i}{n_2\sin r}+\frac{\lambda}{2}\\
=&2d\frac{n_2^2-n_1^2\sin^2 i}{n_2\sqrt{1-\sin^2r}}+\frac{\lambda}{2}\\
=&2d\frac{n_2^2-n_1^2\sin^2 i}{\sqrt{n_2^2-n_1^2\sin^2i}}+\frac{\lambda}{2}\\
=&2d\sqrt{n_2^2-n_1^2\sin^2i}+\frac{\lambda}{2}
\end{aligned}
$$

### 等厚干涉

等厚干涉 (Equal Thickness Interference) 比较简单，按情况分析

#### 牛顿环

牛顿环即 The Newton's Ring

$$
\delta=2e_m+\frac{\lambda}{2}=
\begin{cases}
m\lambda&\max\\
(2m+1)\frac{\lambda}{2}&\min
\end{cases}
$$

$e_m$ 为厚度，$\frac{\lambda}{2}$ 为半波损失。而

$$
r^2=R^2-(R-e_m)^2=2e_mR+e_m^2\approx 2e_mR
(R\gg e_m)
$$

$$
\begin{gathered}
\therefore 
e_m=\frac{r^2}{2R}\\
r=\sqrt{\frac{2m-1}{2}\lambda R},\quad \max\\
r=\sqrt{m\lambda R},\quad \min  
\end{gathered}
$$

### 时间相干性和空间相干性

#### 时间相干性

时间相干性即 Coherence of Time。

波列长度 $L=\tau c$，其中 $\tau$ 为脉冲寿命，$c$ 为光速

最小波列长度 $L_c$

$$
L_c=\frac{\lambda^2}{\Delta \lambda}
$$

$\Delta \lambda$ 表征单色性。

推导：令 $\lambda+\Delta\lambda$ 光的第 $k$ 级与 $\lambda$ 光的第 $k+1$ 级重合

$$
\delta=k(\lambda+\Delta\lambda)=(k+1)\lambda
\Rightarrow k=\frac{\lambda}{\Delta \lambda}
$$

回代得

$$
\delta=\frac{\lambda^2}{\Delta\lambda}+\lambda\approx\frac{\lambda^2}{\Delta\lambda}
$$

则可以取 $L_c=\delta=\displaystyle\frac{\lambda^2}{\Delta\lambda}$

#### 空间相干性

空间相干性即 Coherence of Space。

单缝 + 双缝结构，单缝到双缝距离为 $D'$，单缝缝宽 $a$ 不能太大。

几何关系，考虑近轴条件有

$$
\frac{OP}{D}=\frac{a/2}{D'}
$$

其中 $D$ 是双缝到屏的距离，$OP$ 是因为单缝缝宽造成的中心明纹的偏移。

临界态，中心明纹最大偏移量是 $OP_{\max}=\frac{1}{2}\Delta x=
\frac{1}{2}\frac{D}{d}\lambda$，即偏移后中心明纹在原一级暗纹处，有

$$
a=\frac{2OP_{\max}}{D}D'=\frac{D'}{d}\lambda
$$

## Chap36-2：衍射
Chapters/36-2.tex
## Chap36-3：光栅与光谱
Chapters/36-3.tex
## Chap36-4：偏振
Chapters/36-4.tex