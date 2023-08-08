
#Step 1
import sys
import random
import hangman_art
import hangman_words
import os
os.system("pip install sys")
os.system("pip install random")
print(hangman_art.logo)
ans = ""

word = random.choice(hangman_words.word_list)
blanks = []
t = []

for i in word:
    blanks.append('_')

for x in word:
    t.append(x)

lives = 6
while ans != word:

    ans = ""
    l = input('Enter a letter: \n')

    l = l.lower()
    if l in blanks:
        print('Letter already guessed \nTry again')
    n = 0

    if l in t:
        for i in word:
            if i == l:
                blanks.pop(n)
                blanks.insert(n, l)
                n += 1
            else:
                n += 1

    else:
        print('You lose a life')
        print(hangman_art.stages[lives])
        lives -= 1

    if lives == -1:
        print(f"You lose the word was {word}")
        sys.exit()

    for i in blanks:
        ans += i
    print(blanks, '\n')

print('You Win!')
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#Step 1
import sys
import random
import hangman_art
import hangman_words
import os
os.system("pip install sys")
os.system("pip install random")
print(hangman_art.logo)
ans = ""

word = random.choice(hangman_words.word_list)
blanks = []
t = []

for i in word:
    blanks.append('_')

for x in word:
    t.append(x)

lives = 6
while ans != word:

    ans = ""
    l = input('Enter a letter: \n')

    l = l.lower()
    if l in blanks:
        print('Letter already guessed \nTry again')
    n = 0

    if l in t:
        for i in word:
            if i == l:
                blanks.pop(n)
                blanks.insert(n, l)
                n += 1
            else:
                n += 1

    else:
        print('You lose a life')
        print(hangman_art.stages[lives])
        lives -= 1

    if lives == -1:
        print(f"You lose the word was {word}")
        sys.exit()

    for i in blanks:
        ans += i
    print(blanks, '\n')

print('You Win!')
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
