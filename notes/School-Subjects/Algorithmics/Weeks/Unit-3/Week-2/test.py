def Diamonds(x, y):
    x = x + 2*y
    while True:
        if x < y:
            break
        print(x)
        x = x - 1
    print(f'y is {x}')

Diamonds(2,3)
