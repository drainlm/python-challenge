#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting 
# process.

#You will be given a set of poll data called election_data.csv. The dataset is composed of 
# three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script
#  that analyzes the votes and calculates each of the following values:

    #The total number of votes cast

    #A complete list of candidates who received votes

    #The percentage of votes each candidate won

    #The total number of votes each candidate won

    #The winner of the election based on popular vote

#Your analysis should align with the following results:

#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette

import os 
import csv

path = r"C:\Users\lisam\OneDrive\Documents\GitHub\python-challenge\PyPoll\election_data.csv"
    
election_data = os.path.join("..", "PyPoll", "election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    

    # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file

    # Read through each row of data after the header
    for row in csv_reader:

        # Convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)
