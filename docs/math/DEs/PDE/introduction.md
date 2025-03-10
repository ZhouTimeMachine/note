<link rel="stylesheet" href="../../../../css/counter.css" />

# Introduction

!!! info "Part of note of *Partial Differential Equations*, Lawrence C. Evans"

!!! warning "本页面还在施工中"

## Partial Differential Equations

!!! info "PDE"
    k 阶 PDE 的一般形式为

    $$
        F\left(D^k u(x), D^{k-1}u(x), \cdots, Du(x), u(x), x\right) = 0, \quad x\in U
    $$

    其中已知
    
    $$
        F: \mathbb{R}^{n^k} \times \mathbb{R}^{n^{k-1}} \times \cdots \times \mathbb{R}^{n} \times \mathbb{R} \times U \to \mathbb{R}
    $$

    欲求
    
    $$
        u: U \to \mathbb{R}
    $$

一般来说，我们还会再给一些辅助的边界条件，约定于 $\Gamma\subseteq\partial U$。

!!! info "linear & nonlinear PDEs"
    - **linear PDEs**: 给定函数 $\:a_{\alpha}(|\alpha|\leqslant k)$, $f$

    $$
        \sum_{|\alpha|\leqslant k}a_{\alpha}(x)D^{\alpha}u=f(x)
    $$

    特别地，若 $f\equiv 0$，则称齐次 (homogeneous)。

    - **semilinear PDEs**: 

    $$
        \sum_{|\alpha| = k}a_{\alpha}(x)D^{\alpha}u + a_0\left(D^{k-1}u, \cdots, Du, u, x\right)=0
    $$

    - **quasilinear PDEs**:
    
    $$
        \sum_{|\alpha| = k}a_{\alpha}\left(D^{k-1}u, \cdots, Du, u, x\right)D^{\alpha}u + a_0\left(D^{k-1}u, \cdots, Du, u, x\right)=0
    $$
    
    - **fullly nonlinear PDEs**: 非线性地依赖于最高阶导数

向量化，或者说从单个 PDE 到一个 PDE 的集合，就可以得到 PDE 系统 (system)。

!!! info "system of PDE"
    k 阶 PDE 系统的一般形式为

    $$
        \bm F\left(D^k \bm u(x), D^{k-1}\bm u(x), \cdots, D\bm u(x), \bm u(x), x\right) = 0, \quad x\in U
    $$

    其中已知
    
    $$
        \bm F: \mathbb{R}^{mn^k} \times \mathbb{R}^{mn^{k-1}} \times \cdots \times \mathbb{R}^{mn} \times \mathbb{R}^m \times U \to \mathbb{R}^m
    $$

    欲求
    
    $$
        \bm u: U \to \mathbb{R}^m, \bm u=(u^1,\cdots, u^m)
    $$