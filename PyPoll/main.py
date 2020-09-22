import os
import csv
import numpy as np
#Format
print("Election Results")
print("-----------------------------------")
csvpath = os.path.join('Resources', 'election_data.csv') 
# The total number of votes cast
# A complete list of candidates who received votes
total_votes = 0
candidate_list = []
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate_list: #https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
            candidate_list.append(row[2])
print(f"Total Votes: {total_votes}")
print("-----------------------------------")

# The percentage of votes each candidate won
# The total number of votes each candidate won
counter = np.zeros(len(candidate_list)) #https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
pct = []
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        for i in range(len(candidate_list)):
            if row[2] == candidate_list[i]:
                counter[i] += 1
        #old code below:
        # if row[2] == candidate_list[0]:
        #     counter[0] += 1
        # elif row[2] == candidate_list[1]:
        #     counter[1] += 1
        # elif row[2] == candidate_list[2]:
        #     counter[2] += 1
        # elif row[2] == candidate_list[3]:
        #     counter[3] += 1
    pct = [x/int(total_votes) for x in counter] #https://stackoverflow.com/questions/6645357/doing-math-to-a-list-in-python
    pct = ["{:.3%}".format(x) for x in pct] #https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {pct[i]} ({int(counter[i])})")
print("-----------------------------------")


# The winner of the election based on popular vote.
max_pct = max(pct) #https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/
max_index = pct.index(max_pct) #https://www.programiz.com/python-programming/methods/list/index
winner_name = candidate_list[max_index]
print(f"Winner: {winner_name}")
print("-----------------------------------")

# txt file
with open('main.txt','w') as txt:
    txt.write("Election Results"+'\n')
    txt.write("-----------------------------------"+'\n')
    txt.write(f"Total Votes: {total_votes}"+'\n')
    txt.write("-----------------------------------"+'\n')
    for i in range(len(candidate_list)):
        txt.write(f"{candidate_list[i]}: {pct[i]} ({int(counter[i])})"+'\n')
    txt.write(f"-----------------------------------"+'\n')
    txt.write(f"Winner: {winner_name}"+'\n')
    txt.write("-----------------------------------")
