# 1.write a  lambda funtion to retur the power of two of a given number 


power_of_two = lambda x: x ** 2
print(power_of_two(4))  # Output: 16



# 2.write a python programme that ;

# * take a list of tuples  where each tuple contenst a name(string) and age(integer).
# *Use a lambda function to filter out the tuples where the age is left than 18.

people = [("Alice", 23), ("John", 17), ("Andreew", 25), ("kate", 15)]

result = list(filter(lambda x: x[1] >= 18, people))
print(result)


# 3. write the two parameet give and filter the lagest number print

largest_number = lambda a, b: a if a > b else b
print(largest_number(5, 10))  # Output: 10