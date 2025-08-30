def letters(text):
    upper_count = 0
    lower_count = 0
    for c in text:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
    print(f'{lower_count} are lower cases and {upper_count} are upper cases')

letters ('I love Nacion Sushi')