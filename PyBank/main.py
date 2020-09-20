# Modules
import sys
import os
import csv

def write_analysis_csv():
     # Set path for file
     budgetpath = os.path.join("Resources", "budget_data.csv")
     # Lists to store data
     Date = []
     Profit_Loss = []
     Change = []

     # # Open budget data csv 
     with open(budgetpath) as csvfile:
          csvreader = csv.reader(csvfile, delimiter=",")
          csv_header = next(csvreader)
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
     output_file = os.path.join("budget_w_change.csv")

     # Open the output file
     with open(output_file, "w", newline="") as datafile:
          writer = csv.writer(datafile)

          # Write the header row
          writer.writerow(["Date", "Profit_Loss", "Change"])

          # Write in zipped rows
          writer.writerows(analysis_csv)
     # Run the function to create a csv file with change amount column
if 1==1:
     write_analysis_csv()

analysispath = os.path.join("budget_w_change.csv")
ana_data = dict()
with open(analysispath, newline="") as anafile:
    csv_reader = csv.reader(anafile, delimiter = ",")
    csv_header = next(anafile)
    line_count = 0
    ana_data[0] = []
    ana_data[1] = []
    ana_data[2] = []
    for row in csv_reader:
        ana_data[0].append(row[0])
        ana_data[1].append(float(row[1]))
        ana_data[2].append(float(row[2]))
        line_count += 1

def get_date_mth(change_num):
    getpath = os.path.join("budget_w_change.csv")
    with open(getpath, newline="") as file:
        csv_reader = csv.reader(file, delimiter = ",")
        csv_header = next(file)
        for row in csv_reader:

            if float(row[2]) == float(change_num):
                return row[0]

max_num = max(ana_data[2])
max_mth = str(get_date_mth(max_num))
min_num = min(ana_data[2])
min_mth = str(get_date_mth(min_num))
total_months = line_count
total_amt = sum(ana_data[1])
total_avg_amt = sum(ana_data[2])
Average_chg = total_avg_amt/(line_count-1)

# Print the result to terminal and write to a summary file

print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amt}")
print(f"Average Change: ${Average_chg}")
print(f"Greatest Increase in Profits: {max_mth} (${max_num})")
print(f"Greatest Increase in Profits: {min_mth} (${min_num})")


summary_file = os.path.join("analysis", "PyBankSummary.txt")
with open(summary_file, "w", newline = "") as summary_file:
     # writer = csv.writer(summary_file)
     # writer.writerow([])
     summary_file.write("Financial Analysis\n")
     summary_file.write("--------------------------------------------------------\n")
     summary_file.write(f"Total Months: {total_months}\n")
     summary_file.write(f"Total: ${total_amt}\n")
     summary_file.write(f"Average Change: ${Average_chg}\n")
     summary_file.write(f"Greatest Increase in Profits: {max_mth} (${max_num})\n")
     summary_file.write(f"Greatest Increase in Profits: {min_mth} (${min_num})\n")
