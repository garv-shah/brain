n = input('Please enter a value for n, the amount of locker doors: ')

# validate n as positive integer
while True:
    try:
        n = int(n)
        if n <= 0:
            print('n must be a positive integer')
            n = input('Please enter a value for n, the amount of locker doors: ')
        else:
            break
    except ValueError:
        print('n must be a positive integer')
        n = input('Please enter a value for n, the amount of locker doors: ')

print(f'\nStarting algorithm with {n} locker doors')

doors = [False] * n

for door in range(1, n + 1):
    for i in range(door, n + 1, door):
        doors[i - 1] = not doors[i - 1]

print(doors)
print(f'There are a total of {sum(doors)} doors open at the end')
