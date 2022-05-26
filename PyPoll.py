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

# Initialize a total vot counter.
total_votes = 0

# Candidate optionns and candidate votes
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and alayze the data here.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes +=1

        # Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vot to that candidate's count.
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
   
    print(election_results, end="")
   
    # Save the final vote count to the text file.
   
    txt_file.write(election_results)

    #Determine the perctage of votes for each candidate by looping through the coutns.

    # Iterate through the candidates list with an "for" loop
    for candidate_name in candidate_votes:

        # Retrieve the vote count of a specific candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes)*100

        candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

        # Print each candiadte's voter count and pertage to the terminal.
        print(candidate_results)
        
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

                            # Determine winning vote count and candidate.
        
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    # Print the winning candidates' results to the terminal. 

    winning_candidate_summary=( 
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Perccentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)
    #  To do: print out the winning candidate, vote count and percentage to terminal.

        # Print the candidate name and perctage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Print the candidate vote dictionary
    print(candidate_votes)
     



