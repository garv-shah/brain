fibs = [1, 1]

i = 0

while i < 60:
    num = fibs[i] + fibs[i + 1]
    if num % 4 == 0:
        print(f'{num} has index {len(fibs) + 1}')
    fibs.append(num)
    i += 1

print(fibs)
