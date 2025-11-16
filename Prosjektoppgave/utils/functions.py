# Functions fil for funksjoner som kan brukes som decorators


def log_decorator(func):
    def wrapper():
        print(f"Funksjonen {func.__name__} blir kalt.")
        result = func()
        print(f"Funksjonen {func.__name__} er ferdig.")
        return result
    return wrapper