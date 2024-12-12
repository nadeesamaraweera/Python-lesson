#nested function
def outer (x):
    def inner(y):
        return x+y
    return inner

temp_var = outer(5)
print(temp_var(7))