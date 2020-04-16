# python-challenges

Py Me Up, Charlie

Background
Well... you've made it!
It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this work assignment, you'll be using the concepts you've learned to complete 2 Python Challenges, PyElections and PyFinances.
Both of these challenges encompasses a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead!

Before You Begin


Create a new repository for this project called python-challenge. Do not add this work to an existing repository.


Clone the new repository to your computer.


Inside your local git repository, create a directory for both of the  Python Challenges. Use folder names corresponding to the challenges: PyFinances and  PyElections.


Inside of each folder that you just created, add a new file called main.py. This will be the main script to run for each analysis.


Push the above changes to GitHub or GitLab.



PyElections



In this challenge, you are tasked with helping the city of Houston modernize its vote-counting process for the next mayoral elections. No candidate won a majority (over 50%) of the vote during the general election that took place on November 5, 2019. The 2019 Houston mayoral election was decided by a runoff on December 14, 2019 to elect the Mayor of Space City. 
However, your job is to only write a script that will decide the two candidates with the highest number of votes who will advance to the runoff election. Houstonians are counting on you!


You will be given a set of the last general election data called houston_election_data.csv. The dataset is composed of three columns: Candidate, County, and Voter ID. Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast


A complete list of candidates who received votes


The percentage of votes each candidate won


The total number of votes each candidate won


Print the names of the two candidates who will advance to the runoff election.




As an example, your analysis should look similar to the one below:
Houston Mayoral Election Results
-----------------------------------------
Total Cast Votes: 241032
-----------------------------------------
Sylvester Turner: 46.38% (111789)
Tony Buzbee: 28.78% (69361)
Bill King: 14.01% (33772)
Dwight A. Boykins: 5.90% (14212)
Victoria Romero: 1.22% (2933)
Sue Lovell: 1.22% (2932)
Demetria Smith: 0.70% (1694)
Roy J. Vasquez: 0.65% (1556)
Kendall Baker: 0.41% (982)
Derrick Broze: 0.28% (686)
Naoufal Houjami: 0.23% (560)
Johnny “J.T.” Taylor: 0.23% (555)
-----------------------------------------
1st Advancing Candidate: Sylvester Turner
2nd Advancing Candidate: Tony Buzbee
-----------------------------------------


In addition, your final script should both print the analysis to the terminal and export a text file with the results.


Official Results Link.

PyFinances



In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given a set of financial data called budget_data.csv. The dataset is composed of two columns: Profit/Losses and Date. (Thankfully, your company has rather lax standards for accounting so the records are simple.)


Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset


The net total amount of "Profit/Losses" over the entire period


The average of the changes in "Profit/Losses" over the entire period


The greatest increase in profits (date and amount) over the entire period


The greatest decrease in losses (date and amount) over the entire period




As an example, your analysis should look similar to the one below:
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)



