# Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()  # Automatically decorated
print()


# Decorator with parameter
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")
print()


# Multiple Decorator
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One: Before the function call")
        func(*args, **kwargs)
        print("Decorator One: After the function call")

    return wrapper


def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two: Before the function call")
        func(*args, **kwargs)
        print("Decorator Two: After the function call")

    return wrapper


@decorator_one
@decorator_two
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")
