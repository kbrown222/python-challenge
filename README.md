Python Challenge - Homework # 3

Project Summary - This project has been split into two different challenges to use new Python skills.

    *The first challenge is to create a Python script to analyze the financial records of a company using a set of financial data called [budget_data.csv].

    *The second challenge is to help helping a small, rural town modernize its vote counting process.


System Requirements:
  Python files were created using VSCode

Python dictionaries
sqlalchemy
psycopg2
pandas
Misc. files
db_pw (python file with database password)

File Setup:
Two folders for each portion of the challenge:
PyBank
PyPoll

Each of the folders contains the following:
  * `main.py` - These files contain the main script for each analysis.
  * A `Resources` folder that contains the CSV file used in each main.py file.
  * An `analysis` folder that contains the text file that has the results from the analysis completed.

For the PyBank Analysis:
  * The set of financial data used is called[budget_data.csv](PyBank/Resources/budget_data.csv). 
        -The dataset is composed of two columns: "Date" and "Profit/Losses".
  * The csv file was imported and data was read using csv reader.
  * The records were analyzed to calculate the following:
        #The total number of months included in the dataset
        #The net total amount of "Profit/Losses" over the entire period
        #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in profits (date and amount) over the entire period
  * 
  * Analysis of the data prints to the terminal and exports to a text file with the results in the Analysis folder. This includes



After analyzing the data, the following issues were identified:

Null values in weight column
Null values in height column
Null values in type2 column
The original database schema sets up the table to not allow null values, but upon further discussion, it was determined that for future (hypothetical) analysis, null values were necessary for height and weight. These were left as null rather than 0.0 because 0.0 is still a value that would provide inaccurate results for any analysis.

The last column, evolvesFrom, derives from the second CSV file, df_pokemon. Because of this, the column is initially left blank during the dataframe setup. It was later populated using the python loc function to match the name from the dataframe to the name in the second CSV file.

This process resulted in a key error, which was resolved using the try-except statement. In addition, to remove any extra columns, the national dex number was set as the index.

Table 2: Stats
This table utilizes df_pokemon.csv. Like the first CSV file, this data source also contained more columns than were necessary for the table.

After the data is loaded into a dataframe, the issues that were identified included:

Base Stat are float values
Health Points are float values
Attack are float values
Defense are float values
Special Attack are float values
Special Defense are float values
Speed are float values
Extra rows that are not found in Table 1
Rows with null values
After reviewing the CSV file in Excel, the only rows that contained null values were rows that had no data altogether so the final decision was to exclude them altogether.

Because Table 2 has a dependency on Table 1 through the foreign key of national dex number, extra rows that were not found in Table 1 caused the data to fail. After analyzing the data through Excel, the final solution was to select the rows that had a dex number of 801 or lower. This dex number is the last number in Table 1, so using this condition guaranteed that the rows we load into Table 2 exist in Table 1.

The columns with float values posed an issue because the table schema sets up the columns to only allow integers. Rather than changing the table schema, the columns were converted to an integer using the astype function in Python.

Table 3: Abilities
The last table utilizes the file bridge_pokemon_ability_MAY_HAS.csv. To provide a different process of ETL, this file is imported directly into Postgres via the built-in import function.

From there, three queries are ran to do the following:

List all Pokemon and their respective abilities using a join on Pokedex and Abilities tables


List of Pokemon name and number of abilities they have using the join on Pokedex and Abilities tables and grouped them by name


List of pokemon ablities and number of pokemon using it using the join on Pokedex and Abilities tables and grouped them by ability




## PyPoll Instructions

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

Your analysis should look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations

* Consider what you've learned so far. You've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what you've learned, try to break down your tasks into discrete mini-objectives. 

* The datasets for these challenges are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more robust options for handling big data.

* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to those who don't do their own work. 

* Start early, and reach out for help when you need it! Be sure to identify specific questions for your instructors and TAs so that they understand your thought process and can provide targeted guidance.

* Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your work! Also make sure that your repo has a detailed   `README.md` file. 

