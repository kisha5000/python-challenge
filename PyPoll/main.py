#import modules
import os
import csv

#locate file path
poll_csv=os.path.join("Resources", "election_data.csv")

#Define the lists
tot_votes = [] 


khan_tot = 0
correy_tot = 0
li_tot = 0
otooley_tot = 0


# OPen the reader
with open(poll_csv) as csvfile:

# put data from budget_dat into csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
 #skip over the header  
    csv_header=next(csvfile) 

#start the loop over all rows
    for row in csvreader:
 #total number of votes       
        tot_votes.append(int(row[0]))

#set totals votes per candidates
        if row[2] == "Khan": 
            khan_tot +=1
        elif row[2] == "Correy":
            correy_tot +=1
        elif row[2] == "Li": 
            li_tot +=1
        elif row[2] == "O'Tooley":
            otooley_tot +=1



# create lists together into tuples
candidates_list = ["Khan", "Correy", "Li", "O'Tooley"]
votes=[khan_tot, correy_tot, li_tot, otooley_tot]

# zip candidates and votes together to get the max vote
# winner = max(zip(votes,candidates_list))
zip_candidates_votes = dict(zip(candidates_list,votes))
key = max(zip_candidates_votes, key=zip_candidates_votes.get)


# Create percentages for each voter
khan_pct = (khan_tot/(len(tot_votes))) *100
correy_pct = (correy_tot/(len(tot_votes))) *100
li_pct = (li_tot/(len(tot_votes))) *100
otooley_pct = (otooley_tot/(len(tot_votes))) *100



# Print Summary Poll Data

print(f"Election Results")
print("----------------------------")
print(f"Total Votes: {len(tot_votes)}")
print(f"----------------------------")
print(f"Khan: {khan_pct:.3f}% ({khan_tot})")
print(f"Correy: {correy_pct:.3f}% ({correy_tot})")
print(f"Li: {li_pct:.3f}% ({li_tot})")
print(f"O'Tooley: {otooley_pct:.3f}% ({otooley_tot})")
print(f"----------------------------")
print(f"Winner: {key}")

# export text file with results
output_file = os.path.join( "Analysis", "PyPoll_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to PyBank Summary 
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write(f"Total Votes: {len(tot_votes)}\n")
    file.write(f"Khan: {khan_pct:.3f}% ({khan_tot})\n")
    file.write(f"Correy: {correy_pct:.3f}% ({correy_tot})\n")
    file.write(f"Li: {li_pct:.3f}% ({li_tot})\n")
    file.write(f"O'Tooley: {otooley_pct:.3f}% ({otooley_tot})")
    file.write(f"----------------------------")
    file.write(f"Winner: {key}")
