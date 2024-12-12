# file_1 = open("Day 6\myPython.txt")

# # content =  file_1.read()   #ookoma read wenoo
# # content =  file_1.readline()  #eka line ekai read wenne
# content =  file_1.readlines()  #list ekk

# print(content,type(content))
 
# file_1.close()

with open("Day 6\myPython.txt","r") as file:  #close ek dnn one na
    content=file.read()
    print(content)