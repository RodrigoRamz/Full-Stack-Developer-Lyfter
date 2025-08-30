numbers = []
for i in range (10):
    number = int( input(f'Add Number {i +1}: '))
    numbers.append(number)

highest = numbers [0]
for num in numbers:
    if num > highest:
        highest = num
print(highest, 'is the highest number from the list')