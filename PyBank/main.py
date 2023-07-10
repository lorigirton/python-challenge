import os
import csv
total_months = 0
total=0
difference= []
greatest_increase=["",0]
greatest_decrease=["",999999999]

budget_data = os.path.join('Resources', 'budget_data.csv')
analysis='./analysis/budget_analysis.txt'
with open(budget_data,"r") as file:
    csv_data=csv.reader(file)
    header=next(csv_data)
    first_row = next(csv_data)
    total += int(first_row[1]) 
    total_months += 1
    prev_value= int(first_row[1])
    
    for row in csv_data:
        #define total months
        total_months= total_months+1
        #Find the net total of all profit/losses
        total+=int(row[1])
        #store the difference between row and previous row in a list
        difference.append(int(row[1])-prev_value)
        
        net_change=int(row[1])-prev_value

        #store the difference along with month in a separate list
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        prev_value=int(row[1])
        

#format total
total="${:.0f}".format(total)
#find the average of all the stored numbers
average_difference= sum(difference)/len(difference)
average_difference="${:.2f}".format(average_difference)

#print results
result = "Financial Analysis\n----------------------------\n"
result += f"Total Months: {total_months}\n"
result += f"Total: {total}\n"
result += f"Average Change: {average_difference}\n"
result += f"Greatest Increase in Profits: {greatest_increase}\n"
result += f"Greatest Decrease in Profits: {greatest_decrease}\n"
print(result)
with open("analysis/analysis.txt","w") as file:
    file.write(result)


