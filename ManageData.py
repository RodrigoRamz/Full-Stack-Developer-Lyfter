# Step 1: Open the file and read the lines
with open('/Users/rhoderamirez/Downloads/Songs.txt', 'r') as file:
    songs = file.readlines ()

# Step 2: Delete enter and order alphabetically 
songs = [song.strip() for song in songs]
songs.sort()

# Step 3: Save "songs" in the new ordered file
with open('/Users/rhoderamirez/Downloads/ordered_songs.txt', 'w') as ordered_file:
    for song in songs:
        ordered_file.write(song + '\n')