# Step 1 open the file and read the lines
with open('/Users/rhoderamirez/Code Practices/Data1.txt', 'r') as file:
    data1 = file.readlines()

# Step 2 remove the enter using ' '.join to a single string separated by spaces
final_sentence = ' '.join([line.strip() for line in data1])

# Step 3 This is another valid option using 'output' as the variable name for the new file
with open('/Users/rhoderamirez/Code Practices/data3.txt', 'w') as output:
    output.write(final_sentence)