def arbitraty_keyword_arguments(**kwargs):
    print(kwargs,type(kwargs))
print(arbitraty_keyword_arguments(name="nadee",age = 23,city="matara"))



#  excersize 1

def arbitraty_keyword_argument(**kwargs):
 print(kwargs,type(kwargs))
 for key,value in kwargs.items():
    print("key=",key,"value=",value)
print(arbitraty_keyword_argument(name="nadee",age = 23,city="matara"))