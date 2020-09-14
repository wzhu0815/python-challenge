import os
import csv
#Format
print("Financial Analysis")
print("-----------------------------------")

#The total number of months included in the dataset
csvpath = os.path.join('', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    lines = len(list(csvreader)) # https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
    total_months = lines -1
    print(f"Total Month: {total_months}")

#The net total amount of "Profit/Losses" over the entire period 
total = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        total = total + int(row[1])
    print(f"Total: ${total}")

#The average of the changes in "Profit/Losses" over the entire period
list = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        list.append(row[1])
    average = (int(list[len(list)-1])-int(list[0]))/(len(list)-1)
    formated_average = "{:.2f}".format(average) #https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
    print(f"Average  Change: ${formated_average}")

#The greatest increase in profits (date and amount) over the entire period
max_increase = 0
max_decrease = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        num = int(row[1])
        if num > 0:
            if num > max_increase:
                increase_name = row[0]
                max_increase = num
        elif num < 0:
            if num < max_decrease:
                decrease_name = row[0]
                max_decrease = num     
print(f"Greatest Increase in Profits: {increase_name} (${max_increase})")
print(f"Greatest Decrease in Profits: {decrease_name} (${max_decrease})")