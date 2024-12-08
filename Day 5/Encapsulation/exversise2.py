# write a python program to create a class QuadraticEqueation that repre  of the form ax^2+bx+c=0
#   the class should have,
    
#     1.attributes : private attributes __a,__b and __c to store the quavision of the  QuadraticEqueation
#     2.methods : a constructor to initilize the quavision a,b and c.
#                 A prive method __discriminant() that calculated and return the _discrimminate (D=b^2-4ac)
#                 a public method find_roots() that,
#                            use the private discrimminat method
#                            returns the roots of the quediton equvension. D>0,D=0,D<0




class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def __discriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def find_roots(self):

        D = self.__discriminant()
        if D > 0:
            root_1= (-self.__b + D **0.5)/(2*self.__a)
            root_2= (-self.__b - D **0.5)/(2*self.__a)
            message = "roots are:" + root_1 + "" + root_2
            return message
        elif D== 0:
            root_1 = (-self.__b)/(2*self.__a)
            print("Equsion has one root and it is :",root_1)

        else :
            print("Equation has complex roots")

equation_1 = QuadraticEquation(1,-5,6)
equation_1.find_roots()
            






    