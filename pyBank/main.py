import os
import csv



months = []
totalRevenue = 0
lastNum = 0
monthlyChangeDict = {}
totalChange = 0 


csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csvreader, None)

    #create month list and monthly change
    for row in csvreader:
        
        totalRevenue = totalRevenue + int(row[1])
        
        #add month to list
        if row[0] not in months:
            months.append(row[0])
            #calculate monthly change
            monthlyChangeDict[row[0]] = int(row[1]) - lastNum
            lastNum =  int(row[1])

#calculate total monthly change for average revenue change
for key, value in monthlyChangeDict.items():
    #skip first month
    if key == months[0]:
        num = 0
    else:
        
        totalChange = totalChange + value
        

#find min and max in monthly revenue change
min_price = min(zip(monthlyChangeDict.values(), monthlyChangeDict.keys()))
max_price = max(zip(monthlyChangeDict.values(), monthlyChangeDict.keys()))


#print out results to screen

line = "-------------------------------"
results = (
    "Financial Analysis" +'\n' + line +'\n'
    "Total Months: "+ str(len(months)) +'\n'
    "Total : $"+ str(totalRevenue) +'\n'
    "Average Change: $"+ str(int(totalChange/(len(months) - 1))) +'\n'
    "Greatest Increase in Profits: "+ str((max_price[1] + " $" + str(int(max_price[0])))) +'\n'
    "Greatest Decrease in Profits: "+ str((min_price[1] + " $" + str(int(min_price[0])))) +'\n' + line +'\n'
    )

print(results)

#create output file
file = open("pyBankResult.txt", "w")
file.write(results)
file.close()