class MyClass :
    def __init__(self):
      self.var_1 ="Some Value"    
      self._var_2 ="protected attribute" #protected
      self.__var_3 = "private attribute" #private

    def _protected_method(self):
       print("protected method")  
    def __private_method(self):
       print("private method")  

my_obj=MyClass()

print(my_obj._protected_method)
print(my_obj.__private_method)
