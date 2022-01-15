# Election_Analysis

## Overview of Election Audit
Election data from a recent local congressional election was given to me and I performed the election audit. 

## Election-Audit Results

### By performing my audit in Python, I ended up getting the result shown in the screenshot below:

![election_result](election_analysis_screenshot.png)

#### 1. How many votes were cast in this congressional election?
- 369,711 votes in total were cast 

#### 2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

#### 3. Which county had the largest number of votes?
- Denver 

#### 4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

#### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Diana DeGette was the winner of the election! Diana DeGette's vote count was 272,892, which was 73.8% of the total votes.

## Election-Audit Summary

The script looks like it has too many lines and too complicated, but it is actually well-organized with the comments in between the lines 
(describing what the next line will be doing). 
If you can follow through each line with the comments, you will see what I am trying to do easily.
I tried to pull the names of the unique candidates, pull the names of the unique counties, calculate how many votes each candidates got, 
calculate how many votes each county got, and finally pull the result of the election showing which county had the largest vote count and
who won the election. At the end, the summary of the results will be printed in my text file and saved. 

This script can be used with some modification for any election. 
For example, 


## Here is my script!

    # Add our dependencies.
import csv
import os

    # Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
    # Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Initialize a total vote counter.
total_votes = 0

    # Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

    # 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

    # Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

    # 2: Track the largest county and county voter turnout
largest_county_turnout = ""
largest_county_votes = 0


    # Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_options:
            
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

    # Save the results to our text file.
 with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]
        # 6c: Calculate the percentage of votes for the county.
        county_percent = int(county_vote) / int(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
         # 6e: Save the county votes to a text file.
        print(county_results, end="")
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_result = (f"\n--------------------------------------\n"
                              f"Largest County Turnout: {largest_county_turnout}\n"
                              f"--------------------------------------\n")

    # 8: Save the county with the largest turnout to a text file.
    print(largest_county_result, end = "")
    txt_file.write(largest_county_result)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
