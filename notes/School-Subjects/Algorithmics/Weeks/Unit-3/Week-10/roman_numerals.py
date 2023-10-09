num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman = input("Enter a roman numeral: ")
roman_list = list(roman)
count = 0

for i in range(len(roman_list)):
    # if the next digit is outside the array
    if (i + 1) < len(roman_list):
        next_index = i + 1
    else:
        next_index = i

    current_number = num_dict[roman_list[i]]
    next_number = num_dict[roman_list[next_index]]

    if current_number < next_number:
        count -= current_number
    else:
        count += current_number

print(count)
