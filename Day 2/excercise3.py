marks = input("Enter a marks :")
marks = int(marks)

# option1
if 85 <= marks <= 100:
    print(" Grade is A")
elif 75 <= marks < 85:
    print(" Grade is B")
elif 65 <= marks < 75: 
    print(" Grade is C")
elif 50 <= marks < 65:
    print(" Grade is D")
elif 0 <= marks < 50:
    print(" Grade is F")
else :
    print("Invalid marks")



#Option2
if marks <0 or marks>100 :
    print("out of range")
elif marks >= 85 :
    print("A")
elif marks >= 75 :
    print("B")
elif marks >= 65 :
    print("C")
elif marks >= 50 :
    print("D")
else :
    print("F")

