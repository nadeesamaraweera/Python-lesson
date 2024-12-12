# 1.create  a decorator check_positive that
#       checks if the input or a function is a positive number
#       if the input is not positive print a message "Input must be a positive numbers"
# 2.use this decorators on a function calculate_square_root that
#       Takes one number as inputs. 
#       Returns the square root of the input number.



import math

def check_positive(func):
    def inner(x):
        if x <= 0:
            return "Input must be-4 a positive number."
        else:
            return func(x)
    return inner
@check_positive        
def calculate_square_root(num):
    return int(math.sqrt(num))

num = int(input("Enter a number : "))

print(calculate_square_root(num))

       