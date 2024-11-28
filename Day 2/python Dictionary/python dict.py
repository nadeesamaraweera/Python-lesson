my_dict={
    "name":"Sugar",
    "Price": 250.20,
    "Weight":"1kg",
    
}
print(my_dict)
# {'name': 'Sugar', 'Price': 270.0, 'Weight': '1kg'}

print(my_dict["Price"])
# 250.2

my_dict['Price']=300.00
print(my_dict)
# {'name': 'Sugar', 'Price': 300.0, 'Weight': '1kg'}

print(my_dict.get("Price"))
# 300.0

print(my_dict.get("expire-date"))
# None

print(my_dict.get("expire-date","2025-02-23"))
# 2025-02-23

my_dict.update({"Price":290.00,"Weight":"2kg"})
print(my_dict)
# {'name': 'Sugar', 'Price': 290.0, 'Weight': '2kg'}

my_dict["color"] ="White"
print(my_dict)
# {'name': 'Sugar', 'Price': 290.0, 'Weight': '2kg', 'color': 'White'}

my_dict.pop("Weight")
print(my_dict)
# {'name': 'Sugar', 'Price': 290.0, 'color': 'White'}

del my_dict["color"]
print(my_dict)
# {'name': 'Sugar', 'Price': 290.0}

del my_dict
# mukuth na


my_dict={
    "name":"Sugar",
    "Price": 250.20,
    "Weight":"1kg",
    
}
my_dict.clear()
print(len(my_dict))
print(my_dict)
# 0
# {}

