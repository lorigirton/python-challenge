import csv

budget_data='./Resources/budget_data.csv'
analysis='./analysis/budget_analysis.txt'

with open(budget_data,"r") as file:
    csv_data=csv.reader(file)
    header=next(csv_data)
    for row in csv_data:
        print(row)
