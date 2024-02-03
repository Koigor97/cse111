import time
from time import time as t

# Decorator
def my_decorator(func):
    def wrap_func(name):
        print("**********")
        time.sleep(3)
        func(name)
    return wrap_func

@my_decorator
def say_hello(name):
    print(f"Hellooooo....my name is {name}")

# say_hello(name="Samuel Turay")

# custom decorator
def performance(fn):
    def wrapper(*args, **kwargs):
        time_start = t()
        result = fn(*args, **kwargs)
        time_end = t()

        print(f"It took {round(time_end - time_start, 2)} s to run this function")
        return result
    return wrapper


@performance
def execute_speed():
    for i in range (100000000):
        i * 5

execute_speed()