# you are given the json file name students.json. which contents information about students and their grades.your task is to 

#   1.read the json File.
#   2.display the name of all students who scored about 75.
#   3.add the new student record to the File.
#   4.save the updated data back to the json file.


import json

#1. Read the json file
with open ('Day 6\Json\students.json','r') as file:
    data = json.load(file)
    print(data)

#2. Display the name of the students who scored above 75
for student in data:
    if student['marks'] > 75:
        print(student['name'])


#3.add the new student record to the File.
name = input("Student's Name :")
marks = int(input("Student's Marks :"))

new_student = {
    'name' : name,
    'marks': marks
}

data.append(new_student)

# 4.save the updated data back to the json file.
with open('Day 6\Json\students.json', 'w') as file:
    data = json.dumps(data, indent=4)
    file.write(data)

print("Updated data: " + str(data))

