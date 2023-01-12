#In this Challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will be given a financial dataset called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses".

#Your task is to create a Python script that analyzes the records to calculate each of the 
# following values:

    #The total number of months included in the dataset

    #The net total amount of "Profit/Losses" over the entire period

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes

    #The greatest increase in profits (date and amount) over the entire period

    #The greatest decrease in profits (date and amount) over the entire period

#Your analysis should align with the following results:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

import os 
import csv

path = r"C:\Users\lisam\OneDrive\Documents\GitHub\python-challenge"

budget_data = os.path.join("..", "PyBank", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    
