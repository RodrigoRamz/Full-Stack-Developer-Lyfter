# Step 1 open the file and read the lines
with open('/Users/rhoderamirez/Code Practices/Data1.txt', 'r') as file:
    data1 = file.readlines()

# Step 2 remove the enter using ' '.join to a single string separated by spaces
final_sentence = ' '.join([line.strip() for line in data1])

# Step 3 create the new file in a single line string
with open('/Users/rhoderamirez/Code Practices/data3.txt', 'w') as data3:
    data3.write(final_sentence)