import os
import csv

root = os.path.dirname(os.path.abspath(__file__))
bank_csv = os.path.join(root, "Resources", "budget_data.csv")

def main ():
    dates_list,profits_list= get_columns(bank_csv)
    analysis_dir =os.path.join(root,"analysis")
    if not os.path.isdir(analysis_dir):
        os.mkdir(analysis_dir)
    output= os.path.join(analysis_dir,"analysis.txt")
    create_analysis (output,dates_list,profits_list)

def get_columns(csv_path):
    dates = []
    profits=[]
    with open (csv_path,"r") as fin:
        for line in fin:
            if 'Profit/Losses' in line:
                continue
            line_list=line.replace("\n","").split(",")
            dates.append(line_list[0])
            profits.append(int(line_list[1]))

    return dates,profits

def create_analysis(out, dates, profits):
    num_months = len(dates)

    total =0
    for profit in profits:
        total += profit

    dif_list = [profits[i+1]-profits[i] for i in range(len(profits)-1)]
    avg_change = 0
    for change in dif_list:
        avg_change += change
    avg_change /= len(dif_list)

    minimum=0
    min_date=""
    maximum=0
    max_date =""

    for date,dif in zip(dates[1:],dif_list):
        if dif<=minimum:
            minimum= dif
            min_date =date
        if dif>=maximum:
            maximum =dif
            max_date = date

    with open(out,"w")as fout:
        fout.write("Financial Analysis\n")
        fout.write("____________________\n")
        fout.write(f"Total Months: {num_months}\n")
        fout.write(f"Total: ${total}\n")
        fout.write(f"Average Change: ${round(avg_change,2)}\n")
        fout.write(f"Greatest Increase in Profits: {max_date} (${maximum})\n")
        fout.write(f"Greatest Decrease in Profits: {min_date} (${minimum})\n")

if __name__=="__main__":
    main()