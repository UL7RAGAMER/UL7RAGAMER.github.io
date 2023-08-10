import Data



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
    {'name': 'Dragon', 'parts': ['scales', 'wings']},
    {'name': 'Unicorn', 'parts': ['horn', 'mane', 'hooves']},
    {'name': 'Griffin', 'parts': ['eagle wings', 'beak']},
    {'name': 'Kraken', 'parts': ['tentacles', 'beak']},
    {'name': 'Minotaur', 'parts': ['bull head', 'hooves']},
    {'name': 'Cyclops', 'parts': ['sheepskin clothing']},
    {'name': 'Mermaid', 'parts': ['fish tail']},
    {'name': 'Chimera', 'parts': ['lion head']},
    {'name': 'Werewolf', 'parts': ['Wolf fur']},
    {'name': 'Vampire', 'parts': ['fangs']},
]


def Adventurer():
    print(f'You are now an Adventurer \nThese are the creatures u can find:')    
    for creature in mythical_creatures_drops:
        print(f"{creature['name']}")

   

Adventurer()