# import the os module to create file paths across operating systems
import os

# import csv module for reading CSV files
import csv

# set path for file
election_csv = os.path.join("..", "Resources", "election_data.csv")

file_to_output=os.path.join("election_analysis.txt")

#variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winner = ""
winning_votes = 0


with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)



    for row in csvreader:
        #print(row)
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

with open(file_to_output, "w") as text_file:
    output=(f'''Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------\n''')
    print (output)
   
   
    text_file.write(output)


    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = votes/total_votes*100

        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

        results = f"{candidate}: {vote_percent:.2f}% ({votes:,})\n"    
        print(results)
        text_file.write(results)

    winning_candidate = f'''-------------------------
Winner: {winner}
-------------------------
    '''    
    print (winning_candidate)
   
   
    text_file.write(winning_candidate)
