def only_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"The '{arg}' parameter is incorrect. Add a number. ")
        return func(*args, **kwargs)
    return wrapper

@only_numbers
def multiply(a, b):
    return a * b

print(multiply(4, 2))
print(multiply(4, "two"))
