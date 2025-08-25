import json, os

#creats JSON File
#Incial Data
pokemons = [
    {
        'Name': {'english': 'Pikachu'},
        'Type': ['Electric'],
        'base': {
            'HP': '35', 'Attack': '55', 'Defense': '40', 'Sp. Attack': '50',
            'Sp.Defense': '50', 'Speed': '90'
        }
    },
    {
        'Name': {'english': 'Charmander'},
        'Type': ['Fire'],
        'base':{
            'HP': '39', 'Attack': '52', 'Defense': '43',
            'Sp. Attack': '60', 'Speed': '65'
        }
    },   

]

base_dir= os.path.dirname(os.path.abspath(__file__))
file_path= os.path.join(base_dir, 'pokemons.json')

# Read the existing JSON File
try:
    with open(file_path, 'r', encoding= 'utf-8') as file:
        pokemons = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    pokemons = [
    {
        'Name': {'english': 'Pikachu'},
        'Type': ['Electric'],
        'base': {
            'HP': '35', 'Attack': '55', 'Defense': '40', 'Sp. Attack': '50',
            'Sp.Defense': '50', 'Speed': '90'
        }
    },
    {
        'Name': {'english': 'Charmander'},
        'Type': ['Fire'],
        'base':{
            'HP': '39', 'Attack': '52', 'Defense': '43',
            'Sp. Attack': '60', 'Speed': '65'
        }
    },   

]


print('Current Pokemons List:', pokemons)

#ask the user to add a new pokemon
name= input('Enter the New Pokemon Name: ').strip()
poke_type= input('Enter the Pokemon Type: ').strip()
poke_hp= int(input('Enter the Pokemon HP: ').strip())
poke_attack= int(input('Enter the Pokemon Attack: ').strip())
poke_defense= int(input('Enter the Pokemon Defense: ').strip())
poke_sp_attack= int(input('Enter the Pokemon Sp.Attack: ').strip())
poke_sp_defense= int(input('Enter the Pokemon Sp.Defense: ').strip())
poke_speed= int(input('Enter the Pokemon Speed: ').strip())
new= {
    'Name': {'english': name},
    'Type': [poke_type], 
    'Base': {
        'HP': poke_hp,
        'Attack': poke_attack,
        'Defense': poke_defense, 
        'Sp.Attack': poke_sp_attack,
        'Sp.Defense': poke_sp_defense,
        'Speed': poke_speed
            }
    }        

pokemons.append(new)

#save the update
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(pokemons, file, indent=4)

print(f'{name} added and saved in {file_path}')