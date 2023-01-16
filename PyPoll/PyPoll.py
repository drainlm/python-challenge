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

## Determine the total number of votes cast
    for row in election_data:
        # Adjust number of months by 1
        total_votes += 1
        # If the candidate is in the dictionary, then add to votes
        if row[2] in candidate_data: 
            candidate_data[row[2]] += 1
        # If the candidate is not in the dictionary, then add the candidate and the vote
        else: 
            candidate_data[row[2]] = 1

## Compile a complete list of candidates who received votes
    for candidate in candidate_data: 
        
    ## Determine the percentage of votes each candidate won 
        # Divide the number of candidate votes by the total votes and times by 100 
            #to get each candidate's percentage of all the votes
        percentage = (candidate_data[candidate]/total_votes) * 100

    # Update candidate_data dictionary with the percentage
        candidate_data[candidate] = [percentage, candidate_data[candidate]]

## Determine the total number of votes each candidate won

## Determine the winner of the election based on popular vote
    for candidate, votes in candidate_data.items():
        if candidate_data[candidate][1] > max_votes: 
            winner = candidate
            max_votes = candidate_data[candidate][1] 

print(candidate)
print(percentage)
print(votes)

