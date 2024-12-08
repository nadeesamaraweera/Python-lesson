class Animal:
    def __init__(self):
        self.data = "some data"

    def _make_sound(self):
        print("make animal sound")

class Dog(Animal) :
    def bark(self):
        
        self._make_sound()
        print("barking")