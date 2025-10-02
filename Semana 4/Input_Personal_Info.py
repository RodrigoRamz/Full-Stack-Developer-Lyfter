name = input('Add your name ')
last_name = input ('Add your last name ')
age = int (input ('Add your age '))
concatenate_string = (f' Your Name is ' + name + ' ' + last_name + ' ' + 'Your age is ' + str(age))
print (concatenate_string)
if (age <= 2):
    print ('You are a Baby')
elif (age <= 5):
    print ('You are a child')
elif (age <= 10):
    print ('You are a preadolescent')
elif (age <= 18):
    print ('You are a Teenager')
elif (age <= 25):
    print ('You are an Adult')
elif (age <= 65):
    print ('You are a Senior')