# trapezium method for approximating areas
def f(x):
    return 2*x + 1

a = 1
b = 2
n = 100

h = (b-1)/n
left = a
right = a + h
sum = 0

for i in range(1, n + 1):
    strip = 0.5 * (f(left) + f(right)) * h
    sum += strip
    left += h
    right += h

print(sum)
