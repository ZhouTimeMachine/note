<link rel="stylesheet" href="../../css/counter.css" />

# Physics Ⅱ Review

!!! info "Note taken on ZJU *Physics Ⅱ (H)*, 2021 Fall & Winter"

!!! warning "本页面还在建设中"

## 静电场

### Chap22-1：库仑定律

#### 均匀带电圆环
$$
\begin{aligned}
F&=\frac{q_0}{4\pi \epsilon_0}\int\frac{\mathrm{d}q}{|r|^2}\frac{z}{|r|}\\
&=\frac{q_0}{4\pi \epsilon_0}\int\frac{z}{(z^2+R^2)^\frac{3}{2}}\frac{q}{2\pi R}R\mathrm{d}\varphi\\
&=\frac{q_0q}{4\pi \epsilon_0}\frac{z}{(z^2+R^2)^\frac{3}{2}}\\
&\approx\frac{q_0q}{4\pi \epsilon_0}\frac{1}{z^2}(when\quad z\gg R)(\vec{k})
\end{aligned}
$$

物理上，即退化为点电荷间库仑定律。

#### 均匀带电圆盘
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

#### 均匀带电球体
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

#### 均匀带电直线
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

#### 均匀带电平面
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


### Chap22-2、23：高斯定理

#### Maxwell 方程组

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

#### 电偶极子

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

#### 立体角定义
$$
\mathrm{d}\Omega=\frac{\hat r\mathrm{d}\vec S}{r^2}
$$

#### 静电场高斯定理推导
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

#### Examples

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

### Chap24：电势

#### 电势的导出

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

#### Examples

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

## 电流
### Chap27：电流

#### 电流密度电子漂移模型

$$
\begin{gathered}
    I=\frac{\mathrm dq}{\mathrm dt}=\frac{n(\Delta S\cdot v\mathrm dt)e}{\mathrm dt}=ne(\Delta S)v\\
    j=\frac{I}{\Delta S}=nev\\
\end{gathered}
$$

考虑电子运动方向，则 $\vec{j}=-ne\vec{v}$

#### 欧姆定律微分形式

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

#### 焦耳定律微分形式

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

#### 金属的 Drude 模型

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

### Chap28：电路

#### RC 电路（充电）

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

#### RC 电路（放电）

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

## 磁场与电磁学
### Chap29：磁偶极矩

#### 洛伦兹力导出安培力

$$
\begin{aligned}
f&=q\vec v\times\vec B\\
\mathrm{d}\vec F&=\mathrm{d}Nq\vec v\times \vec B\\
&=n(S\mathrm{d}l)q\vec v\times\vec B\\
&=i\mathrm{d}\vec l\times\vec B;
\end{aligned}
$$

尤其直线、90° 条件下有

$$
F = IBL
$$

#### 闭合线圈在均匀磁场中所受力矩

$$
\tau=iA\hat n\times\vec B\\
\mathrm{d}\tau=i\mathrm{d}A\hat n_A\times\vec B\\
\tau=\sum i\mathrm{d}A\hat n_A\times\vec B\\
$$

#### 磁偶极矩

磁偶极矩 (magnetic dipole moment)

$$
\begin{aligned}
\mu&=NiS\\
\tau&=\mu B\sin\theta\\
\vec\tau&=\vec\mu\times\vec B=NiA\hat n\times \vec B\\
W(\theta)&=-\int_\frac{\pi}{2}^\theta\vec\tau\mathrm d\vec\theta\\
&=-\int_\frac{\pi}{2}^\theta NiAB\sin\theta\mathrm d\theta\\
&=NiAB\cos\theta\\
&=\vec\mu\cdot\vec B\\
U(\theta)&=-W=-\vec\mu\cdot\vec B=-NiA B\cos\theta\\
\end{aligned}
$$

对比电偶极矩 (electric dipole moment)

$$
\begin{aligned}
\vec\tau&=\vec p\times\vec E\\
U(\theta)&=-\vec p\cdot\vec E=-Eqd\cos\theta\\
\end{aligned}
$$

以上的 $U$ 均为能量含义。

### Chap30：毕奥-萨伐尔定律

Laplace 介入 Biot and Savart Law

$$
\begin{aligned}
\mathrm d H&=\mathrm d H(r, \alpha)\\
H&=k\frac{I}{r}\tan\frac{\alpha}{2}\\
\mathrm d H&=\frac{\mathrm d H}{\mathrm d l}\mathrm d l\\
&=\left(\frac{\partial H}{\partial \alpha}\cdot\frac{\mathrm d\alpha}{\mathrm dl}+\frac{\partial H}{\partial r}\cdot\frac{\mathrm dr}{\mathrm dl}\right)\mathrm dl\\
\frac{\partial H}{\partial \alpha}&=\frac{kI}{2r\cos^2\frac{\alpha}{2}},\frac{\partial H}{\partial r}=-k\frac I{r^2}\tan\frac{\alpha}{2}\\
\mathrm{d}l\sin\alpha&=r\mathrm{d}\alpha,\mathrm{d}l\cos\alpha=\mathrm{d}r\Rightarrow
\frac{\mathrm{d}\alpha}{\mathrm{d}l}=\frac{\sin\alpha}{r},\frac{\mathrm{d}r}{\mathrm{d}l}=\cos\alpha\\
\mathrm dH&=\left(\frac{kI}{2r\cos^2\frac{\alpha}{2}}\cdot\frac{\sin\alpha}{r}-k\frac I{r^2}\tan\frac{\alpha}{2}\cdot\cos\alpha\right)\mathrm dl\\
&=\left(\frac{\sin\alpha}{2\cos^2\frac{\alpha}{2}}-\tan\frac{\alpha}{2}\cos\alpha\right)k\frac{I\mathrm dl}{r^2}\\
&=\tan\frac{\alpha}{2}\left(1-\cos\alpha\right)k\frac{I\mathrm dl}{r^2}\\
&=\tan\frac{\alpha}{2}\cdot2\cos^2\frac{\alpha}{2}k\frac{I\mathrm dl}{r^2}\\
&=k\frac{I\mathrm dl}{r^2}\sin\alpha,\text{ 结合方向得到}\\
\mathrm d\vec H&=k\frac{I\mathrm d\vec l\times\vec r}{r^3}\\
\mathrm d\vec H&=\frac{1}{4\pi}\frac{I\mathrm d\vec l\times\vec r}{r^3}\\
\mathrm d\vec B&=\frac{\mu}{4\pi}\frac{I\mathrm d\vec l\times\vec r}{r^3}
\end{aligned}
$$

匀速运动电荷在空间产生磁场(考虑相对论)

$$
\begin{aligned}
\vec B&=\frac{\mu_0}{4\pi}\frac{q\vec v\times\vec r}{r^3(1-\frac{v^2}{c^2}\sin^2\theta)^{\frac{3}{2}}}(1-\frac{v^2}{c^2})\\
v&\ll c,\vec B=\frac{\mu_0}{4\pi}\frac{q\vec v\times\vec r}{r^3}
\end{aligned}
$$

载流直导线产生磁场

$$
\begin{aligned}
B=\int\mathrm d B&=\int\frac{\mu_0}{4\pi}\frac{I\mathrm dz}{r^2}\frac{d}{r}\\
&=\int\frac{\mu_0}{4\pi}\frac{Id\mathrm dz}{(z^2+d^2)^{\frac{3}{2}}}\\
&\xlongequal{z=d\tan\theta}\int\frac{\mu_0I}{4\pi d}\cos\theta\mathrm d\theta\\
&=\frac{\mu_0I}{4\pi d}(\sin\theta_1-\sin\theta_2)\\
\theta_1\to\frac{\pi}{2},\theta_2\to-\frac{\pi}{2},B&=\frac{\mu_0I}{2\pi d}
\end{aligned}
$$

环形线圈产生磁场

$$
\begin{aligned}
B=\int\mathrm d B_z&=\int\frac{\mu_0}{4\pi}\frac{I\mathrm dl}{R^2+z^2}\cdot\frac{R}{\sqrt{R^2+z^2}}\\
&=\frac{\mu_0}{4\pi}\frac{I\cdot2\pi R^2}{(R^2+z^2)^{\frac{3}{2}}}\\
&=\frac{\mu_0 I}{2}\frac{R^2}{(R^2+z^2)^{\frac{3}{2}}}\\
z=0,B&=\frac{\mu_0I}{2R}\\
z>>R,B&=\frac{\mu_0IR^2}{2z^3}=\frac{\mu_0\mu(电偶极矩)}{2\pi z^3}
\end{aligned}
$$


### Chap31-2：电感

#### Example1 螺线管电感

$$
L=\frac{\Phi}{i}=\frac{N\phi}{i}=\frac{N(\mu_0ni)S}{i}=\mu_0nNS=\mu_0n^2lS
$$

#### Example2 环形加速器 Toroid

$$
\phi=\int_a^b(\mu_0\frac{N}{2\pi r}I)h\mathrm dr=\frac{\mu_0NIh}{2\pi}\ln\frac{b}{a}\\
L=\frac{N\phi}{I}=\frac{\mu_0N^2h}{2\pi}\ln\frac{b}{a}
$$

#### LRCircuits

$$
\begin{aligned}
\varepsilon-iR-L\frac{\mathrm di}{\mathrm dt}&=0\\
\frac{\mathrm di}{\varepsilon-iR}&=\frac{\mathrm d t}{L}\\
-\frac{1}{R}\ln\frac{\varepsilon-iR}{\varepsilon}&=\frac{t}{L}\\
\varepsilon-iR&=\varepsilon e^{-\frac{t}{\tau}},\tau=\frac{L}{R}\\
i&=\frac{\varepsilon}{R}(1-e^{-\frac{t}{\tau}})\\
\end{aligned}
$$

移除电源 (放电？)

$$
\begin{aligned}
-iR-L\frac{\mathrm di}{\mathrm dt}&=0\\
\frac{\mathrm di}{i}&=-\frac{R\mathrm dt}{L}\\
i&=\frac{\varepsilon}{R}e^{-\frac{t}{\tau}}\\
\end{aligned}
$$

考虑能量

$$
\begin{aligned}
\varepsilon-iR-L\frac{\mathrm di}{\mathrm dt}&=0\\
\varepsilon i&=i^2R+Li\frac{\mathrm di}{\mathrm dt}\\
\varepsilon i:\text{电源功率}\ \ &i^2R:\text{热功率}\ \ Li\frac{\mathrm di}{\mathrm dt}:\text{电感储能功率}\\
\varepsilon i=\frac{\varepsilon \mathrm dq}{\mathrm dt}&:\text{因此有电源功率的意义}\\
U_L&=\int_0^tLi\frac{\mathrm di}{\mathrm dt}\mathrm dt=\int_0^iLi\mathrm di=\frac{1}{2}Li^2\\
\end{aligned}
$$

#### 磁场能量密度 (从螺线管推导)

$$
\begin{aligned}
u_B=\frac{U}{V}&=\frac{\frac12LI^2}{lA}\\
&=\frac{\frac12\mu_0n^2lAI^2}{lA}\\
&=\frac{(\mu_0nI)^2}{2\mu_0}=\frac{B^2}{2\mu_0}\\
\text{对比 }u_E&=\frac{1}{2}\epsilon_0E^2
\end{aligned}
$$

Example3

$$
\begin{aligned}
\phi&=\int_a^{d-a}(\frac{\mu_0i}{2\pi r}+\frac{\mu_0i}{2\pi(d-r)})l\mathrm dr\\
&=\frac{\mu_0il}{2\pi}\ln\frac{r}{d-r}\bigg|_a^{d-a}=\frac{\mu_0il}{\pi}\ln\frac{d-a}{a}\\
L&=\frac{\phi}{i}=\frac{\mu_0l}{2\pi}\ln\frac{d-a}{a}
\end{aligned}
$$

#### 互感

互感 (Mutual Induction)

$$
\begin{gathered}
i,B\propto i_1\Rightarrow \Phi_{12}=M_{12}i_1\\
\text{同理 }\Phi_{21}=M_{21}i_2\\
\text{变 }i_1\text{ 以动 }i_2,\; M_{12}\frac{\mathrm di_1}{\mathrm dt}=\frac{\mathrm d\Phi_{12}}{\mathrm dt}=-\varepsilon_2\\
\text{同理，变 }i_2\text{ 以动 }i_1,\varepsilon_1=-M_{21}\frac{\mathrm di_2}{\mathrm dt}
\end{gathered}
$$

证明互感系数相等

$$
\begin{gathered}
\phi_{12}=\oint_{L_2}\vec{A_1}\cdot\mathrm d\vec l_2,\vec A_1=\frac{\mu_0I_1}{4\pi}\oint_{L_1}\frac{\mathrm d\vec l_1}{r_{12}}\\
\therefore\phi_{12}=\frac{\mu_0I_1}{4\pi}\oint\limits_{L_1}\oint\limits_{L_2}\frac{\mathrm d\vec l_1\cdot\mathrm d\vec l_2}{r_{12}}\\
M_{12}=M_{21}=\frac{\mu_0}{4\pi}\oint\limits_{L_1}\oint\limits_{L_2}\frac{\mathrm d\vec l_1\cdot\mathrm d\vec l_2}{r_{12}}    
\end{gathered}
$$

Example 4

$$
\begin{gathered}
B=\mu_0\mu_r\frac{N_1}{l}i_1=\mu\frac{N_1}{l}i_1\\
\Phi_{12}=N_2 BS=\mu\frac{N_1N_2S}{l}i_1=Mi_1\\
M=\mu\frac{N_1N_2S}{l}\\
L_1=\mu\frac{N_1^2S}{l},L_1=\mu\frac{N_2^2S}{l}\\
M=\sqrt{L_1L_2}\\
M=K\sqrt{L_1L_2},K\in[0,1],\text{ 同轴 }K=1,\text{ 垂直 }K=0    
\end{gathered}
$$

#### L-C circuit

$$
\begin{gathered}
\frac{q}{C}=-L\frac{\mathrm di}{\mathrm dt}\Rightarrow \frac{\mathrm d^2q}{\mathrm dt^2}+\frac{q}{LC}=0\\
\omega=\sqrt{\frac1{LC}},q=q_0\cos(\omega t+\phi)\\
i=-q_0\omega\sin(\omega t+\phi)\\
U_E=\frac{1}{2}\frac{q_0^2}{C}\cos^2(\omega t+\phi),U_B=\frac12Lq_0^2\omega^2\sin^2(\omega t+\phi)        
\end{gathered}
$$

#### RLC circuit

$$
\varepsilon=iR+\frac qC+L\frac{\mathrm di}{\mathrm dt}\\
$$

Example

$$
\begin{aligned}
E\cdot2\pi rl&=\frac{q}{\epsilon_0}\Rightarrow E=\frac{q}{2\pi r\epsilon_0 l}\\
U_E&=\int_a^b\frac{1}{2}\epsilon_0(\frac{q}{2\pi r\epsilon_0 l})^2(2\pi r\mathrm dr l)\\
&=\frac{q^2}{4\pi \epsilon_0 l}\int_a^b\frac1r\mathrm dr\\
&=\frac{q^2}{4\pi \epsilon_0 l}\ln\frac{b}{a}\\
或C&=\frac{2\pi\epsilon_0l}{\ln\frac ba},U_E=\frac{q^2}{2C}=\frac{q^2}{4\pi\epsilon_0l}\ln\frac ba
\end{aligned}
$$

$$
\begin{aligned}
B\cdot2\pi r&=\mu_0I\Rightarrow B=\frac{\mu_0I}{2\pi r}\\
U_B&=\int_a^b\frac{1}{2\mu_0}(\frac{\mu_0I}{2\pi r})^2(2\pi r\mathrm dr)l\\
&=\frac{\mu_0I^2l}{4\pi}\int_a^b\frac1r\mathrm dr\\
&=\frac{\mu_0I^2l}{4\pi}\ln\frac ba\\
\text{或 }L&=\frac\phi I=\frac{\displaystyle \int_a^b\frac{\mu_0I}{2\pi r}l\mathrm dr}{I}\\
&=\frac{\displaystyle \frac{\mu_0Il}{2\pi }\ln\frac ba}{I}=\frac{\mu_0l}{2\pi }\ln\frac ba\\
U_B&=\frac12LI^2=\frac{\mu_0I^2l}{2\pi }\ln\frac ba
\end{aligned}
$$


### Chap31-3：磁化

#### 从分子电流产生磁矩

$$
\begin{gathered}
i=\frac{e}{T}=\frac{e}{\frac{2\pi r}{v}}=\frac{ev}{2\pi r}\\
|\vec \mu|=i(\pi r^2)=\frac12evr\\
\end{gathered}
$$

根据量子模型，电子轨道并不稳定，不能指望 $v$、$r$，唯角动量量子化守恒。

轨道磁矩(Orbital magnetic dipole moment) 

$$
|\vec{\mu_L}|=\frac{e}{2m}(mvr)=\frac{e}{2m}L
$$

$L$ 为角动量，而 $\displaystyle L=n\hbar=n\frac{h}{2\pi}$，则

$$
|\vec{\mu_L}|=\frac{e}{2m}n\frac{h}{2\pi}
$$

$n=1$ 时，为玻尔磁子 Bohr magneton。自旋磁矩(Spin magnetic dipole moment) 

$$
\vec{\mu_s}=-\frac{e}{2m}\vec{s},\; s=\pm\frac12\hbar
$$

有 $\vec\mu=\vec\mu_L+\vec\mu_S\approx\vec\mu_L$。外加磁场 $\vec B$，会受到力矩 $\vec\tau=\vec\mu\times\vec B$的作用。定义 $\vec{\mu}=\sum_i\vec\mu_i$。

考察不外加磁场的电子轨道

$$
\begin{gathered}
    \frac{Ze^2}{4\pi\epsilon_0 r^2} = m\omega_0^2r \\
    \omega_0 = \sqrt{\frac{Ze^2}{4\pi\epsilon_0mr^3}}
\end{gathered}
$$

考察外加磁场后的角速度变化

当 $\vec{\omega_0}\parallel\vec B$，

$$
    \frac{Ze^2}{4\pi\epsilon_0r^2}+e\omega rB = m\omega^2r
$$


根据 $\omega=\omega_0+\Delta\omega$，代入展开，舍去二阶小量有

$$
    \frac{Ze^2}{4\pi\epsilon_0r^2}+e\omega_0rB+e\Delta\omega rB = m\omega_0^2r+2m\omega_0\Delta\omega r
$$

则

$$
\begin{gathered}
    e\omega_0rB\approx e\omega_0rB+e\Delta\omega rB=2m\omega_0\Delta\omega r\\
    \Delta\omega=\frac{eB}{2m}
\end{gathered}
$$

当 $\vec{\omega_0}\parallel-\vec B$，类似地有

$$
\begin{aligned}
&\frac{Ze^2}{4\pi\epsilon_0r^2}-e\omega rB=m\omega^2r\\
&\frac{Ze^2}{4\pi\epsilon_0r^2}-e\omega_0rB-e\Delta\omega rB=m\omega_0^2r-2m\omega_0\Delta\omega r\\
&e\omega_0rB\approx e\omega_0rB+e\Delta\omega rB=2m\omega_0\Delta\omega r\\
&\Delta\omega=\frac{eB}{2m}
\end{aligned}
$$

由之前结论，$\displaystyle\vec\mu_0=-\frac12evr=-\frac12er^2\vec\omega_0$，$\displaystyle\Delta\vec\mu=-\frac12er^2\Delta\vec\omega=-\frac{e^2r^2}{4m}\vec B$

所以磁矩的变化量总是反抗外加磁场的方向，且 $|\Delta\vec\mu|\ll|\vec\mu|$

定义磁化强度 (Magnetization) $\displaystyle\vec M=\frac{\sum_i\vec\mu_i}{\Delta V}$ (对比极化强度 $\displaystyle\vec P=\frac{\sum_i\vec p_i}{\Delta V}$)

$$
\vec B=\vec B_0+\vec B_M\text{ (对比 }\vec E=\vec E_0+\vec E')
$$

#### Ampere's Law

令 $j_M$ 为磁化电流线密度，则

$$
    \bigg|\sum_i\vec \mu_i\bigg|=i_MS=j_MlS
$$

随后则有

$$
    \Delta V=lS,\bigg|\vec M\bigg|=\frac{\displaystyle\bigg|\sum_i\vec \mu_i\bigg|}{\Delta V}=j_M
$$

即 $\vec j_M=\vec M\times\vec n$。对比电场，$\sigma'=|\vec P|\cos\theta=\vec P\cdot\vec n$。随后

$$
\begin{gathered}
\oint_L\vec M\cdot\mathrm d\vec l=\sum\int_{a_i}^{b_i}\vec M\cdot\mathrm d\vec l=\sum M\overline{a_ib_i}=\sum j_M\overline{a_ib_i}=\sum i_M\\
\oint_L\vec B\cdot\mathrm d\vec l=\oint_L\vec B_0\cdot\mathrm d\vec l+\oint_L\vec B_M\cdot\mathrm d\vec l=\mu_0(\sum i_0+\sum i_M)\; (\text{原 Ampere's Law})\\
\end{gathered}
$$

即得

$$
\begin{gathered}
\sum i_0=\oint_L\frac{\vec B}{\mu_0}\cdot\mathrm d\vec l-\sum i_M=\oint_L\left(\frac{\vec B}{\mu_0}-\vec M\right)\cdot\mathrm d\vec l=\oint_L\vec H\cdot\mathrm d\vec l\\
\vec M=\chi_m\vec H\left(=\chi_m\frac{\vec B}{\mu}\right)\;(对比P=\chi_e \vec D=\chi_e\epsilon E)\\
\vec B=\mu_0\vec H+\mu_0\vec M=\mu_0(1+\chi_m)\vec H\xlongequal{\mu_r=1+\chi_m}\mu_0\mu_r\vec H(=\mu\vec H)=\mu_r\vec B_0=\kappa_m\vec B_0
\end{gathered}
$$

国外常用 $\kappa_m$ 而非 $\mu_r$，用 $\kappa_e$ 而非 $\epsilon_r$，对比 $\vec E=\frac{\vec E_0}{\epsilon_r}=\frac{\vec E_0}{\kappa_e}$。

最终磁场大于外加磁场，电场小于外加电场。

$$
\chi_m\vec B_0=\mu_0(\chi_m\vec H)=\mu_0\vec M=\vec B-\mu_0\vec H=\kappa_m\vec B_0-\vec B_0=(\kappa_m-1)\vec B_0
$$

因此 $\chi_m=\kappa_m-1\Rightarrow\kappa_m(\mu_r)=\chi_m+1$，对比 $\kappa_e(\epsilon_r)=\chi_e+1$

考虑如下四种情况：

- 顺磁性 (Paramagnetism): $\kappa_m>1$, $\vec B>\vec B_0$
- 逆磁性 (Diamagnetism): $\kappa_m<1$, $\vec B<\vec B_0$
- 铁磁性 (Ferromagnetism): $\kappa_m\gg 1$, $\vec B\gg\vec B_0$
- 超导体 (Superconductor): $\kappa_m=0$, $\vec B=0$

#### Example1 旋转环形电荷
$$
i=\frac{\Delta q}{\Delta t}=\frac{q}{\frac{2\pi}{\omega}}=\frac{q\omega}{2\pi}\\
\mu=i(\pi R^2)=\frac{q\omega R^2}{2}
$$

#### Example1-plus 旋转圆盘电荷
$$
\begin{gathered}
d\mu=\pi r^2(\frac{\sigma\cdot2\pi r\mathrm d r}{\frac{2\pi}{\omega}})=\sigma\pi\omega r^3\mathrm d r\\
\mu=\int_0^R\sigma\pi\omega r^3\mathrm d r==\frac{\sigma\pi\omega R^4}{4}=\frac{q\omega R^2}{4}\\
\end{gathered}
$$

#### Exmple2 旋转球电荷
$$
\begin{gathered}
\rho=\frac{q}{\frac{4}{3}\pi R^3}=\frac{3q}{4\pi R^3}\\
\mathrm d\mu=\frac{[\rho\pi (R\sin\theta)^2\mathrm dz]\omega (R\sin\theta)^2}{4}\\
\mathrm dz=\mathrm d(R\cos\theta)=-R\sin\theta\mathrm d\theta\\
\end{gathered}
$$

$$
\begin{aligned}
\mu&=\int_R^{-R}\frac{[\rho\pi (R\sin\theta)^2\mathrm dz]\omega (R\sin\theta)^2}{4}\\
&=\int_0^\pi\frac{[\rho\pi (R\sin\theta)^2R\sin\theta\mathrm d\theta]\omega (R\sin\theta)^2}{4}\\
&=\frac14\rho\pi\omega R^5\int_0^\pi\sin^5\theta\mathrm d\theta\\
&=\frac{3q\omega R^2}{16}\cdot2\frac{4\cdot2}{5\cdot3\cdot1}=\frac{q\omega R^2}{5}\\
\end{aligned}
$$

$$
\begin{gathered}
\mu=\left\{\begin{matrix}
\displaystyle\frac{q\omega R^2}{2}\text{，圆环}\\
\displaystyle\frac{q\omega R^2}{4}\text{，圆盘}\\
\displaystyle\frac{q\omega R^2}{5}\text{，球}
\end{matrix}\right.\quad\quad\quad
J\text{ (转动惯量)}=\left\{\begin{matrix}
MR^2\text{，圆环}\\
\displaystyle\frac{1}{2}MR^2\text{，圆盘}\\
\displaystyle\frac25MR^2\text{，球}
\end{matrix}\right.
\end{gathered}
$$

#### Example3

$$
\begin{gathered}
2\pi rB_{10}=\mu_0\frac{\pi r^2}{\pi R^2}I\Rightarrow B_{10}=\frac{\mu_0 Ir}{2\pi R^2},B_{1}=\mu_{r}B_{10}=\frac{\mu_{r1}\mu_0Ir}{2\pi R^2}\\
2\pi rB_{20}=\mu_0I\Rightarrow B_{20}=\frac{\mu_0I}{2\pi r},B_2=\mu_{r2}B_{20}=\frac{\mu_{r2}\mu_0I}{2\pi r}\\
M_1=\frac{B_1-B_{10}}{\mu_0}=\frac{\mu_{r1}-1}{\mu_0}B_{10}=\frac{(\mu_{r1}-1)Ir}{2\pi R^2}\\
M_2=\frac{B_2-B_{20}}{\mu_0}=\frac{\mu_{r2}-1}{\mu_0}B_{20}=\frac{(\mu_{r2}-1)I}{2\pi r}
\end{gathered}
$$

#### Example4

已知 $L,N,I$。

$$
\begin{gathered}
B_0=\mu_0nI=\frac{\mu_0NI}{L}\\
\mu_r=\frac{B}{B_0}\\
I=\frac{B_0L}{\mu_0N}\\
M=\frac{B-B_0}{\mu_0}=\frac{(\mu_r-1)NI}{L}=\frac{i}{l}\\
\therefore i=(\mu_r-1)NI=\frac{(\mu_r-1)B_0L}{\mu_0}
\end{gathered}
$$

#### Example5

已知 $n,I,B$。

$$
\begin{gathered}
B=\mu_rB_0\Rightarrow\mu_r=\frac{B}{B_0}=\frac{B}{\mu_0nI}\\
H\cdot 2\pi r=NI\Rightarrow H=\frac{NI}{2\pi r}=nI\\
j_m=M=\frac{B}{\mu_0}-H\\
\end{gathered}
$$


### Chap32：综合应用

Example1 平行板电容器

$$
\Delta V=4+3t(电势差),\phi_E=?,i_d=?,B=?
$$

解：

$$
\begin{gathered}
E=\frac{\Delta V}{D}=\frac{4+3t}{D},\phi_E=E\pi R^2=\frac{\pi R^2}{D}(4+3t)\\
i_d=\varepsilon_0\iint\frac{\mathrm dE}{\mathrm dt}\mathrm dS=\frac{3\varepsilon_0\pi R^2}{D}\\
B\cdot2\pi r=\mu_0\frac{\pi r^2}{\pi R^2}i_d=\frac{3\mu_0\varepsilon_0\pi r^2}{D}\Rightarrow B=\frac{3\mu_0\varepsilon_0 r}{2D}\\
\end{gathered}
$$

新设：

$$
q=q_m\sin\omega t,\phi_E=?,i_d=?,B=?
$$

解：

$$
\begin{gathered}
    E=\frac{q_m\sin\omega t}{CD}=\frac{q_m\sin\omega t}{\epsilon_0 \pi R^2}\\
    i_d=\varepsilon_0\cdot\frac{q_m\omega\cos\omega t}{\epsilon_0 \pi R^2}\cdot\pi R^2=q_m\omega\cos\omega t
\end{gathered}
$$

Example3

$$
\begin{gathered}
j=\sigma E\Rightarrow E=\rho \frac i{\pi R^2}\\
B\cdot2\pi R=\mu_0 i
\end{gathered}
$$


## 光学
### Chap34：几何光学
Chapters/34.tex
### Chap36-1：干涉
Chapters/36-1.tex
### Chap36-2：衍射
Chapters/36-2.tex
### Chap36-3：光栅与光谱
Chapters/36-3.tex
### Chap36-4：偏振
Chapters/36-4.tex

## 量子理论
### Chap38-1：黑体辐射与光电效应
Chapters/38-1.tex
### Chap38-2：物质波
Chapters/38-2.tex
### Chap39-1：薛定谔方程
Chapters/39-1.tex
### Chap39-2：氢原子光谱
Chapters/39-2.tex