import os
import csv
#Format
print("Election Results")
print("-----------------------------------")

# The total number of votes cast
csvpath = os.path.join('', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    lines = len(list(csvreader)) # https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
    total_votes= lines -1
    print(f"Total Votes: {total_votes}")

# A complete list of candidates who received votes
candidate_list = []
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        if row[2] not in candidate_list: #https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
            candidate_list.append(row[2])

# The percentage of votes each candidate won
# The total number of votes each candidate won
counter = [0,0,0,0]
pct = []
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[2] == candidate_list[0]:
            counter[0] += 1
        elif row[2] == candidate_list[1]:
            counter[1] += 1
        elif row[2] == candidate_list[2]:
            counter[2] += 1
        elif row[2] == candidate_list[3]:
            counter[3] += 1
    pct = [x/int(total_votes) for x in counter] #https://stackoverflow.com/questions/6645357/doing-math-to-a-list-in-python
    pct = ["{:.3%}".format(x) for x in pct] #https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
    for i in range(4):
        print(f"{candidate_list[i]}: {pct[i]} ({counter[i]})")
print("-----------------------------------")


# The winner of the election based on popular vote.
max_pct = max(pct) #https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/
max_index = pct.index(max_pct) #https://www.programiz.com/python-programming/methods/list/index
winner_name = candidate_list[max_index]
print(f"Winner: {winner_name}")
print("-----------------------------------")
