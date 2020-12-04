# The data we need to retrieve
# 1. The total number of votes
# 2. A complete list of candidates that received votes
# 3. The percentage of votes for each candidate
# 4. The total number of votes each candiate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the new file
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    # print each row is the CSV file
    # print the header row
    headers = next(file_reader)
    print(headers)



