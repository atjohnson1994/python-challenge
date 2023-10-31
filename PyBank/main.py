import os
import csv
import numpy

# Retrieve dataset
budgetcsv = os.path.join("Resources", "budget_data.csv")

# Generate lists
date = []
amount = []
change = []

# Read dataset
with open(budgetcsv) as budget:
    csvreader = csv.reader(budget, delimiter=",")
    # Skip Line
    next(csvreader, None)

    # Record all data from dataset into lists
    for row in csvreader:
        # Record date
        date.append(row[0])
        # Record amount
        amount.append(row[1])
        
# Convert string values into integers
amount_array = numpy.array(amount, dtype=int)
amount_int = list(amount_array)

# Calculate the change
amount_length = len(amount_int)
i=0
while i < amount_length:
    # Ignore first data point
    if i == 0:
        prequel = 0
        current = 0
    # Set variables
    else:
        prequel = amount_int[i-1]
        current = amount_int[i]
    # Run calculation    
    difference = (current - prequel)
    change.append(difference)
    i = i + 1

# Calculate net profit/loss
total = sum(amount_int)

# Calculate number of months in dataset
months = len(date)

# Calculate the total change
changesum = sum(change)

# Calculate the average change
average = changesum/(months-1)
average_rounded = round(average,2)

# Calculate max profit and reference date from data set
inc_amount = max(change)
refdatemax = change.index(inc_amount)
inc_date = date[refdatemax]

# Calculate max loss and reference date from data set
dec_amount = min(change)
refdatemin = change.index(dec_amount)
dec_date = date[refdatemin]

# Print title
print("Financial Analysis")
print("---------------------------")

# Print total months
print("Total Months: " + str(months))

# Print total profit/loss
print("Total: $" + str(total))

# Print average change
print("Average Change: $" + str(average_rounded))

# Print greatest profit
print("Greatest Increase in Profits: " + str(inc_date) + " " + "(" + str(inc_amount) + ")")

# Print greatest loss
print("Greatest Decrease in Profits: " + str(dec_date) + " " + "(" + str(dec_amount) + ")")



# Output file
output_file = os.path.join("analysis", "Financial Analysis")
# Open output file
with open(output_file, "w") as analysis:
    
    
# Write in results
    analysis.write("Financial Analysis\n")
    analysis.write("------------------\n")
    analysis.write("Total Months: " + str(months) + "\n")
    analysis.write("Total: $" + str(total) + "\n")
    analysis.write("Average Change: $" + str(average_rounded) + "\n")
    analysis.write("Greatest Increase in Profits: " + str(inc_date) + " " + "(" + str(inc_amount) + ")\n")
    analysis.write("Greatest Decrease in Profits: " + str(dec_date) + " " + "(" + str(dec_amount) + ")")
    analysis.close()