def sorted_words(text):
    words = text.split('-')
    words = sorted(words)
    return '-'.join(words)

result = sorted_words('python-variable-funcion-computadora-monitor')
print(result)