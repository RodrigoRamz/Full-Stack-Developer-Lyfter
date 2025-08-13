# This is the adding function
def add (first_number, second_number): # first_number will be the fist int input, second_number will be the second int input
    return first_number + second_number


# This is the subtraction function
def subtract (first_number, second_number):
    return first_number - second_number


# This is the multiplication function
def multiply (first_number, second_number):
    return first_number * second_number


# This is the division function
def divide (first_number, second_number):
        return first_number / second_number


# This is the exception "ValueError" when the user did not add a valid number
def ask_num1(message): 
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Please enter a valid number')


# This is the function that makes the calculation to process the mathematical operation
def ask_operation():
    while True:
        operation = input('Enter the operation using the correspondent sign (+, -, *, /): ')
        if operation in ['+', '-', '*', '/']:
            return operation
        else: 
            print ('Enter a valid operation: +, -, *, /')


# This is the function to show a Error by diving by cero
def ask_num2 (operation):
    while True:
        num2 = ask_num1('Enter a number: ')
        if operation == '/' and num2 == 0:
            print('You cannot divide by 0')
        else:
            return num2
        

# This is the function that execute the main program calculator       
def main():
    print('Calculator')
    num1 = ask_num1('Enter a number: ')

    while True:
        operation = ask_operation()
        num2 = ask_num2(operation)

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = 'Invalid Operation'

        print(f'Result: {result}')

        while True:
            next_step = input('\nWhat do you want to do next:\n a - another operation with result\n c - clear and start over\n q - quit\n').lower()
            if next_step == 'a':
                num1 = result
                print(f'Previous result is: {result}')
                break # This take the result as num1 to perform another operation
            elif next_step == 'c':
                num1 = ask_num1('Enter a number: ')
                break # This clean and start the program asking for num1, the first number to be added in the calculator
            elif next_step not in ['a', 'c', 'q']:
                print('Invalid Choice. Please enter a valid option')
            elif next_step == 'q': # This is the step to finish the program
                print('Calculator turned off')
                exit()
            

# This function executes the entire program
main()