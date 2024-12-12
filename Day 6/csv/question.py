# manage employee record with csv

# yout task with creating the python programm to manage a company employee records stored in csv file.The programm should read the employee details  from a csv file filter the record base on the condition and write the filter record to a new csv file.
#      file provider : input file 'employees.csv'
#      contain the following fields : Employee_ID,Name,Department,Salary

# example:
#    1,John,It,60000
#    2,Jane,HR,
#    3,Jane,HR,55000

# 2.output file : high_salary_employees.csv
#   you will create this file, it should contain records of the employee whose salaries are above 57000. The fields should remains the same.

# Tasks
# 1. read the input file. Use csv.reader to read employees.csv and display all the records.
# 2. filter the records.Identify employees with the salary>65000
# 3.write the filter record.use csv.Dictwriter to write the filter record to  new file name high_salary_employees.csv 


import csv

fieldnames = ['Name', 'Department', 'Salary']

#1. read the input file. Use csv.reader to read employees.csv and display all the records on the console.
with open("Day 6\csv\employee.csv","r") as file:
    rows = csv.reader(file)

    for row in rows:
        print(row)

csv_path = 'Day 6\csv\highSalaryEmployees.csv'

#2. filter the records identify the employee with the salary > 57000

with open("Day 6\csv\employee.csv","r") as file:
    reader = csv.DictReader(file)
    writer = csv.DictWriter(open(csv_path, "w"), fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if int(row['Salary']) > 57000:
            writer.writerow(row)

#3. Write the filter records to highSalaryEmployees.csv using csv.DictWriter to write the filtered records.

print(f"Filtered records have been written to {csv_path}")