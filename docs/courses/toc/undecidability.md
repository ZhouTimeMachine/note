<link rel="stylesheet" href="../../../css/counter.css" />

# Undecidability

!!! info "Part of note taken on ZJU *Introductiion to Theoretical Computer Science*, 2022 Fall & Winter"

## The Church-Turing Thesis

**Church-Turing 论题**: 可计算就是图灵可计算。

!!! tip "Remark"
    - 这只是一个论题，不是被证明的定理
    - 可计算要给出保证能停机的算法，因此指的是递归而不是递归可枚举
    - 根据该论题，可判定就是递归，不可判定就是不递归

## Universal Turing Machines

为了能够实现图灵机，关键是对图灵机进行通用的编码。

- 编码操作（写/左移/右移）：即考虑 $\Sigma\cup \{\leftarrow, \rightarrow\}$，$a$ 前导标识，使用最小的位数编码，即
    
$$
    j=\min\{j\;|\; j\in N, 2^j\geqslant |\Sigma|+2\}
$$

对于每个图灵机必须有的四个符号，强制编码为：$\sqcup=0^j, \triangleright=0^{j-1}1, \leftarrow=0^{j-2}10, \rightarrow=0^{j-2}11$。

- 编码状态：同样也选取最小的位数编码，共 $|K|$ 个状态。用 $q$ 前导标识。
- 编码图灵机：即编码状态转移列表，以 $\delta(s, \sqcup)$ 作为开始。注意并不把 $H$ 加入编码，因为状态转移列表已经隐含了停机状态的信息。在判定语言问题中，规定字典序较小的停机状态为 $y$，另一者为 $n$。

 
完成以上编码后，通用图灵机 (Universal Turing Machine, UTM) 的 alphabet 就固定了，为

$$
    \Sigma=\{q, a, 0, 1, ,, (, )\}
$$


中间连着三个“,”不是写错了，因为逗号也在 alphabet 中。这样，每次使用通用图灵机 $U$ 都输入“$M$”和“$w$”，计算相当于

$$
    U("M""w")="M(w)"
$$


$U$ 可以设计为一个 3-tape TM，如下：
<div style="text-align:center;">
    <img src="../../imgs/toc/5.1.png" alt="5.1" style="zoom:50%;" />
</div>

可以看到，带1输入 “$M$” 和 “$w$” ，然后拷贝 “$M$” 到带2，带1的 “$w$” 左移以形成 STM 的标准起始格局。带3写上起始状态 “$s$”。模拟时，查询带2获得状态转移列表，在带1上模拟TM执行，在带3上实时更新状态。直到带3进入停机状态，整个模拟结束。

## The Halting Problem

- $\operatorname{halts}(P, X)$: 如果对输入 $X$，程序 $P$ 停机，输出“yes”，反之输出“no”
- $\operatorname{diagonal}(X)$: $\operatorname{halts}(X, X)$ 则不停机，反之停机

假设 $\operatorname{diagonal}$ 可计算，那么计算其的图灵机也可以进行编码。

- 那么考虑 $\operatorname{diagonal}(\operatorname{diagonal})$，它停机当且仅当 $\operatorname{halts}(\operatorname{diagonal}, \operatorname{diagonal})$ 输出“no”
- 根据 $\operatorname{halts}$ 的定义，等价于 $\operatorname{diagonal}(\operatorname{diagonal})$ 不停机
- 这里产生矛盾，因此 $\operatorname{diagonal}$ 不可计算。

!!! abstract "Theorem"
    考虑语言
    
    $$
        H=\{"M""w":\; \text{TM }M\text{ 对输入}"w"\text{停机}\text\}
    $$

    可知 $H$ 不递归。因此递归语言类是递归可枚举类的真子集。

!!! tip "Remark"
    $H$ 是停机问题的正式表述。由于通用图灵机半判定 $H$，所以 $H$ 是递归可枚举的。

??? general "Proof"
    令
    
    $$
        H_1=\{"M":\; \text{TM }M\text{ 对输入}"M"\text{停机}\text\}
    $$

    证明思路为
    
    - $H$ 递归 $\Rightarrow$ $H_1$ 递归
    - $H_1$ 递归 $\Rightarrow$ $\overline{H_1}$ 递归
    - $\overline{H_1}$ 甚至不 r.e.

    前两步很自然，第三步的矛盾和前面的矛盾是类似的。假设 $\overline{H_1}$ r.e.，那么存在 $M^*$ 半判定 $\overline{H_1}$。那么是否有"$M^*$"$\in\overline{H_1}$呢？
    
    $$
        \begin{aligned}
            "M^*"\in \overline{H_1} 
            & \iff "M^*"\notin H_1\\
            & \iff M^*\text{ 对 }"M^*"\text{ 不停机}\\
            & \iff "M^*"\notin \overline{H_1} 
        \end{aligned}
    $$

    第二行等价来自于 $H_1$ 的定义，第三行等价是根据半判定。

需要注意的是，$H$ 相当于递归可枚举语言中的一个“完全”问题。如果 $H$ 递归，那么递归可枚举=递归。

这是因为假设 $M_0$ 判定 $H$，那么另外任意某个 TM $M$ 半判定语言 $L(M)$，那我们可以设计另外一个 TM $M'$ 判定 $L(M)$。即向通用图灵机输入"$M$""$w$"，然后模拟 $M_0$ 的运行。则通用图灵机运行的就是"$M$""$w$"是否属于 $M_0$ 的问题，虽然 $M$ 对 $w$ 不停机，但这个停机问题的解决只是停机并输出 $n$ 而已，也就判定了。

由于证明了 $H$ 不是递归、但依然是递归可枚举，就证明了递归语言是递归可枚举语言的真子集。

!!! abstract "Theorem"
    递归可枚举语言在补运算下不封闭，如 $H_1$ 递归可枚举，但 $\overline{H_1}$ 不递归可枚举。

!!! tip "Remark"
    后续会说到，如果封闭就说明递归。

## Undecidable Problems about TM

通过规约可以从停机问题出发得到更多不可判定问题。

!!! info "规约 (reduction)"
    $L_1, L_2\subseteq \Sigma^*$，从 $L_1$ 到 $L_2$ 的**规约 (reduction)** 被定义为一个**递归函数** $\tau$: $\Sigma^*\to \Sigma^*$，满足
    
    $$
        x\in L_1\iff \tau(x)\in L_2
    $$


!!! abstract "Theorem"
    存在 $L_1$ 到 $L_2$ 的规约，则若 $L_2$ 递归，$L_1$ 也递归；若 $L_1$ 不递归，则 $L_2$ 也不递归。（把递归看作“解决”，可以认为 $L_1$ 的解决依赖于 $L_2$）

??? general "Proof"
    往证 $L_1$ 不递归 $\Rightarrow L_2$ 不递归。
    
    假设 $L_2$ 递归，则存在 TM $M_2$ 判定之。存在规约 $\tau$，设 TM $T$ 计算该规约，则 TM $TM_2$ 可以判定 $L_1$，与 $L_1$ 不可判定矛盾。

!!! abstract "Theorem"
    以下问题都不可判定。
    
    - 给定TM $M$、输入 $w$，$M$ 在 $w$ 上停机吗？
    - 给定TM $M$，$M$ 空带上停机吗？
    - 给定TM $M$，存在输入让 $M$ 停机吗？
    - 给定TM $M$，$M$ 对每种输入都停机吗？
    - 给定TM $M_1, M_2$，它们在相同输入上停机吗？
    - 给定TM $M$，$M$ 半判定的语言是否正则？是否上下文无关？是否递归？
    
    除此之外，存在某台固定机器 $M_0$，对它来说下列问题不可判定：给定 $w$，$M_0$ 是否在 $w$ 上停机？

??? general "Proof"
    
    - 即停机问题
    - 吾有一机，名曰 $M_w$。输入为空，而行之始必写 $w$ 于带，遂仿 $M$ 之行。得之
        
        $$
            Ra_1Ra_2R\cdots Ra_n L_{\sqcup} M
        $$


        向能判定 $L=\{"M":\; M\text{ 对 }e\text{ 停机}\}$ 的 TM 输入 $M_w$，从而就能判断 $M$ 输入 $w$ 能否停机了。这里就建立了一个 $\tau:\; "M""w"\to M_w$ 的规约，以上用图灵机构造出了 $M_w$，从而证明了这个规约是递归的。
    - 从(2)向此规约。吾有一机，名曰 $M'$。输入任意，而行之始擦输入，遂仿 $M$ 之行。
        
        $M'$ 对一些输入停机，就是 $M'$ 对所有输入停机，也就是 $M$ 对 $e$ 停机。
    - 同(3)
    - 从(4)向此规约。吾有一机，名曰 $y$，接受任意。这其实可以看出一个常数，那么构造规约
        
        $$
            \tau("M")="M""y"
        $$

        因为 $y$ 接受所有输入，那么如果解决了(5)，那么 $M$ 和 $y$ 在相同输入停机 $\iff$ $M$ 接受所有输入，也就解决了(4)，即完成了(4)到(5)的规约。
    - 从(2)向此规约。构造 $M'$，先模拟运行输入 $e$ 的 $M$，停机之后再继续判定任意 $w'$ 是否属于 $H$。$M$ 对 $e$ 不停机，则 $M'$ 也不停机，其半判定空语言（正则、上下文无关、递归）；$M$ 对 $e$ 停机，则 $M'$ 半判定 $H$，它不正则、不上下文无关、不递归。
    - 就是通用图灵机 $U$
    

## Properties of Recursive Languages

!!! abstract "Theorem"
    $L\:$ 递归 $\iff$ $L$ 和 $\overline{L}$ 都 r.e.

??? general "Proof"
    
    - $L$ 递归 $\Rightarrow$ $L$ r.e.
    - $L$ 递归 $\Rightarrow$ $\overline{L}$ 递归 $\Rightarrow$ $\overline{L}$ r.e.
    - $L, \overline{L}$ 都 r.e. $\Rightarrow$ $L$ 可判定
    

    前两点已经证明，只需要证明比较难的第三点。第三点只需要让 $\forall w\in L$，把 $w$ 输入给半判定 $L$ 和 $\overline{L}$ 的两台 TM。无论 $w\in L$ 还是 $w\notin L$，都总有一台会停机，那就完成了判定。

!!! info "枚举 (enumerate)"
    TM $M$ **枚举 (enumerate)** $L$，当且仅当存在一个固定的状态 $q$ 满足
    
    $$
        L=\{w: (s, \triangleright) \vdash_M^* (q, \triangleright\underline{\sqcup}w)\}
    $$

    称语言**图灵可枚举 (Turing-enumerable)** 当且仅当存在图灵机枚举它。

!!! abstract "Theorem"
    $L$ 递归可枚举 $\iff$ $L$ 图灵可枚举

??? general "Proof"
    $\Rightarrow$: $M$ 半判定 $L$，寻找 $M'$ 以枚举 $L$。字典序地输入所有字符串，考虑前 $n$ 个串，就对每个串执行 $n$ 步。$M'$ 本身没有输入，只是模拟 $M$ 运行，$M$ 的接受状态就是枚举的展示状态。

    $\Leftarrow$: $M$ 枚举 $L$，修改 $M$ 以半判定 $L$。开始枚举前，$M$ 保存输入给它的字符串。枚举过程中，每一次进入特殊状态 $q$，就把生成的串和保存的输入比对，如果输入属于语言，那么在枚举过程中总会比对匹配最后停机。

!!! info "字典序枚举 (lexicographically enumerate)"
    枚举过程中，如果第 $n$ 次进入展示状态 $q$ 的字符串 $w_n$ 字典序在 $w_{n-1}$ 之后，则称 TM $M$ **字典序枚举 (lexicographically enumerate)** $L$，同理有**字典序图灵可枚举 (lexicographically Turing-enumerable)** 的概念。

!!! abstract "Theorem"
    $L$ 递归 $\iff$ $L$ 字典序图灵可枚举

??? general "Proof"
    $\Rightarrow$: 和前面不同的是，这里因为判定，所以一个个按字典序喂输入就行了。

    $\Leftarrow$: 枚举测试的时候，当 $L$ 枚举完或字典序在 $w$ 之后的字符串出现的时候就可终止。

!!! abstract "Rice Theorem"
    设 $\mathscr{C}$ 是所有递归可枚举语言组成的类的非空真子集，那么下列问题不可判定：给定 TM $M$，是否 $L(M)\in \mathscr{C}$？

??? general "Proof"
    已经排除了 $\mathscr{C}$ 为空或者为全集的情况，因为这样的话就直接能判定了。

    证明方法略，大概就是很无耻地先运行 $M_e$ 再运行本职。