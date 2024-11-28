# you have list of temin celcious,
# temperatures = [20,30,25,40,15]
# then write a python program using the map function to convert these tempertures in to Fahrenhite.
# Use the formula,
#  Fahrenhite = celsious * 9/5 + 32

temperatures = [20,30,25,40,15]

def Feranheit(f):
    return (f* 9/5) + 32
result =list( map(Feranheit, temperatures))
print(result)   #[68.0, 86.0, 77.0, 104.0, 59.0]