# Functions of a Real Variable

> *real analysis* (实分析) is too difficult for me, so I just try to learn *functions of a real variable* (实变函数) first. 

!!! warning "本页面还在施工中。目前计划在[智云课堂](https://classroom.zju.edu.cn)学习贾厚玉老师开设的《实变函数》"

## Contents

- [Basics of Set Theory](sets.md)
- [Lebesgue Measure](LebesgueMeasure.md)
- ......(to be continued)

## Objective: Lebesgue Integral

Riemann 可积函数列存在一个问题，极限运算是不封闭的，也即可积函数列的极限函数可能不可积。

!!! example "极限运算不封闭"
    记 $[0, 1]$ 上的可积函数类为 $R[0, 1]$，则考虑 $[0, 1]$ 上的“二进有理数”数列：

    $$
        0, 1, \frac{1}{2}, \frac{1}{4}, \frac{3}{4}, \frac{1}{8}, \frac{3}{8}, \frac{5}{8}, \frac{7}{8}, \cdots
    $$

    即该数列由 $0, 1$ 以及形式为 $1/2^n, 3/2^n, \cdots, (2^n-1)/2^n$ 的数构成，记该数列为 $\{r_n\}$。则定义函数列 $f_k(x)$ 如下：

    $$
        f_k(x) = \begin{cases}
            1, & x = r_n, k\geqslant n \in \mathbb{N} \\
            0, & \text{otherwise}
        \end{cases}
    $$

    对于其极限函数 $f(x)$，对于任意细的划分，每个子区间一定有取值为 1 的离散点和取值为 0 的离散点，因此类似于 Dirichlet 函数，有 $f\notin R[0, 1]$。

引入 Lebesgue 可积函数类，是因为其在极限运算下是封闭的，即积分和极限运算可以交换：

$$
\lim_{n\to \infty} \int_a^b f_n(x)\mathrm{d}x = \int_a^b \lim_{n\to \infty} f_n(x)\mathrm{d}x
$$

而且 Lebesgue 可积是对 Riemann 可积的扩展，即原来 Riemann 可积的函数依然也是 Lebesgue 可积的。因此，Lebesgue 积分对 Riemann 积分进行了完备化。Lebesgue 积分正是实变函数的核心内容。
