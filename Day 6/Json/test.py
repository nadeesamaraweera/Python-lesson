import json

#Specify the path to the JSON file
json_path = 'Day 6\Json\example_1.json'

#open the JSON file for reading
with open(json_path, 'r') as json_file:
    #load the JSON data in to a  python Dictionary
    data = json.load(json_file)

print(data, type(data))

for key,value in data.items():
    print(key + ":" + value)