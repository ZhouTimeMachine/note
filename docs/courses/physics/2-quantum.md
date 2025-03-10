<link rel="stylesheet" href="../../../css/counter.css" />

# 量子理论

!!! info "Part of note taken on ZJU *Physics Ⅱ (H)*, 2021 Fall & Winter"

## Chap38-1：黑体辐射与光电效应

### 基尔霍夫定律

基尔霍夫定律 (Kirchhoff's Law) 其实就是发射率等于吸收率，$\varepsilon_\lambda=A_\lambda$

发射率：单色辐射强度与相应的黑体辐射的比率

$$
\varepsilon_\lambda=\frac{I_\lambda(\text{emitted})}{B_{\lambda}(T)}
$$

吸收率：吸收的单色光强度与入射光强度的比率

$$
A_\lambda=\frac{I_\lambda(\text{absorbed})}{I_\lambda(\text{incident})}
$$


单色辐射出射度 (Spectral emittance)：单位面积单位时间辐射强度

$$
R_\lambda(T)=\frac{\mathrm dR_\lambda}{\mathrm d\lambda}(W\cdot m^{-3})
$$

辐射出射度 (the totle intensity)：单色辐射出射度对波长的积分

$$
R(T)=\int_0^\infty R_\lambda(T)\mathrm d\lambda(W\cdot m^{-2})
$$



### 斯特藩-玻尔兹曼定律

即 Stefan-Boltzmann Law：

$$
R(T)=\sigma T^4,\quad \sigma=5.67\times 10^{-8}W\cdot m^{-2}\cdot K^{-4}
$$

### 维恩位移定律

即 Wien displacement law：

$$
T\lambda_{\max}=b,\quad b=2.898\times 10^{-3} m\cdot K
$$

当 $T$ 升高时，$\lambda_{\max}$ 将会减小，即蓝移。

维恩公式长波糟糕，瑞丽-金斯公式短波糟糕（紫外灾难）。

### 普朗克辐射公式 (1900)

$$
R(\lambda,T)=\frac{2\pi hc^2}{\lambda^5(e^{\frac{h\nu}{kT}}-1)}, \quad h=6.626\times 10^{-34}J\cdot s
$$

推导：第 $i$ 类量子的能量为 $ih\nu$，根据麦克斯韦-玻尔兹曼分布律，有

$$
N(E)=\frac{2N}{\sqrt{\pi}}\frac{1}{(kT)^{3/2}}E^{1/2}e^{-E/kT}
$$

根据普朗克量子假设，每个能级 $E=ih\nu$，且应该做一个平均积分。直接使用 PPT 上的结论：

$$
N_i=Ne^{-\frac{ih\nu}{kT}}
$$

平均能量为

$$
\overline{\varepsilon}=\frac{\sum ih\nu\cdot N_i}{\sum N_i}=\frac{\displaystyle\sum_{i=0}^\infty ih\nu\cdot Ne^{-\frac{ih\nu}{kT}}}{\displaystyle\sum_{i=0}^\infty Ne^{-\frac{ih\nu}{kT}}}\Rightarrow \overline{\varepsilon}=\frac{h\nu}{e^{\frac{h\nu}{kT}}-1}
$$

在 Rayleigh-Jeans 公式中，令 $kT=\overline{\varepsilon}$，则

$$
R(\lambda,T)=\frac{2\pi}{\lambda^4}kT\cdot c=\frac{2\pi c}{\lambda^4}\frac{h\nu}{e^{\frac{h\nu}{kT}}-1}=\frac{2\pi hc^2}{\lambda^5(e^{\frac{hc}{\lambda kT}}-1)}
$$

在普朗克辐射公式中，令 $\lambda\to0$，$e^{\displaystyle\frac{hc}{\lambda kT}}\gg 1$ 可以得到维恩公式

$$
R(\lambda,T)=\frac{C_1}{\lambda^5}e^{-\frac{C_2}{\lambda T}}
$$

令 $\lambda\to\infty$，$e^{\displaystyle\frac{hc}{\lambda kT}}=1+\dfrac{hc}{\lambda kT}+o(\dfrac{1}{\lambda})$，则得到瑞丽-金斯公式

$$
R(\lambda,T)=\frac{2\pi ckT}{\lambda^4}
$$

### 爱因斯坦光电效应方程

$$
h\nu=K_{\max}+A=\frac{1}{2}mv_{m}^2+A
$$

$A$ 为逸出功。

### 康普顿散射效应

即 The Compton Effect。结论：

$$
\Delta\lambda=\frac{h}{m_0c}(1-\cos\varphi)
$$

康普顿波长 $\lambda_C=\dfrac{h}{m_0c}=0.00243 nm$。

推导：

$$
\begin{cases}
\begin{aligned}
    &m_0c^2+h\nu=mc^2+h\nu'\\
    &(mv)^2=\left(\frac{h\nu}{c}\right)^2+\left(\frac{h\nu'}{c}\right)^2-2\left(\frac{h\nu'}{c}\right)\left(\frac{h\nu}{c}\right)\cos\varphi\\
    &m^2=\frac{m_0^2}{1-\frac{v^2}{c^2}}
\end{aligned}
\end{cases}
$$

首先对第三条方程进行变换，得到

$$
m^2(c^2-v^2)=m_0^2c^2
$$

变换第一条方程得到

$$
m^2c^2=\left(m_0c+\frac{h\nu}{c}-\frac{h\nu'}{c}\right)^2
$$

减去第二条方程，代换得到

$$
m_0c^2=\left(m_0c+\frac{h\nu}{c}-\frac{h\nu'}{c}\right)^2-\left(\dfrac{h\nu}{c}\right)^2-\left(\dfrac{h\nu'}{c}\right)^2+2\left(\dfrac{h\nu'}{c}\right)\left(\dfrac{h\nu}{c}\right)\cos\varphi
$$

化简得到

$$
\Delta\lambda=\lambda'-\lambda=\frac{c}{\nu'}-\frac{c}{\nu}=\dfrac{h}{m_0c}(1-\cos\varphi)=\dfrac{2h}{m_0c}\sin^2\frac{\varphi}{2}
$$

## Chap38-2：物质波

$$
E=h\nu=h\frac{c}{\lambda},\quad p=\frac{h}{\lambda}
$$

因为 $m_0=0$, $E=pc$。

### 德布罗意波

即 de Broglie wave，

$$
\lambda=\frac{h}{p}=\frac{h}{mv}=\frac{h_0}{m_0v}\sqrt{1-\frac{v^2}{c^2}}
$$

$$
\nu=\frac{E}{h}=\frac{mc^2}{h}=\frac{m_0c^2}{h\sqrt{1-\dfrac{v^2}{c^2}}}
$$

### 海森堡不确定性原理

即 Heisenberg’s Uncertainty Principle，

$$
\Delta x\cdot \Delta p\geqslant \frac{\hbar}{2}
$$

不考虑相对论，有

$$
\begin{gathered}
2mE=p^2\\
2m\Delta E=2p\Delta p\\
\Delta E=\frac{p}{m}\Delta p=v\Delta p=
\frac{\Delta x\cdot \Delta p}{\Delta t}
\geqslant \frac{\hbar}{2\Delta t}
\end{gathered}
$$

即有

$$
\Delta E\cdot \Delta t\geqslant \frac{\hbar}{2}
$$

### 概率波

$$
\Psi(x,t)=\psi_0(x)e^{i(kx-\omega t)}
$$

有概率密度

$$
\begin{aligned}
p(x)&=\Psi(x,t)\Psi^*(x,t)\\
&=\psi_0\psi^*_0e^{i(kx-\omega t)}e^{-i(kx-\omega t)}\\
&=|\psi_0|^2
\end{aligned}
$$

概率归一化条件

$$
\int_{-\infty}^{+\infty}p(x)\mathrm{d}x=\int_{-\infty}^{+\infty}\Psi\Psi^*\mathrm{d}x=1
$$

## Chap39-1：薛定谔方程

在波函数

$$
\Psi(x,t)=\psi_0e^{i(kx-\omega t)}
$$

中，根据德布罗意波有

$$
\begin{gathered}
E=h\nu=\frac{h}{2\pi}\omega=\hbar \omega\\
p=\frac{h}{\lambda}=\frac{h}{2\pi}\cdot\frac{2\pi}{\lambda}=\frac{h}{2\pi}k=\hbar k
\end{gathered}
$$

则波函数转化为

$$
\Psi(x,t)=\psi_0\exp\{\frac{i}{\hbar}(px-Et)\}
$$

原始一维薛定谔方程：

$$
i\hbar \frac{\partial \Psi (x,t)}{\partial t}=
\left[-\frac{\hbar}{2m}
\frac{\partial^2}{\partial t^2}+U(x,t)\right]\Psi (x,t)
$$

当 $U(x,t)$ 与 $t$ 无关（变为 $U(x)$），则可以得到一维薛定谔定态方程

$$
\frac{\partial^2 \psi (x)}{\partial x^2}
+\frac{2m}{\hbar}\left[E-U(x)\right]\psi(x)=0
$$

推导：利用如下的式子进行变换

$$
\Psi(x,t)=\psi(x)\exp\{-\frac{E}{\hbar}t\}\\
$$

### 一维自由粒子

$$
U(x)=0
$$

$$
\frac{\partial^2 \psi (x)}{\partial x^2}
+\frac{2mE}{\hbar^2}\psi(x)=0
$$

可以解得 (虽然我用常微分无法理解，2022-1-2 注)

$$
\psi(x)=\psi_0e^{ikx},\quad \psi^*(x)=\psi_0^*e^{-ikx},\quad k=\frac{\sqrt{2mE}}{\hbar}
$$

则 $\psi\psi^*=|\psi_0^2|$，一维自由例子在空间各处分布概率密度相同。

### 一维无限深势阱

即 Infinitely Deep Potential Well，

$$
U(x)=
\begin{cases}
0,&0\leqslant x\leqslant a\\
+\infty,&x< 0 \text{ or } x>a
\end{cases}
$$

那么，$(0,a)$ 之外，都有 $\psi(x)\equiv 0$。只考虑 $x\in [0,a]$，则

$$
\frac{\partial^2 \psi (x)}{\partial x^2}
+\frac{2mE}{\hbar^2}\psi(x)=0
$$

$$
\psi(x)=A\sin kx+B\cos kx
$$

有初值条件

$$
\psi(0)=\psi(a)=0
$$

则

$$
B=0,\quad A\sin ka=0\Rightarrow \sin ka=0\Rightarrow k=\frac{n\pi}{a}
$$

则 $[0,a]$ 上，有

$$
\psi(x)=A\sin\frac{n\pi}{a}x
$$

根据归一化条件有

$$
\begin{aligned}
\int_{-\infty}^{+\infty}\psi(x)\psi^*(x)\mathrm{d}x&=
A^2\int_{-\infty}^{+\infty}\sin^2\frac{n\pi}{a}x\mathrm{d}x\\
&\xlongequal{t=\frac{n\pi x}{a}}\frac{a}{n\pi}A^2\int_0^{n\pi}\frac{1-\cos 2t}{2}\mathrm{d}t\\
&=\frac{a}{n\pi}A^2\frac{n\pi}{2}=1
\end{aligned}
$$

得到 $A=\displaystyle\sqrt{\frac{2}{a}}$

因此一维无限深势阱有波函数

$$
\psi(x)=
\begin{cases}
    \sqrt{\dfrac{2}{a}}\sin\dfrac{n\pi}{a}x,&0<x<a\\
    0,&x\leqslant 0\text{ or }x\geqslant a
\end{cases}
$$

考虑其能量，有

$$
k=\frac{n\pi}{a}=\frac{p}{\hbar}=\frac{\sqrt{2mE}}{\hbar}
$$

所以有

$$
E=\frac{n^2\pi^2\hbar^2}{2ma^2}
$$

### 谐振子

即 The Harmonic Oscillator，

$$
U(x)=\frac{1}{2}kx^2=\frac{1}{2}m\omega^2x^2,\quad \omega=\sqrt{\frac{k}{m}}
$$

解一维薛定谔定态方程，最终可以得到

$$
E_n=(n+\frac{1}{2})\hbar \omega,\quad n=0,1,2,\cdots
$$

### 隧穿效应

即 Tunneling effect, Barrier Tunneling。

传播率 (Transmissivity):

$$
T=\exp\{-\frac{2}{\hbar}\sqrt{2m(U_0-E)}a\}=e^{-2ka},\quad k=\frac{\sqrt{2m(U_0-E)}}{\hbar}
$$

## Chap39-2：氢原子光谱

### 玻尔模型

1. 定态 (stationary state) 假设：$E=E(n)$
2. $h\nu=E_i-E_j$
3. 角动量量子化假设：$L=mvr=n\hbar$

角动量量子化假设可以根据稳定轨道驻波条件推出：

$$
2\pi r=n\lambda=n\frac{h}{mv}
$$

$$
\begin{cases}
    \begin{aligned}
        &\frac{1}{4\pi \varepsilon_0}\frac{e^2}{r^2}=\frac{mv^2}{r}\\
        &mvr=n\hbar
    \end{aligned}
\end{cases}
$$

得

$$
r=\frac{4\pi \varepsilon_0 n^2\hbar^2}{me^2}
=\frac{n^2 \varepsilon_0 h^2}{\pi me^2}
\quad E_n=\frac{1}{2}mv^2-\frac{e^2}{4\pi \varepsilon_0 r}=
-\frac{ke^2}{8\pi \varepsilon_0r}=-\frac{me^4}{8n^2\varepsilon_0^2h^2}
$$

其中基态能量为

$$
E_1=-13.6eV
$$
