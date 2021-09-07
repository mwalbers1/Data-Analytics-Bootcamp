# Election Analysis

## Project Overview
The Board of Elections employee has given you the following task to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Calculate the total number of votes and percentage each county received
3. List the county with the largest voter turnout
4. Calculate the total number of votes and percentage each candidate received
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.8, JetBrains PyCharm 2021.2.1

## Summary

The analysis of the election shows that:
- There were 369,711 votes cast in the election

- The counties were:
  - Jefferson
  - Denver
  - Arapahoe

- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The county turnout was:
  - Jefferson received 10.5% of the votes and 38,855 votes
  - Denver received 82.8% of the votes and 306,055 votes
  - Arapahoe received 6.7% of the votes and 24,801 votes

- The largest county turnout was Denver

- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
    - Diana DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes

- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 votes

## Election Audit Summary

This script can be used for any election by making the following modifications: 

- Update the Python script to handle any source CSV file that is placed into a folder.

- Combine the election data for candidates and counties into a single Python dictionary to allow the script to be easier to maintain.

- Load election candidates and counties directly into the `election_results` dictionary, instead of first loading a list and then populating the dictionary from the list. This will allow the script run more efficiently.

- Use the csv.DictReader class when loading the `election_results` dictionary from the source csv file.

Each change is described in detail below.

### Election source file

The election source file will be read in from a folder and it can have any name along with a CSV extension.

```python
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
```

### Load county and candidate votes into single Dictionary

A new dictionary called election_results will contain two nested dictionaries, one for counties and the other for candidates.  This will make the script more readable and easier to maintain.

```python
# Create dictionary to store both candidate and county votes
election_results = {
    'counties': {},
    'candidates': {}
}
```

### Read CSV records directly into Python Dictionary

The candidates and counties no longer need to be read into a list before populating the dictionary for candidates and counties.

```python
# If the candidate does not match any existing candidate add it to the candidate dictionary
        if candidate_name not in election_results['candidates'].keys():
            # And begin tracking that candidate's voter count.
            election_results['candidates'][candidate_name] = 0

        # If county does not match any existing county in the county list, add it to counties dictionary
        if county_name not in election_results['counties'].keys():
            # 4b: Add the existing county to the list of counties.
            election_results['counties'][county_name] = 0
```

### csv.DictReader

The csv.DictReader class can reference specific column names from the csv file header which makes code easier to read and maintain.

```python
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
```
<br/>

The modified script is called **PyPoll_All_Elections.py**
