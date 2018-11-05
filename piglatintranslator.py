# A fun pig-latin translator.

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = ('%s%s%s' % (word, first, pyg))
    new_word = new_word[1: len(new_word)]
    print(new_word)

else:
    print('Error! Try again without spaces, numbers, or characters.')