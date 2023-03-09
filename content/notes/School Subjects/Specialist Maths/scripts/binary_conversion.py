n = 9647
binary_array = []
div = 2

while n > 0:
    q = n // div
    r = n % div
    binary_array.append(r)

    n = q

print(list(reversed(binary_array)))
