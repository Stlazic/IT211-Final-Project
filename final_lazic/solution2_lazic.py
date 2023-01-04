f = open('words.txt')

lines = f.readlines()
f.close()
words_19 = 0
words = []

for i in lines:
    if len(i) > 19:
        words_19 += 1
        words.append(i)
print('There are %d words with over 19 characters' % words_19)
print()
print('They are:')
print(''.join(words))
