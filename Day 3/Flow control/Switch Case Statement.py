#Example 1
response_code = 500

match response_code :
    case 200 :
        print("Ok")
    case 201 :
        print("Created")
    case 404 :
        print("404 Not Found")
    case 500 :
        print("Internal Server Error")
    case _ :
        print("Somthing Else")


#Example 2
numbers =[4,3,7]
match numbers :
    case[x,y]:  #element 2 k unoth meka wenwa
        print(x*y)
    case [x,y,z]:   # element 3 k unoth meka wenwa
        print(x+y+z)
    case _:
        print("the list does not contain 3 or 2 numbers")


