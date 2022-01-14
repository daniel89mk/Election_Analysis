# Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
#with open (file_to_load) as election_data:
    # To do:
    #print(election_data)

# Different way to open the file

import csv
import os
# Assign a variable for the file to load and the path
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
#with open(file_to_load) as election_data:
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
# election_data.close()

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""

# Declare a variable for the "winning count" and "winning percentage" 
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # print the cadidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate:
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#print(candidate_options)        
# Print the candidate vote dictionary
print(candidate_votes)

# The percentage of votes each candidate won
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = (float(votes) / float(total_votes) * 100)
        
    # print(f'{candidate_name}: received {vote_percentage} of the vote.')


    # Determine if the vote is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # Set the winning_candidate to the candidate's name
        winning_candidate = candidate_name
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

# Finally print winning candidate summary:
winning_candidate_summary = (f"------------------------------\n"
                             f"Winner: {winning_candidate}\n"
                             f"Winning Vote Count: {winning_count:,}\n"
                             f"Winning Percentage: {winning_percentage:.1f}%\n"
                             f"------------------------------\n")
print(winning_candidate_summary)



#import datetime as dt
#now = dt.datetime.now()
#print("The time right now is  ", now)