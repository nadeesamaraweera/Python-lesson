class MyClass:

    def __init__(self) :
        self.__data = "some data"

    def get_value(self) :
        print(self.__data)

    
    def set_value(self,new_value) :
        self.__data = new_value

my_obj = MyClass()
my_obj.get_value()
my_obj.set_value('Maya')
my_obj.get_value()