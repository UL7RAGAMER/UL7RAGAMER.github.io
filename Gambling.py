coins = 10000
num = [1,2,3,4,5,6,7,8,9,10]
import random
import sys
def gamble():
    
    global end_game
    global coins
    print(f'You have {coins}')
    bet = int(input('Enter bet amount \n'))
    
    while bet == 0 :    
        print('Make bet more than 0')
        bet = int(input('Enter bet amount \n'))
    
    cm = input('Type pull to pull a card \n')
    
    if cm == 'pull':
        user = random.choice(num)
        
        comp = random.choice(num)
        
        print(f'You got {user} and the computer got {comp}')
        
        
    if user > comp:
        print('You win u doubled ur money')
        coins -= bet
        coins = (2 * bet) + coins
    
    if comp > user:
        print('You Lost u lose ur money')
        coins -= bet
    if comp == user:
        print('It is a tie!')
        
    if coins == 0:
        sys.exit('You have 0 coins U LOSE L bozo')
    
        
    ch = input('Type yes to continue or no to stop \n')  
    
    if ch == 'no':
        end_game = True

    
    
    

