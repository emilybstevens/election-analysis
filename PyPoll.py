# add dependencies
import csv
import os

# assign a variable for the file to load from path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # read and analyze data here
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)




