# Import Dependencies
import os 
import csv

# Variables
num_months = 0 #hold the total number of months
net_total = 0 #hold the total sum of profits
profit_change = [] #list of changes in profit
dates = [] #list of dates associated with changes in profit

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# Open the budget_data.csv file
with open(budget_data) as csvfile:
    # Split the data on commas
    budget_data = csv.reader(csvfile, delimiter=",")

    # Skip the header row, but store it because that's on the grading rubric
    header = next(budget_data)

    # Define previous_profits to read data from "Profit/Losses"
    previous_profit = int(next(budget_data)[1])

    # Adjust number of months by 1
    num_months += 1

    # Add to the first row of "Profit/Losses" to net total
    net_total += previous_profit

    # Read each row of data after header to make calculations
    for row in budget_data:

        ## Determine total number of months included in the dataset
        # Add one num_months for each loop
        num_months += 1

        ## Determine the net total amount of "Profit/Losses" 
        # Add "Profit/Losses" to net_total
        net_total += int(row[1])

        ## Determine the changes in "Profit/Losses" over the entire period
        # Subtract the previous date "Profit/Losses" from the current date 
        profit_change.append(int(row[1])-int(previous_profit))
        # Update the previous_profit for next loop
        previous_profit = int(row[1])

        # Add the date associated with profit_change
        dates.append(row[0])

## Average changes in "Profit/Losses" using the formula of the sum of profit_change over its length
    average_change = sum(profit_change) / (len(profit_change))

## Determine The greatest increase in profits (date and amount) over the entire period
# Find the greatest profit change and equate that to max_profit_amount
max_profit_amount = max(profit_change)

# Use index to locate the max_profit_amount
max_profit_index = profit_change.index(max_profit_amount)

# Use index to locate the associated date of the max_profit_amount to set max_profit_date value
max_profit_date = dates[max_profit_index]

## Determine the greatest decrease in profits (date and amount) over the entire period
# Find the smallest profit change and equate that to min_profit_amount
min_profit_amount = min(profit_change)

# Use index to locate the min_profit_amount
min_profit_index = profit_change.index(min_profit_amount)

# Use index to locate the associated date of the min_profit_amount to set min_profit_date value
min_profit_date = dates[min_profit_index]

# Define summary_results including Title: "Financial Analysis", break line, "Total Months", "Total" of 
    #profits, "Average Change", "Greatest Increase in Profits", and "Greatest Decrease in Profits" 
    #use round function so the average change includes only two decimal points
summary_results = (f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {num_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: {max_profit_date} ({max_profit_amount})\n"
    f"Greatest Decrease in Profits: {min_profit_date} ({min_profit_amount})")

# Print summary_results to terminal
print(summary_results)

# Create txt file inside directory
path = os.path.join("PyBank", "analysis", "Financial Analysis.txt")
dataFile = open(path, 'w')

# Write summary_results into text file
dataFile.write(summary_results)

dataFile.close()
