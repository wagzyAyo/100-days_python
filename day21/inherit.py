class Animal:
    def __init__(self):
        pass

    def breathe(self):
        print("Inhale, Exhale.")

    def eyes(self):
        print("Has 2 eyes")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this under the water")

    def swim(self):
        print("Fish is swiming")


nemo = Fish()

nemo.breathe()
nemo.eyes()
nemo.swim()
