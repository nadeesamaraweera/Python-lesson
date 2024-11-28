# write the python function called employee_info that accept the require "name" parameter and an arbitraty number of keyword arguments representing additional details about the employee.
# The function should,

# *print the employee names,
# *alterate keyword arguments and print each key-value faie in the format "<key>:<value>"

# modify the employee_info funtion to return the dictinary containing all the employee details (including name and the additional attributes passed were keyword arguments )


# def employee_info(name,**kwargs):
#     print("Employee Name: ", name)
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
    
#     print(kwargs)

# print(employee_info(name = "Employee1", age = 23, section = "Academic"))

def employee_info(name, **kwargs):
    print("Employee Name:", name)
    for key, value in kwargs.items():
        print(key, ":",value)

    # employee_details={"name":name,**kwargs}
    employee_details = {"name": name} | kwargs
    return employee_details

employee= employee_info("John Doe", age=30, department="IT", role="Developer")
print(employee)


