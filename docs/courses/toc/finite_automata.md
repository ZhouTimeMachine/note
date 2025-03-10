<link rel="stylesheet" href="../../../css/counter.css" />

# Finite Automata

!!! info "Part of note taken on ZJU *Introductiion to Theoretical Computer Science*, 2022 Fall & Winter"

## Deterministic Finite Automata

考虑确定性有限自动机(Deterministic Finite Automata, DFA)，有输入带(Input tape)、读头(Reading head, 可以认为从左向右读，一次读一格)、有限控制(Finite control)。

!!! info "Definition"
    DFA 被定义为五元组 (quintuple)：$(K, \Sigma, \delta, s, F)$，即包括
    
    - 状态(state)的**有限**集 $K$
    - 字符集 $\Sigma$
    - 是初态 $\delta\in K$
    - 末态**集合** $F\subseteq K$
    - 状态转移**函数** $\delta: K\times \Sigma\to K$
    

!!! tip "Remark"
    
    - **格局(configuration)**：对 DFA $(K, \Sigma, \delta, s, F)$ 而言，由现态和待处理的 input tape 字符串组成，即是 $K\times \Sigma^*$ 中的一个元素
    - $\vdash_M$：二元关系“一步产生” (yields in one step)， 格局到格局。
    
    $$
        (q, w) \vdash_M\left(q^{\prime}, w^{\prime}\right)
        \iff
        \exists\; a \in \Sigma, w=a w^{\prime}\text{, and }\delta(q, a)=q^{\prime}
    $$

    - $\vdash^*_M$：$\vdash_M$ 的自反传递闭包，允许零步(自反)
    - **接受(accepet)**：$w\in\Sigma^*$ 被 $M$ 接受指
    
    $$
        \exists\; q\in F \text{ s.t. } (s, w)\vdash_M^* (q, e)
    $$

    $L(M)$ 代表被 $M$ 接受的语言，即所有被 $M$ 接收的字符串的集合。

!!! example "Example"
    $L(M)$ 求补，$M=(K, \Sigma, \delta, s, F)$ 中只需要把 $F$ 关于 $K$ 求补就行。


## Nondeterministic Finite Automata

### NFA

非确定性有限自动机 (Nondeterministic Finite Automata, NFA) 相对 DFA 只是允许了多个次态，但就此就能够简化 DFA 的表示。

!!! info "NFA"
    NFA 是 quintuple $(K, \Sigma, \Delta, s, F)$，和 DFA 有所区别的只有 $\Delta$。
    
    不同于 $\delta$ 是状态转移**函数**，$\Delta$ 仅仅是状态转移**关系**，有

    $$
        \Delta \subseteq K\times (\Sigma\cup \{e\})\times K
    $$

!!! tip "Remark"
    - 不同于 $\delta$，$\Delta$ 允许读头不从 input tape 读取字符。即 $(q, u, p)\in\Delta$，允许 $u=e$，此时不读取输入字符。
    - 格局，$\vdash_M$，$\vdash_M^*$ 和接受同理可定义
    
!!! question "Example"
    为 $L=\left\{ w\in\left\{ a, b \right\}^*\;|\; w\text{ 中有 }bb\text{ 或 }bab \right\}$ 设计 NFA

这个例子难度不高，但是PPT上需要做一个勘误：$q_2$ 应该也是一个末态。

!!! question "Example"
    $\Sigma=\left\{ a_1,\cdots , a_n \right\},\; n\geqslant 2$, $L=\left\{ w\in\Sigma^*\;|\; \exists a_i\text{ 没有在 }w\text{ 中出现} \right\}$

初态 $e$ 转移到 $q_1,\cdots, q_n$，然后在 $q_i$ 只接受非 $a_i$ 的输入。

两个 FA 的等价性：仅当 $L(M_1)=L(M_2)$。需要将 DFA 和 NFA 统一为 FA。

### NFA/DFA Equivalence

整体分两步：

- $\forall$ DFA, 创建 NFA 以接受相同的语言
- $\forall$ NFA, 创建 DFA 以接受相同的语言

由于每个 DFA 都是 NFA，所以第一步不言自明。因此只需要做第二步。（其实就是只需要构造 DFA 表达 NFA，使得证明看似计算能力更强的 NFA 计算能力也能被 DFA 包括）

证明的关键思想：将 NFA $(K, \Sigma, \Delta, s, F)$ 的 $K$ 的子集作为所构造的DFA的状态。这样，DFA $(L', \Sigma, \delta, s', F')$ 中至多有 $|K'|=2^{|K|}$。引入如下的定义：

!!! info "Definition"
    $E(q)=\left\{ p\in K: (q, e) \vdash_M^* (p, e) \right\}$

!!! tip "Remark"
    $E(q)$ 表示 NFA 从 $q$ 状态 $e$ 转移能到达的所有状态。

??? general "Proof"
    这样，令

    $$
        K' = 2^{K},\quad
        s' = E(s),\quad
        F' = \left\{ Q\subseteq K \;|\; Q\cap F\neq \emptyset \right\}
    $$

    对于 $\delta$, $\forall\; Q\in K'(Q\subseteq K), a\in \Sigma$, 

    $$
        \delta(Q, a)=\bigcup \left\{ E(p) \;|\; p\in K\text{, and }\exists \; q\in Q \text{ s.t. } (q, a, p)\in\Delta \right\}
    $$

    记上式为 (1)。
    
    然后证明这个构造得到的 $M'$ (1) deterministic (2) equivalence with NFA $M$
    
    - **deterministic**: 根据 $\delta$ 的定义，它是单值 ($\delta(Q, a)$ 值确定) 且良定义的 ($\delta(Q, a)\in K'$)。注意，$\emptyset\in K'$，所以 $\delta(Q, a)=\emptyset$ 也是合法的。
    - **equivalence**: 假设我们证明了以下 claim：$\forall w\in\Sigma^*, p, q\in K$，
    
    $$
        (q, w)\vdash_M^* (p, e) \iff
        \exists \; P\subseteq K \text{ s.t. } (E(q), w) \vdash_{M'}^* (P, e), p\in P
    $$

    这样就有

    $$
        \begin{aligned}
            w\in L(M)
            &\iff \exists f\in F \text{ s.t. } (s, w)\vdash_M^* (f, e)\\
            &\iff \exists Q\subseteq F \text{ s.t. } (E(s), w)\vdash_{M'}^* (Q, e), f\in Q\\
            &\iff (E(s), w)\vdash_{M'}^* (Q, e), Q\in F' \\
            &\iff w\in L(M')
        \end{aligned}
    $$

    第一行利用了 DFA 接受 $w$ 的定义，第二行利用了 claim，第三行利用了 $F'$ 的定义，第四行利用了 NFA 接受 $w$ 的定义。

    因此只要证明了 claim，就能证明 equivalence。下面利用数学归纳证明 claim。

    **Basis step**: 考虑$|w|=0$，即$w=e$。根据$E(q)$定义，有$(q, e)\vdash_M^*(p, e)\iff p\in E(q)$。另一方面，$(E(q), e) \vdash_{M'}^* (P, e), p\in P\iff p\in P=E(q)$。

    **Induction hypothesis**: claim对于$|w|\leqslant k$都成立，$k\geqslant 0$
    
    **Induction step**: 令$|w|=k+1$，则可以表示$w=va, v\in \Sigma^*, a\in \Sigma$。
    
    $$
        (q, w)\vdash_M^* (p, e) \iff (q, va)\vdash_M^* (r_1, a) \vdash_M (r_2, e) \vdash_M^* (p, e)
    $$

    以上式子记为 (2) 式。

    由于 $|v|=k$，利用 (2) 
    
    $$
        (q, va)\vdash_M^* (r_1, a)
        \iff (q, v)\vdash_M^* (r_1, e)
        \iff (E(q), v)\vdash_{M'}^* (R_1, e), r_1\in R_1
    $$

    以上式子记为 (3)。利用 (2) 右侧的中间部分，有
    
    $$
        (r_1, a)\vdash_M (r_2, e)\iff
        (r_1, a, r_2)\in \Delta
        \Rightarrow E(r_2)\subseteq \delta(r_1, a) \; (\text{根据 (1) 式})
    $$

    以上式子记为 (4)。再结合 (2) 右侧的右部分有

    $$
        (r_2, e)\vdash_M^* (p, e) \iff
        p\in E(r_2)
    $$

    以上式子记为 (5)。因此结合 (4)(5) 有 (2) $\Rightarrow p\in E(r_2)\subseteq \delta (r_1, a)$，则令 $P=\delta (r_1, a)$ 有
    
    $$
        (2)\Rightarrow
        (E(q), w)\vdash_{M'}^* (R_1, a) \vdash_{M'} (P, e),\quad p\in P
    $$

    需要注意区分的是以上的双向 $\iff$ 和单向 $\Rightarrow$，双向往往是根据定义的等价，以及多步 $\vdash_M^*$ 和单步 $\vdash_M$ 也需要注意。**接下来证明反推**，可以从以下出发：

    $$
        \exists \; P\subseteq K \text{ s.t. } (E(q), w) \vdash_{M'}^* (R_1, a) \vdash_{M'} (P, e), \;p\in P
    $$

    注意 DFA $M'$ 每步读且只读一个字符，且 $R_1$ 是设出来的，即尚未知 $r_1\in R_1$，甚至 $r_1, r_2$ 还未定义。首先利用上式后半部分，有

    $$
        (R_1, a) \vdash_{M'} (P, e) \Rightarrow \delta(R_1, a)=P
    $$

    不同于正推时定义 $P=\delta(R_1, a)$，这次是根据 $P$ 的存在性推导出了此式。回顾 (1) 式有

    $$
        p\in P=\delta(R_1, a)=\bigcup\left\{E(r_2) \;|\; r_2\in K\text{, and }\exists \; r_1\in R_1 \text{ s.t. } (r_1, a, r_2)\in\Delta \right\}
    $$

    因此 $\exists \;r_1\in R_1, r_2\in K, \text{ s.t. } (r_1, a, r_2)\in\Delta,\; p\in E(r_2)$。利用 $r_1\in R_1$，由 (3) 反推有 $(q, va)\vdash_M^* (r_1, a)$，由此继续就有

    $$
        (q, va)\vdash_M^* (r_1, a)\underbrace{\vdash_M (r_2, e)}_{(r_1, a, r_2)\in\Delta}\underbrace{\vdash_M^* (p, e)}_{p\in E(r_2)}
    $$

    由此完成了 claim 的证明，也完成了整体的证明。
    

!!! tip "Remark"
    构造的 DFA 的 size 相对原 NFA 发生了指数增长。从以上证明过程中，我们也得到了 NFA 转换为 DFA 的构造方法。第一步先无脑计算所有 $E(q)$，然后根据 $\delta(Q, a)$ 的定义慢慢算就行。

## Finite Automata and Regular Expressions

即将证明 FA 的表达能力就是正则语言。

### Closure Properties of Regular Languages

!!! Abstract "正则语言运算封闭性"
    被 FA 接受的语言(后续将证明就是正则语言)在以下运算下是封闭 (closed) 的：
    
    1. Union
    2. Concatenation
    3. Kleene star
    4. Complementation
    5. Intersection

??? general "Proof"
    
    (1) 构造NFA如下
    <div style="text-align:center;">
    	<img src="../../imgs/toc/2.1.drawio.png" alt="2.1" style="zoom:60%;" />
    </div>

    事实上也可以认为是一种并行模拟，哪边走得通走哪边。

    令 $M_1=(K_1, \Sigma, \Delta_1, s_1, F_1), M_2=(K_2, \Sigma, \Delta_2, s_2, F_2)$，则 $M(K, \Sigma, \Delta, s, F)$ 有

    $$
    \begin{aligned}
        K &= \left\{ s \right\} \cup K_1 \cup K_2\\
        F &= F_1 \cup F_2\\
        \Delta &= \Delta_1 \cup \Delta_2 \cup \left\{ (s, e, s_1), (s, e, s_2) \right\}
    \end{aligned}
    $$

    注意 $K_1, K_2$ 各状态编码需要不同，以免 Union 时重复。

    (2) 构造 NFA 如下
    <div style="text-align:center;">
    	<img src="../../imgs/toc/2.2.drawio.png" alt="2.2" style="zoom:60%;" />
    </div>

    $M_1$ 的末态不再是末态，并 $e$ 转移到 $M_2$ 的初态。即

    $$
    \begin{aligned}
        K &= K_1 \cup K_2\\
        F &= F_2\\
        s &= s_1\\
        \Delta &= \Delta_1 \cup \Delta_2 \cup \left\{ (f_1, e, s_2): f_1\in F_1 \right\}
    \end{aligned}
    $$

    (3) 构造 NFA 如下
    <div style="text-align:center;">
    	<img src="../../imgs/toc/2.3.drawio.png" alt="2.3" style="zoom:60%;" />
    </div>

    单独的 $s$ 是必要的，否则如果把 $s_1$ 简单地作为 $s$，并且为了包含空串把它变成末态之一的话，如果 $M_1$ 中有非末态的状态可以转移到 $s_1$，那么就寄了。

    这样就有

    $$
    \begin{aligned}
        K &= K_1 \cup \left\{ s \right\}\\
        F &= F_1 \cup \left\{ s \right\}\\
        \Delta &= \Delta_1 \cup \left\{ (s, e, s_1) \right\} \cup \left\{ (f_1, e, s_1): f_1\in F_1 \right\}
    \end{aligned}
    $$

    (4) 非常简单，转 DFA 后对 $F$ 关于 $K$ 求补即可。
    (5) 简单地，把Intersection使用Union和Complementation表示，即

    $$
        L_1\cap L_2=\overline{\overline{L_1}\cup \overline{L_2}}
    $$

    硬去构造 DFA，可以使用并行模拟的方法。
    
    设 $M_1=(K_1, \Sigma, \delta_1, s_1, F_1), M_2=(K_2, \Sigma, \delta_2, s_2, F_2)$，则

    $$
        \begin{aligned}
            K &= K_1 \times K_2\\
            s &= (s_1, s_2)\\
            F &= F_1 \times F_2\\
            \delta &: K \times \Sigma \to K,\quad \delta((q_1, q_2), a)=(\delta(q_1, a), \delta(q_2, a))
        \end{aligned}
    $$

#### Regular Languages and FA

!!! Abstract "正则语言与 FA 的统一"
    $L$ 是正则语言 $\iff$ $L$ 被一个 FA 接受

??? general "Proof"
    $\Rightarrow$: 基本正则表达式为 $\circleddash$ 和 $\left\{ x \right\}(\forall x\in \Sigma)$，两者都可以被 FA 表示，再通过前面的方法将表达基本正则表达式的 FA 按照 $L$ 对应的正则表达式进行并、连接、Kleene Star 对应的方法进行连接，这样就可以构造出接受 $L$ 的 FA。

    $\Leftarrow$: 考虑 FA $M=(K, \Sigma, \Delta, s, F)$, $K=\{q_1, \cdots, n\}$, $s = q_1$, $F = \{q_n\}$。这里改造了 $F$，如必要增加一个末态使得所有原来的末态都e转移到这个末态，并把原来的末态从 $F$ 中删去。

    !!! info "$R(i, j, k)$"
        对 $i, j=1,\cdots, n$ 和 $k=0, \cdots, n$，令 $R(i, j, k)$ 为 $\Sigma^*$ 中能使从状态 $q_i$ 到达 $q_j$，且中间不经过编号大于 $k$ 的中间状态的字符串。（类似 Warshall 的思想）
        
    当 FA 是 DFA 时，$\Delta=\delta$，$R(i, j, k)$ 可以写作

    $$
        R(i, j, k) = \left\{ w \in \Sigma^*\;|\; \delta(q_i, w)=q_j\text{, 且对 }\forall w \text{ 的前缀 }x, x\neq e, \delta(q_i, x)=q_l, \text{有 }l\leqslant k \right\}
    $$
    
    特别地，$k=0$ 时，就是能让 $q_i$ 直接到达 $q_j$ 的字符串（单字符或 $e$）。

    $$
        R(i, j, 0) = 
        \begin{cases}
            \left\{ a\;|\;\delta(q_i, a)=q_j \right\},& i\neq j\\
            \left\{ a\;|\;\delta(q_i, a)=q_j \right\}\cup \{e\},& i= j
        \end{cases}
    $$

    上式记为 (1) 式。扩展到 $k=n$ 时，就是能够让 $q_i$ 到达 $q_j$ 的所有字符串。

    $$
        R(i, j, n) = \left\{ w\in\Sigma^* \;|\; (q_i, w)\vdash_M^* (q_j, e) \right\}
    $$


    最后就能把被 $M$ 接受的语言表示为

    $$
        L(M)=\bigcup \left\{ R(1, j, n) \;|\; q_j \right\}
    $$

    该式记为 (2)。

    !!! Abstract "Theorem"
        $R(i, j, k)$ 总是正则语言。


    ??? general "Proof"
        关于 $k$ 应用数学归纳。
        
        **Basis step**: $k=0$，由 (1) 可知 $R(i, j, 0)$ 是有限语言，自然正则。

        **Induction step**: 从 $q_i$ 到 $q_j$ 利用编号小于等于 $k+1$ 的中间状态能实现的字符串，首先如果用不到 $q_{k+1}$ 肯定可以，也就是 $R(i, j, k)$；然后对于用到 $q_{k+1}$ 的情况，则把整个变换路径中所有 $q_{k+1}$ 都 highlight，如果只有一个那就是 $R(i, k+1, k)R(k+1, j, k)$，但是出现多个 $q_{k+1}$ 的情况就需要在中间使用 $R(k+1, k+1, k)^*$ 进行传递，保证每一小段中间都只用到编号小于等于 $k$ 的状态。最后就得到下式：

        $$
            R(i, j, k+1)=R(i, j, k)\cup R(i, k+1, k)R(k+1, k+1, k)^* R(k+1, j, k)
        $$
        
        上式记为 (3) 式。利用 Induction Hypothesis，则证得 $R(i, j, k+1)$ 正则。数学归纳证得定理。

    
    根据 (2)，就完成了证明。

然后就需要实操 FA 到正则表达式的转换。总体上有以下技巧：

!!! tip "Remark"
    对每一对状态 $q_i\neq q, q_j\neq q$，在消去 $q$ 的时候要对 $q_i\to q_J$ 做如下更新：

    <div style="text-align:center;">
    	<img src="../../imgs/toc/2.4.png" alt="2.4" style="zoom:50%;" />
    </div>

## Languages that are and are not Regular

有三种方法可以证明一种语言**是**正则语言：

- 被 FA 接受
- 被正则表达式指定
- 利用正则语言运算封闭性

!!! question "Example"
    $\Sigma=\{0, 1, \cdots, 9\}$, $L=\{w\in\Sigma^*\;|\; w\text{ 是无前导 0 的非负整数的十进制表示，被 2 和 3 整除}\}$。 求证 $L$ 是正则语言。

**hint**: “无前导 0 的非负整数”得到 $L_1$，最后一位确认后再与 $L_1$ 相交可以得到整除 2 的 $L_2$，再得到整除 3 的 $L_3$，通过 $L_2\cap L_3$ 证明。

FA 状态有限，因此只能“记住”有限的东西。例如 Balanced parentheses(需要记住一个任意的嵌套深度)和 $\{a^nb^n\;|\; n\geqslant 0\}$ 都是不正则的。

证明不正则的一个充分条件（逆否，正则的必要条件）是泵定理(Pumping Theorem)：

!!! Abstract "Pumping Theorem"
    对正则语言 $L$，$\exists\; n\geqslant 1\text{ s.t. } \forall w\in L, |w|\geqslant n$，$w$ 可以重写作 $w=xyz$，满足
    
    - $y\neq e$
    - $|xy|\leqslant n$
    - $\forall i\geqslant 0$, $xy^iz\in L$

??? general "Proof"
    设 $L$ 被有 $n$ 个不同状态的 DFA $M$ 接受，考虑 $\forall w\in L$, $|w|\geqslant n$

    考虑 $M$ 的前 $n$ 步计算：

    $$
        (q_0, a_1\cdots a_n) \vdash_M
        (q_1, a_2\cdots a_n) \vdash_M \cdots \vdash_M
        (q_n, e)
    $$

    这里出现了 $n+1$ 个状态，根据鸽巢原理，必然 $\exists \; 0\leqslant i < j\leqslant n \text{ s.t. } q_i=q_j$。
    
    这样，取 $y=a_i\cdots a_j, x=a_1\cdots a_{i-1}, z=a_{j+1}\cdots a_m$ 即可。根据 $0\leqslant i < j\leqslant n$ 就可见 $y\neq e$ 且 $|xy|\leqslant n$。
    
    既然 $q_i=q_j$，那么多叠几次，甚至去掉这一段都无所谓，即 $xy^nz\in L$。

!!! question "Example"
    证明 $\{a^ib^i\;|\; i\geqslant 0\}$ 不是正则语言。

**hint**: 取 $w=a^nb^n$，则 $x, y$ 只有 $a$。

!!! question "Example"
    证明 $\{a^i\;|\; i \text{ 是质数}\}$ 不是正则语言。

**hint**: $x=a^p, y=a^q, z=a^r$, 要求 $p+nq+r$ 总是质数。然而令 $n=p+2q+r+2$ 就有 $p+nq+r=(q+1)(p+2q+r)$。这里比较自然的是取 $n=p+q+r+q$，但这样有 $p+nq+r=(q+1)(p+q+r)$，$q+1\geqslant 2$，但是 $p+q+r\geqslant 1$ 还不够，所以需要多凑一点。

!!! question "Example"
    证明 $\{w\in\{a, b\}^*\;|\; w \text{ 中 }a\text{ 和 }b\text{ 数量相同}\}$ 不是正则语言。

**hint**: $L\cap a^*b^*$

!!! question "Examples"
    辨析：以下的语言是正则的吗？

    - 有限语言
    - 有限个正则语言的并
    - 可数无限个正则语言的并
    - 可数无限个正则语言的交
    - $\{x: \; x\in L_1, x\notin L_2\}$, $L_1, L_2$ regular
    - 正则语言的子集

??? general "Answer"
    - True
    - True
    - False，考虑 $\{a^nb^n\;|\;n\geqslant 0\}$
    - False，考虑

    $$
        \bigcap L_i \text{ regular }\Rightarrow \bigcup \overline{L_i} = \overline{\bigcap L_i} \text{ regular }
    $$

    然后令 $L_i=\{a, b\}^*-\{a^ib^i\}$

    - True, $L_1-L_2=L_1\cap \overline{L_2}$
    - False, $L\subseteq \Sigma^*$

## State Minimization

尽量减少 DFA 的状态数。对 $\forall$ 正则语言，都有唯一的 “标准” DFA，拥有最少的状态数。

整体分两步：1. 除去不可达状态 2. 合并等价状态

### Equivalent Class with String

考虑输入串的两种等价关系：相对语言等价 $\approx_L$ 和相对机器等价 $\sim_M$

!!! info "相对语言等价 $\approx_L$"
    $L\subseteq \Sigma^*, x, y\in \Sigma^*$，则定义 $x, y$ 相对 $L$ 等价为

    $$
        x\approx_L y\iff \forall z\in\Sigma^*, (xz\in L\iff yz\in L)
    $$

!!! tip "Remark"
    $x\approx_L y$: $x,y$ 本身要么同属于 $L$，要么同不属于；在 $x,y$ 后面加上相同的 $z$，然后也同属于/不属于 $L$

!!! question "Example"
    用 $[x]$ 写出 $L=(ab\cup ba)^*$ 的等价类

**hint**: $[e]=L, [a]=La, [b]=Lb$ 都是可能被接受的等价类。$[aa]=L(aa\cup bb)\Sigma^*$ 是不可能被接受的等价类，所以写成 $[aa]$ 还是 $[bb]$ 都无所谓。

!!! info "相对机器等价 $\sim_M$"
    DFA $M=(K, \Sigma, \delta, s, F)$，则定义 $x, y$ 相对 $M$ 等价为

    $$
        x\sim_M y\iff \exists\; q\in K \text{ s.t. } 
        ((s, x)\vdash_M^*(q, e)) \wedge
        ((s, y)\vdash_M^*(q, e))
    $$

两种等价的关联：$x\sim_M y\Rightarrow x\approx_{L(M)}y$

??? general "Proof"
    $\forall x\in \Sigma^*$，设 $q(x)$ 为 $s$ 输入 $x$ 后到达的状态 ($(s, x)\vdash_M^*(q(x), e)$)。

    $\forall x, z\in \Sigma^*$ 有

    $$
        xz\in L(M)\iff \exists\; f\in F, (q(x), z)\vdash_M^* (f, e)
    $$

    $x\sim_M y$ 说明 $q(x)=q(y)$，从而利用上式通过 $M$ 可以把 $xz\in L(M)$ 和 $yz\in L(M)$ 等价起来。

!!! tip "Remark"
    这说明 $\sim_M$ 是 $\approx_{L(M)}$ 的一种**细化** (refinement)。

!!! info "Definition"
    定义 $\sim$ 是 $\approx$ 的细化 (refinement)，当以下式子满足时：

    $$
        \forall x, y,\quad x\sim y\Rightarrow x\approx y
    $$

!!! tip "Remark"
    综上可以见得，DFA 的状态数的下界就是 $L(M)$ 的等价类数量。

### Reach the Lower Bound

上一小节所说的 DFA 状态数下界是可以达到的，只需要通过 $\approx_L$ 构造 DFA $M=(K, \Sigma, \delta, s, F)$:

$$
    \begin{aligned}
        K &= \{[x]:\; x\in \Sigma^*\}\\
        s &= [e]\\
        F &= \{[x]:\; x\in L\}\\
        \delta([x], a) &= [xa],\quad \forall [x]\in K, a\in \Sigma
    \end{aligned}
$$

证明这样构造的DFA是符合DFA定义的，需要以下三点：

- $K$ 有限
- $\delta([x], a)$ 是函数
- $L=L(M)$

??? general "Proof"
    
    - $L$ 正则 $\Rightarrow$ $L$ 被某个 DFA $M'$ 接受
    
    根据细化的关系，可知 $M$ 状态数 = $\approx_L$ 等价类数 $\leqslant\sim_{M'}$ 等价类数 = $M'$ 状态数

    $M'$ 是 DFA，那么其状态数有限，所以 $K$ 有限。

    - 考虑 $x_1, x_2\text{ s.t. } [x_1]=[x_2]=[x]$，由于 $x_1\approx_L x_2\iff x_1a\approx x_2a$，可知 $\delta([x_1], a)=[x_1a]=[x_2a]=\delta([x_2], a)$，因此良定义
    - 由于 $\delta([x], y)\vdash_M^*([xy], e)$，有
    
    $$
        \begin{aligned}
            x\in L(M)
            &\iff ([e], x)\vdash_M^* (f, e), f\in F\\
            &\iff f=[ex]=[x]\in F\\
            &\iff x\in L
        \end{aligned}
    $$
    

!!! Abstract "The Myhill-Nerode theorem"
    $L$ 正则 $\iff$ $\approx_L$ 等价类数量有限

??? general "Proof"
    $\Rightarrow$: 同理找出接受 $L$ 的 $M'$，用 $M'$ 的状态数限制
    
    $\Leftarrow$: 按前面的方法构造 DFA 即可

应用：对$\{a^nb^n\;|\; n\geqslant 0\}$，可以发现 $[a^i]$ 和 $[a^j](i\neq j)$ 必然是不同的等价类，所以有无限多等价类，所以不正则。

最后就是 Minimization algorithm。需要定义一个 $\equiv$:

!!! info "$\equiv$"
    $p\equiv q\iff\forall z\in \Sigma^*$,

    $$
        \delta(p, z)\in F \iff
        \delta(q, z)\in F
    $$

    $p\equiv_n q\iff$上式中有限制$|z|\leqslant n$ 

串长从 0 扩充到 $n$，直到没有变化。

- $\equiv_0$ 就是划分为 $F$ 和$K-F$
- $p\equiv_n q$, 要求 $p\equiv_n q$，且 $\forall a\in \Sigma, \delta(q, a)\equiv_n\delta(p, a)$

## Algorithms for Finite Automata

### NFA $\to$ DFA Algorithm and Analysis

NFA $M=(K, \Sigma, \Delta, s, F)$，复杂度主要来自于 DFA $M'=(K', \Sigma, \delta, s', F')$ 中 $\delta$ 的计算。

- 计算所有 $E(q)$。先得到一步 $e$ 转移可以完成的状态转移矩阵，然后使用 Warshall 等闭包算法计算自反传递闭包，就可以得到所有 $E(q)$。复杂度 $O(|K|^3)$
- 计算所有 $\delta(Q, a)$。给定 $Q$ 和 $a$，回顾证明 DFA/NFA 等价性中的 (1) 式：

$$
    \delta(Q, a)=\bigcup \left\{ E(p) \;|\; p\in K\text{, and }\exists \; q\in Q \text{ s.t. } (q, a, p)\in\Delta \right\}
$$

可知可以遍历 $Q$ 中的 $q$，然后对每个给定的 $q, a$ 遍历 $\Delta$ 找到所有合法的 $p$，然后把这些 $E(p)$都并起来。遍历 $q$ 需要 $|Q|\leqslant |K|$，遍历 $\Delta$ 需要 $|\Delta|$，而需要并的 $E(p)$ 数量受到 $p\in K$ 的限制(也就是至多 $|K|$ 的操作数)。

因此给定 $Q, a$，需要的求并操作数为 $|\Delta||K|^2$。

$Q\in 2^K$，则遍历 $Q$ 需要 $2^{|K|}$；$a\in\Sigma$，遍历 $a$ 需要 $\Sigma$。这样总共的求并操作数为 $O(2^{|K|}|\Sigma||\Delta||K|^2)$。

- 求并复杂度不会超过 $O(|K|^3)$(甚至如果编码合适，只需要 $O(|K|)$)，然后考虑到还有预计算的 $O(|K|^3)$，因此简单地把整体的复杂度处理为 $O(2^{|K|}|K|^3|\Sigma||\Delta||K|^2)$

可以见得是指数时间的。

### Other Algorithms

!!! question "Problems with Complexity"
    - NFA$\to$等价DFA，复杂度为$O(2^{|K|}|K|^3|\Sigma||\Delta||K|^2)$。（多项式时间）
    - 正则表达式$\to$等价NFA，转移数$|\Delta|$至多为$4|R|^2$。（多项式时间）
    - NFA$\to$正则表达式，正则表达式长度可能达到$3^{|K|}$。（指数时间）
    - 状态最小化算法$O(|\Sigma||K|^3)$。（多项式时间）
    - 2个DFA等价性判断——多项式时间。
    - 2个NFA等价性判断——指数时间。
    - 判断字符串$w$是否在DFA中，需要$O(|w|)$
    - 判断字符串$w$是否在NFA中，需要$O(|K|^2|w|)$

??? general "Proof"
    - 略
    - 数学归纳可以证明长度为 $|R|$ 的正则表达式 $R$ 生成的等价 NFA 的状态不多于 $2|R|$ 个（基本的 2 状态；连接不加状态；并/Kleene Star 都只加 1 状态，但是本身也占 1 长度）。所以转移 $|\Delta|\leqslant 4|R|^2$
    - 尽管在计算 $R(i, j, k)$ 的闭包算法中，只计算了 $|K|^3$ 次的级数，但是生成的正则表达式长度在指数增长。关于 $k$ 的每一次迭代中，从证明正则语言和 FA 的统一中的 (3) 式可以看到关于 $k-1$ 的更新部分由三段拼接，则 worst case 长度可能乘 3，最后导致正则表达式长度达到 $3^{|K|}$
    - 状态最小化算法最多 $|K|-1$ 次迭代，每次迭代中，对每个状态 ($|K|$) 需要考虑每种可能的输入字符 ($O(\Sigma)$)，然后查找哪个状态会被达到 ($|K|$)。因此最后整体复杂度为 $O(|\Sigma||K|^2)$
    - 使用状态最小化算法解决
    - 先 NFA 转 DFA，再状态最小化
    - DFA 走一遍就行了
    - 维护一个状态集，初始化为 $E(s)$，对 $w$ 每个输入都让这个状态集中的每个状态 $(O(|K|))$ 都走一步并生成 $E(p)$（类似 $\delta(Q, a)$ 的算法）
