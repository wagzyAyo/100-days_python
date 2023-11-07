# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        func = function.__name__
        print("You called {}".format(func))
        result = function(args[0], args[1], args[2])
        print(f"The result is {result}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def the_func(a, b, c):
    return a*b*c


the_func(2, 3, 4)
