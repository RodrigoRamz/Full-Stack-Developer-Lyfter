def ask_video_games():
    Name = input('Video Game Name: ')
    Type = input('Type: ')
    Developer = input ('Developer: ')
    Classification = input ('Classification ESBR: ')

    return {
        'Name': Name,
        'Type': Type,
        'Developer': Developer,
        'Classification': Classification 
    }

games = [] #This is the empty list to save and store all the video games

number_video_games = int(input('Add number of video games to be added: ')) # Ask the user how many video games will be added to the list

for i in range(number_video_games): # This bucle is repeated n times 
    print(f'\n- Video Game #{i+1} -')
    game = ask_video_games() # this is the function call
    games.append(game) # add the dictionary to the game's list

print('\nAll Video Games: ')
print(games)

import csv
import os

# after add games

# here is where the script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path= os.path.join(script_dir, 'Videogames.csv')

# save as CSV (separated by commas)
with open(csv_path, 'w', encoding= 'utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Type', 'Developer', 'Classification'])
    writer.writeheader()
    writer.writerows(games)

# save as TSV (separated by tabs)
tsv_path = os.path.join(script_dir, 'Videogames.tsv')

with open(tsv_path, 'w', encoding= 'utf-8', newline='') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['Name', 'Type', 'Developer', 'Classification'],
        delimiter='\t'
    )
    writer.writeheader()
    writer.writerows(games)

print(f' TSV File created in: {tsv_path}')