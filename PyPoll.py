# add dependencies
import csv
import os

# assign a variable for the file to load from path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)
    # print each row in the csv file
    for row in file_reader:
        total_votes += 1 
        candidate_name = row[2]
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100
    print(f"{candidate_name}: received {vote_percentage}% of the vote")

print(candidate_votes)

# print candidate name for each row





