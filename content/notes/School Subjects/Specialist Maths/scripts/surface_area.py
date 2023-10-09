min = float('inf')
xmin = 0
ymin = 0

for x in range(1, 33):
    for y in range(1, 33):
        S = x * y + 64/x + 64/y
        if S <= min:
            min = S
            xmin = x
            ymin = y
            print(f"min is {min}, xmin is {xmin}, ymin is {ymin}")
