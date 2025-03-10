<link rel="stylesheet" href="../../../css/counter.css" />

# 静电场

!!! info "Part of note taken on ZJU *Physics Ⅱ (H)*, 2021 Fall & Winter"

## Chap22-1：库仑定律

### 均匀带电圆环
$$
\begin{aligned}
F&=\frac{q_0}{4\pi \epsilon_0}\int\frac{\mathrm{d}q}{|r|^2}\frac{z}{|r|}\\
&=\frac{q_0}{4\pi \epsilon_0}\int\frac{z}{(z^2+R^2)^\frac{3}{2}}\frac{q}{2\pi R}R\mathrm{d}\varphi\\
&=\frac{q_0q}{4\pi \epsilon_0}\frac{z}{(z^2+R^2)^\frac{3}{2}}\\
&\approx\frac{q_0q}{4\pi \epsilon_0}\frac{1}{z^2}(when\quad z\gg R)(\vec{k})
\end{aligned}
$$

物理上，即退化为点电荷间库仑定律。

### 均匀带电圆盘
$$
\begin{aligned}
F&=\frac{q_0}{4\pi \epsilon_0}\int_0^R\frac{z}{(z^2+r^2)^\frac{3}{2}}\sigma2\pi r\mathrm{d}r\\
&=\frac{q_0}{4\epsilon_0}\frac{q}{\pi R^2}\int_0^R\frac{zd(z^2+r^2)}{(z^2+r^2)^\frac{3}{2}}\\
&=\frac{q_0q}{4\pi \epsilon_0R^2}(-2)\frac{z}{\sqrt{z^2+r^2}}\bigg|^R_0\\
&=\frac{q_0q}{2\pi \epsilon_0R^2}\left(1-\frac{z}{\sqrt{z^2+R^2}}\right)(\vec{k})\\
&=\frac{q_0q}{2\pi \epsilon_0R^2}\left(1-\frac{1}{\sqrt{1+(\frac{R}{z})^2}}\right)\\
&=\frac{q_0q}{2\pi \epsilon_0R^2}\left(1-1+\frac{1}{2}(\frac{R}{z})^2-\frac{3}{8}(\frac{R}{z})^4\cdots\right)\\
&\approx\frac{q_0q}{4\pi \epsilon_0}\frac{1}{z^2}(when\quad z\gg R)(\vec{k})\\
&\approx\frac{q_0q}{2\pi \epsilon_0R^2}(when\quad R\gg z)=\frac{\sigma}{2\epsilon_0}q_0(\vec k)
\end{aligned}
$$

### 均匀带电球体
$$
\begin{aligned}
\mathrm{d}F&=\frac{q_0}{4\pi\epsilon_0}\frac{(z-R\cos\theta)\sigma(2\pi R\sin\theta\cdot R\mathrm{d}\theta)}{[(z-R\cos\theta)^2+(R\sin\theta)^2]^\frac{3}{2}}\\
&=\frac{q_0R^2}{2\epsilon_0}\sigma\frac{(z-R\cos\theta)\sin\theta\mathrm{d}\theta}{(z^2+R^2-2zR\cos\theta)^\frac{3}{2}}\\
&=\frac{q_0q}{8\pi\epsilon_0}\frac{(z-R\cos\theta)\sin\theta}{(z^2+R^2-2zR\cos\theta)^\frac{3}{2}}\mathrm{d}\theta(\sigma=\frac{q}{4\pi R^2})
\end{aligned}
$$

$$
\begin{aligned}
F&=\frac{q_0q}{8\pi\epsilon_0}\int_0^\pi\frac{(z-R\cos\theta)\sin\theta}{(z^2+R^2-2zR\cos\theta)^\frac{3}{2}}\mathrm{d}\theta\\
&\xlongequal{t=-R\cos\theta}\frac{q_0q}{8\pi\epsilon_0R}\int_{-R}^R\frac{z+t}{(z^2+R^2+2zt)^\frac{3}{2}}\mathrm{d}t\\
&=-\frac{q_0q}{8\pi\epsilon_0Rz}\int_{-R}^R(z+t)\mathrm{d}\frac{1}{\sqrt{z^2+R^2+2zt}}\\
&=-\frac{q_0q}{8\pi\epsilon_0Rz}\left(\frac{z+t}{\sqrt{z^2+R^2+2zt}}\bigg|_{-R}^R-\int_{-R}^R\frac{\mathrm{d}t}{\sqrt{z^2+R^2+2zt}}\right)\\
&=-\frac{q_0q}{8\pi\epsilon_0Rz}\left(1-\frac{z-R}{|z-R|}-\frac{1}{z}\sqrt{z^2+R^2+2zt}\bigg|_{-R}^R\right)\\
&=-\frac{q_0q}{8\pi\epsilon_0Rz}\left(1-\frac{z-R}{|z-R|}-\frac{(z+R)-|z-R|}{z}\right)\\
&=\left\{\begin{matrix}
\dfrac{q_0q}{4\pi\epsilon_0}\dfrac{1}{z^2},z>R\\
0,z<R
\end{matrix}\right.
\end{aligned}
$$

### 均匀带电直线
$$
\begin{aligned}
F&=\int_{-L}^L\frac{q_0\lambda\mathrm{d}l}{4\pi\epsilon_0}\frac{1}{z^2+l^2}\frac{z}{\sqrt{z^2+l^2}}\\
&=\frac{q_0q}{8\pi\epsilon_0L}\int_{-L}^L\frac{z}{(z^2+l^2)^{\frac{3}{2}}}\mathrm{d}l\\
&\xlongequal{l=z\tan\theta}\frac{q_0q}{8\pi\epsilon_0L}\int_{-\arctan\frac{L}{z}}^{\arctan\frac{L}{z}}\frac{\cos^3\theta}{z^2}\cdot z\frac{\mathrm{d}\theta}{\cos^2\theta}\\
&=\frac{q_0q}{8\pi\epsilon_0Lz}\int_{-\arctan\frac{L}{z}}^{\arctan\frac{L}{z}}\cos\theta\mathrm{d}\theta\\
&=\frac{q_0q}{4\pi\epsilon_0}\frac{1}{z\sqrt{L^2+z^2}}(\vec{k})\\
&\approx\left\{\begin{matrix}
\dfrac{q_0q}{4\pi\epsilon_0}\dfrac{1}{z^2},z\gg L\\
\dfrac{q_0q}{4\pi\epsilon_0}\dfrac{1}{L}=\dfrac{\lambda}{2\pi\epsilon _0}\dfrac{q_0}{z},z\ll L
\end{matrix}\right.
\end{aligned}
$$

### 均匀带电平面
$$
\begin{aligned}
F&=\int_{-b}^b\frac{q_0(\sigma\cdot2L\mathrm{d}x)}{4\pi\epsilon_0}\frac{1}{\sqrt{x^2+z^2+L^2}\sqrt{x^2+z^2}}\cdot\frac{z}{\sqrt{x^2+z^2}}\\
&=\int_{-b}^b\frac{q_0}{2\pi\epsilon_0}\frac{q}{4bL}\cdot\frac{z}{x^2+z^2}\mathrm{d}x(L\gg b, z)\\
&=\int_{-b}^b\frac{q_0q}{8\pi b\epsilon_0L}\cdot\frac{1}{(\frac{x}{z})^2+1}\mathrm{d}\frac{x}{z}\\
&=\frac{q_0q}{8\pi b\epsilon_0L}\cdot\arctan\frac{x}{z}\bigg|^b_{-b}\\
&=\frac{q_0q}{4\pi b\epsilon_0L}\arctan\frac{b}{z}(\vec k)\\
&=\frac{q_0\sigma}{\pi \epsilon_0}\arctan\frac{b}{z}\xlongequal{b\gg z}\frac{\sigma}{2\epsilon_0}q_0
\end{aligned}
$$


## Chap22-2、23：高斯定理

### Maxwell 方程组

静电场有源无旋，静磁场有旋无源

$$
\begin{aligned}
&\left\{\begin{matrix}
\nabla\times\mathbf{H}=\boldsymbol j+\dfrac{\partial\mathbf{D}}{\partial t}\\
\nabla\times\mathbf{E}=-\dfrac{\partial\mathbf{B}}{\partial t}\\
\nabla\cdot\mathbf{B}=0\\
\nabla\cdot \mathbf{D}=\rho
\end{matrix}\right.(\text{微分形式})\\
&\left\{\begin{matrix}
\displaystyle\oint_l\mathbf{H}\cdot \mathrm d\boldsymbol{l}=\int_S\boldsymbol j\cdot\mathrm d\mathbf S+\int_S\frac{\partial\mathbf{D}}{\partial t}\cdot\mathrm d\mathbf S\\
\displaystyle\oint_l\mathbf{E}\cdot\mathrm d\boldsymbol{l}=-\int_S\dfrac{\partial\mathbf{B}}{\partial t}\cdot\mathrm d\mathbf S\\
\displaystyle\oint_S\mathbf{B}\cdot\mathrm d\boldsymbol{S}=0\\
\displaystyle\oint_S\mathbf{D}\cdot\mathrm d\boldsymbol{S}=\int_V\rho\cdot\mathrm dV
\end{matrix}\right.(\text{积分形式})
\end{aligned}
$$

其中 

$$
\mathbf{D}=\epsilon \mathbf{E}, \quad
\mathbf{B}=\mu \mathbf{H}, \quad
\mathbf{j}=\sigma \mathbf{E}
$$

- 第一条，安培环路 $\Rightarrow$ 全电流定律，传导电流 + 位移电流
- 第二条，电磁感应定律
- 第三条，磁通连续性原理(磁场高斯定律)
- 第四条，电场高斯定律

### 电偶极子

即 A Charged Electric Dipole

$$
\begin{aligned}
\vec p&=q\vec d\\
\vec r_\pm&=(r\cos\varphi\mp\frac{d}{2})\hat i+r\sin\varphi \hat j\\
\vec r_\pm^2&=r^2\mp rd\cos\varphi+\frac{d^2}{4}\approx r^2\mp rd\cos\varphi(r\gg d)\\
\vec E_p&=\frac{1}{4\pi\epsilon_0}\left[\frac{q\vec r_+}{r_+^3}+\frac{(-q)\vec r_-}{r_-^3}\right]\\
&=\frac{q}{4\pi\epsilon_0}\left[\frac{(r\cos\varphi-\frac{d}{2})\hat i+r\sin\varphi \hat j}{(r^2-rd\cos\varphi)^{\frac{3}{2}}}-\frac{(r\cos\varphi+\frac{d}{2})\hat i+r\sin\varphi \hat j}{(r^2+rd\cos\varphi)^{\frac{3}{2}}}\right]\\
&=\frac{q}{4\pi\epsilon_0}[\frac{(r\cos\varphi-\frac{d}{2})\hat i+r\sin\varphi \hat j}{r^3}(1-\frac{3d}{2r}\cos\varphi)-\\
&\quad\quad\quad\quad\frac{(r\cos\varphi+\frac{d}{2})\hat i+r\sin\varphi \hat j}{r^3}(1+\frac{3d}{2r}\cos\varphi)]\\
&\left((r^2\pm rd\cos\varphi)^{-\frac{3}{2}}=r^{-3}(1\pm\frac{d}{r}\cos\varphi)^{-\frac{3}{2}}\approx r^{-3}(1\mp\frac{3d}{2r}\cos\varphi)\right)\\
&=\frac{q}{4\pi\epsilon_0r^3}\left[3d\cos\varphi(\cos\varphi\hat i+\sin\varphi \hat j)-d\hat i\right]\\
&=\frac{1}{4\pi\epsilon_0r^3}\left[\frac{3\vec r(\vec r\cdot \vec p)}{r^2}-\vec p\right]\\
&=\left\{\begin{matrix}
\dfrac{\vec p}{2\pi\epsilon_0 r^3},x\quad axis\\
-\dfrac{\vec p}{4\pi\epsilon_0 r^3},y\quad axis\\
\end{matrix}\right.
\end{aligned}
$$

$$
\begin{aligned}
E\cdot 2\pi rh&=\frac{\lambda_1h}{\epsilon_0}\Rightarrow E=\frac{\lambda_1}{2\pi\epsilon_0 r}\\
F&=\int_L^{2L}\frac{\lambda_1}{2\pi\epsilon_0 r}\lambda_2\mathrm{d}r\\
&=\frac{\lambda_1\lambda_2}{2\pi\epsilon_0}\int_L^{2L}\frac{\mathrm{d}r}{r}\\
&=\frac{\lambda_1\lambda_2}{2\pi\epsilon_0}\ln 2
\end{aligned}
$$

### 立体角定义
$$
\mathrm{d}\Omega=\frac{\hat r\mathrm{d}\vec S}{r^2}
$$

### 静电场高斯定理推导
$$
\mathrm d\phi=\vec E\cdot \mathrm d\vec A=\frac{q}{4\pi\epsilon_0r^2}(r^2\mathrm d \Omega)=\frac{q}{4\pi \epsilon_0}\mathrm d\Omega
$$

$$
\oint\vec E\cdot\mathrm d\vec A=\phi=\oint\frac{q}{4\pi \epsilon_0}\mathrm d\Omega=\frac{q}{4\pi \epsilon_0}\cdot4\pi=\frac q {\epsilon_0}
$$

多个点电荷，叠加原理即可，即最后有

$$
\oint\vec E\cdot\mathrm d\vec A=\frac {\sum q_i}{\epsilon_0}
$$

### Examples

Example 4

$$
\begin{aligned}
&E(x)(2S)=\frac{\displaystyle2\int_0^x\rho_0xS\mathrm dx}{\epsilon_0}\Rightarrow E(x)=\frac{\rho_0x^2}{2\epsilon_0}(x\in(-b,b))\\
&E(x)=\frac{\sigma}{2\epsilon_0}=\frac{\displaystyle2\int_0^b\rho_0x\mathrm dx}{2\epsilon_0}=\frac{\rho_0b^2}{2\epsilon_0}(|x|>b)\\
\end{aligned}
$$

Example 5

$$
\begin{aligned}
&r\in[R_1,R_2],E(2\pi rh)=\frac{-\sigma(2\pi R_1h)}{\epsilon_0}\Rightarrow E=-\frac{\sigma R_1}{\epsilon_0r}\\
&r>R_2,E(2\pi rh)=\frac{-\sigma(2\pi R_1h)+\sigma(2\pi R_2h)}{\epsilon_0}\Rightarrow E=\frac{\sigma (R_2-R_1)}{\epsilon_0r}\\
&\therefore E(r)=\left\{\begin{matrix}
0,r\in(0,R_1)\\
-\dfrac{\sigma R_1}{\epsilon_0r},r\in(R_1,R_2)\\
\dfrac{\sigma (R_2-R_1)}{\epsilon_0r},r\in(R_2, +\infty)
\end{matrix}\right.
\end{aligned}
$$

## Chap24：电势

### 电势的导出

$$
\begin{aligned}
W_{a\to b}&=\int_{a,C}^b(q_0\vec E)\cdot\mathrm d\vec l\\
&=\frac{q_0q}{4\pi\epsilon_0}\int_{a,C}^b\frac{\vec r\cdot\mathrm d\vec l}{r^3}
&\text{(库仑定律)}\\
&=\frac{q_0q}{4\pi\epsilon_0}\int_{r_a,C}^{r_b}\frac{\mathrm dr}{r^2}
&(\vec r\cdot \mathrm d\vec l=r\mathrm d l\cos \theta\approx r\mathrm dr)\\
&=\frac{q_0q}{4\pi\epsilon_0}\left(\frac{1}{r_a}-\frac{1}{r_b}\right)
&\text{(只与初末位置有关)}
\end{aligned}
$$

多个电荷，则叠加即可，则

$$
W_{a\to b}=\frac{q_0\sum q_i}{4\pi\epsilon_0}\left(\frac{1}{r_a}-\frac{1}{r_b}\right)
$$

电势的导出

$$
V_b-V_\infty=-\frac{W_{\infty\to b}}{q_0}=-\int_{\infty}^b\vec E\cdot\mathrm d\vec s=\int_b^\infty\vec E\cdot\mathrm d\vec s
$$

某点电势等于 E 从该点到无穷远的线积分

三电荷系统电势能

$$
\begin{aligned}
U&=\frac{1}{2}\frac{1}{4\pi\epsilon_0}\left[q_1(\frac{q_2}{r_{12}}+\frac{q_3}{r_{13}})+q_2(\frac{q_1}{r_{12}}+\frac{q_3}{r_{23}})+q_3(\frac{q_1}{r_{13}}+\frac{q_2}{r_{23}})\right]\\
&=\frac{1}{4\pi\epsilon_0}\left[\frac{q_1q_2}{r_{12}}+\frac{q_1q_3}{r_{13}}+\frac{q_2q_3}{r_{23}}\right]\\
&=\frac{1}{4\pi\epsilon_0}\sum_{i<j,i,j\in\{1,2,3\}}\frac{q_iq_j}{r_{ij}}
\end{aligned}
$$

### Examples

A Charged Electric Dipole（电偶极子）

$$
\begin{aligned}
V&=\frac{1}{4\pi\epsilon_0}\left(\frac{q}{r_+}+\frac{-q}{r_-}\right)\\
&=\frac{q}{4\pi\epsilon_0}\frac{r_--r_+}{r_+r_-}\\
&\approx\frac{q}{4\pi\epsilon_0}\frac{d\cos\theta}{r_+r_-}\\
&(r\gg d，r_--r_+\approx d\cos\theta)\\
&\approx\frac{1}{4\pi\epsilon_0}\frac{qd\cos\theta}{r^2}\\
&\left(r_+r_-\approx (r-\frac d 2\cos\theta)(r+\frac d 2\cos\theta)=r^2-\frac{d^2\cos\theta^2} 4\approx r^2\right)\\
&=\frac{1}{4\pi\epsilon_0}\frac{p\cos\theta}{r^2}\\
&=\frac{1}{4\pi\epsilon_0}\frac{p\cdot r}{r^3}
\end{aligned}
$$

电偶极子在匀强电场受到的力矩

$$
\begin{gathered}
    \vec F = q\vec E \\
    \tau = \vec r\times\vec F=q\vec r\times\vec F=\vec p\times\vec F
\end{gathered}
$$

Example5 An Charged Ring

$$
\vec E=\frac{1}{4\pi\epsilon_0}\frac{qz}{(R^2+z^2)^{\frac 3 2}}\hat k\\
$$

$$
\begin{aligned}
V&=\int_z^\infty\frac{1}{4\pi\epsilon_0}\frac{qh}{(R^2+h^2)^{\frac 3 2}}\mathrm dh\\
&=\frac{q}{8\pi\epsilon_0}\int_z^\infty\frac{\mathrm d(R^2+h^2)}{(R^2+h^2)^{\frac 3 2}}\\
&=\frac{q}{4\pi\epsilon_0\sqrt{R^2+z^2}}=\frac{\lambda R}{2\epsilon_0\sqrt{R^2+z^2}}
\end{aligned}
$$

Example6 A Charged Disk

根据 Example5 的结论，直接积分即可。

$$
\begin{aligned}
V&=\int_0^R\frac{\frac{q}{\pi R^2}(2\pi r\mathrm dr)}{4\pi\epsilon_0\sqrt{r^2+z^2}}\\
&=\frac{q}{4\pi\epsilon_0R^2}\int_0^R\frac{\mathrm d(r^2+z^2)}{\sqrt{r^2+z^2}}\\
&=\frac{q}{2\pi\epsilon_0R^2}(\sqrt{R^2+z^2}-z)\\
&=\frac{\sigma}{2\epsilon_0}(\sqrt{R^2+z^2}-z)
\end{aligned}
$$


Example7 A Charged Spherical Shell

$$
\frac{1}{4\pi\epsilon_0}\frac{q}{R}\text{, 定义积分/对球心计算}
$$