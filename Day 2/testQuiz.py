my_list=[8,10,12,9,11,15,16,4]
print(my_list[1:3])   
print(my_list[1:6])
print(my_list[1:6:2])

# [10, 12]
# [10, 12, 9, 11, 15]
# [10, 9, 15]


# merging dict

d_1 = {'a':1}
d_2 = {'b':2}

d_3 =d_1 | d_2
print(d_3)
print(len(d_3))

# {'a': 1, 'b': 2}
# 2