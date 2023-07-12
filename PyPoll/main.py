import os
import csv

#Path to collect data from the Resources folder
election_data="./Resources/election_data.csv"
analysis="./analysis/budget_analysis.txt"
total_votes=0
candidates={}

with open(election_data,"r") as file:
    csv_data=csv.reader(file)
    header=next(csv_data)
    
    for row in csv_data:
        #define total votes
        total_votes += 1
        #add candidates to dictionary
        if row[2] in candidates:
            #if the candidate exsists in the dictionary, add 1 to their vote count
            candidates[row[2]]+=1
        else:
            #if the candidate does not exsist in the dictionary, add them and set their vote count to 1
            candidates[row[2]]=1



# print (total_votes)
print (candidates)

#     winner=0
#     winner_name=0
#define the function and have it accept "candidate" as it's sole parameter
def print_percentages(name, votes):
    #return the candidate name and percentage of votes
    return(f"{name}: {votes/total_votes*100:.3f}% ({votes})")

#     #assign columns to variables
#     candidates= str("candidate"[2])
#     votes= str("ballot"[0])
winner= 0
winner_name= ""
       
result = "Election Results\n----------------------------\n"
result += f"Total Votes: {total_votes}\n"
result += "--------------------------\n"
for name,votes in candidates.items():
    result += print_percentages(name,votes)+"\n"
    if votes > winner:
        winner = votes
        winner_name = name
result += "--------------------------\n"
result += f"Winner: {winner_name}\n"
result += "--------------------------\n"
print(result)
with open("analysis/analysis.txt","w") as file:
    file.write(result)
