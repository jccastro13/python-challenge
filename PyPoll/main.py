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
with open(os.path.join("analysis", "analysis.txt"),'w') as poll_analysis:

    print("Election Results")
    poll_analysis.write("Election Results\n")
    print("--------------------")
    poll_analysis.write("---------------\n")
    print("Total Votes: " + str(voter_count))
    poll_analysis.write("Total Votes: "+str(voter_count)+"\n")
    print("--------------------")
    poll_analysis.write("---------------\n")

    max_candidate_votes =0

    for candidate in candidate_list:
        percentage=round(float(candidate_list[candidate]/voter_count)*100,4)
        print(f"{candidate}: {percentage}% ({candidate_list[candidate]})")
        poll_analysis.write(f"{candidate}: {percentage}% ({candidate_list[candidate]})\n")

        if candidate_list[candidate] > max_candidate_votes:
            max_candidate_votes = candidate_list[candidate]
    for candidate in candidate_list:
        if candidate_list[candidate]==max_candidate_votes:
            print("_________________")
            poll_analysis.write("----------------\n")
            print("Winner: "+ str(candidate))
            poll_analysis.write("Winner: "+ str(candidate)+"\n")
            print("-----------------")
            poll_analysis.write("----------------\n")
