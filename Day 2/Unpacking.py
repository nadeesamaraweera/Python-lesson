# #----- List-----------

# my_list =[10,12,7]
# x,y,z =my_list
# print(x,y,z)

# # 10 12 7


# #----- Tuple------------

# my_tuple =[22,42,17]
# x,y,z =my_tuple
# print(x,y,z)

# 22 42 17

#----- Dictionary----------

person ={
    "name" :"nadeesha",
    "age"  : 24,
    "gender" : "Female"

}
for key,value in person.items() :
  print(key,value)

# name nadeesha
# age 24
# gender Female

for key in person.keys() :
  print(key)
 
# name
# age
# gender

for value in person.values() :
  print(value)

# nadeesha
# 24
# Female
