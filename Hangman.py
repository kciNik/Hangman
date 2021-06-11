import random

f = open('word_rus.txt', 'r', encoding='utf-8')
words = f.readlines()
w = words[random.randint(1, 34010)]
print(w)
print('Your word:')
print('_' * (len(w) - 1))
