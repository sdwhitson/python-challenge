import os
import csv

csvpath= os.path.join("PyBank","Resources", "budget_data.csv")

#The total number of months included in the dataset

with open(csvpath) as month:
    month_reader = csv.reader(month)
    header = next(month_reader)

    num_months = 0

    for row in month_reader:
        if row[0]:
            num_months += 1
        
print("Total Months: ", num_months)

Total_Months ="Total Months: ", num_months

#The net total amount of "Profit/Losses" over the entire period
with open(csvpath) as pl:
    pl_reader = csv.reader(pl)
    header = next(pl_reader)

    total_pl= 0

    for row in pl_reader:
        total_pl+= int(row[1])

print("Total: ","$" + format(total_pl))
Total= "Total: ","$" + format(total_pl)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
with open(csvpath) as change:
    change_reader = csv.reader(change)
    header = next(change_reader)

    prev_pl = next(change_reader)
    change_pl =[]

    for row in change_reader:
        pl_change = int(row[1])-int(prev_pl[1])
        change_pl.append(pl_change)

    prev_pl = row

    avg_change = sum(change_pl) / len(change_pl)

    print("Average Change: $",str(round(avg_change,2)))

    Average_Change= "Average Change: ","$" + format(str(round(avg_change,2)))

#The greatest increase in profits (date and amount) over the entire period
with open(csvpath) as profit:
    profit_reader= csv.reader(profit)
    header = next(profit_reader)

    max_value = float("-inf")
    max_row = None

    for row in profit_reader:
        if float(row[1])> max_value:
            max_value = float(row[1])
            max_row = row

        
    if max_row is not None:

        print("Greatest Increase in Profits: ",max_row[0], "$" + format(max_row[1]))
        Greatest_Increase_in_Profits= "Greatest Increase in Profits: ",max_row[0], "$" + format(max_row[1])

# he greatest decrease in profits (date and amount) over the entire period
with open(csvpath) as loss:
    loss_reader= csv.reader(loss)
    header = next(loss_reader)

    max_loss = float("inf")
    min_row = None

    for row in loss_reader:
        if float(row[1])< max_loss:
            max_loss = float(row[1])
            min_row = row

        
    if min_row is not None:

        print("Greatest Decrease in Profits: ", min_row[0], "$" + format(min_row[1]))
        Greatest_Decrease_in_Profits = "Greatest Decrease in Profits: ", min_row[0], "$" + format(min_row[1])

#export a text file with the results.
Lines = [str(Total_Months), str(Total), str(Average_Change), str(Greatest_Increase_in_Profits), 
         str(Greatest_Decrease_in_Profits) ]
with open("PyBank_Results.txt","w") as file:
    for line in Lines:
        file.write(line)
        file.write("\n")

import shutil

shutil.move("Pybank_Results.txt", "PyBank/PyBank_Results.txt")
