animal = 'Shark'


def favorite_animal():
    global animal
    if animal == 'Shark':
        animal = 'Cat'


favorite_animal()
print('Now favorite animal is a', animal)