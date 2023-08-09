import random
import sys
import Data
print(Data.Logo)
def globals_gamble():
    
    print(f'You have {Data.coins}')
    bet = int(input('Enter bet amount \n'))
    
    while bet == 0 :    
        print('Make bet more than 0')
        bet = int(input('Enter bet amount \n'))
    
    cm = input('Press any key to pull \n')
    
    user = random.choice(Data.num)
    
    comp = random.choice(Data.num)
    
    print(f'You got {user}and the computer got {comp}')
    
        
    if user > comp:
        print('You win u doubled ur money')
        Data.coins -= bet
        Data.coins = (2 * bet) + Data.coins
    
    if comp > user:
        print('You Lost u lose ur money')
        Data.coins -= bet
    if comp == user:
        print('It is a tie!')
        
    if Data.coins == 0:
        sys.exit('You have 0 Data.coins U LOSE L bozo')
    

    
    
    

