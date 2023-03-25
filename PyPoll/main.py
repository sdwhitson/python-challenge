import os
import csv

csvpath= os.path.join("PyPoll", "Resources", "election_data.csv")

# The total number of votes cast
with open(csvpath) as votes:
    votes_reader = csv.reader(votes)
    header = next(votes_reader)

    num_votes = 0

    for row in votes_reader:
        if row[0]:
            num_votes += 1
        
print("Total Votes:", num_votes)

Total_Votes="Total Votes: ", num_votes

#A complete list of candidates who received votes
candidates= set()

with open(csvpath) as can:
    can_reader = csv.reader(can)
    header= next(can_reader)

    for row in can_reader:
        candidates.add(row[2])
    
canidates_names= tuple(candidates)

#The percentage of votes each candidate won
names_candidates= canidates_names
count_per ={}

with open(csvpath, "r") as per:
    per_reader = csv.reader(per)
    header = next(per_reader)

    for row in per_reader:

        if row[2] in names_candidates:

            if row[2] in count_per:
                count_per[row[2]] += 1
            else:
                count_per[row[2]]= 1

for name in names_candidates:
   if name in count_per:
       print(f"{name}: {round((100 * count_per[name]/num_votes), 2)} %, {count_per[name]}") 
    

winner_canidate= max(count_per, key=count_per.get)
print(f"Winner: {winner_canidate}")

#writting to text file
with open("Election_Results.txt", "w") as text_file:

    text_file.write(f"{Total_Votes[0]}{Total_Votes[1]}\n")

    for name in names_candidates:
        if name in count_per:
            text_file.write(f"{name}: {round((100 * count_per[name]/num_votes), 2)} %, {count_per[name]}\n")
    
    text_file.write(f"Winner: {winner_canidate}")

import shutil

shutil.move("Election_Results.txt", "PyPoll/Election_Results.txt")
