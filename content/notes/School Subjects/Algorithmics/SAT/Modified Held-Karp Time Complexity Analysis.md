---
title: Modified Held-Karp Time Complexity Analysis
author: Garv Shah
date: 02/12/2023
abstract: The formal proof below is part of a larger investigation into the practical applications of the TSP, which I completed for my University Algorithmics course this year. This incorporates elements of formal proof which I have learnt in Specialist Mathematics. If you would like to read the full investigation, you can view it [here](https://garv-shah.github.io/applications_of_tsp.pdf).
geometry: margin=2cm
output: pdf_document
colorlinks: true
linkcolor: blue
urlcolor: red
---
## Modified Held-Karp Time Complexity

Now that we have an established cost function, we can attempt to evaluate $T_{n}$ in terms of $d(n)$. To reiterate:

$$
T_{n} = \left\{
        \begin{array}{ll}
            n(T_{n-1}+d(n)) & \quad n > 0 \\
            d(n) & \quad n=0
        \end{array}
    \right.
$$
$$
d(n)=2LR+\frac{1}{2}L^{3}+\frac{1}{2}L^{2}+L
$$

Keeping this in terms of $d(n)$, we can create a table to see how this recurrence relation gets bigger as $n$ increases.

| $n$ | $T_{n}$   |
|-----|-----------|
| 0   | $d(n)$    |
| 1   | $2d(n)$   |
| 2   | $6d(n)$   |
| 3   | $21d(n)$  |
| 4   | $88d(n)$  |
| 5   | $445d(n)$ |

The working for this table is shown below, but you can easily keep going to follow the pattern for higher values of $n$:

$n = 0$: $T_{n}=d(n)$

$n = 1$: $T_{n}=1(T_{0}+d(n))=2d(n)$

$n = 2$: $T_{n}=2(T_{1}+d(n))=6d(n)$

$n = 3$: $T_{n}=3(T_{2}+d(n))=21d(n)$

$n = 4$: $T_{n}=4(T_{3}+d(n))=88d(n)$

$n = 5$: $T_{n}=5(T_{4}+d(n))=445d(n)$

### Recurrence Relation

Just looking at the coefficients for a second, we have the following recurrence relation:

$$
T_{n}=n(T_{n-1}+1), \space T_{0}=1
$$ 

It is easy to see that this recurrence relation implies that the running time for the algorithm is factorial. After all, the recurrence relation for $n!$ is $T_{n}=n(T_{n-1}), \space T_{0}=1$. 

### Attempting to Find an Explicit Formula

Now clearly it is of interest to solve this [recurrence relation](#recurrence-relation) and find a non-recursive formula, and here we run into a bit of an issue. If the relation were a linear recurrence with constant coefficients or a typical divide-and conquer recurrence, it would likely be solvable by well-known methods such as telescoping or the Master Theorem, but this is not the case.

#### Theorem 1

While trying to find a way to solve this [recurrence relation](#recurrence-relation), I arrived at the conjecture that $T_{n}=n!+\sum_{i=0}^{n-1} \frac{n!}{i!}$, so let us try to prove it.

> For $n \in \mathbb{N}$, the number of operations used to solve an n-sized visit set TSP by the above algorithm (ignoring the cost function) satisfied the formula: $T_{n}=n!+\sum_{i=0}^{n-1} \frac{n!}{i!}$.

First let us work with the RHS to rearrange it a bit into a more convenient form:
$RHS$

$= n!+\sum_{i=0}^{n-1} \frac{n!}{i!}$

$= n!+\frac{n!}{0!}+\frac{n!}{1!}+\frac{n!}{2!}+\cdots+\frac{n!}{(n-2)!}+\frac{n!}{(n-1)!}$

$= n! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(n-2)!}+\frac{1}{(n-1)!})$

##### Base Case

When $n=0$, the base case of the [recurrence relation](#recurrence-relation) says that $T_{0}=1$. The above formula matches that with $T_{0}=0!\times(1+0)=1$, $\therefore$ base case is true.

##### Induction Step

Pick an arbitrary $k \in \mathbb{N}$. Assume that the theorem holds for any TSP with a visit set of size $k$. Thus, it is assumed that $T_{k}= k! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(k-2)!}+\frac{1}{(k-1)!})$.

Proof by induction requires showing the following: 

$T_{k+1}= (k+1)! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(k-1)!}+\frac{1}{k!})$. 

Next, we can combine the recurrence above with the induction hypothesis as follows:

$LHS$

$=T_{k+1}$

$=T_{k}(k+1)+(k+1)$ (from [recurrence relation](#recurrence-relation)) 

$=[k! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(k-2)!}+\frac{1}{(k-1)!})](k+1)+(k+1)$

$=(k+1)! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(k-2)!}+\frac{1}{(k-1)!})+(k+1)$

$=(k+1)! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(k-2)!}+\frac{1}{(k-1)!})+(k+1)\times\frac{(k+1)!}{(k+1)!}$

$=(k+1)! \times \left(1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{\left(k-2\right)!}+\frac{1}{(k-1)!}+\frac{k+1}{(k+1)!}\right)$

$=(k+1)! \times \left(1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{\left(k-2\right)!}+\frac{1}{(k-1)!}+\frac{1}{k!}\right)$

$=RHS$

Thus $T_{n}=n!+\sum_{i=0}^{n-1} \frac{n!}{i!}$ by the principle of mathematical induction.

#### Theorem 2

Looking all over the web for this, the only place I could find any reference to this sequence is [here](https://oeis.org/A033540), which provides us with the relation $T_{n}=n! + \lfloor e\times n!\rfloor - 1$ for the coefficients. This can be rearranged to $T_{n}=\lfloor n!(e+1)-1 \rfloor$, but just to be sure that this works for every case, we should probably prove it too.

> For $n \in \mathbb{Z}^{+}$, the number of operations used to solve an n-sized visit set TSP by the above algorithm (ignoring the cost function) satisfied the formula: $T_{n}=\lfloor n!(e+1)-1 \rfloor$.

##### Case 1

This is the case where $n=1$. As seen above, $T_{1}=2$ and the proposed formula predicts that $T_{1}= \lfloor 1!(e+1)-1 \rfloor = \lfloor e+1-1 \rfloor = \lfloor e \rfloor = 2$. Thus, the base case holds.

##### Case 2

This is the case where $n>1$. Because of the floor function, if it can be shown that the following difference is small enough, it will probably be possible to prove that this case works as well.
$$
\textrm{Let } \space r_{n}=n!(e+1)-1-T_{n}
$$

##### Lemma 1

> When $n>1$, the following must be true: $r_{n}=\frac{1}{n+1}+\frac{1}{(n+1)(n+2)}+\frac{1}{(n+1)(n+2)(n+3)}+\cdots$

This sum looks like it might be related to the power series for $e^{x}$ at $x=1$. We already know the power series for $e^{x}$, a proof for which can be found [here](https://proofwiki.org/wiki/Power_Series_Expansion_for_Exponential_Function):

$$
e^{x}=\frac{1}{0!}+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots
$$

It therefore follows that:

$$
e=e^{1}=\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\cdots
$$
Since we know that $T_{n} = n! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots+\frac{1}{(n-2)!}+\frac{1}{(n-1)!})$ from the [first theorem](#theorem-1), we can sub both the power series for $e$ and this fact into our definition of $r_{n}$:

$r_{n}$

$= n!(e+1)-1-T_{n}$ (by definition)

$= n!(1+\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots)-1-T_{n}$ (power series for $e$)

$= n!(1+\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\cdots)-1-n! \times (1 + \frac{1}{0!}+\frac{1}{1!}+\cdots+\frac{1}{(n-2)!}+\frac{1}{(n-1)!})$ 

$=n!\times(\frac{1}{n!}+\frac{1}{(n+1)!}+\frac{1}{(n+2)!}+\cdots)-1$

$=(1+\frac{1}{n+1}+\frac{1}{(n+1)(n+2)}+\cdots)-1$

$=\frac{1}{n+1}+\frac{1}{(n+1)(n+2)}+\frac{1}{(n+1)(n+2)(n+3)}+\cdots$

$\therefore$ The lemma is true.

##### Lemma 2

> When $n>1$, it is true that $r_{n}<\frac{1}{n+1}+\frac{1}{(n+1)^{2}}+\frac{1}{(n+1)^{3}}+\cdots=\frac{1}{n}$

This is easily proven using the [first lemma](#lemma-1):

$r_{n}$

$=\frac{1}{n+1}+\frac{1}{(n+1)(n+2)}+\frac{1}{(n+1)(n+2)(n+3)}+\cdots$ (Lemma 1)

$< \frac{1}{n+1}+\frac{1}{(n+1)(n+1)}+\frac{1}{(n+1)(n+1)(n+1)}+\cdots$

$= \frac{1}{n+1}+\frac{1}{(n+1)^{2}}+\frac{1}{(n+1)^{3}}+\cdots$


This upper bound above is in the form of an infinite geometric series with ratio $\frac{1}{n+1}$, so the usual formula of $S_{\infty}=\frac{a}{1-r}$ can be used: $r_{n} <\frac{\frac{1}{n+1}}{1-\frac{1}{n+1}} =\frac{1}{n}$.

$\therefore$ The lemma is true.

##### Lemma 3

> If $n > 1$, $0<r_{n}<1$ must hold true.

From [Lemma 1](#lemma-1), it is clear that $r_{n}$ is positive $\therefore 0< r_{n}$. 

Then, by [Lemma 2](#lemma-2), the following must hold: $r_{n}<\frac{1}{n}\le\frac{1}{2}<1$. $\therefore r_{n}<1$.

$\therefore$ The lemma is true.

##### Conclusion

Thus, the proof for this theorem is complete for the case $n>1$:

By the [definition](#case-2) of $r_{n}$, it must be true that $T_{n}+r_{n}=n!(e+1)-1$. Since the [recurrence relation](#recurrence-relation) set up $T_{n}$ as integer and $0<r_{n}<1$ by [Lemma 3](#lemma-3), it must hold that $\lfloor n!(e+1)-1 \rfloor = \lfloor T_{n}+r_{n} \rfloor=T_{n}$.

### Time Complexity

Now that we have proved this works for the coefficients of the cost function, we have the formula of $T(n)=d(n) \lfloor n!(e+1)-1 \rfloor$.The floor function here is just to deal with the difference of $r_{n}$ so that we can get an integer output. Subbing in our known time complexity of $d(n)$, we get a final Big O of $O(\lfloor n!(e+1) \rfloor(2LR+L^{3}))$ for the original implementation of our modified Held-Karp with no caching of its own Dijkstra's outputs. Note that it should already have been obvious that the running time for this algorithm would be in factorial time from the recurrence relation itself, even before finding an explicit formula.

We have already verified that this is correct given that the recurrence relation is correct, but we can also do so by general intuition . If we look back at Part 1, we can get the time taken to run the unoptimised modified Held-Karp on our data with different $n$ values. $(2LR+L^{3})$ should be a constant for any particular predefined graph, meaning that if our Big O time complexity is correct then $\textrm{execution time} \propto \lfloor n!(e+1) \rfloor$[^4].

| n | $\frac{\textrm{execution time}}{\lfloor n!(e+1) \rfloor}$ |
|---|-----------------------------------------------------------|
| 5 | $3\times10^{-5}$                                          |
| 6 | $4\times10^{-5}$                                          |
| 7 | $3\times10^{-5}$                                          |
| 8 | $3\times10^{-5}$                                          |
| 9 | $3\times10^{-5}$                                          |

[^4]: Note that $n<5$ would be rather unreliable due to the decimal inaccuracy of my recorded execution times (4dp)

As we can see, this proportionality is fairly constant, so it would probably be safe to assume that the worst-case time complexity for the unoptimised modified Held-Karp algorithm would be $O(\lfloor n!(e+1) \rfloor(2LR+L^{3}))$, or at least something pretty close to it.