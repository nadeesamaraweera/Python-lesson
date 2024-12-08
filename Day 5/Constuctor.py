class Car :
    category = "motor bicycle"

    def __init__(self,name):
       self.name = name

new_car = Car("Audi")
print(new_car.name)