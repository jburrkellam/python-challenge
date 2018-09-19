import os
import csv


mainfile= os.path.join("Resources", "budget_data.csv")
print(mainfile)

Total_Months = 0
average = 0
sumPL = 0
first_row = 0
second_row = 0
i = 0
maxPL = 0
minPL = 0

net_changes = []


with open(mainfile) as openfile:
    print(openfile)

    budgetdata = csv.reader(openfile)
    print(budgetdata)

    header = next(budgetdata)
    # print(header)

    # Total Months
    list_budgetdata = list(budgetdata)
    

    # Sum of data
    for i in range(1, len(list_budgetdata)):
        net_changes.append(int(list_budgetdata[i][1]) - int(list_budgetdata[i-1][1]))

    
    for delta in net_changes:

        if delta > maxPL:
            maxPL = delta

    for delta in net_changes:
        if delta < minPL:
            minPL = delta


    Total_Months = len(list_budgetdata)

    for row in list_budgetdata:
        sumPL = sumPL + int(row[1])

    print(Total_Months)
    print(sumPL)
    print(sum(net_changes) / len(net_changes))
    print(maxPL)
    print(minPL)




    