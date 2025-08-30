first_number = int(input('Add the first number: '))
second_number = int(input('Add the second number: '))
third_number = int(input('Add the third number: '))
if first_number >= second_number and first_number > third_number:
    highest = first_number
elif second_number >= first_number and second_number > third_number:
    highest = second_number
else:
    highest = third_number  
print (f' The highest number is ' + str (highest))