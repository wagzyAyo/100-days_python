def add(*args):
    for x in args:
        return sum(args)


# print(add(2, 3, 4, 5, 6))


class Car:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.color = kwargs.get("color")
        self.model = kwargs.get("model")


my_car = Car(model="Gt-3", name="Nissan")
print(my_car.model, my_car.name)
