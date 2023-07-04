import csv
election_data="./Resources/election_data.csv"
analysis="./analysis/budget_analysis.txt"

with open(election_data,"r") as file:
    csv_data=csv.reader(file)
    header=next(csv_data)
    for row in csv_data
        print(row)