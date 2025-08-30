my_string = 'Pizza con piña'
my_reverse_list = ''
for i in range (len(my_string) -1, -1, -1):
        my_reverse_list += my_string[i]
print(my_reverse_list)