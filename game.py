print('Welcome to U7 world')
import gam
import Gambling
end_game = False
print('Commands are\n- Gamble\n- Job\n- Stop')

while end_game == False:
    cm = input(f'You have {Gambling.coins} coins \nYou want to Gamble or Job \n')
    if cm == 'Gamble':
        Gambling.gamble()
    if cm == 'Job':
        gam.globals_Chef()
    if cm == 'Stop':
        end_game = True