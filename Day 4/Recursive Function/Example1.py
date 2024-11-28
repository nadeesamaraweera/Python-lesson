# 1. Calculate the sum of all the elements in an or list

my_list = [2,4,6,8,10]

def sum_elements(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum_elements(n[1:]) 
    
print(sum_elements(my_list))