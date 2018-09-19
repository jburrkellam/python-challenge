import os
import csv

mainfile = os.path.join("Resources", "election_data.csv.txt")
print(mainfile)

Total_Votes = 0
sum = 0
line = 0

with open(mainfile) as openfile:
    print(openfile)

    electiondata = csv.reader(openfile)
    print(electiondata)

    header = next(electiondata)
    print(header)

    Total_Votes = len(list(electiondata))
    print(Total_Votes)

  



        













# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.