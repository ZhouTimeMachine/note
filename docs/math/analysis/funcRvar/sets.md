<link rel="stylesheet" href="../../../../css/counter.css" />

# Basics of Set Theory

## Common Symbols

- 幂集 (power set)：$\mathcal{P}(X) = \{A: A\subseteq X\}$
- 用指标集 $\Lambda$ 选取 $X$ 的子集构成集族：$\mathcal{A} = \{A_{\alpha}\subseteq X: \alpha\in\Lambda\}$
- 用指标集可以方便地表示多个集合的并、交等运算：

$$
\begin{gathered}
    \bigcup_{\alpha\in\Lambda}A_{\alpha} = \{x: \exists \alpha\in \Lambda, x\in A_{\alpha}\}, \\
    \bigcap_{\alpha\in\Lambda}A_{\alpha} = \{x: \forall \alpha\in \Lambda, x\in A_{\alpha}\}. \\
\end{gathered}
$$

- 差集 $A \backslash B = \{x: x\in A, x\notin B\}$，补集 $A^c = \Omega \backslash A$（用 $\Omega$ 表示全集）

??? example "基本集合论练习"
    - $\{x: \sup _n f_n(x) > t\} = \bigcup_{n=1}^{\infty}\{ x: f_n(x) > t \}$
    - $\{x: \sup _n f_n(x) \leqslant t\} = \bigcap_{n=1}^{\infty}\{ x: f_n(x) \leqslant t \}$

    第二行由第一行应用 De Morgan 律容易得到。令 $A=\{x: \sup _n f_n(x) > t\}$, $A_n=\{ x: f_n(x) > t \}$
    
    - $\forall x\in A$，如果不存在 $n_0$ 使得 $f_{n_0}(x) = \sup_n f_n(x)$，则有 $f_n(x) < \sup_n f_n(x)$，两边同取 $\sup_n$ 后发现矛盾，因此有 $f_{n_0}(x) > t$, $x\in A_{n_0}$，也就有 $x\in \bigcup A_n\Rightarrow A\subseteq \bigcup A_n$
    - $\forall x\in \bigcup A_n$，存在 $n_0$ 使得 $x\in A_{n_0}$，也就有 $\sup_n f_n(x) \geqslant f_{n_0}(x) > t$，因此 $x\in A\Rightarrow \bigcup A_n\subseteq A$

## Limitation of Set Sequence

像定义数列的极限一样，讨论对集列的极限的定义之前，先考虑单调集列这一特殊情况。

- 单增集列：$A_k\subseteq A_{k+1}$, $k\in \mathbb{N}$，一定在全集 $\Omega$ 中，其极限一定存在，为 $\bigcup_{k=1}^{\infty} A_k\subseteq \Omega$
- 单减集列：$A_k\supseteq A_{k+1}$, $k\in \mathbb{N}$，其极限一定存在，为 $\bigcap_{k=1}^{\infty} A_k$



!!! warning "本页面还在施工中"