class Car :
    category = "motor bicycle"

    def __init__(self,name):
       self.name = name

    def display(self):
        print("name:",self.name)

    def update(self,new_value):
        self.name = new_value

new_car =Car("Audi")
print(new_car.display())

new_car.update("Ferrary")
print(new_car.display())
   