class MyClass:
    def __init__(self):
        self.__data = "some data"  

    def __check_my_values(self):  
        print("checking numbers")  

    def get_check_method(self):  
        self.__check_my_values() 

obj = MyClass()

obj.get_check_method()