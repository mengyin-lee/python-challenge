# Modules
import os
import csv

# month_total = 0
# net_total = 0
# pre_row = 0
# pre_change = 0
# change = 0
# greatest_change = 0
# least_change = 0
# change_total = 0
def write_analysis_csv():
     # Set path for file
     budgetpath = os.path.join("Resources", "budget_data.csv")
     # Lists to store data
     Date = []
     Profit_Loss = []
     Change = []

     # # Open budget data csv -- This section works
     with open(budgetpath) as csvfile:
          csvreader = csv.reader(csvfile, delimiter=",")
          header = next(csvreader)
          pre_row_amt = 0
          change_amt = 0
          count=0
          for row in csvreader:
               # Add Date
               Date.append(row[0])

               # Add Profit_Loss
               Profit_Loss.append(row[1])

               # Add Change
               count +=1
               if count == 1:
                    pre_row_amt = float(row[1])
               change_amt = float(row[1])-pre_row_amt
               pre_row_amt = float(row[1])
               Change.append(change_amt)

     # Zip lists together
     analysis_csv = zip(Date, Profit_Loss, Change)

     # Set variable for output file
     output_file = os.path.join("budget_analysis.csv")

     # Open the output file
     with open(output_file, "w", newline="") as datafile:
          writer = csv.writer(datafile)

          # Write the header row
          writer.writerow(["Date", "Profit_Loss", "Change"])

          # Write in zipped rows
          writer.writerows(analysis_csv)
if 1==1:
     write_analysis_csv

     analysispath = os.path.join(budget_analysis_data.csv")
ana_data = dict()
with open(analysispath, newline="") as anafile:
    csv_reader = csv.reader(anafile, delimiter = ",")
    csv_header = next(anafile)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            ana_data[0] = []
            ana_data[1] = []
            line_count += 1
            
    reader = csv.reader(anafile)
    data = list(reader)
    greatest = max(data, key)