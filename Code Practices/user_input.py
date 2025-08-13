user_input = input('Enter your text: ') # Prompt the user for a string input

with open('/Users/rhoderamirez/Code Practices/new_line.txt', 'a') as file: # Open, create and write a file without deleting the existing content
    file.write(user_input + '\n') #add the string input in a new line