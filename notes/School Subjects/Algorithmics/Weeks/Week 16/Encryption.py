import string

encrypt = 'DUGOFXHO'
key = [3, 1, 2]
decrypt = ''

for i in range(len(encrypt)):
    print(encrypt[i], end='')
    char_num = list(string.ascii_lowercase).index(encrypt[i].lower())
    letter = char_num - key[i % 3]
    decrypt += string.ascii_lowercase[letter % len(string.ascii_lowercase)]

print(decrypt)
