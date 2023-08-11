import Data
import random
import time
mythical_creatures = [
    'Dragon'] * 1 + [
    'Unicorn'] * 5 + [
    'Griffin'] * 15 + [
    'Kraken'] * 10+ [
    'Minotaur'] * 14 + [
    'Cyclops'] * 15 + [
    'Mermaid'] * 7 + [
    'Chimera'] * 10 + [
    'Werewolf'] * 6 + [
    'Vampire'] * 17 
mythical_creatures_drops = [
    {'name': 'Dragon', 'parts': ['scales', 'wings'], 'hitpoints': 300},
    {'name': 'Unicorn', 'parts': ['horn', 'mane', 'hooves'], 'hitpoints': 150},
    {'name': 'Griffin', 'parts': ['eagle wings', 'beak'], 'hitpoints': 225},
    {'name': 'Kraken', 'parts': ['tentacles', 'beak'], 'hitpoints': 360},
    {'name': 'Minotaur', 'parts': ['bull head', 'hooves'], 'hitpoints': 240},
    {'name': 'Cyclops', 'parts': ['sheepskin clothing'], 'hitpoints': 270},
    {'name': 'Mermaid', 'parts': ['fish tail'], 'hitpoints': 120},
    {'name': 'Chimera', 'parts': ['lion head'], 'hitpoints': 330},
    {'name': 'Werewolf', 'parts': ['Wolf fur'], 'hitpoints': 210},
    {'name': 'Vampire', 'parts': ['fangs'], 'hitpoints': 180}
]

swords = [
    {'name': 'Frostbite', 'damage': 25},
    {'name': 'Blizzard', 'damage': 30},
    {'name': 'Venomfang', 'damage': 40},
    {'name': 'Sunflare', 'damage': 45},
    {'name': 'Runeblade', 'damage': 55},
    {'name': 'Shadowstrike', 'damage': 50},
    {'name': 'Voidreaper', 'damage': 65},
    {'name': 'Eclipse', 'damage': 65},
    {'name': 'Firestorm', 'damage': 70},
    {'name': 'Dawnbreaker', 'damage': 90},
    {'name': 'Excalibur', 'damage': 100},
    {'name': 'Thunderstrike', 'damage': 100},
    {'name': 'Soulrender', 'damage': 110}
]
def choose_random_sword():
    total_damage = sum(sword['damage'] for sword in swords)
    sword_probabilities = [(total_damage - sword['damage']) / total_damage for sword in swords]
    
    random_sword = random.choices(swords, weights=sword_probabilities, k=1)[0]['name']
    return random_sword

r_sword = choose_random_sword()
sword_data = next(item for item in swords if item['name'] == r_sword)


def Quest():
    creature_name = random.choice(mythical_creatures)
    creature_data = next(item for item in mythical_creatures_drops if item['name'] == creature_name)
    health = creature_data["hitpoints"] 
    print(f"You encountered a {creature_name}!")
    print(f"It drops the following parts: {', '.join(creature_data['parts'])}")
    print(f'It has {creature_data["hitpoints"]} hitpoints.')
    print(f'You deal {sword_data["damage"]} damage.')



    while health > 0:
        input('Press any key to strike it')
        health -= sword_data['damage']
        if health < 0:
            health = 0
        print(f"It has {health} hitpoints remaining.")
        print('Cooldown for 5 sec')
        for i in range(1,6):
            print(f'{i}')# Introduce cooldown after each strike
            time.sleep(1)
    print('Good job, you won!')
    input('Press Enter to exit')

def Adventurer():
    print("You are now an Adventurer.\nThese are the creatures you can find:")
    for creature in mythical_creatures_drops:
        print(creature['name'])
    
    input("Press Enter to start your quest")
    print('While exploring you found some thing')
    print(f"You've obtained the sword: {r_sword}")
    Quest()

Adventurer()