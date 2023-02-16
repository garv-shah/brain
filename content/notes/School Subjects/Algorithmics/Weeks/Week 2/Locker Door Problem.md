---
title: "Locker Door Problem"
---

> [!info]
> 
> There are _n_ lockers in a hallway, numbered sequentially from 1 to _n_. Initially all the locker doors are closed. You make _n_ passes by the lockers, each time starting with locker 1.
> 
> On the _ith_ path, i = 1,2,..._n_ you toggle the door of every _ith_ locker; if the door is closed, you open it; if it is open, you close it.
> 
> After the last pass, which locker doors are open and which are closed? How many of them are open?

```python
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
```



