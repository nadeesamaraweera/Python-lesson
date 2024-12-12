import csv

csv_path = 'Day 6/csv/sample_output.csv'

data = [
    {"Name" : "Max", "Age" : 20, "City" : "Colombo"},
    {"Name" : "John", "Age" : 25, "City" : "New York"},
    {"Name" : "Alice", "Age" : 30, "City" : "London"}
]

field_names = ["Name", "Age", "City"]

with open('Day 6/csv/sample_output.csv','w',newline='') as file:
    csv_writer = csv.DictWriter(file,fieldnames=field_names)

    csv_writer.writeheader()

    for row in data:
        csv_writer.writerow(row)
print(f'csv data has been wriiten to{csv_path}')