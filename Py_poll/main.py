import os
import csv

mainfile = os.path.join("Resources", "election_data.csv.txt")
print(mainfile)

Total_Votes = 0
line = 0
i = 0

candidates = []


with open(mainfile) as openfile:
    #  print(openfile)

    electiondata = csv.reader(openfile)
    # print(electiondata)

    header = next(electiondata)
    #print(header)

    # Total_Votes
    list_electiondata = list(electiondata)
    Total_Votes = len(list_electiondata)
    
    
    # List of Candidates
    for i in range(2):
        candidates.append(list_electiondata[i][2])

    
# def percentages(Election_Data):
#     win_percent = (int(Election_Data[2])/ Total_Votes) * 100
    
    
    
    print(f"Election Results")
    print("-----------------")
    print(f"Total Votes: {str(Total_Votes)}")
    print("-----------------")
    print(f"Candidates: {str(candidates)}")
    # print(f"Win Percent:{str(win_percent)}")

output_path = os.path.join("Resources", "Py-Poll.csv")
with open(output_path, 'w') as f:
    text_file = ("Output.txt", "w")

    f.write(f"Election Results\n")
    f.write("--------------------\n")
    f.write(f"Total Votes: {str(Total_Votes)}\n")
   
    
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.