import sys
import random
import hangman_art
import hangman_words
import Data

def hangman():
    end_game = False
    print(f'It will cost {5/100 * Data.coins} coins but if u win can Double it')
    ch = input('Do you want to continue \n')
    if ch == 'no':
        end_game = True

    while end_game == False:
        Data.coins -= (5/100 * Data.coins)
        ans = ""

        word = random.choice(hangman_words.word_list)
        blanks = []
        t = []

        for i in word:
            blanks.append('_')

        for x in word:
            t.append(x)

        lives = 6
        while ans != word and end_game == False:

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
                end_game = True
                

            for i in blanks:
                ans += i
            print(blanks, '\n')

            if ans==word:
                print('You Win!')
                Data.coins = (5/100 * Data.coins * 2) + Data.coins 
                print(f'You have {Data.coins}')
                end_game = True