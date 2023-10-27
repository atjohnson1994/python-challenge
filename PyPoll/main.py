import csv
import os

# Retrieve dataset
electioncsv = os.path.join("Resources", "election_data.csv")

# Generate lists
voter_id = []
county = []
candidate = []
voted_candidate = []



# Read the dataset
with open(electioncsv) as election:
    csvreader = csv.reader(election, delimiter=",")
    
    # Skip line
    next(csvreader, None)
    # For each row in the dataset
    for row in csvreader:
        # Record voter id
        voter_id.append(row[0])
        # Record county
        county.append(row[1])
        # Record candidate
        candidate.append(row[2])
        
# Calculate total votes
total_votes = len(voter_id)

# Print total votes
print("Election Results")
print("------------------")
print("Total Votes: " + str(total_votes))
print("------------------")

# Set the export file
output_file = os.path.join("analysis", "Election_Results")
with open(output_file, "w") as results:

    # Write total votes in export file
    results.write("Election Results\n")
    results.write("------------------\n")
    results.write("Total Votes: " + str(total_votes) + "\n")
    results.write("------------------\n")

    # Determine length of dataset
    candidate_length = len(candidate)
    i=0

    # Determine the unique entries in dataset
    while i < candidate_length:
        cand = candidate[i]
        if cand not in voted_candidate:
            voted_candidate.append(cand)
        i = i + 1


    # Determine length of unique entry dataset
    voted_candidate_length = len(voted_candidate)
    

    # Calculate percent and total votes for each candidate    
    valmax = 0
    winner = ""
    j=0
    while j < voted_candidate_length:
        dup = voted_candidate[j]
        val = candidate.count(dup)
        percent = round((val/total_votes)*100,3)

        # Print candidate results
        candresult = (str(dup) + ": " + str(percent) + "% " + "(" + str(val) + ")")
        print(candresult)

        # Write candidte results
        results.write(candresult + "\n")


        # Determine the winner
        if val > valmax:
            valmax = val
            winner = dup
        j = j+1

    # Print winner
    print("-------------------")
    print("Winner: " + winner)
    print("-------------------")
    results.write("-------------------\n")
    results.write("Winner: " + winner + "\n")
    results.write("-------------------")