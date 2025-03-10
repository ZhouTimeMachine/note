<link rel="stylesheet" href="../../../css/counter.css" />

# Sets, Relations and Languages

!!! info "Part of note taken on ZJU *Introductiion to Theoretical Computer Science*, 2022 Fall & Winter"

## Sets

!!! info "partition"

	partition $\sqcap$ of A$\neq \emptyset$，有 $\sqcap\in 2^A$
	
	- $\emptyset \notin \sqcap$
	- $S, T\in\sqcap, S\neq T\Rightarrow S\cap T=\emptyset$
	- $\cup \sqcap=A$

## Relations and Functions

### Inverse

$$
    R\subseteq A\times B\Rightarrow
    R^{-1} \subseteq B\times A
$$

### Function

函数的本质是一种二元关系。因此，对函数 $f:A\rightarrow B$，有 $f\subseteq A\times B$。

回顾单射(one-to-one)，满射(onto)，双射(bijection)。

## Special Types of Binary Relations

### Properties of Relations

!!! info "自反、对称、传递"
	- 自反(reflexive): $\forall a\in A, (a, a)\in R$
		- 反自反(antireflexive):$\forall a\in A, (a, a)\notin R$
	- 对称(symmetric): $(a, b)\in R \Rightarrow (b, a)\in R$
		- 反对称(antisymmetric):$(a, b)\in R \Rightarrow (b, a)\notin R$
	- 传递(transitive): $(a, b)\in R, (b, c)\in R\Rightarrow (a, c)\in R$

### Equivalence Relation

等价关系要求自反，对称且传递。等价类用中括号表示：

$$
    [a]=\{b\;|\; (a, b)\in R\}
$$

!!! abstract "Theorem"
	$R$ 是非空集 $A$ 上的等价关系，则 $R$ 的所有等价类构成 $A$ 的一个 partition。

### Partial Order

**偏序**(partial order) 关系要求自反，**反对称**且传递。

**全序**(total order, or linear order 线序) 关系要求**完全性**(total, or strongly connected)，反对称且传递。

其中完全性定义为对$R$ on $X$，有

$$
    \forall a, b\in X, (a, b)\in R \text{ or } (b, a)\in R
$$


## Finite and Infinite sets

### Equinumerous

!!! info "$A$ 与 $B$ 等势 (equinumerous)"
	存在 $A$ 到 $B$ 的双射。

基数 (cardinality) 可能是要求有限的，但是有了广义基数 (generalized cardinality) 之后，就可以考虑无限集的势了。

!!! info "可数无限 (coutably infinite)" 
	可数无限即和 $\mathbb{N}$ 等势。$S$ 是不可数集 $\iff |S|>|\mathbb{N}|$

从 $\mathbb{R}$ 到 $(0,\;1)$ 的等势：

$$
    f(x)=\frac{1}{\pi}\arctan(x)+\frac{1}{2}
$$

### Continuum Hypothesis

首先，aleph number 有如下等式：

$$
    2^{\aleph_0}=\aleph_1,\quad
    \aleph_0=|\mathbb{N}|,\quad
    \aleph_1=|\mathbb{R}|
$$

!!! abstract "连续统假设 (Continuum Hypothesis)"
	没有一个集合的基数严格居于 $\aleph_0$ 和 $\aleph_1$ 之间。

连续统假设独立于 ZFC 公理。

## Three Fundamental Proof Techniques

三大基本的证明方法：**数学归纳** (Mathematical Induction)、**鸽巢原理** (Pigeonhole Principle) 和**对角线原理** (Diagonalization Principle)。

!!! abstract "鸽巢原理 (Pigeonhole Principle)"
	对有限集 $A, B$, $|A|>|B|$，则不存在 $A$ 到 $B$ 的单射 (one-to-one function)。

!!! abstract "对角线原理 (Diagonalization Principle)"
	对定义于 $A$ 上的二元关系 $R$，定义对角线集 $D$：

	$$
		D=\{a:a\in A\wedge (a, a)\notin R\}
	$$
	
	$\forall a\in A$，定义$R_a$：
	
	$$
		R_A=\{b:b\in A \wedge(a, b)\in R\}
	$$
	
	则$D$ 与任意 $R_a$ 都不同。

可以看出，$D$ 是对角线上没有的元素集，$R_a$ 是 $a$ 在邻接矩阵对应行的元素集。

## Closure

## Alphabet and Language

### Alphabet and String

!!! info "Definition"
	字符集 (alphabet)：符号构成的**有限**集

	字符串 (string)：**有限**符号序列，$e$ 表示空串

字符串操作：

- 连接(concatenation): $x\circ y$ 或 $xy$
- 乘方(exponentiation): $w^0=e$, $w^{i+1}=w^i\circ w$, $\forall i\geqslant 0$ (递归定义)
- 反转(reversal): $|w|=0$, 则 $w^R=w=e$; $|w|=n+1>0$, 则存在 $a\in \Sigma$ 使得 $w=ua$，那么$w^R=au^R$

注意子串(substring)、前缀(prefix)、后缀(suffix)三个概念。如果加上proper则代表不相等。

### Language

!!! info "Definition"
	语言 (language)：字符串的集合。

最大的语言为$\Sigma^*$，即任意由$\Sigma$中字符组成的字符串的集合。特别地，$\emptyset, \Sigma, \Sigma^*$都是语言。

由于$\Sigma$是有限集，可知$|\Sigma^*|=\aleph_0$。

语言除了基本集合运算 Union, Intersection, Difference, Complement之外，还可以进行连接Concatenation 和 Kleene Star。

$$
    \begin{gathered}
        L_1L_2=\{w_1w_2\;|\; w_1\in L_1 \wedge w_2\in L_2 \}\\
        L^*=L^0\cup L^1\cup L^2\cup \cdots\\
        L^+= L^1\cup L^2\cup L^3\cup \cdots
    \end{gathered}
$$

!!! question "Example"

	令 $L=\left\{ w\in \left\{ 0, 1 \right\}^* \;|\;  w\text{中}0\text{和}1\text{的数量不相等} \right\}$，那么 $L^*=\{0, 1\}^*$

**hint**：利用 $L_1\subseteq L_2\Rightarrow L_1^*\subseteq L_2^*$

??? general "Proof"
	$\{0, 1\}\subseteq L$，所以$\{0, 1\}^*\subseteq L^*$，但是根据$L$的定义又有$L\in \{0, 1\}^*\Rightarrow L^*\in\{0, 1\}^*$，则$L=\{0, 1\}^*$。

!!! tip "Remark"
	$\emptyset^*=\{e\}$(空语言不同于仅有空串的语言)，$L^+=LL^*$，$(L^*)^*=L^*$，$L\emptyset=\emptyset L=\emptyset$

## Finite Representations of Languages

### Finite Representations

明确语言的有限表示这一概念的意义：

- 是一个字符串。
- 不同语言的表示不同。

可以认为语言的有限表示就是语言中所有的字符串按照字典序拼接形成的字符串。收到alphabet的限制，语言的有限表示至多有$|\Sigma^*|$种(可数)，但是语言有$2^{|\Sigma^*|}$种(不可数)，因此必然存在无法描述的语言。

!!! question "支线任务"
	证明 $2^{\Sigma^*}$ 不可数

??? general "Proof"
    $2^{\Sigma^*}$ 和 $2^{\mathbb{N}}$ 等势。即证 $2^{\mathbb{N}}$ 不可数。

    若 $2^{\mathbb{N}}$ 可数，那么 $\mathbb{N}$ 的所有子集可以被列为 $A_0, A_1, \cdots, A_n, \cdots$。构造 $A\subseteq \mathbb{N}$，对 $\forall i\in\mathbb{N}$ 满足
    
    $$
        \begin{cases}
            i\in A_i\Rightarrow & i\notin A\\
            i\notin A_i\Rightarrow & i\in A
        \end{cases}
    $$
    
    可见 $A$ 与任意一个 $A_i$ 都不相等，矛盾。

### Regular Expressions

!!! example "Example"
    $L=\{w\in\{0, 1\}^*\;|\; w\text{中有 2 或 3 个 1，第 1 个和第 2 个不连续}\}$

可以将之写作正则表达式：$L=0^*10^*010^*(10^*\cup \emptyset^*)$

!!! info "正则表达式(regular expressions)"
	定义正则表达式为基于 $\Sigma\cup \left\{ (, ), \circleddash, \cup, * \right\}$ 的字符串。
    
    - $\circleddash$ 和 $\left\{ x \right\}(\forall x\in \Sigma)$ 都是正则表达式
    - $\alpha,\beta$ 是正则表达式 $\Rightarrow$ $(\alpha\beta), (\alpha\cup\beta), \alpha^*$都是正则表达式(连接，并，Kleene Star封闭)
    - 唯有通过以上两条构建的才是正则表达式

用函数 $\mathcal{L}(\cdot)$ 建立从**正则表达式**到其表示的**语言**的映射

!!! info "$\mathcal{L}(\cdot)$"
    - $\mathcal{L}(\circleddash)=\emptyset$, $\mathcal{L}(a)=\left\{ a \right\}(\forall a\in\Sigma)$
    - $\alpha, \beta$ 都是正则表达式，则（直接拆开）
    
	$$
		\begin{aligned}
			& \mathcal{L}(\alpha\beta)=\mathcal{L}(\alpha)\mathcal{L}(\beta)\\
			& \mathcal{L}(\alpha\cup \beta)=\mathcal{L}(\alpha)\cup \mathcal{L}(\beta)\\
			& \mathcal{L}(\alpha^*)=\mathcal{L}(\alpha)^*
		\end{aligned}
	$$

!!! example "Examples"
	- $\mathcal{L}(((a\cup b)^*a))=\left\{ w\in\{a, b\}^* \;|\;  w\text{以}a\text{结尾} \right\}$
	- $\mathcal{L}((c^*(a\cup (bc^*))^*))=\left\{ w\in\{a, b, c\}^* \;|\;  w\text{不含子串}ac \right\}$
	- $0^*\cup 0^*(1\cup 11)(00^*(1\cup 11))^*0^*$表示不含$111$的语言

后续不再严格区分正则表达式和语言。给出正则表达式的重要性质：

- $\emptyset^*=\left\{ e \right\}$
- $(R^*)^*=R^*$
- $(R^*S^*)^*=(R\cup S)^*$
- $(\left\{ e \right\}\cup R)^*=R^*$

!!! tip "Remark"
    - 每种可被正则表达式表达的语言可以用无穷多个正则表达式表达。（利用括号和 $\circleddash$ 等）
    - 正则语言类：正则语言是所有能用正则表达式描述的语言。$\Sigma$ 上的正则语言类恰好是

		$$
			\left\{ \left\{ \sigma \right\}:\sigma\in\Sigma \right\}\cup\left\{ \emptyset \right\}
		$$
	
		关于并、连接、Kleene Star 的**闭包**
	- 正则表达式不能表达所有语言
	- 两种表示语言的重要方式：
	    - 语言识别装置(language recognition device)：判定string是否属于language
	    - 语言生成器(language generator)