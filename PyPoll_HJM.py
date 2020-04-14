#PyPoll HJM
import os
import csv

#variables
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

#set path
csvpath = os.path.join('election_data.csv')

#open/read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #header row
    csv_header = next(csvfile)

    #rows
    for row in csvreader:
        
        #total numbers
        total_votes += 1
        
        #Total # of votes
        if (row[2] == "Khan"):
            khan += 1
        elif (row[2] == "Correy"):
            correy += 1
        elif (row[2] == "Li"):
            li += 1
        else:
            otooley += 1
            
    # % of votes
    kahn_percent = khan / total_votes
    correy_percent = correy / total_votes
    li_percent = li / total_votes
    otooley_percent = otooley / total_votes
    
    #winner
    winner = max(khan, correy, li, otooley)

    if winner == khan:
        winner_name = "Khan"
    elif winner == correy:
        winner_name = "Correy"
    elif winner == li:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

#Print
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan})")
print(f"Correy: {correy_percent:.3%}({correy})")
print(f"Li: {li_percent:.3%}({li})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

#write to
output_file = os.path.join('We_Got_a_Winner.text')

#open file
with open(output_file, 'w',) as txtfile:

#write new amazing file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")