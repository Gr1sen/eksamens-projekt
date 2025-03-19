def debugDecorator(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper