import random
guessed = False
secret_number = random.randint(1, 10)
while not guessed:
    attempt = int (input('Try a Number from 1 to 10: '))
    if attempt == secret_number:
        print ('You Win! You Have guessed the secret number')
        guessed = True
    else:
        print ('Try Again')