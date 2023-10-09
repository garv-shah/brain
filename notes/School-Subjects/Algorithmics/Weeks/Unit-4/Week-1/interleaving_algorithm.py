def to_string(List):
    return "".join(List)


def interleaving_recursive(word1, word2, iStr, m, n, i):
    # Base case: If all characters of word1 and word2 have been
    # included in output string, then print the output string
    if m == 0 and n == 0:
        print(to_string(iStr))

    # If some characters of word1 are left to be included, then
    # include the first character from the remaining characters
    # and recur for rest
    if m != 0:
        iStr[i] = word1[0]
        interleaving_recursive(word1[1:], word2, iStr, m - 1, n, i + 1)

    # If some characters of word2 are left to be included, then
    # include the first character from the remaining characters
    # and recur for rest
    if n != 0:
        iStr[i] = word2[0]
        interleaving_recursive(word1, word2[1:], iStr, m, n - 1, i + 1)


def interleaving(word1, word2, m, n):
    character_list = [''] * (m + n)

    interleaving_recursive(word1, word2, character_list, m, n, 0)


word1 = "at"
word2 = "MY"
interleaving(word1, word2, len(word1), len(word2))
