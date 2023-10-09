import string

scrambled_word = input('Enter a scrambled word: ')
guess_word = input('Enter a guess as to what the word is: ')

scrambled_list = list(scrambled_word.lower())
guess_list = list(guess_word.lower())

scrambled_dict = {}
guess_dict = {}

for letter in list(string.ascii_lowercase):
    scrambled_dict[letter] = scrambled_list.count(letter)
    guess_dict[letter] = guess_list.count(letter)

print(scrambled_dict == guess_dict)
