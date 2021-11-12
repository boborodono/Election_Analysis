#   Add Dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read & Print the header row.
    headers = next(file_reader)
    print(headers)

#1. Total Number of Votes Cast

#2. A complete listof candidates who received votes

#3. Percentage of votes each candidate won

#4. The total number of votes each candidate won

#5. The winner of the election based on popular vote