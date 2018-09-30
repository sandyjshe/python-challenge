import os
import csv

totalVotes = 0
candidates = []
voteCountDict = {}
votePercDict = {}
result = ""
space = "-------------------------------"

#path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join("Resources", "election_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvreader, None)
    
    
    #calculate totalVotes and list candidates
    for row in csvreader:
        
        totalVotes = totalVotes + 1        

        #if row[2] not in candidates and row[2] not in "Candidate":
        if row[2] not in candidates:
            candidates.append(row[2])
            voteCountDict[row[2]] = 1
        #elif row[2] in candidates and row[2] not in "Candidate":
        elif row[2] in candidates:
            voteCountDict[row[2]] = voteCountDict[row[2]] + 1

    #calculate percent OF totalVotes
    for key, value in voteCountDict.items():
        votePercDict[key] = str(round(((value/totalVotes)*100),3)) + "% ("+str(value) + ")"
    
    #find winner
    winner = max(voteCountDict, key=(lambda k: voteCountDict[k])) 

    
    #put candidate result into one single variable
    for key, val in votePercDict.items():
        result = result + key + ": " + val + '\n'
   
   #print result to screen
    print("Election Results" + '\n' + space + '\n' + "Total Votes: "+ str(totalVotes)+ '\n' + space + '\n')
    print(result)
    print(space + '\n'+ "Winner: "+ str(winner)+ '\n' + space + '\n')

   #create output file 
    file = open("pyPollResult.txt", "w")

    file.write("Election Results" + '\n' + space + '\n' + "Total Votes: "+ str(totalVotes)+ '\n' + space + '\n')
    file.write(result)
    file.write(space + '\n'+ "Winner: "+ str(winner)+ '\n' + space + '\n')
    
    file.close()