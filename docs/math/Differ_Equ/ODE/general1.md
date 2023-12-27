# ODE 一般理论：存在性定理

## Preliminaries

Lipschitz 条件： $f(x, y)$ 关于 $y$ 在 $D$ 满足 Lipschitz 条件

$$
|f(x, y_1) - f(x, y_2)| \leqslant L |y_1 - y_2|, \quad \forall (x, y_1), (x, y_2) \in D
$$

注：若 $f(x, y)$ 在凸域 $D$ 有

$$
\left| \frac{\partial f}{\partial y} \right| \leqslant L
$$

则根据 Lagrange 中值定理，$f(x, y)$ 满足 Lipschitz 条件

$$
|f(x, y_1) - f(x, y_2)| = \left| \frac{\partial f}{\partial y}(x, \xi) \right| |y_1 - y_2| \leqslant L |y_1 - y_2|
$$


## Picard 存在唯一性定理

!!! info "Picard 存在唯一性定理"
    如果 $f(x, y)$ 在闭矩形域
    
    $$
    R := \{(x; y) : |x - x_0|\leqslant a, |y - y_0|\leqslant b\}
    $$
    
    上连续，且关于变量 $y$ 满足 Lip 条件，则下述初值问题

    $$
    \begin{cases}
        \frac{\mathrm{d}y}{\mathrm{d}x} = f(x, y)\\
        y(x_0) = y_0       
    \end{cases}
    $$

    在区间 $I = [x_0 - h; x_0 + h]$ 上**存在唯一解** $y = \varphi(x)$ ，其中
    
    $$
    h = \min\left\{a, \frac{b}{M}\right\}, \quad M = \max_{(x, y) \in R} |f(x, y)|
    $$

解的存在区间与 $M$ 相对 $a, b$ 的大小有关。

- $M$ 相对 $a, b$ 比较小：积分曲线更容易碰到左右边界，$h=a$
- $M$ 相对 $a, b$ 比较大：积分曲线更容易碰到上下边界，$h<a$

