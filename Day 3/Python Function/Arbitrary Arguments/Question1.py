# 1.write a python function called "summarize_grades"  that accept a student's names as a  mandetory arguments  and anArbitraty grade scores. The function should,

# *print the student's names.
# * Calculate and print the higher grades,lowerst grades and the average grades from the provided scores.
# *if no grades are provided you should print no grades availble


# def summarize_grades(*args):
#     if len(args) ==0:
#         return "No Grades Available"
#     sumGrade = 0
#     for grade in args:
#         sumGrade += grade
#     average = sumGrade / len(args)
#     print("Average is: ", average)
#     maxGrade = max(args)
#     print("Highest Grade is: ", maxGrade)
#     minGrade = min(args)
#     print("Lowest Grade is: ", minGrade)
    
# name = input("Enter your name: ")
# print("Hello ", name)   
# print(summarize_grades(90,89,30,24,35,45,67))



def calculate_Grades(name, *args):
    print("Hello ", name)
    if not args:
        print("No Grades Available")
    else:
        print("Average is: ", sum(args) / len(args))
        print("Highest Grade is: ", max(args))
        print("Lowest Grade is: ", min(args))
      
print(calculate_Grades("nadee",10,32,11,23,65,75,32))