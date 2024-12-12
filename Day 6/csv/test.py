import csv

with open ('Day 6\csv\customers-100.csv', newline='') as file:
    csv_reader=csv.reader(file)

    for row in csv_reader:
        print(row,type(row))