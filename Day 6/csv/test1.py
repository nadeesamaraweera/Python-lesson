import csv

with open ("Day 6\csv\customers-100.csv","r",newline="") as file:
    csv_reader= csv.DictReader(file)
# print(csv_reader,type(csv_reader))
    for row in csv_reader:
        print(row,type(row))