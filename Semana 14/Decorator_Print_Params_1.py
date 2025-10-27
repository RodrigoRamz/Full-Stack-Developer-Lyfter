def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def log_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Received Params: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned Value: {result}")
        return result
    return wrapper

@log_params_and_return
def add(a, b):
    return a + b

add(5, 3)
