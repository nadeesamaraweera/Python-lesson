# # ------abs() :-----------

print(abs(-20))  # 20
print(abs(20))   # 20

# # ------map() :-----------

def cal_square(x):
  return (x*x)
my_list =[5,8,9,1,3]
result = map(cal_square,my_list)
print(result,type(result)) #<map object at 0x0000020833ABBC40> <class 'map'>
print(list(result)) #[25, 64, 81, 1, 9]


# ------filter() :-----------

my_list1=[5,8,10,9,6,3]
def check_even(x):
  
  return x% 2 ==0
result=filter(check_even,my_list1)
print(result,type(result)) #<filter object at 0x0000024112D7BB80> <class 'filter'>
print(list(result)) #[8, 10, 6]
