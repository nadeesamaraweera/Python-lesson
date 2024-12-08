class Animal : #super /parent
    def __init__(self,name):
       self.name = name

    def speak(self):
       pass

class Dog (Animal) :
    def speak(self):
      print(self.name,"says woof")

dog_1 =Dog("Roxy")
print(dog_1.name)