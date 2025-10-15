def log_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Received Params: {args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Returned value: {result}")
        return result
    
@log_params_and_return
def suma(a, b):
    return a + b

suma(5, 3)