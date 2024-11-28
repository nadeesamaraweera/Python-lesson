add = lambda x,y : x+y
print(add(3,4)) #7

add =(lambda x,y: x+y)(5,3)
print(add) #8


# example 2

def my_func(n):
    return lambda a: a*n
my_doubler = my_func(2)
print(my_doubler(5)) #10