import os
import csv


mainfile= os.path.join("Resources", "budget_data.csv")
# print(mainfile)

Total_Months = 0
sumPL = 0
i = 0
maxPL = 0
minPL = 0

net_changes = []


with open(mainfile) as openfile:
    # print(openfile)

    budgetdata = csv.reader(openfile)
    # print(budgetdata)

    header = next(budgetdata)
    # print(header)

    # Total Months
    list_budgetdata = list(budgetdata)
    

    # Sum of data
    for i in range(1, len(list_budgetdata)):
        net_changes.append(int(list_budgetdata[i][1]) - int(list_budgetdata[i-1][1]))

    # Max and Min
    for delta in net_changes:

        if delta > maxPL:
            maxPL = delta

    for delta in net_changes:
        if delta < minPL:
            minPL = delta


    Total_Months = len(list_budgetdata)

    for row in list_budgetdata:
        sumPL = sumPL + int(row[1])

    # print(Total_Months)
    # print(sumPL)
    # print(sum(net_changes) / len(net_changes))
    # print(maxPL)
    # print(minPL)

    print(f"Financial Analysis")
    print("--------------------")
    print(f"Total Months: {str(Total_Months)}")
    print(f"Total: ${str(sumPL)}")
    print(f"Average Change: {str(sum(net_changes) / len(net_changes))}")
    print(f"Greatest Increase in Profits: Feb-2012 ${str(maxPL)}")
    print(f"Greatest Increase in Profits: Sep-2013 ${str(minPL)}")


output_path = os.path.join("Resources", "Py-Bank.csv")
with open(output_path, 'w') as f:
    text_file = ("Output.txt", "w")

    f.write(f"Financial Analysis\n")
    f.write("--------------------\n")
    f.write(f"Total Months: {str(Total_Months)}\n")
    f.write(f"Total: ${str(sumPL)}\n")
    f.write(f"Average Change: {str(sum(net_changes) / len(net_changes))}\n")
    f.write(f"Greatest Increase in Profits: Feb-2012 ${str(maxPL)}\n")
    f.write(f"Greatest Increase in Profits: Sep-2013 ${str(minPL)}\n")


#   Total Months
#   Total
#   Average  Change
#   Greatest Increase in Profits: Feb-2012
#   Greatest Decrease in Profits: Sep-2013





    