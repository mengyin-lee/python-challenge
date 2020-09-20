# Modules
import os
import csv

# Set path for file
pollpath = os.path.join("Resource", "election_data.csv")


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
     voter_pct1 = "{:.3%}".format(voter_cnt1/total_votes)
     voter_pct2 = "{:.3%}".format(voter_cnt2/total_votes)
     voter_pct3 = "{:.3%}".format(voter_cnt3/total_votes)
     voter_pct4 = "{:.3%}".format(voter_cnt4/total_votes)

polloutpath = os.path.join("poll_w_votes.csv")

with open(polloutpath, 'w', newline="") as csvfile:

     csvwriter = csv.writer(csvfile, delimiter= ',')

     csvwriter.writerow(["Khan", voter_cnt1, voter_pct1])
     csvwriter.writerow(["Correy", voter_cnt2, voter_pct2])
     csvwriter.writerow(["Li", voter_cnt3, voter_pct3])
     csvwriter.writerow(["O'Tooley", voter_cnt4, voter_pct4])

# Open poll votes
# Find winner
pollvotespath = os.path.join("poll_w_votes.csv")

with open(pollvotespath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     max_vote = 0
     max_pct = 0
     winner = ""

     for row in csvreader:
          if float(row[1]) > float(max_vote):
               winner = row[0]
               max_vote = row[1]
               max_pct = row[2]
                   
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------")
print(f"Khan: {voter_pct1} ({voter_cnt1})")
print(f"Correy: {voter_pct2} ({voter_cnt2})")
print(f"Li: {voter_pct3} ({voter_cnt3})")
print(f"O'Tooley: {voter_pct4} ({voter_cnt4})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

summary_file = os.path.join("analysis", "PyPollSummary.txt")
with open(summary_file, "w", newline = "") as summary_file:
     # writer = csv.writer(summary_file)
     # writer.writerow([])
     summary_file.write("Election Results\n")
     summary_file.write("-------------------------------------\n")
     summary_file.write(f"Total Votes: {total_votes}\n")
     summary_file.write("-------------------------------------\n")
     summary_file.write(f"Khan: {voter_pct1} ({voter_cnt1})\n")
     summary_file.write(f"Correy: {voter_pct2} ({voter_cnt2})\n")
     summary_file.write(f"Li: {voter_pct3} ({voter_cnt3})\n")
     summary_file.write(f"O'Tooley: {voter_pct4} ({voter_cnt4})\n")
     summary_file.write("-------------------------------------\n")
     summary_file.write(f"Winner: {winner}\n")
     summary_file.write("-------------------------------------\n")
