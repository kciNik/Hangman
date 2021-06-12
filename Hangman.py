import random

f = open('word_rus.txt', 'r', encoding='utf-8')
words = f.readlines()
w = words[random.randint(1, 34010)]
answer = list('_' * (len(w) - 1))
flag = True
lives = 6
used = list()
print('Your word:')
print(''.join(answer))
while flag:
    fl = False
    print('Select a letter:')
    letter = input()
    used.append(letter)
    for a in range(len(w)):
        if letter == w[a]:
            answer[a] = letter
            fl = True
    if not fl:
        lives -= 1
    if lives == 0:
        print('Your word:')
        print(''.join(answer))
        print('')
        print('Lives:', lives)
        print('')
        print('You lose(')
        print('Correct answer:', w)
        flag = False
    elif '_' not in answer:
        print('Your word:')
        print(''.join(answer))
        print('')
        print('Lives:', lives)
        print('')
        print('CONGRATULATIONS!')
        flag = False
    else:
        print('Your word:')
        print(''.join(answer))
        print('')
        print('Lives:', lives)
        print('Used letters:', ' '.join(used))
