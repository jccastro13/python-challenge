import os
import csv
voter_count=0
candidate_list={}


with open(os.path.join("Resources", "election_data.csv"),'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)


    for row in csvreader:
        candidate = row[2]
        voter_count+=1

        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate]= 1

print("Election Results")
print("--------------------")
print("Total Votes: " + str(voter_count))
print("--------------------")

max_candidate_votes =0

for candidate in candidate_list:
    print(candidate + "("+ str(candidate_list[candidate])+")")
    print(round(float(candidate_list[candidate]/voter_count)*100,4))

    if candidate_list[candidate] > max_candidate_votes:
        max_candidate_votes = candidate_list[candidate]
for candidate in candidate_list:
    if candidate_list[candidate]==max_candidate_votes:
        print("_________________")
        print("Winner: "+ str(candidate))
        print("-----------------")

