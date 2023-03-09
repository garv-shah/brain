# Finds the HCF
a = 762
b = 372

r = a % b

while r != 0:
    a = b
    b = r

    if (a % b) == 0:
        break
    else:
        r = a % b

print(b)
