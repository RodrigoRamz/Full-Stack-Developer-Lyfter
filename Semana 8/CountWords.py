# Step 1 read the file with the words to be counted
with open('/Users/rhoderamirez/Code Practices/words.txt', 'r') as file:
    content = file.read() # Read the file as single string

# Step 2 split the content to individual words
words_content = content.split()

# Step 3 filter by boolean method if true it is excluded
filtered_words = [word for word in words_content if not word.isdigit()]

# Step 4 Count only words as elements
word_count = len(filtered_words) 

# Step 5 Prints the result
print('This file contains', word_count, 'words')