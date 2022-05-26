# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Create a filename variable to a direct or indirect path to the file.

import csv

import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and alayze the data here.
    file_reader = csv.reader(election_data)
    
    # Print each row in the CSV file.
    headers = next(file_reader)

    print(headers)
        
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save,"w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Use the with statement open the file as a text file.

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write 3 counties

    txt_file.write("Counties in the Election")

    txt_file.write("\nArapahoe\nDenver\nJefferson")



