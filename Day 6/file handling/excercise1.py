# Simple contact management

# 1.requirements
#     create the programm that store and manage contacts in a file name  "contacts.txt"
#     each contact enty shoud have name,phone number and email

# 2.feature to implements
#      view all contacts :rad and display all contacts from the file.
#      Add a new contact : append the contact to the file.
   
# 3.exist from the programm

# Sturcture of contacts.txt : John Doe,12345678,john@example.com
#                             Kate Ferry ,453423423,kate@example.com



def read_contact():
    with open("Day 6\file handling\excercise1.txt", "r") as file:
        content = file.read()
        print(content)

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")

    with open("Day 6\file handling\excercise1.txt", "a") as file:
        file.write(f"{name},{phone_number},{email}\n")
        print("Contact added successfully")


while True:                          
    print("1. View all contacts")
    print("2. Add a new contact")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        read_contact()
    if choice == 2:
        add_contact()
    if choice == 3:
        break
    else:
        print("Invalid Input")
  