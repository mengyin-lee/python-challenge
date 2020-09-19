# Modules
import os
import csv

month_total = 0
net_total = 0
pre_row = 0
pre_change = 0
change = 0
greatest_change = 0
least_change = 0
change_total = 0

# Set path for file
budgetpath = os.path.join("Resources", "budget_data.csv")

# # Open budget data csv -- This section works
with open(budgetpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     header = next(csvreader)
     count=0
     for row in csvreader:
          count +=1
          if count == 1:
               pre_row = float(row[1])
               pre_change = float(row[1])-pre_row

          month_total +=1
          net_total += float(row[1])
             
          change = float(row[1])-pre_row

          # print(f"pre {pre_change}")
          # print(f"change {change}")
          # if (change >= 0 and change >= pre_change):
          #      greatest_change = change
          # elif(change < 0 and change < pre_change):
          #      least_change = change

          # pre_change = change  
          # print(f"greatest {greatest_change}")
          # print(f"least {least_change}")
          # print(f"post pre {pre_change}")
          # print(f"post pre {pre_change}")

          # print(f"post change {change}")

          #print(change)
          pre_row = float(row[1])
          change_total += change

     avg_change = change_total/(month_total-1)
     greatest_change = max(change)
     least_change = min(change)

     print(f"The total month: {month_total}")
     print(f"The total net: {net_total}")
     print(f"change tot: {change_total}")
     print(f"The avg: {avg_change}")
     print(f"greatest: {greatest_change}")
     print(f"greatest: {least_change}")
     
     # budget_data = list(csvreader)
     # month_count = len(csv_data)- 1
     # net_total = 
     #print(f"Total Month: {month_count}")
    # Loop through
    #for row in csvreader:

     