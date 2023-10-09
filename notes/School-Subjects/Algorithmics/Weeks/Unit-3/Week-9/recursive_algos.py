word = ['B', 'U', 'T', 'T', 'E', 'R']


def reverse_list(list):
    if len(list) == 1:
        return list
    else:
        # list[1:] is all but first element of list
        # first element list[0] goes to the end
        return reverse_list(list[1:]) + [list[0]]


print(reverse_list(word))

number = 234


def sum_integer(integer):
    if integer == 0:
        return 0
    else:
        # get last digit (remained when div 10)
        # input back in rest of numbers (integer divided by 10)
        return integer % 10 + sum_integer(integer // 10)


print(sum_integer(number))


def fibonacci(n, n1):
    if n > 150:
        return [n1]
    else:
        return [n1] + fibonacci(n1, n1 + n)


print(fibonacci(0, 1))
