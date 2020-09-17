import os
import csv
#Format
print("Financial Analysis")
print("-----------------------------------")
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period 
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
csvpath = os.path.join('', 'Resources', 'budget_data.csv')
total = 0
total_months = 0
max_increase = 0
max_decrease = 0
lst = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        total_months += 1
        total = total + int(row[1])       
        lst.append(row[1])
        num = int(row[1])
        if num > 0:
            if num > max_increase:
                increase_name = row[0]
                max_increase = num
        elif num < 0:
            if num < max_decrease:
                decrease_name = row[0]
                max_decrease = num     
    average = (int(lst[total_months-1])-int(lst[0]))/(total_months-1)
    formated_average = "{:.2f}".format(average) #https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
    print(f"Total Month: {total_months}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${formated_average}")
    print(f"Greatest Increase in Profits: {increase_name} (${max_increase})")
    print(f"Greatest Decrease in Profits: {decrease_name} (${max_decrease})")

# txt file
with open('main.txt','w') as txt:
    txt.write("Financial Analysis"+'\n')
    txt.write("-----------------------------------"+'\n')
    txt.write(f"Total Month: {total_months}"+'\n')
    txt.write(f"Total: ${total}"+'\n')
    txt.write(f"Average  Change: ${formated_average}"+'\n')
    txt.write(f"Greatest Increase in Profits: {increase_name} (${max_increase})"+'\n')
    txt.write(f"Greatest Decrease in Profits: {decrease_name} (${max_decrease})")