# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# # Open budget data csv
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     csv_data = list(csvreader)
     month_count = len(csv_data)-1
     print(f"Total Month: {month_count}")
    # Loop through
    #for row in csvreader:
     