# Step 1 read the input file
with open('/Users/rhoderamirez/Code Practices/entrada.txt', 'r') as file:
    lines = file.readlines()

# Step 2 create a new list in uppercase
uppercase_lines = [line.upper() for line in lines]

# Step 3 create the output file for the uppercase_lines list
with open('/Users/rhoderamirez/Code Practices/uppercase_lines.txt', 'w') as output_file:
    output_file.writelines(uppercase_lines)
