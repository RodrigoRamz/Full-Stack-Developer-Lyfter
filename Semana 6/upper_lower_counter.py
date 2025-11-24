def letters(text):
    upper_count = 0
    lower_count = 0
    for c in text:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
    return lower_count, upper_count

if __name__ == "__main__":
    lower, upper = letters("I love Nation Sushi")
    print(f'{lower} are lower cases and {upper} are upper cases')

