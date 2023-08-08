print('Welcome to job simulater')
import random
jobs = ['Hunter'] * 20 + ['Chef'] * 30 + ['Painter'] * 50

job = random.choice(jobs)
if job == 'Chef':
    print(f'You are no a {job} ')

if job == 'Hunter':
    print(f'You are no a {job}')


if job == 'Painter':
    print(f'You are no a {job}')    
 
coin = 10000

vegetables = ['Tomato', 'Onion', 'Lettuce', 'Carrot', 'Peas']
meat = ['Pork', 'Chicken', 'Fish', 'Lamb']

    
    
def globals_Chef():
       
    print('There are 3 dishes \n ' ,' 1: Fish and  Chips \n', '2: Lasagna \n', '3: Ramen' )
    
    dishes = ['Ramen'] * 10 + ['Lasagna'] * 30 + ['Fish and Chips'] * 60
    
    dish = random.choice(dishes)
    
    if dish == 'Fish and Chips':
        print(f'You have to make {dish} \n', 'It costs 700')
        
        Fish = []
        
        for i in range(1,4):
            i = random.choice(meat)
            Fish.append(i)
        for i in Fish:
            if i == 'Fish':
                i = i
            else:
                Fish.remove(i)
                Fish.append('Fish')
                break
        print(Fish)      
                    
            
    
    if dish == 'Lasagna':
        print(f'You have to make {dish} \n', 'It costs 1500')
        
        Tom = []
        for i in range(1,4):
            i = random.choice(vegetables)
            Tom.append(i)
        for i in Tom:
            if i == 'Tomato':
                i = i
            else:
                Tom.remove(i)
                Tom.append('Tomato')
                break
        print(Tom)                
        Bef = []        
        for i in range(1,4):
            i = random.choice(meat)
            Bef.append(i)
        for i in Bef:
            if i == 'Beef':
                i = i
            else:
                Bef.remove(i)
                Bef.append('Beef')
                break   
            
    if dish == 'Ramen':
        print(f'You have to make {dish} \n', 'It costs 3000')
        Pork = []
        for i in range(1,4):
            i = random.choice(meat)
            Pork.append(i)
        for i in Pork:
            if i == 'Pork':
                i = i
            else:
                Pork.remove(i)
                Pork.append('Beef')
                break        
        print(Pork)
globals_Chef()    