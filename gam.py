import random
import Gambling
jobs = ['Hunter'] * 20 + ['Chef'] * 30 + ['Painter'] * 50
vegetables = ['Tomato', 'Onion', 'Lettuce', 'Carrot', 'Peas']
meat = ['Pork', 'Chicken', 'Fish', 'Lamb']
from itertools import permutations

    

def globals_Chef():
    
    print('There are 3 dishes \n','1: Fish and  Chips \n', '2: Lasagna \n', '3: Ramen' )
# CHANGE THE CHANCES   
    dishes = ['Ramen'] * 1 + ['Lasagna'] * 1 + ['Fish and Chips'] * 1

    dish = random.choice(dishes)
    if dish == 'Fish and Chips':

        print(f'You have to make {dish} \n', 'It costs 700')
        Gambling.coins -= 700
        fish = ['Fish']
        perm = permutations(['Pork', 'Chicken', 'Lamb'],2)
        x = random.randint(1,6)
         
        count = 1
        for i in list(perm):            
            if count == x:
                for n in i:
                    pz = random.randint(0,2)
                    fish.insert(pz,n)
                    
            count += 1
            
        
        
        print(fish) 
        ch = input("Select the correct ingredient \n")
        if ch == 'Fish':
            profit = (700 * 1/10 ) + 700
            print(f'Great job u earnt {profit} coins')
            Gambling.coins += profit
        else:
            chance = 0 
            while chance < 1:
                ch = input("Try again \n")
                if ch == 'Fish':
                    profit = (700 * 1/20 ) + 700
                    print(f'Great job u earnt {profit}')
                    Gambling.coins+=profit
                else:
                    print('You lost 700 coins')
                    Gambling.coins -= 700
                chance = 1
                    
            
    
    if dish == 'Lasagna':
        print(f'You have to make {dish} \n', 'It costs 1500')
        Gambling.coins -= 1500
        
        Tom = ['Tomato']
        perm = permutations(['Onion', 'Lettuce', 'Carrot', 'Peas'],2)
        x = random.randint(1,12)
        count = 1
        for i in list(perm):            
            if count == x:
                for n in i:
                    pz = random.randint(0,2)
                    Tom.insert(pz,n)
                    
            count += 1
        print(Tom)
        ch = input("Select the correct ingredient \n")
        if ch == 'Tomato':
            profit = (1500 * 1/10 )          
        else:
            chance = 0 
            while chance < 1:
                ch = input("Try again \n")
                if ch == 'Tomato':
                    profit = (1500 * 1/20 ) 
                else:
                    print('You lose 300')
                    Gambling.coins -= 300   
                chance = 1
                    
        Bef = ['Beef']        
        perm = permutations(['Pork', 'Chicken', 'Lamb'],2)
        x = random.randint(1,6)         
        count = 1
        for i in list(perm):            
            if count == x:
                for n in i:
                    pz = random.randint(0,2)
                    Bef.insert(pz,n)
                    
            count += 1 
        print(Bef)
        ch = input("Select the correct ingredient")
        if ch == 'Beef':
            profit2 = (1500 * 1/10 ) + profit + 1500
            print(f'Great job u earnt {profit2}')
        else:
            chance = 0 
            while chance < 1:
                ch = input("Try again /n")
                if ch == 'Beef':
                    profit2 = (1500 * 1/50 ) + profit + 1500
                    print(f'Great job u earnt {profit2}')
                    Gambling.coins+=profit2
                else:
                    print('You lost 1200 coins')
                    Gambling.coins -= 1200       
                chance = 1
                    
    if dish == 'Ramen':
        print(f'You have to make {dish} \n', 'It costs 3000')
        Gambling.coins -= 3000
        Pork = ['Pork']
        perm = permutations(['Beef', 'Chicken', 'Lamb'],2)
        x = random.randint(1,6)         
        count = 1
        for i in list(perm):            
            if count == x:
                for n in i:
                    pz = random.randint(0,2)
                    Pork.insert(pz,n)                    
            count += 1       
        
        print(Pork)
        ch = input("Select the correct ingredient  \n")
        if ch == 'Pork':
            profit = (3000 * 1/10 ) 
            
        else:
            chance = 0 
            while chance < 1:
                ch = input("Try again \n")
                if ch == 'Pork':
                    profit = (3000 * 1/50 ) 
                chance = 1
                            

        Carrot=['Carrot']
        perm = permutations(['Tomato', 'Onion', 'Lettuce', 'Peas'],2)
        x = random.randint(1,12)
        count = 1
        for i in list(perm):            
            if count == x:
                for n in i:
                    pz = random.randint(0,2)
                    Carrot.insert(pz,n)
            count += 1        
        print(Carrot)
        ch = input("Select the correct ingredient \n")
        if ch == 'Carrot':
            profit2 = (3000 * 1/10 ) + 3000 + profit
            print(f'Great job u earnt {profit2}')
        else:
            chance = 0 
            while chance < 1:
                ch = input("Try again \n")
                if ch == 'Carrot':
                    profit2 = (3000 * 1/100 ) + 3000 + profit
                    print(f'Great job u earnt {profit2}')
                    Gambling.coins += profit2
                else:                    
                    print('You lost 1500 coins')
                    Gambling.coins -= 3000 
                chance = 1
                        
    print(Gambling.coins)                      
globals_Chef()