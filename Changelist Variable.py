animals = ['Monkey', 'Snake', 'Shark']


def favorite_animal():
    for i in range(len(animals)):
        if animals[i] == ('Shark'):
            animals[i] = 'Cat'


favorite_animal()
print('Now favorite animals are:', ', ' .join(animals))