number = int(input("Enter a number: "))

square_num =[]
count =1
temp_square = 1

while temp_square<=number:
   square_num.append(temp_square)
   count+=1
   temp_square = count * count
print(square_num)


    
