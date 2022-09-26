
# import the os module to create file paths across operating systems
import os

# import csv module for reading CSV files
import csv

# set path for file
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

file_to_output=os.path.join("budget_analysis.txt")

#variables
total_months=0
month_of_change=[]
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",9999999999999]
total_net=0


# budget_csv = "./Resources/budget_data.csv";

with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]  
        month_of_change += [row[0]]

#The total number of months included in the dataset

    
#The net total amount of "Profit/Losses" over the entire period
   
   
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change


    #The greatest decrease in profits (date and amount) over the entire period
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list)/len(net_change_list)
print(f"{sum(net_change_list)}")
print(f"{len(net_change_list)}")
     #Prints the Financial Analysis

#Format analysis and add explanations of each calculation.
output=(f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net:,.2f}
Average Change: ${net_monthly_avg:,.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})
''')
print(output)

    #final script should both print the analysis to the terminal & export a text file with the results
with open(file_to_output, "w") as text_file:
    text_file.write(output)