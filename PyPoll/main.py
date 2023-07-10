import os
import csv
election_data="./Resources/election_data.csv"
analysis="./analysis/budget_analysis.txt"
#define out of loop variables
with open(election_data,"r") as file:
    csv_data=csv.reader(file)
    header=next(csv_data)
    
    for row in csv_data
        #define loop variables
#result = "Election Results\n----------------------------\n"
#result += f"Total Votes: {variable}\n"
#result = "--------------------------/n"
#result += f{candidate variable}\n
#result = "--------------------------/n"
#result += f"Winner: {winner variable}\n"
#result = "--------------------------/n"
#print(result)
#with open("analysis/analysis.txt","w") as file:
    #file.write(result)
