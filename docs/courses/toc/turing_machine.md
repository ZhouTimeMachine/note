<link rel="stylesheet" href="../../../css/counter.css" />

# Turing Machine

!!! info "Part of note taken on ZJU *Introductiion to Theoretical Computer Science*, 2022 Fall & Winter"

## The Definition of a Turing Machine

- 图灵机：
    - 头可读写，双向移动
    - 带无限长，带上默认字符为空格 ($\sqcup$)
- 实际计算过程中，带上只有有限的空格被读取

### Turing Machine and its Configuration

!!! info "图灵机 (Turing Machine, TM)"
    图灵机即 quintuple $(K, \Sigma, \delta, s, H)$，有所特别的唯 $\Sigma, \delta, H$：
    
    - $\Sigma$: 要求 $\{\sqcup,\triangleright\}\subseteq \Sigma$; $\leftarrow, \rightarrow\notin \Sigma$
    - $H$: 停机状态集合 (halting states)，不同于先前的 $F$ 被称为末态，到达末态之后也可以再转移，到达停机状态之后就不能再转移了（可以从下面 $\delta$ 的定义看出）
    - $\delta$: 转移**函数**，要求 $\forall \delta(q, a)=(p, b)$，$(K-H)\times \Sigma\to K\times(\Sigma\cup \{\leftarrow, \rightarrow\})$
        - $b\neq \triangleright$，即不可写左端标记
        - $a=\triangleright$ 时，$b=\to$。即读到左端标记则右移。

!!! info "格局 (configuration)"
    图灵机 $M=(K, \Sigma, \delta, s, H)$ 的格局 $\in K\times \triangleright\Sigma^*\times(\Sigma^*(\Sigma-\{\sqcup\})\cup \left\{ e \right\})$

    - 首先状态肯定是必要的
    - 然后是两段字符串，是读写头左右侧的字符串
        - 左侧边缘为左端标记 $\triangleright$（左侧字符串包括当前字符）
        - 右侧边缘为最右侧的非 $\sqcup$ 字符，或者如果右侧没有非 $\sqcup$ 字符则取 $e$

!!! tip "Remark"
    特别地，格局中状态 $\in H$ 时该格局称为停机格局 (halted configuration)。

格局符号也存在简写：

$$
    (q, wa, u)\Rightarrow (q, w\underline{a}u)
$$


### Turing Machines Computation and Notation

图灵机 $M=(K, \Sigma, \delta, s, H)$，考虑格局的单步变换：

$$
    (q_1, w_1\underline{a_1}u_1)\vdash_M 
    (q_2, w_2\underline{a_2}u_2)
$$


需要 $\:b\in \Sigma\cup \{\leftarrow, \rightarrow\}$, $\delta(q_1, a_1)=(q_2, b)$，包括以下情况：

- $b\in \Sigma$: 写操作，头不动，$w_1=w_2$, $a_2=b$
- $b=\leftarrow$: 左移操作，$w_1=w_2a_2$
    - $a_1= \sqcup, u_1=e$: $u_2=e$
    - otherwise: $u_2=a_1u_1$
- $b=\rightarrow$: 右移，同理分析。
    

!!! tip "Remark"
    除了 $\vdash_M$ 的自反传递闭包 $\vdash_M^*$ 之外，还有 $n$ 步计算/长度为 $n$ 的计算 $\vdash_M^n$。

根据图灵机的基本计算操作类型，定义图灵机的基本图灵机 (basic machines)

!!! info "基本图灵机 (basic machines)"

    $$
        M_a=(\{s, h\}, \Sigma, \delta, s, \{h\})
    $$


    其中 $\delta$ 定义为

    $$
        \delta(s, \triangleright)=(s, \rightarrow),\quad
        \delta(s, b)=(h, a), \forall b\in\Sigma-\{\triangleright\}
    $$

    - Symbol-writing Machines: $M_a$，简写作 $a$ ($a\notin \{\leftarrow, \rightarrow\}$)
    - Hand-moving Machines: $M_{\leftarrow}$，简写作 $L$；$M_{\rightarrow}$，简写作 $R$


根据基本图灵机可以组合得到复杂图灵机。中间的基本图灵机把停机状态改成普通状态，然后根据基本图灵机之间的关系在原停机状态和指向的图灵机初态之间建立转移。


- $R^2$: 右移两格
- $R_{\sqcup}$: 移到右侧第一个空格$\sqcup$
- $R_{\overline{\sqcup}}$: 移到右侧第一个非空格字符
- 同理$L_{\sqcup}, L_{\overline{\sqcup}}$


\automata[->,>={Stealth[round]},auto,node distance=4em,on grid,semithick,inner sep=2pt,bend angle=50,initial text=,every state/.style={draw=none,minimum size=0pt,inner sep=1pt}]
        \node[initial,state]           (q0) {$R$};
        \node[initial,state] at (3, 0) (q1) {$R$};
        \node[initial,state] at (6, 0) (q2) {$L$};
        \node[initial,state] at (9, 0) (q3) {$L$};
        
        \path
            (q0) edge [loop right] node {$\sqcup$} ()
            (q1) edge [loop right] node {$\overline{\sqcup}$} ()
            (q2) edge [loop right] node {$\sqcup$} ()
            (q3) edge [loop right] node {$\overline{\sqcup}$} ();

上图中，从左到右分别为 $R_{\sqcup}, R_{\overline{\sqcup}}, L_{\sqcup}, L_{\overline{\sqcup}}$。注意，第一步的右移/左移是必然发生的，也就是至少移动一步。

!!! example "拷贝机 The Copying Machine"
    从 $\underline{\sqcup} w\sqcup$ 得到 $\sqcup w\sqcup w \underline{\sqcup}$ (要求 $w$ 中无 $\sqcup$)

    \automata[->,>={Stealth[round]},auto,node distance=4em,on grid,semithick,inner sep=2pt,bend angle=50,initial text=,every state/.style={draw=none,minimum size=0pt,inner sep=1pt}]
        \node[initial,state]     (q_0)  {$R$};
        \node[state] at (3, 0)   (q_1)  {$\underbrace{\sqcup}_{mark} R^2_{\sqcup}aL^2_{\sqcup}\underbrace{a}_{restore}$};
        \node[state] at (0, -1)  (q_2)  {$R_{\sqcup}$};
        
        \path
            (q_0) edge node {$a\neq\sqcup$} (q_1)
                  edge node {$\sqcup$} (q_2)
            (q_1) edge [bend right] node {} (q_0);


!!! example "左移机 The Left-shifting Machine"
    The Left-shifting Machine $S_{\leftarrow}$，从 $\sqcup w\underline{\sqcup}$ 得到 $w \underline{\sqcup}$ (要求 $w$ 中无 $\sqcup$)
    
    \automata[->,>={Stealth[round]},auto,node distance=4em,on grid,semithick,inner sep=2pt,bend angle=50,initial text=,every state/.style={draw=none,minimum size=0pt,inner sep=1pt}]
        \node[initial,state]    (q_0)                   {$L_{\sqcup}$};
        \node[state]      at (1, 0)      (q_1)    {$R$};
        \node[state]      at (3, 0)      (q_2)     {$\sqcup LaR$};
        \node[state]      at (1, -1)      (q_3)     {$L$};
        
        \path
            (q_0) edge node {} (q_1)
            (q_1) edge node {$a\neq\sqcup$} (q_2)
                  edge node {$\sqcup$} (q_3)
            (q_2) edge [bend right] node {} (q_1);

!!! question "画出擦除右侧第一段连续的 $a$ 的图灵机"
    
??? general "Answer"
    \automata[->,>={Stealth[round]},auto,node distance=4em,on grid,semithick,inner sep=2pt,bend angle=50,initial text=,every state/.style={draw=none,minimum size=0pt,inner sep=1pt}]
        \node[initial,state]     (q_0)  {$R$};
        \node[state] at (2, 0)   (q_1)  {$\sqcup$};
        
        \path
            (q_0) edge node {$a$} (q_1)
            (q_1) edge [bend right] node {} (q_0);


## Computing with Turing Machines

为方便，定义 $\Sigma_0=\Sigma-\{\sqcup, \triangleright\}$。

### Deciding Languages

图灵机可用于判定是否有 $w\in L$。

- 给定 TM $M=(K, \Sigma, \delta, s, H)$，$w\in \Sigma_0^*$
- 为判定 $w\in L$，需要有初始格局 $(s, \triangleright\underline{\sqcup}w)$
- 当然，要求 $w$ 中没有 $\sqcup$

令 $H=\{y, n\}$，然后根据格局中状态为 $y, n$ 分别定义**接受格局** (accepeting configuration) 和**拒绝格局** (rejecting configuration)；根据初始格局运行后得到接受/拒绝格局判断 $M$ **接受/拒绝** $w$。

!!! info "TM 判定 (decide) 语言"
    $M$ **判定 (decide)** $L\subseteq \Sigma_0^*$ 当且仅当 $\forall w\in \Sigma_0^*$ 有

    - $w\in L\iff L$接受$w$
    - $w\notin L\iff L$拒绝$w$

当存在 TM 判定 $L$ 时，称 $L$ 是**递归 (recursive)** 的。**递归、可判定、可计算是一致的概念。**

!!! question "Example"
    写出判定 $L=\{a^nb^nc^n:\; n\geqslant 0\}$ 的 TM，或者说证明 $L$ 是递归的

!!! tip "提示"
    考虑

    $$
    \triangleright \sqcup a a \cdots b b \cdots c c \cdots \sqcup
    $$

    思路：每次从左到右依次删去一组 $a, b, c$，然后分别改为 $x, y, z$ 作为删除的标记。注意 $\sqcup$ 表示字符串的结束。

??? general "Answer"
    \automata[->,>={Stealth[round]},auto,node distance=5em,on grid,semithick,inner sep=2pt,bend angle=50,initial text=,every state/.style={draw=none,minimum size=0pt,inner sep=1pt}]
        \node[initial,state]    (q_0)                   {$R$};
        \node[state]            (q_1) [right=of q_0]    {$xR$};
        \node[state]            (q_2) [right=of q_1]    {$yR$};
        \node[state]            (q_3) [right=of q_2]    {$zL_{\sqcup}$};
        \node[state]            (q_4) [below=of q_0]    {$y$};
        \node[state]            (q_5) [right=of q_4]    {$n$};
        
        \path
            (q_0)   edge                    node                {$a$}               (q_1)
                    edge                    node [swap]         {$\sqcup$}          (q_4)
                    edge [bend right=30]    node [font=\small]  {$b,c,y,z$}         (q_5)
                    edge [loop above]       node                {$x$}               (q_0)
            (q_1)   edge                    node                {$b$}               (q_2)
                    edge                    node                {$c,\sqcup,x,z$}    (q_5)
                    edge [loop above]       node                {$a,y$}             (q_1)
            (q_2)   edge                    node                {$c$}               (q_3)
                    edge [bend left=30]     node [font=\small]  {$\sqcup,a,x,y$}    (q_5)
                    edge [loop above]       node                {$b,z$}             (q_2)
            (q_3)   edge [bend right]       node                {}                  (q_0);


### Computing Functions

给定 TM $M=(K, \Sigma, \delta, s, H)$，$w\in \Sigma_0^*$。

设 $M$ 对输入 $w$ 停机，输出为 $y\in \Sigma_0^*$，即有

$$
    (s, \triangleright\underline{\sqcup}w)
    \vdash_M^*
    (h, \triangleright\underline{\sqcup}y)
$$


这样，$y$ 就可以表示为 $M$ 对输入 $w$ 的输出 $M(w)$。

!!! info "$M$ compute $f$"
    - $f:\; \Sigma_0^*\to \Sigma_0^*$，则 $M$ **计算** $f$ 当且仅当
        
    $$
        \forall w\in \Sigma_0^*,\quad M(w)=f(w)
    $$

    - $f:\; \N^k\to \N$，则 $M$ **计算** $f$ 当且仅当 $\forall w_1,\cdots,w_k\in 0\cup 1\{0, 1\}^*$
        
    $$
        \operatorname{num}(M(w_1;\cdots;w_k))=f(\operatorname{num}(w_1),\cdots, \operatorname{num}(w_k))
    $$

    $\operatorname{num}$是将二进制串转换为十进制数的函数。
    
    可计算 $\iff$ 递归，存在 TM $M$ 计算 $f$ 时称 $f$ **递归**。

!!! example "Example"
    $\kappa:\; \Sigma^*\to\Sigma^*,\kappa(w)=ww$，则 $\kappa$ 被 $CS_{\leftarrow}$ 计算，即拷贝+左移。

!!! question "Example"
    设计图灵机计算后继函数 (successor function): $\operatorname{suc}(n)=n+1$

??? general "Answer"
    $$
        \triangleright \underline{\sqcup} n \sqcup 
        \quad \to \quad
        \triangleright \underline{\sqcup} (n+1) \sqcup
    $$

    \automata[->,>={Stealth[round]},auto,node distance=4em,on grid,semithick,inner sep=2pt,bend angle=50,initial text=,every state/.style={draw=none,minimum size=0pt,inner sep=1pt}]
            \node[initial,state]     (q_0)  {$R_{\sqcup}L$};
            \node[state] at (2, 1.5)   (q_1)  {$0$};
            \node[state] at (2, 0)   (q_2)  {$1L_{\sqcup}$};
            \node[state] at (2, -1.5)  (q_3)  {$1S_R$};
            
            \path
                (q_0) edge node {$1$} (q_1)
                      edge node {$0$} (q_2)
                      edge node {$\sqcup$} (q_3)
                (q_1) edge [bend right] node {} (q_0);

### Semideciding and Properties

给定 TM $M=(K, \Sigma, \delta, s, H)$，$H$ 不一定就是 $\{y, n\}$ 了。

!!! info "TM 半判定 (semidecide) 语言"
    若 $\forall w\in \Sigma_0^*$，
    
    $$
        w\in L\iff M\text{ 在输入 }w\text{ 上停机}
    $$

    则称 $M$ **半判定 (semidecide)** $L$。
    
    存在 TM 半判定 $L$ 时，称 $L$ 是**递归可枚举 (recursive enumerable, r.e.)** 的。

!!! tip "Remark"
    半判定（递归可枚举）情形下，TM 只能判定 $w\in L$ 情况（能停机），而 $w\notin L$ 情况通过不停机逃避了回答。
    
    现在给不停机一个符号表示：
    
    $$
        M(w)=\uparrow\iff M\text{ 对输入 }w\text{ 不停机}
    $$

    即
    
    $$
        M(w)=\uparrow\iff w\notin L
    $$


!!! example "Example"
    对 $L=\{w\in\{a, b\}^*:\; w\text{ 含有至少 1 个 }a\}$，可以设计图灵机遇到非 $a$ 字符永远右移，遇到 $a$ 停机，这样就半判定了。
    
    设计永远向右寻找空格的图灵机，以及永远循环的图灵机（如卡在左端标记和右移的a之间的图灵机），都可以让图灵机永不停机。

对于正则语言、上下文无关语言，都已经考虑了其封闭性质，这里也研究一下递归语言和递归可枚举的封闭性质。

!!! abstract "Theorem"
    递归语言的**交、并、补**还是递归语言。递归语言一定是递归可枚举语言。

    递归可枚举语言的**交、并**还是递归可枚举语言。

!!! tip "Remark"
    关于补的封闭，将 $y, n$ **交换**就可证明。交、并的封闭性需要后续的图灵机模拟和多带图灵机的知识。

    证明递归语言也是递归可枚举的，只需要把 $n$ 从停机状态中删去，到达原来的 $n$ 状态后让图灵机一直复写（循环）就行。

    递归可枚举语言**关于补不封闭**。如果递归可枚举语言的补语言也是递归可枚举语言，那么可以证明他们都是递归语言。

## Extensions of the Turing Machine

### $k$-tape TM

简单地拓展图灵机，考虑多带、双向无限带、多头、多维带、不确定性。事实上这些都没能真正扩展图灵机的计算能力，但是提供了 feature，对同一问题可以做出简化。后续将主要阐述多带图灵机和不确定性图灵机。

$k$ 带图灵机 ($k$-tape TM) 关键的是 $\:\delta$: $(K-H)\times \Sigma^k\to K\times(\Sigma\cup \{\leftarrow, \rightarrow\})^k$

格局也变化为$\in K\times(\triangleright \Sigma^*\times(\Sigma^*(\Sigma-\{\sqcup\})\cup \{e\}))^k$

我们规定输入和输出都在第一条带，其他带起始全空，停机时忽略带上内容。

!!! example "Example"
    拷贝机。目标：$\triangleright \underline{\sqcup}w\sqcup \to \triangleright \sqcup w\sqcup w \underline{\sqcup}$。

2-tape 拷贝机画起来会比较自然。

<div style="text-align:center;">
    <img src="../../imgs/toc/4.4.png" alt="4.4" style="zoom:50%;" />
</div>

- 1 带到 2 带同位置拷贝 $w$
- 2 带移动读写头到最左 $\sqcup$
- 2 带到 1 带错位拷贝 $w$

2-tape 拷贝机两带变化可以用下表展示：

<div class="center" markdown="1">

|            | At beginning | After (1) | After (2) | After (3) |
| :--------: |    :----:    | :---:     | :---:     | :---:     |
| **Tape-1** | $\triangleright \underline{\sqcup}w$ | $\triangleright \sqcup w\underline{\sqcup}$ | $\triangleright \sqcup w\underline{\sqcup}$ | $\triangleright \sqcup w\sqcup w\underline{\sqcup}$ |
| **Tape-2** | $\triangleright \underline{\sqcup}$ | $\triangleright \sqcup w\underline{\sqcup}$ | $\triangleright \underline{\sqcup}w$ | $\triangleright \sqcup w\underline{\sqcup}$ |

</div>

!!! example "Example"
    计算 $x+y, x, y\in 0\cup 1\{0, 1\}^*$。

选用分号分割输入的 $x, y$。2-tape $x+y\:$ 两带变化表如下。

<div class="center" markdown="1">

|            | At beginning | After (1) | After (2) |
| :--------: |    :----:    | :---:     | :---:     |
| **Tape-1** | $\triangleright \underline{\sqcup}x;y$ | $\triangleright \sqcup0\underline{0}y$ | $\underline{\triangleright} \sqcup x+y$ |
| **Tape-2** | $\triangleright \underline{\sqcup}$ | $\triangleright \sqcup x\underline{\sqcup}$ | $\triangleright \underline{\sqcup}w$ |

</div>

下图最后细节上可能不太对，但是整体思路是对的。

<div style="text-align:center;">
    <img src="../../imgs/toc/4.5.png" alt="4.5" style="zoom:50%;" />
</div>

### $k$-tape TM/Standard TM Equivalence

$k$-tape TM $M=(K, \Sigma, \delta, s, H)$, $\exists$ STM $M'=(K', \Sigma', \delta', s', H)$, $\Sigma\subseteq \Sigma'$，满足

- 对相同的输入，$M, M'$ 能到达相同的停机状态，且输出相同
- $M$ 对输入 $x$ 在 $t$ 步后停机，则 $M'$ 对 $x$ 停机前所需步数为 $O(t(|x|+t))$


把 $M'$ 的单带分割为 $2k$ 份，记录 $k$ 条带的内容和 $k$ 个读写头的位置。

$\Sigma'=\Sigma\cup (\Sigma\times\{0, 1\})^k$，左端标记和空格依然存在，中间都是 $2k$ 元组。

<div style="text-align:center;">
    <img src="../../imgs/toc/4.6.png" alt="4.6" style="zoom:50%;" />
</div>

2-tape TM $\to$ STM


- 初态：写 $\triangleright$, 然后 $(\sqcup, 1, \cdots, \sqcup, 1)$，接着 $(a, 0, \sqcup, 0, \cdots, \sqcup, 0)$，直到第 1 条带上 $a$ 到达最右侧的非 $\sqcup$，后续就写 $\sqcup$
- 模拟 $M$ 计算：每步模拟开始时带头总在右侧第一个“真正空格” $\sqcup$ 处(下称“右标记”)
    - **向左扫描全带**，获取 $k$ 带带头信息。随后**返回右标记**，通过**改变状态**反映 $k$ 带上的字符内容。
    - 根据 $M$ 的模拟结果更新 $k$ 带
- 停机格局：$2k$ 元组只取第 1 元，带头和状态与 $M$ 保持一致

$M'$ 需要的步数为 $O(t(|x|+t))$，因为

- 初始化需要 $O(|x|)$
- $M$ 上有 $2k$ 元组的部分长度，初始为 $|x|+2$，后续模拟的每步长度增加不超过 1，则 $t$ 步时长度至多为 $|x|+2+t$，因此 $M$ 的每步可以用 $M'$ 的 $O(|x|+t)$ 步模拟

简单提一提其他图灵机扩展：

- Two-way infinite tape: 从某处切开，可以被 2-tape TM 模拟
- Multiple heads: 可以用 $k$-tape TM 模拟，除了第 1 条带其他带只用来记录带头位置
- Two dimensional tape: “带”变成了无穷二维网格。有利于解决铺砖问题等，但是也可以被 STM 模拟

## Nondeterministic Turing Machines

### NTM

非确定性图灵机 (nondeterministic Turing Machine, NTM) $M=(K, \Sigma, \Delta, s, H)$ 的关键是从 STM 的 $\delta$ 变成了 $\Delta\subseteq ((K-H)\times \Sigma)\times(K\times(\Sigma\cup\{\leftarrow, \rightarrow\}))$，即**函数**到**关系**。

$\vdash_M, \vdash_M^*$定义类似 STM，但 $\vdash_M$ 不一定单值。

!!! info "NTM 的基本概念"
    考虑 NTM $M=(K, \Sigma, \Delta, s, H)$, $\Sigma_0=\Sigma-\{\triangleright, \sqcup\}$
    
    - $M$ **接受** $w\in \Sigma_0^*$: 指能对 $w$ 停机，即 $\exists h\in H, a\in \Sigma, u, v\in \Sigma^*\text{ s.t. }$
        
    $$
        (s, \triangleright\underline{\sqcup}w)\vdash_M^* (h, u\underline{a}v)
    $$

    - $M$ **半判定** $L\subseteq \Sigma_0^*$:属于$L$就停机，即$\forall w\in \Sigma_0^*$有
        
    $$
        w\in L\iff M\text{接受}w
    $$

    - $M$ **判定** $L\subseteq \Sigma_0^*$: 属于$L$就停机于$y$，要求有限步停机，$H=\{y, n\}$，$\exists \; a\in \Sigma, u, v\in \Sigma^*$
        
    $$
        w\in L \iff
        (s, \triangleright\underline{\sqcup}w)\vdash_M^* (y, u\underline{a}v)
    $$

    - $M$ **计算** $f: \Sigma_0^*\to \Sigma_0^*$: 要求有限步停机，且输出就是$v=f(w)$，即
        
    $$
        (s, \triangleright\underline{\sqcup}w)\vdash_M^* (h, u\underline{a}v)\iff
        ua=\triangleright \sqcup, v=f(w)
    $$

    -  **有限步停机**的刻画: $\exists\; N(M, w)\in \N\text{ s.t. }$不存在格局$C$满足$(s, \rightarrow\underline{\sqcup}w)\vdash_M^N C$
    

!!! tip "Remark"
    半判定时，只要有一种停机格局就行；判定时，只要有一种达到 $y$ 就行。但是计算 $f$ 时要求所有可能的计算的输出结果一致。

!!! example "Example"
    设计 NTM 半判定 $C=\{\operatorname{num}(p\cdot q):\; p,q\geqslant 2\}$ (合数集)

NTM 可以随机选择 $p, q$ 尝试 $p, q$ 相乘是否等于该合数，如果是合数就能在有限步内终止。当然，如果随机选择变成按序遍历，就可以实现判定。

### NTM/STM Equivalence

!!! abstract "Theorem"
    如果 NTM $M$ 半判定/判定一个语言，或能计算一个函数，那么存在一个 STM $M'$ 也半判定/判定同一语言，也能计算同一函数。

??? general "Proof"
    下面以半判定为例进行证明。注意到 $\Delta\in ((K-H)\times \Sigma)\times(K\times (\Sigma\cup \{\leftarrow, \rightarrow\}))$，因此给定当前的状态和读到的字符，次态和操作的不同分支最多只有 $|K|\cdot(|\Sigma|+2)$ 种。

    因此可以按照层序遍历整个 NTM 可能产生的计算树，按照字典序遍历同样计算步数能够达到的格局，观察是否能够停机，来实现半判定的效果。

    遍历所有可能的状态-输入二元组($q$, $a$)，可以确定最大可能的转移数量为 $r\leqslant |K|(|\Sigma|+2)$。那么给定 $(q, a)$，可以通过编码使得一个 1 位 $r$ 进制数能够表示下一步可能的转移分支。

    定义选好分支的 NTM $M$ 的确定性版本 $M_d$：$M_d$ 是 2-tape TM，和 $M$ 有相同的状态。$M_d$ 1 带就是 $M$ 的带，2 带上面一个 $n$ 位 $r$ 进制数，表示第 1 到第 $n$ 步要选择的转移分支。

    接下来构建 3-tape TM $M'$（由于 3-tape TM 和 STM 等价，所以直接构造 3-tape TM）。1 带放置 $M$ 的最初输入，整个模拟过程中保持不变。2 带是模拟带，3 带是分支选择带，2、3 带相当于 $M_d$。

    <div style="text-align:center;">
        <img src="../../imgs/toc/4.7.png" alt="4.7" style="zoom:40%;" />
    </div>

    $M'$ 按照字典序更改 3 带，尝试 1 步计算到 $n$ 步计算的所有 $M_d$，从而层序遍历 $M$ 的计算树。每个 $M_d$ 模拟完毕停机时，擦除 2 带，拷贝 1 带到 2 带，然后更改 3 带以准备下一个 $M_d$ 的模拟。

    <div style="text-align:center;">
        <img src="../../imgs/toc/4.8.png" alt="4.8" style="zoom:60%;" />
    </div>
    
    如果 NTM $M$ 能停机，那么它一定在某个计算树 $n$ 步（取最小的 $n$）的分支停机，那么 $M'$ 模拟的某一个选择了 $n$ 个分支的 $M_d$ 也一定能够模拟进入停机状态，从而实现半判定。

    但是 $M$ 需要 $n$ 步停机时，$M'$ (worst case) 就需要 $r + r^2+\cdots +r^n$ 步停机，即 $M$ 步数的指数倍。P 类和 NP 类的差别可见一斑。

## Grammars

### Grammar

!!! info "文法 (grammar)"
    文法 (grammar, or unrestricted grammar) 是一个 quadruple $G=(V, \Sigma, R, S)$，和 CFG 不同之处只有 $R\subseteq (V^*(V-\Sigma)V^*)\times V^*$。

!!! tip "Remark"
    $\to G, \Rightarrow_G, \Rightarrow_G^*, L(G)$ 以及推导的概念都类似 CFG。CFG 就是一种文法。

!!! example "Example"
    以下给出的 $G=(V, \Sigma, R, S)$ 生成语言 $\{a^nb^nc^n: n\geqslant 1\}$

    <div style="text-align:center;">
        <img src="../../imgs/toc/4.9.png" alt="4.9" style="zoom:50%;" />
    </div>

    grammar for $\{a^nb^nc^n: n\geqslant 1\}$

### Grammar/TM Equivalence

!!! abstract "Theorem"
    $L$ 由文法 $G$ 生成 $\iff$ $L$ 递归可枚举

??? general "Proof"
    $\Rightarrow$: 构造 3-tape TM。1带输入 $w$，保持不变。2 带模拟 $G$ 从 $S$ 开始的推导。3 带包含的是状态转移的分支选择信息。
    
    每一步推导有 $|R|+1$ 种可能的状态转移，其中 $|R|$ 种都来自于 $R$，如果选择这 $R$ 种中的一种，就在 2 带中搜索可以应用该规则的地方，“非确定性”地应用该规则进行推导。

    第 $|R|+1$ 种选择则是判断当前 2 带模拟结果是否与 1 带一致，若一致则停机并接受。

    $\Leftarrow$: 指定 $L$ 被 $M-(K, \Sigma, \delta, s, \{h\})$ 半判定。令 $\Sigma\cap K=\emptyset$，且都不包含右端标记 $\triangleleft$ （新引入的一个记号）。再规定停机格局总是 $(h, \triangleright\underline{\sqcup})$（即原停机后还要再删除带上内容，并到达唯一停机状态 $h$）。
    
    这样，基于从规定的停机格局到初始格局的**反向计算** (backwards computation) 方法，构造生成 $M$ 半判定的语言 $L\subseteq \Sigma_0^*=(\Sigma-\{\sqcup, \triangleright\})^*$ 的文法 $G=(V, \Sigma_0, R, S)$。($V=\Sigma\cup K\cup \{S, \triangleleft\}$)

    反向计算的关键是用字符串模拟格局，即用 $\triangleright uaqw\triangleleft$ 模拟 $(q, \triangleright u\underline{a}w)$。这里利用了状态 $q$ 标识了带头所在的位置 $q$。$\forall q\in K, a\in \Sigma$，根据 $\delta(q, a)$，$G$ 建立如下规则：
    
    - 写操作：$\exists\; p\in K, b\in \Sigma \text{ s.t. } \delta(q, a)=(p, b)$，有 $bp\to aq$
    - 右移操作：$\exists\; p\in K \text{ s.t. } \delta(q, a)=(p, \rightarrow)$，有 $abp\to aqb$
    - 左移操作：$\exists\; p\in K \text{ s.t. } \delta(q, a)=(p, \leftarrow)$，要考虑删除空格操作
        
    $$
        \begin{cases}
            pa\to aq, & a\neq \sqcup\\
            p\sqcup b\to \sqcup qb(\forall b\in \Sigma), p\triangleleft\to \sqcup q\triangleleft, &a=\sqcup
        \end{cases}
    $$

    - 初始和终止：$S\to \triangleright\sqcup h\triangleleft$, $\triangleright\sqcup s\to e$, $\triangleleft\to e$
    

Claim: 对 $M$ 的 $\forall$ 格局 $(q_1, u_1\underline{a_1}w_1), (q_2, u_2\underline{a_2}w_2)$，有

$$
    (q_1, u_1\underline{a_1}w_1)\vdash_M(q_2, u_2\underline{a_2}w_2)
    \iff
    u_2a_2q_2w_2\triangleleft \Rightarrow_G u_1a_1q_1w_1\triangleleft
$$


有这个claim成立就能证明构造等价了。证明见课本练习。

但至此文法生成的语言等价的是递归可枚举语言，与递归函数等价的是文法可计算函数。
!!! info "文法可计算函数"
    $G=(V, \Sigma, R, S)$ 是文法，$f: \Sigma^*\to\Sigma^*$ 是函数
    
    - $G$ **计算** $f$: $\forall w, v\in \Sigma^*$，有
        
    $$
        SwS\Rightarrow_G^* v\iff v=f(w)
    $$

    - 当 $\exists\; G$ 计算 $f$ 时，$f$ 称为**文法可计算** (grammatically computable) 的。
    

!!! abstract "Theorem"
    $f: \Sigma^*\to \Sigma^*$ 是递归的 $\iff$ $f$ 是文法可计算的

## Numerical Functions

### Primitice Recusive Functions

!!! info "基本函数"
    给出三个基本函数
    
    - $\forall k\geqslant 0$，定义 $k$ 元**零函数**($k$-ary zero function)
        
    $$
        \operatorname{zero}_k(n_1, \cdots, n_k)=0,\quad \forall n_1, \cdots, n_k\in \N
    $$

    - $\forall k\geqslant j>0$，定义第 $j$ 个 $k$ 元**恒等函数** ($j$-th $k$-ary identity function)
        
    $$
        \operatorname{id}_{k, j}(n_1, \cdots, n_k)=n_j,\quad \forall n_1, \cdots, n_k\in \N
    $$

    - 定义**后继函数** (successor function)
        
    $$
        \operatorname{suc}(n)=n+1,\quad \forall n\in\N
    $$


!!! tip "Remark"
    恒等函数可以理解为投影函数。

有两种合成较复杂函数的方法：

- $\forall k, l \geq 0$, $g: \mathbb{N}^k \rightarrow \mathbb{N}$, $h_1, \ldots, h_k$ 是 $l$ 元函数。则 $g$ 和 $h_1, \ldots, h_k$ 的**复合** (composition) 为如下 $l$ 元函数
    
$$
    f(n_1,\cdots, n_l)=g(h_1(n_1,\cdots, n_l), \cdots, h_k(n_1,\cdots, n_l))
$$

- $\forall k \geq 0$，$g$ 是 $k$ 元函数，$h$ 是 $(k+2)$ 元函数。则用 $g, h$ **递归定义**的 $k+1$ 元函数 $f$ 为
    
$$
    \begin{aligned}
        & f\left(n_1, \ldots, n_k, 0\right) = g\left(n_1, \ldots, n_k\right) \\
        & f\left(n_1, \ldots, n_k, m+1\right) = h\left(n_1, \ldots, n_k, m, f\left(n_1, \ldots, n_k, m\right)\right)
    \end{aligned}
$$

!!! info "原始递归函数 (primitive recursive functions)"
    原始递归函数 (primitive recursive functions) 就是基本函数及所有由基本函数通过若干次复合/递归定义得到的函数。

!!! question "Example"
    证明下列函数都是原始递归的
    
    - $\operatorname{plus}(m, n)=m+n$
    - $\operatorname{mult}(m, n)=m \cdot n$
    - $\exp (m, n)=m^n$
    

??? general "Proof"
    
    $$
    \begin{aligned}
        & \operatorname{plus}(m, 0)=m \\
        & \operatorname{plus}(m, n+1)=\operatorname{succ}(\operatorname{plus}(m, n)) \\
        & \operatorname{mult}(m, 0)=\operatorname{zero}(m) \\
        & \operatorname{mult}(m, n+1)=\operatorname{plus}(m, \operatorname{mult}(m, n)) \\
        & \exp (m, 0)=\operatorname{succ}(z \operatorname{ero}(m)) \\
        & \exp (m, n+1)=\operatorname{mult}(m, \exp (m, n))
    \end{aligned}
    $$


!!! tip "Remark"
    不直接写 $\exp (m, 0)=1$ 是因为还没证明常数函数也是原始递归的。

!!! example "Example"
    常数函数、符号函数都是原始递归的。常数函数可以通过 $\operatorname{zero}$ 加上若干次 $\operatorname{suc}$ 得到，符号函数则直接定义 0 的时候是 0，正数的时候是 1。

!!! question "Example"
    证明 $m\sim n=\max\{m-n, 0\}$ 也是原始递归的。

??? general "Proof"
    定义原始递归的前驱函数 (predecessor function):
    
    $$
        \begin{aligned}
            & \operatorname{pred}(0) = 0\\
            & \operatorname{pred}(n+1) = n
        \end{aligned}
    $$


    根据前驱函数递归定义
    
    $$
        \begin{aligned}
            & m\sim 0 = m\\
            & m\sim (n+1) = \operatorname{pred}(m\sim n)
        \end{aligned}
    $$


!!! info "原始递归谓词 (primitive recursive predicate)"
    即只取值 0, 1 的原始递归函数

!!! example "Example"
    
    - 零判定 $\:\operatorname{iszero}(n)$: $\operatorname{iszero}(0)=1, \operatorname{iszero}(m+1)=0$
    - 正判定 $\operatorname{positive}(n) = \operatorname{sgn}(n)$
    - 大于等于 $\text{greater-than-or-equal}(m, n) = \operatorname{iszero}(n\sim m)$
    - 小于 $\operatorname{less-than}(m, n) = 1 \sim \text{greater-than-or-equal}(m, n)$
    - 取反 negation: $\neg p(m)=1\sim p(m)$
    - 析取合取 disjunction and conjunction: 
        
        $$
            \begin{gathered}
                p(m, n) \vee q(m, n) = \operatorname{sgn}(p(m, n) + q(m, n))\\
                p(m, n) \wedge q(m, n) = \operatorname{sgn}(p(m, n)\cdot q(m, n))
            \end{gathered}
        $$

    - 条件语句: $f(n_1,\cdots, n_k)=\begin{cases}
            g(n_1,\cdots, n_k), & p(n_1,\cdots, n_k)\\
            h(n_1,\cdots, n_k), & \neg p(n_1,\cdots, n_k)
        \end{cases}$, 因为
        
        $$
            f(n_1,\cdots, n_k)= p(n_1,\cdots, n_k)\cdot g(n_1,\cdots, n_k)+ \neg p(n_1,\cdots, n_k)\cdot h(n_1,\cdots, n_k)
        $$

    

!!! example "Example"
    定义 div 和 rem：
    
    $$
        \begin{aligned}
            \operatorname{rem}(0, n) &= 0\\
            \operatorname{rem}(m+1, n) &= \begin{cases}
                    0, &\operatorname{equal}(\operatorname{rem}(m, n), \operatorname{pred}(n))\\
                    \operatorname{rem}(m, n)+1, & \operatorname{otherwise}
                \end{cases}\\
            \operatorname{div}(0, n) &= 0\\
            \operatorname{div}(m+1, n) &= \begin{cases}
                \operatorname{div}(m, n) + 1, & \operatorname{equal}(\operatorname{rem}(m, n), \operatorname{pred}(n))\\
                \operatorname{div}(m, n), & \text{otherwise}
                \end{cases}
        \end{aligned}
    $$


!!! tip "Remark"
    $\operatorname{equal}(m, n) = \operatorname{iszero}(n\sim m) \wedge \operatorname{iszero}(m\sim n)$

!!! example "Example"
    $\operatorname{digit}(m, n, p)$: $n$ 在 $p$ 进制表示下的第 $m$ 位（低位向高位数）
    
    $$
        \operatorname{digit}(m, n, p)=\operatorname{div}(\operatorname{rem}(n, p^ m), p^{m\sim 1})
    $$


    特别地，判断奇数的 $\operatorname{odd}(n)=\operatorname{digit}(1, n, 2)$。

!!! example "Example"
    $f(n, m)$ 原始递归，则 $\operatorname{sum}$
    
    $$
        \operatorname{sum}_f(n, m)=\sum_{k=0}^m f(n, k)
    $$

    也原始递归。因为它被递归定义为
    
    $$
        \begin{aligned}
            \operatorname{sum}(n, 0) &= 0\\
            \operatorname{sum}(n, m+1) &= \operatorname{sum}_f(n, m) + f(n, m+1)
        \end{aligned}
    $$


    同理，$\operatorname{mult}_f(n, m)=\displaystyle\prod_{k=0}^m f(n, k)$ 也是原始递归的。

!!! example "Example"
    由于
    
    $$
        \begin{gathered}
            \exists \; t_{(\leqslant m)}p(n_1, \cdots, n_k, t)\iff \sum_{t=0}^m p(n_1, \cdots, n_k, t)\neq 0\\
            \forall \; t_{(\leqslant m)}p(n_1, \cdots, n_k, t)\iff \prod_{t=0}^m p(n_1, \cdots, n_k, t)\neq 0
        \end{gathered}
    $$


    所以考虑 $\leqslant m$ 范围的存在和任意谓词也是原始递归的。

!!! example "Example"
    有了存在和任意，很多就好搞了。
    
    - 整除 $y | x\iff \exists\; t_{(\leqslant x)}(y\cdot t=x)$
    - 质数判定 $\operatorname{prime}(x)\iff(x\geqslant 2)\wedge\forall\; t_{(<x)}[t<2\vee \neg(t|x)]$
    

!!! example "Example"
    原始递归函数是**可数无限**的。这是因为将三个基本函数，两种合成运算以及括号等组成一个 $\Sigma$，那么所有原始递归函数 $\in\Sigma^*$。

    基于其可列性，可以将所有原始递归函数按字典序排列，编号为 $f_0, f_1, f_2, \cdots$。定义函数 $g(n)=f_n(n)=1$，可见 $g(n)$ 可以通过所有原始递归函数实现可计算（即 $g(n)$ 是**递归**的），但是它不与任何一个原始递归函数相同（即 $g(n)$ **不是原始递归**的）

    可见，**原始递归函数是递归函数的真子集**。

### Minimalization and $\mu$-recursive

!!! info "极小化 (minimalization)"
    对 $k+1$ 元函数 $g$，$k\geqslant 0$
    
    - $g$ 的**极小化**(minimalization): 得到 $k$ 元函数 $\mu \;m[g(n_1, \cdots, n_k, m)=1]$
        
        $$
            f(n_1,\cdots, n_k)=
            \begin{cases}
                \text{ 最小的 }m\text{ s.t. } g(n_1,\cdots, n_k, m)=1, & \exists m\\
                0, & \text{otherwise}
            \end{cases}
        $$

    - **可极小化**(minimalizable): 如果下式满足，则 $g$ 可极小化
        
        $$
            \forall n_1,\cdots, n_k\in N, \exists\; m\in \N \text{ s.t. } g(n_1,\cdots, n_k, m)=1
        $$

    - $\mu$-**递归** ($\mu$-recursive): 在原始递归的两个运算中再加入**可极小化函数**的极小化运算，形成 $\:\mu$-递归函数类。
    

!!! tip "Remark"
    
    - 无明显算法可计算极小化，但是可以从 $m=0$ 开始慢慢试能不能极小化（不一定停止）
    - 无法通过对角线原则判断是否有可计算函数不是 $\:\mu$-递归的，因为极小化只能对可极小化函数应用，一个自称 $\:\mu$-递归函数的函数可能其中极小化不作用于可极小化函数。
    

!!! example "Example"
    可以利用极小化定义一个对数 (logarithm) 函数（但是对数函数可以不使用极小化定义）
    
    $$
        \log(m, n)=\mu\; p[\text{greater-than-or-equal}((m+2)^p, n+1)]
    $$


    注意这里定义 $\log(m, n)=\left\lceil\log_{(m+2)}(n+1)\right\rceil$，和通常的对数函数不同，这是为了保证底数 $m+2\geqslant 2$，以及 $n+1\geqslant 1$。

    可以通过判定 $\mu\; p$ 里面的函数可极小化来判定该 $\:\mu$-递归函数定义的恰当性。

!!! abstract "Theorem"
    $f:\; \N^k\to \N$ 是 $\:\mu$-递归函数 $\iff f$ 是递归的(可被 TM 计算)

??? general "Proof"
    $\Rightarrow$: 三个基本函数都图灵可计算，合成相当于子程序调用，递归定义相当于递归调用，极小化也给出了方法（$\mu$-递归定义中可极小化的限定保证停机），因此整个 $\:\mu$-递归函数类都是图灵可计算的。（可以用随机存取图灵机证明）

    $\Leftarrow$: 首先想法是把 TM 每个格局编码为一个数字。不妨令 TM $M=(K, \Sigma, \delta, s, \{h\})$，其中 $K\cap \Sigma=\emptyset$。设 $b=|\Sigma|+|K|$，建立映射 $\mathbb{E}:\;\Sigma\cup K\to \{0, 1, \cdots, b-1\}$，有
    
    $$
        \mathbb{E}(0)=0,\;
        \mathbb{E}(1)=1
    $$


    格局 $(q, a_1a_2\cdots\underline{a_k}\cdots a_n)$ 改写为 $b$ 进制整数  $a_1a_2\cdots\underline{a_k}q\cdots a_n$ ($q$ 利用其特殊的编码表明了 $a_k$ 的位置)，即
    
    $$
        \mathbb{E}(a_1)b^n+\cdots+\mathbb{E}(a_k)b^{n-k+1}+\mathbb{E}(q)b^{n-k}+\cdots + \mathbb{E}a_n
    $$


    最后可以把 $f(n)$ 表示为
    
    $$
        f(n)=\operatorname{num}(\operatorname{output}(\operatorname{last}(\operatorname{comp}(n))))
    $$

    - $\operatorname{num}()$ 将 $b$ 进制转换为 2 进制
    - $\operatorname{output}()$从停机格局 $\triangleright \sqcup hw'$ 中删除前导字符获得输出 (output) 结果 $w'=f(w)$
    - $\operatorname{comp}(n)$ 将从初始格局 $n$ 出发的一系列计算 (computation) 进行编码，图灵可计算保证整个计算序列存在
    - $\operatorname{last}()$则用于从这个计算序列中选取最终 (last) 的停机格局

    这四个函数都是 $\:\mu$-递归的（具体可见课本），终得证。