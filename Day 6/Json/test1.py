import json 

data = {
    "name" : "Nadeesha",
    "age" : 24,
    "city" : "Matara"
}

json_file_path = 'test_1.json'

with open(json_file_path,"w")  as file:

  json_data = json.dumps(data,indent=4)
  file.write(json_data)

# print(f'JSON data has been saved to {json_file_path}')