import os
import csv
csvpath = os.path.join('','Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # lines = len(list(csvreader)) # https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
    # total_months = lines -1
# print(f"Total Months: {total_months}")
    print(csvreader)

        


