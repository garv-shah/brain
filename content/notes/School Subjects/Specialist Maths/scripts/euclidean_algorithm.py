# Finds the HCF
a = 72
b = 42

r = a % b

while r != 0:
    a = b
    b = r
    r = a % b

print(b)
