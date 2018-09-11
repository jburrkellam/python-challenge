import os
import csv

mainfile= os.path.join("Resources", "budget_data.csv")
print(mainfile)

sum = 0
count = 0


with open(mainfile) as openfile:
    print(openfile)

    budgetdata = csv.reader(openfile)
    print(budgetdata)

    header = next(budgetdata)
    print(budgetdata)

    for row in budgetdata:
        count += 1
        print(count)
        
        sum = sum + int(row[1])
        print(sum)









# Final Result = some sort of function(calculation)
# # # Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period