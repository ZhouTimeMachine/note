<link rel="stylesheet" href="../../css/counter.css" />

# Theory of Computation Review

!!! info "Note taken on ZJU *Introductiion to Theoretical Computer Science*, 2022 Fall & Winter"

!!! warning "本页面还在建设中"

## Sets, Relations and Languages

### Sets

!!! info "partition"

	partition $\sqcap$ of A$\neq \emptyset$，有 $\sqcap\in 2^A$
	
	- $\emptyset \notin \sqcap$
	- $S, T\in\sqcap, S\neq T\Rightarrow S\cap T=\emptyset$
	- $\cup \sqcap=A$

### Relations and Functions

#### Inverse

$$
    R\subseteq A\times B\Rightarrow
    R^{-1} \subseteq B\times A
$$

#### Function

函数的本质是一种二元关系。因此，对函数 $f:A\rightarrow B$，有 $f\subseteq A\times B$。

回顾单射(one-to-one)，满射(onto)，双射(bijection)。

### Special Types of Binary Relations

#### Properties of Relations

!!! info "自反、对称、传递"
	- 自反(reflexive): $\forall a\in A, (a, a)\in R$
		- 反自反(antireflexive):$\forall a\in A, (a, a)\notin R$
	- 对称(symmetric): $(a, b)\in R \Rightarrow (b, a)\in R$
		- 反对称(antisymmetric):$(a, b)\in R \Rightarrow (b, a)\notin R$
	- 传递(transitive): $(a, b)\in R, (b, c)\in R\Rightarrow (a, c)\in R$

#### Equivalence Relation

等价关系要求自反，对称且传递。等价类用中括号表示：

$$
    [a]=\{b\;|\; (a, b)\in R\}
$$

!!! abstract "Theorem"
	$R$ 是非空集 $A$ 上的等价关系，则 $R$ 的所有等价类构成 $A$ 的一个 partition。

#### Partial Order

**偏序**(partial order) 关系要求自反，**反对称**且传递。

**全序**(total order, or linear order 线序) 关系要求**完全性**(total, or strongly connected)，反对称且传递。

其中完全性定义为对$R$ on $X$，有

$$
    \forall a, b\in X, (a, b)\in R \text{ or } (b, a)\in R
$$


### Finite and Infinite sets

#### Equinumerous

!!! info "$A$ 与 $B$ 等势 (equinumerous)"
	存在 $A$ 到 $B$ 的双射。

基数 (cardinality) 可能是要求有限的，但是有了广义基数 (generalized cardinality) 之后，就可以考虑无限集的势了。

!!! info "可数无限 (coutably infinite)" 
	可数无限即和 $\mathbb{N}$ 等势。$S$ 是不可数集 $\iff |S|>|\mathbb{N}|$

从 $\mathbb{R}$ 到 $(0,\;1)$ 的等势：

$$
    f(x)=\frac{1}{\pi}\arctan(x)+\frac{1}{2}
$$

#### Continuum Hypothesis

首先，aleph number 有如下等式：

$$
    2^{\aleph_0}=\aleph_1,\quad
    \aleph_0=|\mathbb{N}|,\quad
    \aleph_1=|\mathbb{R}|
$$

!!! abstract "连续统假设 (Continuum Hypothesis)"
	没有一个集合的基数严格居于 $\aleph_0$ 和 $\aleph_1$ 之间。

连续统假设独立于 ZFC 公理。

### Three Fundamental Proof Techniques

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

### Closure

### Alphabet and Language

#### Alphabet and String

!!! info "Definition"
	字符集 (alphabet)：符号构成的**有限**集

	字符串 (string)：**有限**符号序列，$e$ 表示空串

字符串操作：

- 连接(concatenation): $x\circ y$ 或 $xy$
- 乘方(exponentiation): $w^0=e$, $w^{i+1}=w^i\circ w$, $\forall i\geqslant 0$ (递归定义)
- 反转(reversal): $|w|=0$, 则 $w^R=w=e$; $|w|=n+1>0$, 则存在 $a\in \Sigma$ 使得 $w=ua$，那么$w^R=au^R$

注意子串(substring)、前缀(prefix)、后缀(suffix)三个概念。如果加上proper则代表不相等。

#### Language

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

Hint：利用 $L_1\subseteq L_2\Rightarrow L_1^*\subseteq L_2^*$

??? general "Proof"
	$\{0, 1\}\subseteq L$，所以$\{0, 1\}^*\subseteq L^*$，但是根据$L$的定义又有$L\in \{0, 1\}^*\Rightarrow L^*\in\{0, 1\}^*$，则$L=\{0, 1\}^*$。

!!! tip "Remark"
	$\emptyset^*=\{e\}$(空语言不同于仅有空串的语言)，$L^+=LL^*$，$(L^*)^*=L^*$，$L\emptyset=\emptyset L=\emptyset$

### Finite Representations of Languages

#### Finite Representations

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

#### Regular Expressions

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

## Finite Automata

## Context-Free Language

### Context-Free Grammars

!!! info "上下文无关文法 (context-free grammar, CFG)"
    上下文无关文法 (context-free grammar, CFG) 是四元组 (quadruple) $G=(V, \Sigma, R, S)$，其中
    
	- $V$: alphabet
	- $\Sigma\subseteq V$: 终结符集合
	- $S$: 起始符
	- $R\subseteq (V-\Sigma)\times V^*$: 规则(有限)集合

!!! tip "Remark"
    - $A\in V-\Sigma$ 称为非终结符(nonterminal)，
    	
		$$
	    	A\to _G u\iff (A, u)\in R
		$$
	
	- $\Rightarrow_G$ 表示通过 $G$ 的一步变换。$\forall u, v\in V^*$, 
	
		$$
			u\Rightarrow_G v\iff
			\exists x, y\in V^*, A\in V-\Sigma \text{ s.t. } u=xAy,v=xv'y, A\to_G v'
		$$
	
	    $\Rightarrow_G^*$ 是其自反传递闭包。每一步都是推导 (derivation)。
	- 可见CFG $G$ 能够产生一个语言
	
		$$
	    	L(G)=\{w\in\Sigma^*:\; S\Rightarrow _G^* w\}
		$$
	
	当有一个 CFG 生成的 $L(G)=L$ 时，称 $L$ 是上下文无关语言 (context-free language, CFL)。

!!! question "Examples"
    - $R=\{S\to aSb,S\to e\}$，有$L=\{a^nb^n:\; n\geqslant 0\}$
    - $R=\{S\to e, S\to SS, S\to(S)\}$，生成嵌套括号表达式(balanced parentheses)
    - $R=\{S\to e, S\to SS, S\to aSb,S\to bSa\}$，有$L(G)=\{w\in\{a, b\}^*:\; w$中$a$, $b$等量\}
    - 电脑程序语言很多可以用CFG生成

??? general "Proof"
    只对 3 进行证明。$w\in L(G)\Rightarrow w\in L$ 是简单的，从 $R$ 可以看出每一步生成的 $a, b$ 等量。也可以选用数学归纳，归纳时只需要第一步自己走就行。

    $w\in L \Rightarrow w\in L(G)$ 还是归纳比较方便。
    
    **Basis step**: $|w|=0$，则 $w=e$，$S\to e$ 直接得到 $w\in L(G)$
    
    **Induction hypothesis (IH)**: 对 $|w|\leqslant k$ 都成立，$k$ 是偶数。（$w\in L$ 可以得到 $|w|$ 是偶数）
    
    **Induction step**: $|w|$ 是偶数，所以考虑 $|w|=k+2$。有
    
    $(1)w=axa$, $(2)w=axb$, $(3)w=bxa$, $(4)w=bxb$, $|x|=k$。
    
    根据 IH，(2)(3) 可以直接得到$x\in L(G)$，那么可以通过 $S\Rightarrow_G aSb(bSa)\Rightarrow_G^* axb(bxa)$ 证明 $w\in L(G)$。
    
    对(1)，$x$ 中 $b$ 比 $a$ 多 2 个，分解 $x=uv$，$u, v$ 中都是 $b$ 比 $a$ 多1个(则 $|u|, |v|\geqslant 1\Rightarrow |u|, |v|\leqslant k-1$)。则有 $S\Rightarrow_G^* au, S\Rightarrow_G^* va$，故 $S\Rightarrow_G SS\Rightarrow_G^* auva=w$。(4) 同理。

!!! abstract "Theorem"
    正则语言都是 CFL。

- 根据 3.3 的方法，可以通过 FA 是一种 PDA 证明
- 根据 3.5 的方法，可以通过基本正则语言是 CFL 的，以及 CFL 在并、连接、Kleene Star 下封闭得到
- 下面给出一种直接根据 DFA 生成对应的 CFG 的方法。

??? general "Proof"
	简单地，就是(当前状态) $\to$ (输入字符)(下一状态)，把输入字符一个个搬到左边。正式写出来就是CFG $G=(V, \Sigma, R, S)$
	
	$$
		\begin{aligned}
			V &= K\cup \Sigma\\
			S &= s\\
			R &= \{q\to ap:\;\delta(q, a)=p\}\cup\{q\to e:\; q\in F\}
		\end{aligned}
	$$

### Parse Tree

语法树从 $S$ 起始，中间结点为非终结符，叶子结点为终结符，叶子从左往右构成字符串。

- $a\in\Sigma$ 本身就是语法树
- $A\to e$ 也构成语法树
- 此外根据 $R$ 中的规则可以伸出语法树
- 其他的都不是语法树。

语法树与推导 (derivation) 密切相关。为了导出推导的等价关系，不严格地阐述**先于** (preced) 关系($\prec$)，即两个推导只有中间的一步有所不同，更先的一步走的较左边的非终结符(记作$A$)，更后的一步走的较右边的非终结符 (记作 $B$)，再下一步更先的走 $B$、更后的走 $A$ 恢复一致。

对 $\prec$ 关系取**自反对称传递**闭包，就得到了**相似** (similar) 关系。相似关系是一种等价关系，同一相似关系等价类中的推导具有相同的语法树。

每种语法树都有其**最左推导** (leftmost) 和**最右推导** (rightmost)，单步分别记作 $\stackrel{L}{\Rightarrow}$ 和 $\stackrel{R}{\Rightarrow}$。推导得到 $w$，和语法树生成 $w$，以及存在最左或最优推导得到 $w$，这些都是等价的。

!!! tip "Remark"
	- $\prec$ 不是传递的
	- 一个文法被称为有歧义的 (ambiguous)，如果它的某些字符串对应两棵以上的语法树

### Pushdown Automata

!!! info "下推自动机(pushdown automata, PDA)"
    下推自动机是六元组 (sextuple) $M=(K, \Sigma, \Gamma, \Delta, s, F)$，其中
    
    - $\Gamma$: 栈字符的alphabet
    - $\Delta\subseteq (K\times(\Sigma\cup \{e\})\times\Gamma^*\times(K\times\Gamma^*))$: 转移关系

!!! tip "Remark"
    - PDA是非确定性的
    - 格局 $\in K\times\Sigma^*\times\Gamma^*$
    - 同理定义 $\vdash_M$ 和其自反传递闭包 $\vdash_M^*$

PDA 的接受，除了要处理完全部字符串、进入末态之外，还需要把栈清空。则 PDA $M$ 接受的语言为

$$
    L(M)=\{w\in\Sigma^*\;|\; (s, w, e)\vdash_M^* (f, e, e), f\in F\}
$$

!!! question "Examples"
    设计 PDA 以接受

    1. $L=\{wcw^R:\; w\in\{a, b\}^*\}$
    2. $L=\{ww^R:\; w\in\{a, b\}^*\}$
    3. $L=\{w\in\{a, b\}^*:\; w$ 中 $a, b$ 等量\}

??? general "Proof"
    1. 如下图
	<div style="text-align:center;">
		<img src="../imgs/toc/3.1.jpg" alt="3.1" style="zoom:15%;" />
	</div>
    2. 将上题 $\Sigma$ 中 $c$ 删去，$\Delta$ 中第三条改为 $((s, e, e), (f, e))$ 即可
    3. 利用下一节的 CFG $\to$ PDA 的方法，可以这么构造
    <div style="text-align:center;">
		<img src="../imgs/toc/3.2.jpg" alt="3.2" style="zoom:15%;" />
	</div>
    然而直接构造可以这样
	<div style="text-align:center;">
		<img src="../imgs/toc/3.3.jpg" alt="3.3" style="zoom:15%;" />
	</div>
    这里的 $c$ 充当**栈底符**的作用，即说明已经读到了栈底。由于读到 $e$ 并不能说明已经到栈底了（即使栈里还有很多也可以读 $e$），所以这个栈底符是必要的。
    
    整体逻辑很清晰：第一步放入栈底符，然后不断读，过量的存入栈，读入和栈顶(非 $c$)不同的可以相消。这样，$c$ 上方就只能都是 $a$ 或都是 $b$。直到 $c$ 出现在栈顶时就可以进入终结状态，当然也可以继续读输入。

显然地，只要不做任何栈操作，PDA 就是 NFA。所以 FA 就是一种 PDA。

### Pushdown Automata and Context-Free Grammars

将 PDA 接受的语言和 CFL 等价起来。

#### CFG $\to$ PDA

CFG $G=(V, \Sigma, R, S)$，$M=(K, \Sigma, \Gamma, \Delta, s, F)$，令

$$
    \begin{aligned}
        K &= \{s, f\}\\
        \Gamma &= V\\
        F &= \{f\}\\
        \Delta &= \{    ((s, e, e), (f, S)),\\
                &\qquad ((f, e, A), (f, x)), \forall A\to x,\\
                &\qquad ((f, a, a), (f, e)), \forall a\in \Sigma \}
    \end{aligned}
$$

!!! question "Example"
    $L=\{wcw^R:\; w\in\{a, b\}^*\}$ 对应的 CFG 为 $G=(V, \Sigma, R, S)$，其中 $V=\{S, a, b, c\}$, $\Sigma=\{a, b, c\}$, $R=\{S\to aSa, S\to bSb, S\to c\}$

    给定 $abbcbba$，写出推导过程和计算过程中格局的变化。

CFG $\to$ PDA 的本质就是模拟最左推导。下面给出 $L(G)=L(M)$ 的证明：
??? general "Proof"
    给出一个 claim：$\forall w\in\Sigma^*$, $\alpha\in (V-\Sigma)V^*\cup\{e\}$, 
    
	$$
	    S\stackrel{L}{\Rightarrow}^* wa \iff
	    (q, w, S)\vdash_M^*(q, e, \alpha)
	$$
	
	如果该 claim 成立，则取 $\alpha=e$，左侧就等价于 $w\in L(G)$，右侧就等价于 $w\in L(M)$，从而得证。于是下证该 claim。
	
	(1) 正推基于最左推导的步数进行数学归纳。
	
	**Basis step**: 推导长度为 0，$w=e$，$\alpha=S$，显然有 $(q, w, S)\vdash_M^*(q, e, \alpha)$ (一步都没有)
	
	**Induction hypothesis**: 对 $n\geqslant 0$ 步以内的最左推导都成立
	
	**Induction step**: 设 $n+1$ 步的最左推导如下
	
	$$
	    S=u_0\stackrel{L}{\Rightarrow}u_1\stackrel{L}{\Rightarrow}\cdots
	    \stackrel{L}{\Rightarrow} u_n \stackrel{L}{\Rightarrow} u_{n+1}=w\alpha
	$$
	
	设 $u_n=xA\beta$，其中 $A$ 是 $u_n$ 中最左的非终结符。再设第 $n+1$ 步最左推导使用的是 $R$ 中的 $A\to \gamma$ 规则，则 $u_{n+1}=x\gamma\beta$。以上有 $x\in\Sigma^*, \beta, \gamma\in V^*$。
	
	对 $S\stackrel{L}{\Rightarrow}^* u_n$ 利用 IH，可知有 $(q, x, S)\vdash_M^*(q, e, A\beta)$。利用 $A\to \gamma$ 有
	
	$$
	    (q, e, A\beta)\vdash_M(q, e, \gamma \beta)
	$$
	
	根据 $u_{n+1}=w\alpha=x\gamma\beta$ 有 $\exists\; y\in \Sigma^*$ s.t. $w=xy, y\alpha=\gamma\beta$ ($w$ 是左侧最长连续的 $\Sigma^*$，所以 $x$ 一定是其前缀)。这样就有
	
	$$
	    (q, x, S)\vdash_M^*(q, e, \gamma \beta)\Rightarrow
	    (q, w, S)\vdash_M^*(q, y, y\alpha)\vdash_M^*(q, e, \alpha)
	$$
	
	$y$ 的消除利用了所构造的 $M$ 的第三阶段规则，故完成了正推。
	
	(2) 反推基于第二阶段 PDA 转移的次数进行数学归纳。
	<div style="text-align:center;">
		<img src="../imgs/toc/3.4.jpg" alt="3.4" style="zoom:15%;" />
	</div>

#### PDA $\to$ CFG

整体分为 3 步：

- 定义简单 PDA
- PDA $\to$ 简单 PDA
- 简单 PDA $\to$ CFG

!!! info "简单 PDA"
    如果满足如下条件，则 PDA $M=(K, \Sigma, \Gamma, \Delta, s, F)$ 是简单 (simple) 的：
    
	$$
	    \forall ((q, a, \beta), (p, \gamma))\in\Delta, \text{若}q\neq s,\text{则}\beta\in\Gamma, |\gamma|\leqslant 2
	$$
	
	即读栈只读1字符，写栈长度不超过2。但是对初始状态出发的转移不做限制。

把原有的 $M=(K, \Sigma, \Gamma, \Delta, s, F)$ 改造为简单PDA $M'=(K', \Sigma, \Gamma\cup \{Z\}, \Delta', s', {f'})$。

- 保证$((s', e, e), (s, Z))\in\Delta'$，到达原起始状态并压入栈底符$Z$
- 保证$\forall f\in F, ((f, e, Z), (f', e))$，使每一个原终结状态都能吸收栈底符到达真正的唯一终结状态。
- 接下来考虑中间的转移改造。
    - 除去读栈 $\beta\geqslant 2$ 的转移，只需要增加中间状态分次读，每次只读 1 字符，最后一次又读 1 字符又写 $\gamma$。
    - 除去写栈 $\gamma\geqslant 2$ 的转移，但不引入 $\beta\geqslant 2$ 的转移。同理分次写，每次写1字符。
    - 除去不读栈 ($\beta=e$) 的转移，且不引入 $\beta\geqslant 2, \gamma > 2$ 的转移。这里只需要增加 $|\Gamma\cup \{Z\}|$ 个转移：
    
	$$
        ((q, a, A), (p, \gamma A)), \forall A\in\Gamma\cup \{Z\}
    $$

    即每次多读 1 个，然后写回。由于至少有一个栈底符，因此总是可读的。

综上，完成了 PDA $\to$ simple PDA，那么接下来就是 simple PDA $\to$ CFG。

设计的新 CFG 中的非终结符表达了一种推导进度的含义。非终结符 $<q, A, p>$，$q$ 在前 $p$ 在后，期望最后 $q=p$ 然后可以消为 $e$，而初始为 $<s, Z, f'>$ 表达最遥远的距离。而 $A$ 是栈顶符，因为 simple PDA 的“每次读且只读栈顶符”的设计，导致只需要原状态 + 栈顶符，就可以通过遍历 $K'$ 掌握所有可能的状态转移。

$R$ 中的规则有四种类型：

- $S \rightarrow\left\langle s, Z, f^{\prime}\right\rangle$: 初始压栈
- $\langle q, B, p\rangle \rightarrow a\langle r, C, p\rangle$: 不压栈或压栈 1 字符的转移
    - $\forall ((q, a, B),(r, C))\in \Delta$, 保证 $q, r \in K^{\prime}-\left\{s^{\prime}\right\}$
    - 可知有 $a \in \Sigma \cup\{e\}, B \in \Gamma \cup\{Z\}$ 及 $C \in \Gamma \cup\{Z, e\}$
    - 根据每一个这样的转移，遍历 $p \in K^{\prime}-\left\{s^{\prime}\right\}$ 以创建此规则。
- $\langle q, B, p\rangle \rightarrow a\left\langle r, C_1, p^{\prime}\right\rangle\left\langle p^{\prime}, C_2, p\right\rangle$: 压栈2字符的转移
    - $\forall \left((q, a, B),\left(r, C_1 C_2\right)\right)\in \Delta$，同样保证 $q, r \in K^{\prime}-\left\{s^{\prime}\right\}$
    - 可知有 $a \in \Sigma \cup\{e\}$ 及 $B, C_1, C_2 \in \Gamma \cup\{Z\}$
    - 根据每一个这样的转移，遍历 $p, p^{\prime} \in K^{\prime}-\left\{s^{\prime}\right\}$以创建此规则
- $\langle q, e, q\rangle \rightarrow e$: 到达叶节点，变$e$
    - $\forall q \in K^{\prime}-\left\{s^{\prime}\right\}$ 添加该规则。

!!! tip "Remark"
    2、3 中在所有状态中任意选择 $p, p'$，这是因为不知道中间状态，所以只能由规则提供通过每个中间状态的途径，然后实际推导的时候不断模拟压栈试错，直到找出正确路径。

关于证明这样构造的 CFG 恰恰能够产生 $L(M)$，需要如下 claim：$\forall q, p\in K, A\in \Gamma\cup \{e\}, x\in \Sigma^*$ 有

$$
    <q, A, p>\Rightarrow_G^* x \iff
    (q, x, A)\vdash_M^* (p, e, e)
$$

取 $q=s, p=f\in F, A=e$，那么左侧就等价于 $x\in L(G)$，右侧等价于 $x\in L(M)$。

和 CFG $\to$ PDA 类似，基于推导步数/PDA 转移的次数进行数学归纳就可以证明 claim。

### Languages that are and are not Context-Free

#### Closure Properties

!!! abstract "Theorem"
    CFL 关于**并、连接、Kleene Star** 封闭。

??? general "Proof"
    设 CFG $G_1=(V_1, \Sigma_1, R_1, S_1), G_2=(V_2, \Sigma_2, R_2, S_2)$。调整编码保证 $(V_1-\Sigma_1)\cap (V_2-\Sigma_2)=\emptyset$，得到 $G=(V, \Sigma, R, S)$。具体构造方法类似正则表达式运算构造 FA，如下所示：
    
    - 并：$V=V_1 \cup V_2 \cup \{S\}$, $\Sigma=\Sigma_1 + \Sigma_2$
        
    $$
    	R = R_1 \cup R_2 \cup \{S\to S_1, S\to S_2\}
    $$
        
    - 连接：$V=V_1 \cup V_2 \cup \{S\}$, $\Sigma=\Sigma_1 + \Sigma_2$
        
    $$
    	R = R_1 \cup R_2 \cup \{S\to S_1S_2\}
    $$
    
    - Kleene Star：$V=V_1 \cup \{S\}$, $\Sigma=\Sigma_1$
        
    $$
    	R = R_1 \cup \{S\to e, S\to SS_1\}
    $$


!!! abstract "Theorem"
    CFL 和正则语言的交还是 CFL。

??? general "Proof"
    并行模拟。PDA $M_1=(K_1, \Sigma, \Gamma_1, \Delta_1, s_1, F_1)$, DFA $M_2 = (K_2, \Sigma, \delta, s_2, F_2)$，构造 PDA $M=(K, \Sigma, \Gamma, \Delta, s, F)$:
    
	$$
        \begin{aligned}
            K &= K_1 \times K_2\\
            \Gamma &= \Gamma_1\\
            s &= (s_1, s_2)\\
            F &= F_1\times F_2\\
            \Delta &= \{(((q_1, q_2), a, \beta), ((p_1, \delta(q_2, a)), \gamma)):\; ((q_a, a, \beta), (p_1, \gamma))\in \Delta_1, q_e\in K_2\}
        \end{aligned}
    $$


!!! question "Example"
    证明 $L=\{w\in\{a, b\}^*:\; w$ 中 $a, b$ 等量，且不含子串 $abaa$ 或 $babb$\} 是CFL。

??? general "Proof"
    设 $\Sigma=\{a, b\}$。
	
	$L_1=\{w\in\Sigma^*:\; w$ 中 $a, b$ 等量 \}是 CFL，
	
	而 $L_2=\Sigma^*-\Sigma^*(abaa\cup babb)\Sigma^*$ 是正则语言。所以 $L=L_1\cap L_2$ 是CFL 。

#### Pumping Theorem

!!! abstract "Lemma"
    $G$ 高为 $h$ 的语法树生成的字符串长度至多为 $\phi(G)^h$。$\phi(G)$ 是扇出 (Fanout)，描述 $R$ 中推导规则右侧最大的字符数量。

数学归纳很容易就能证明这个引理。

!!! abstract "泵定理 (Pumping Theorem)"
    对 CFG $G=(V, \Sigma, R, S)$, $\forall w\in L(G)$，若 $|w|>\phi(G)^{|V-\Sigma|}$，则 $w$ 可以表示为 $w=uvxyz$，满足
    
	$$
	    |vy|\geqslant 1, \text{且}\forall n\geqslant 0, uv^nxy^nz\in L(G)
	$$

??? general "Proof"
    $|w|>\phi(G)^{|V-\Sigma|}$，根据Lemma可知语法树高度$>|V-\Sigma|$，所以存在一条至少长$|V-\Sigma|+1$的路径，上面有$|V-\Sigma|+2$个结点。这$|V-\Sigma|+2$个结点中，只有叶节点是终结符，根据鸽巢原理，剩下$|V-\Sigma|+1$个结点中至少两个结点相同。语法树分割如下：
	<div style="text-align:center;">
		<img src="../imgs/toc/3.5.png" alt="3.5" style="zoom:50%;" />
	</div>

    显然可看出重复$v, y$依然属于 $L(G)$。如果预先要求语法树是生成$w$的叶子最少的语法树（因为叶子是$e$的话不影响结果），那么若$vy=e$，删去其相关部分之后依然能生成$w$，但是叶子更少，就不行了。由此就可以证明$|vy|\geqslant 1$。


!!! question "Example"
    证明 $L=\{a^nb^nc^n:\; n\geqslant 0\}$不是 CFL。

<div style="text-align:center;">
	<img src="../imgs/toc/3.6.jpg" alt="3.6" style="zoom:15%;" />
</div>

!!! question "Example"
    证明 $L=\{a^n:\; n\text{是质数}\}$ 不是CFL。

    设 $vy=a^q, uxz=a^r$，则要求 $r+nq$ 总是质数，这是不现实的，如令 $n=r+2q+2$。


!!! tip "Remark"
    单字符 alphabet 上的 CFL 都是正则语言。

!!! question "Example"
    $L=\{w\in\{a, b, c\}^*\;|\;w$ 中 $a, b, c$ 等量\}不是 CFL，将其和 $a^*b^*c^*$ 相交即可。


!!! abstract "Theorem"
    CFL 在**交**和**补**运算下不封闭。

??? general "Proof"
    $L_1=\{a^nb^n:\;n\geqslant 0\}c^*, L_2=a^*\{b^nc^n:\; n\geqslant 0\}$，则 $L_1\cap L_2$非 CFL。

    对于补，考虑 $L_1\cap L_2=\overline{\overline{L_1}\cup \overline{L_2}}$ 即可。

### Algorithms for Context-Free Grammars

!!! abstract "Theorem"
    - CFG $\to$ 等价 PDA: 多项式时间
    - PDA $\to$ 等价 CFG: 多项式时间
    - 给定 CFG 和 $x$，判定是否 $x\in L(G)$: 多项式时间

!!! tip "Remark"
    - 没有算法可以判定两个 CFG 是否等价，或者两个 PDA 是否等价
    - 正则语言不需要以上的第三个算法，因为 DFA 就是天然确定性算法。但是 CFG 只有非确定性的 PDA 对应，因此要设计确定性的算法去判定成员资格

对于这个成员资格判定问题，暴力穷举当然可以，但是是指数时间的。考虑动态规划：

- 将 $G$ 转化为 Chomsky 范式(Chomsky normal form, CNF)
- 针对 CNF 语法应用算法

!!! info "Chomsky 范式 (CNF)"
    如果 $R\subseteq (V-\Sigma)\times V^2$，则称 CFG $G=(V, \Sigma, R, S)$ 是 CNF。

- 要求右侧生成的不多不少是 2 个字符。
- CNF 无法生成长度小于 2 的串，但这不影响成员资格判定。

!!! abstract "Theorem"
    $\forall$ CFG $G$，有 CNF 下的 CFG $G^{\prime}\text{ s.t. } L\left(G^{\prime}\right)=L(G)-\left(\sum \cup\{e\}\right)$。
    
    创建 $G^{\prime}$ 的时间复杂度是关于 $G$ 的 size 的多项式时间。

??? general "Proof"
    需要解决 $R$ 中以下三种规则：
    
    - 长规则: $A \rightarrow \alpha$, $|\alpha|>2$
    - $e$-规则: $A \rightarrow e$
    - 短规则: $A \rightarrow a$ 或 $A \rightarrow B$
    
    分别进行处理：
    
    - 切断长规则 $A\to B_1B_2\cdots B_n\in R, n\geqslant 3$。得到 $n-1$ 条规则：
    
    $$
        \begin{aligned}
            & A\to B_1A_1\\
            & A_1\to B_2A_2\\
            & \cdots\\
            & A_{n-2}\to B_{n-1}B_n
        \end{aligned}
    $$
    
    - 除去 $e$-规则，定义 $\mathcal{E}=\{A\in V-\Sigma:\; A\Rightarrow ^* e\}$，即能导出 $e$ 的非终结符集合
  
    ```pseudocode title="计算 E"
    E := emptyset
	while there is A->a in R, a in E^*, A not in E:
		add A to E
    ```
    
    其实算法和计算 NFA 转 DFA 的 $E(p)$ 是一样的。计算完 $\mathcal{E}$ 之后，对推导得到 $\mathcal{E}$ 中元素的规则需要进行替换，如下所示：
    <div style="text-align:center;">
    	<img src="../imgs/toc/3.7.png" alt="3.7" style="zoom:50%;" />
    </div>
    最后除去这些 $e$-规则
    - 除去短规则同样也要考虑后果。考虑每个 $A\in V$ 能够推导出来的所有单字符集合 $\mathcal{D}(A)=\{B\in V:\; A\Rightarrow^* B\}$
    ```pseudocode title="计算 D(A)"
    D(A) := {A}
	while there is B->C in R, B in D(A), C not in D(A):
		add C to E
    ```

    注意总有 $A\in \mathcal{D}(A)$，若 $a\in \Sigma$，则 $\mathcal{D}(a)=\{a\}$。
    
    接下来的操作 PPT 上不够全面，采纳课本的说法。
    
    先计算全部 $\mathcal{D}(A)$，再删去所有短规则。然后剩下的就都是 $A\to BC$ 规则了，全部替换为 $A\to B'C'$ 规则，其中 $B'\in \mathcal{D}(B), C'\in \mathcal{D}(C)$。这里就模拟了 $B$ 产生 $B'$ 以及 $C$ 产生 $C'$ 的一系列短规则的效果。
    
    最后还有一条特殊的，回过头再看每一条 $A\to BC$，如果 $A\in \mathcal{D}(S)-\{S\}$，就添加规则 $S\to BC$。

!!! question "Example"
    $R=\{S\to SS, S\to (S), S\to e\}$，转换对应的CFG为CNF。

<div style="text-align:center;">
	<img src="../imgs/toc/3.8.jpg" alt="3.8" style="zoom:15%;" />
</div>

最后给出动态规划算法。定义能够推导出 $x_i\cdots x_{i+s}$ 的字符集

$$
    N[i, i+s]=\{X\in V:\; X\Rightarrow^* x_i\cdots x_{i+s}\}
$$

```pseudocode title="判定是否有 x in L(G)"
初始化所有 N[i, j] 为空集
for i = 1 to n:
	N[i, i] := {x_i}

for s = 1 to n-1:
	for i = 1 to n-s:
		for k = i to i+s-1:
			if there is A->BC in R, B in N[i, k], C in N[k+1, i+s]:
				N[i, i+s] := N[i, i+s] U {A}

when S in N[1, n], accept x
```

先计算能推导出长度为 $2$ 的字符集，然后 $3$ ……最后算出长度为 $n$ 的字符集。每一长度下，移动区间起点一一计算，每一区间都遍历所有的分割方式。

!!! question "Example"
    继续上个example计算的CNF，判定是否有$(()(()))\in L(G)$?

<div style="text-align:center;">
	<img src="../imgs/toc/3.9.png" alt="3.9" title="图片标题" style="zoom:50%;" />
</div>

计算时从对角线开始，向左下角慢慢计算。根据最左下角的 $S$，判定属于。

## Turing Machine

## Undecidability