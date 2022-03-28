#Open the data file.
# 1.The total number of vote casts.
# 2.A complete list of candidates of recieved votes.
#3.The Percentage of votes each candidate to won.
# 4.The total votes for each candidate Won.
# 5. Winner of election based on popular votes.

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)
    # Close the file.
#election_data.close()

#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

      # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
     print(row)