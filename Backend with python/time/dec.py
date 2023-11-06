import time


def decorate_func(function):

    def delay_func():
        time.sleep(2)
        function()
        time.sleep(2)
        function()
    return delay_func


@decorate_func
def say_hello():
    print("Hello")


@decorate_func
def say_bye():
    print("Bye for now!")


say_hello()
say_bye()
