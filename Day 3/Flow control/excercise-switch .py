length =[4,3,7]
match length :
    case[ ]:  
        print("Empty")
    case [x]:  
        print("Has One Element")
    case [x,y]:  
        print("Has One Element")
    case _:
        print("Somthing Else")