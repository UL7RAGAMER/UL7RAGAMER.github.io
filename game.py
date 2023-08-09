import Chef
import Gambling
import Data
import Hangman
print(Data.Logo)
end_game = False
print('Commands are\n- Gamble\n- Job\n- Stop\n- Hangman\n- Placeholder\n')

while end_game == False:
    cm = input(f'You have {Data.coins} coins \n \nEnter command \n')
    cm = cm.lower()
    if cm == 'gamble':
        Gambling.globals_gamble()
    if cm == 'job':
        Chef.globals_Chef()
    if cm == 'stop':
        end_game = True
    if cm == 'hangman':
        Hangman.hangman()        