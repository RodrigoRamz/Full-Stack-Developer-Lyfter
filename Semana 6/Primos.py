numbers = [1, 4, 6, 7, 13, 9, 67]
primos_list = []

def primos(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for n in numbers:
    if primos(n):
        primos_list.append(n)


print('Los numbers primos son:', primos_list)      