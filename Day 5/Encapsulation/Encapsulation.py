class MyClass :
    def __init__(self):
      self.var_1 ="Some Value"    
      self._var_2 ="protected attribute" #protected
      self.__var_3 = "private attribute" #private

my_obj=MyClass()

print(my_obj.var_1)
print(my_obj._var_2)
print(my_obj.__var_3)