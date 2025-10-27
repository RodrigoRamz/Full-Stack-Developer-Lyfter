def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"This param '{arg}' is not a number.")
        for kwarg in kwargs.values():
            if not isinstance(kwarg, (int, float)):
                raise TypeError(f"This param '{kwarg}' is not a number.")
        return func(*args, **kwargs)
    return wrapper

@validate_numbers
def multiply(a, b):
    return a * b

print(multiply(5, 2))
print(multiply(3.5, 2))
print(multiply("T", 2))