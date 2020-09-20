# A copy from PyBank to start with
# Modules
import os
import csv


def poll_analysis_csv():
     # Set path for file
     pollpath = os.path.join("Resource", "election_data.csv")
     # Lists to store data
     #poll = dict()

     # # Open poll data csv -- This section works
     with open(pollpath) as csvfile:
          csvreader = csv.reader(csvfile, delimiter=",")
          csv_header = next(csvreader)

          voter_cnt1 = 0
          voter_cnt2 = 0
          voter_cnt3 = 0
          voter_cnt4 = 0
          i=0

          for row in csvreader:
               if(row[2].strip()== "Khan"):
                    voter_cnt1 += 1
                    i += 1
               elif (row[2].strip() == "Correy"):
                    voter_cnt2 += 1
                    i += 1
               elif (row[2].strip() == "Li"):
                    voter_cnt3 += 1
                    i += 1
               elif (row[2].strip() == "O'Tooley"):
                    voter_cnt4 += 1
                    i += 1
               else:
                    i += 1

          total_votes = i
          voter_pct1 = voter_cnt1/total_votes*100
          voter_pct2 = voter_cnt2/total_votes*100
          voter_pct3 = voter_cnt3/total_votes*100
          voter_pct4 = voter_cnt4/total_votes*100
          
          print(f"i : {i}")
          print(f"cnt1 : {voter_cnt1}")
          print(f"cnt2 : {voter_cnt2}")
          print(f"cnt3 : {voter_cnt3}")
          print(f"cnt4 : {voter_cnt4}")

if 1==1:
     poll_analysis_csv()

#      # Zip lists together
#      analysis_csv = zip(Date, Profit_Loss, Change)

#      # Set variable for output file
#      output_file = os.path.join("budget_analysis.csv")

#      # Open the output file
#      with open(output_file, "w", newline="") as datafile:
#           writer = csv.writer(datafile)

#           # Write the header row
#           writer.writerow(["Date", "Profit_Loss", "Change"])

#           # Write in zipped rows
#           writer.writerows(analysis_csv)
# if 1==1:
#      write_analysis_csv

# analysispath = os.path.join(budget_analysis_data.csv")
# ana_data = dict()
# with open(analysispath, newline="") as anafile:
#     csv_reader = csv.reader(anafile, delimiter = ",")
#     csv_header = next(anafile)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             ana_data[0] = []
#             ana_data[1] = []
#             line_count += 1
            
#     reader = csv.reader(anafile)
#     data = list(reader)
#     greatest = max(data, key)