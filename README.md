# python-challenge
I have created two Python scripts to analyze different data compiled in csv documents. 1. PyBank (budget_data) and 2. PyPoll (election_data)

1. PyBank
This script analyzes financial records included in the budget_data.csv (two columns: "Date" and "Profit/Losses") and calculates several values including: 
    - The total number of months in the data set
    This is done by using a for loop that sums the months together

    - The net total amount of Profit/Losses over the entire period
    This is also accomplished in the for loop that sums the Profit/Losses

    -The changes in Profit/Losses, and the average of those changes
    This is accomplished by subtracting "Profit/Loss" the previous date to gather the profit_change

    -The average of change in Profit/Loss
    This is accomplished by taking the sum of the profit_change and dividing it by the total number of values in the set (length)

    -The greatest increase in profits by date and amount
    This is accomplished by finding the max profit_change, indexing the data, and then using the index to find the corresponding date

    -The greatest decrease in profits by date and amount 
    This is accomplished by finding the min profit_change, indexing the data, and then using the index to find the corresponding date

The script then prints this data summary in the terminal and exports a text file with the results. 
    -This is accomplished by storing the data using f-string, using \n to create a new line, and using round, 2 function to limit the average_change, and then printing in the terminal and writing to a text file. 

The output should look like this: 

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 (1862002)
Greatest Decrease in Profits: Feb-14 (-1825558)


2. PyPoll
This script anaylzes election data included in the election_data.csv (three columns: "Ballot ID", "County", and "Candidate") and calucates the following values:
    - The total number of votes cast
    This is accomplished by using a for loop that sums the total votes together using the dataset

    -A complete list of candidates who received votes and the total number of votes won by each candidate 
    This is accomplished by using a candidate_data dictionary to holding the candidate names, the number of votes, and percentage. Then the for loop that is gathering the total votes, loops through the data to determine if a candidate name has been added (adding it if not), and adding to the candidate vote tally

    -The percentage of votes each candidate won
    This is accomplished by another for loop that sums each candidate's vote tally and divides this over the number of total votes and multiplies by 100 for the percentage. Next, it updates the percentage to the candidate data dictionary


    -The winner of the elction based on popular vote
    This is accomplished by a third for loop that loopes through the candidate data items to find the candidate with the highest number of votes

The script then prints this data summary in the terminal and exports a text file with the results. 
    -This is accomplished by first using a dictionary key to pull the candidate and their stored data (percentage and total votes), storing the data in summary_results while using f-string, using round, 3 and % for formating, and using \n to create new lines. Then I set summary_results to print in the terminal and write to a text file. 

The output should look like this: 

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------