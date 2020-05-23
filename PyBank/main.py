#import modules
import os
import csv

#Create lists for total number of Months, total amount of P/L and Average Change of P/L
tot_mths=[]
tot_pl=[]
avg_chg_pl=[]

#locate file path
budget_csv=os.path.join("Resources", "budget_data.csv")

# OPen the reader
with open(budget_csv) as csvfile:

# put data from budget_dat into csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
 #skip over the header  
    csv_header=next(csvfile) 

# for loop iterate ovr the file
    for row in csvreader:

# total number of months included in the dataset. append to list
        tot_mths.append(row[0])

# total amount of "Profit/Losses" over the entire period, aopend to list
        tot_pl.append(int(row[1]))

# The average of the changes in "Profit/Losses"
    for i in range(len(tot_pl)-1):
    
        
#  Take the difference between two months and append to monthly profit change
        avg_chg_pl.append(tot_pl[i+1]-tot_pl[i])
        
# Obtain the max and min of the the montly profit change list
        max_increase = max(avg_chg_pl)
        max_decrease = min(avg_chg_pl)

# The greatest increase in profits (date and amount) over the entire period
        max_mth = avg_chg_pl.index(max(avg_chg_pl)) + 1

# The greatest decrease in losses (date and amount) over the entire period
        min_mth = avg_chg_pl.index(min(avg_chg_pl)) + 1 

# Print Financial Analysis Summary Data

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(tot_mths)}")
print(f"Total: $ {sum(tot_pl)}")
print(f"Average Change: {round(sum(avg_chg_pl)/len(avg_chg_pl),2)}")
print(f"Greatest Increase in Profits: {tot_mths[max_mth]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {tot_mths[min_mth]} (${(str(max_decrease))})")

# export text file with results
output_file = os.path.join( "Analysis", "PyBank_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to PyBank Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write(f"Total Months: {len(tot_mths)}\n")
    file.write(f"Total: ${sum(tot_pl)}\n")
    file.write(f"Average Change: {round(sum(avg_chg_pl)/len(avg_chg_pl),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {tot_mths[max_mth]} (${(str(max_increase))})\n")
    file.write(f"Greatest Decrease in Profits: {tot_mths[min_mth]} (${(str(max_decrease))})")