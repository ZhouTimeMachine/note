# After Story of TOC

!!! info "Some useful things about TOC after I have completed ZJU *Introductiion to Theoretical Computer Science*, 2022 Fall & Winter"

## Parikh's Theorem

!!! tip "See [wikipedia](https://en.wikipedia.org/wiki/Parikh%27s_theorem) for more details"

Let $\Sigma=\left\{a_1, a_2, \ldots, a_k\right\}$ be an alphabet. 

!!! info "Parikh vector"
    The Parikh vector of a word is defined as the function $p: \Sigma^* \rightarrow \mathbb{N}^k$, given by ${ }^{[1]}$

    $$
    p(w)=\left(|w|_{a_1},|w|_{a_2}, \ldots,|w|_{a_k}\right)
    $$
    
    where $|w|_{a_i}$ denotes the number of occurrences of the letter $a_i$ in the word $w$.

!!! info "linear and semi-linear subset of $\mathbb{N}^k$"
    A subset of $\mathbb{N}^k$ is said to be **linear** if it is of the form
    
    $$
    u_0+\mathbb{N} u_1+\cdots+\mathbb{N} u_m=\left\{u_0+t_1 u_1+\cdots+t_m u_m \mid t_1, \ldots, t_m \in \mathbb{N}\right\}
    $$
    
    for some vectors $u_0, \ldots, u_m$. A subset of $\mathbb{N}^k$ is said to be semi-linear if it is a union of finitely many linear subsets.

!!! abstract "Parikh's Theorem"
    Let $L$ be a context-free language or a regular language, let $P(L)$ be the set of Parikh vectors of words in $L$, that is, $P(L)=\{p(w) \mid w \in L\}$. Then $P(L)$ is a semi-linear set.

    If $S$ is any semi-linear set, then there exists a regular language (which a fortiori is context-free) whose Parikh vectors is $S$.

- In short, the image under $p$ of context-free languages and of regular languages is the same, and it is equal to the set of semilinear sets. 
- Two languages are said to be **commutatively equivalent** if they have the **same set of Parikh vectors**. 
- Thus, every context-free language is commutatively equivalent to some regular language.