import os
import csv
from collections import defaultdict

#Declarations
votecount = 0
results_d = defaultdict(int)
p_temp = 0

#Read file in
ifile_path = os.path.join("Resources", "election_data.csv")
ifile_obj = open(ifile_path, mode='r')
reader_obj = csv.reader(ifile_obj)
next(reader_obj)  #move below header

#Main loop
for row_ls in reader_obj:

    #increment count of votes
    if row_ls[0] != "":
        votecount = votecount + 1
    results_d[str(row_ls[2])] += 1

#~~~set this value to rig the election~~~
#results_d['Bernie S.'] = 10000000

#look through results for winner, print & write results
with open("Election Results.txt","w", newline="") as ofile_obj:
    
    print("Election Results")
    print("--------------------")
    print("Total Votes:", votecount)
    print("--------------------")
    
    ofile_obj.write("Election Results\n")
    ofile_obj.write("--------------------\n")
    ofile_obj.write("Total Votes: "+str(votecount)+"\n")        
    ofile_obj.write("--------------------\n")
    
    for candidate in results_d:
        #calculate the winner
        percentage = float(results_d[candidate])/(votecount)*100
        if percentage > p_temp:
            winner = str(candidate)
            p_temp = percentage
        
        perc_str = str("{:.2f}%".format(percentage))
        print (candidate + ": " + perc_str + " (" + str(results_d[candidate]) + ")")
        ofile_obj.write(str(candidate)+": " + perc_str + " (" + str(results_d[candidate]) + ")\n")

    
    print("--------------------")
    print("Winner: " + winner)
    print("--------------------")
    
    ofile_obj.write("--------------------\n")
    ofile_obj.write("Winner: " + winner + "\n")   
    ofile_obj.write("--------------------\n")

ofile_obj.close() 
