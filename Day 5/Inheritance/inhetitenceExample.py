class Animal : #super /parent
    def __init__(self,name):
       self.name = name

class Dog (Animal) :
    def __init__(self, name,color):
       super().__init__(name)
       self.color =color

dog_1 =Dog("Roxy","Red")
print(dog_1.name,dog_1.color)