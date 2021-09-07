# -*- coding: UTF-8 -*-
"""
PyPoll Homework Challenge Solution

1. Calculate the total number of votes cast
2. Calculate the total number of votes and percentage each county received
3. List the county with the largest voter turnout
4. Calculate the total number of votes and percentage each candidate received
5. Determine the winner of the election based on popular vote

"""

# Add our dependencies.
import csv
import os
from collections import Counter


def exit_script():
    """
    Exit script if exception is found
    """
    print("exiting script")
    exit()


# remove hard-coded reference to source file name
# get list of data files residing in folder
_, _, data_files = next(os.walk(top='resources'))

# return list csv files
csv_file_list = list(filter(lambda x: x.endswith('.csv'), data_files))

# set election filename variable if csv file found
if len(csv_file_list) > 0:
    election_filename = csv_file_list[0]
else:
    print("election source file(s) not found.")
    exit_script()

if election_filename is not None:
    file_to_load = os.path.join("resources", election_filename)
else:
    print("invalid source file.")
    exit_script()

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "all_election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Create dictionary to store both candidate and county votes
election_results = {
    'counties': {},
    'candidates': {}
}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row["Candidate"]

        # 3: Extract the county name from each row.
        county_name = row["County"]

        # If the candidate does not match any existing candidate add it to the candidate dictionary
        if candidate_name not in election_results['candidates'].keys():
            # And begin tracking that candidate's voter count.
            election_results['candidates'][candidate_name] = 0

        # If county does not match any existing county in the county list, add it to counties dictionary
        if county_name not in election_results['counties'].keys():
            # 4b: Add the existing county to the list of counties.
            election_results['counties'][county_name] = 0

        # 5: Add a vote to the candidate and county's vote counts.
        election_results['candidates'][candidate_name] += 1
        election_results['counties'][county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results_output = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results_output, end="")

    txt_file.write(election_results_output)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in election_results['counties'].keys():
        # 6b: Retrieve the county vote count.
        c_votes = election_results['counties'].get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        c_vote_pct = float(c_votes) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = f"{county_name}: {c_vote_pct:.1f}% ({c_votes:,})\n"
        print(county_results, end="")

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

    # Get winning county name and voter turnout
    winning_county = Counter(election_results['counties']).most_common(1)
    winning_county_name = winning_county[0][0]
    winning_county_count = winning_county[0][1]
    winning_county_percentage = float(winning_county_count) / float(total_votes) * 100

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"\n-------------------------------------\n"
        f"Largest County Turnout: {winning_county_name}\n"
        f"-------------------------------------\n\n")
    print(winning_county_summary, end="")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in election_results['candidates'].keys():
        # Retrieve vote count and percentage
        votes = election_results['candidates'].get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results, end="")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate = Counter(election_results['candidates']).most_common(1)
    winning_candidate_name = winning_candidate[0][0]
    winning_candidate_count = winning_candidate[0][1]
    winning_candidate_pct = float(winning_candidate_count) / float(total_votes) * 100

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n-------------------------------------\n"
        f"Winner: {winning_candidate_name}\n"
        f"Winning Vote Count: {winning_candidate_count:,}\n"
        f"Winning Percentage: {winning_candidate_pct:.1f}%\n"
        f"-------------------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

