Let $H(a,i)$ be function that tells if $a$ halts given $i$ as an input.
Let $H+(a,i)$ be the function that does the opposite.

What will the output of $H+(H, H)$ be?

```python
def H(algo: function, input: string):
	return will algo halt with input

def H+(algo: H(a, i)):
	if H(algo, input) == true:
		repeat forever/don't halt
	else:
		terminate/halt

print(H+(H)) // should be a syntax error for datatype
```

```python
def addnum():
	return 5 * int

addnum(addnum)
```

```
f(g) = |the minimum value of g|
f(f) = 0
```
g(x) = f(x)+limx-> 0

g(x) = x^2