# Import Dependencies
import os 
import csv

# Variables
total_votes = 0 #holds the total number of votes
candidate_data = {} #creates a dictionary to store the canidates, perecentage of votes, and number of votes won
winner = None #holds the name of the winner
max_votes = 0 #holds value of max votes 

election_data = os.path.join("PyPoll", "election_data.csv")

# Open the election_data.csv file
with open(election_data) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(election_data)

## Compile a complete list of candidates who received votes, the number of votes
    #each candidate received, and the total number of votes cast
    for row in election_data:
        # Adjust number of votes by 1
        total_votes += 1
        # If the candidate is in the dictionary, then add to votes
        if row[2] in candidate_data: 
            candidate_data[row[2]] += 1
        # If the candidate is not in the dictionary, then add the candidate and the vote
        else: 
            candidate_data[row[2]] = 1

    for candidate in candidate_data: 
        
    ## Determine the percentage of votes each candidate won 
        # Divide the number of candidate votes by the total votes and times by 100 
            #to get each candidate's percentage of all the votes
        percentage = (candidate_data[candidate]/total_votes) * 100

    # Update candidate_data dictionary with the percentage
        candidate_data[candidate] = [percentage, candidate_data[candidate]]

## Determine the winner of the election based on popular vote
    for candidate, votes in candidate_data.items():
        # If the number of votes of a candidate is greater than max_votes, then declare winner
        if candidate_data[candidate][1] > max_votes: 
            winner = candidate
            # Update the current number of votes before looping again
            max_votes = candidate_data[candidate][1] 


# Define summary_results including Title "Election Results", break line, "Total Votes", break line, 
# each candidate name with percent of votes (total votes), break line, winner, and another break line
summary_results = (f"Election Results\n"f"----------------------------\n"f"Total Votes: {total_votes}\n"
f"----------------------------\n"f"{candidate_data}\n"f"----------------------------\n"
f"Winner: {winner})\n"f"----------------------------")

# Print summary_results to terminal
print(summary_results)

# Create txt file
dataFile = open('Election Results.txt', 'w')

# Write summary_results into text file
dataFile.write(summary_results)

dataFile.close()