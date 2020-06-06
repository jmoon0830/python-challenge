import csv
import os

#path the csv file to the main file
csvpath = os.path.join("Resources","budget_data.csv")

monthcount = 0
netprofit = 0
montharray = []
profitarray = []

#open the csv file
with open(csvpath) as csvfile:

    #define csv reader and separates the strings by comma
    csvreader = csv.reader(csvfile, delimiter = ",")
    #unnecessary
    print(csvreader)

    #defining the csvheader as the first row in csvreader
    csvheader = next(csvreader)
    #returns the csv header 
    print(f"CSV Header: {csvheader}")

    #prints every row in csvreader
    for row in csvreader:
        monthcount = monthcount + 1
        netprofit = netprofit + int(row[1])
        if monthcount == 1:
            begyr = int(row[1])
        if monthcount == 86:
            finalyr = int(row[1])
        profitarray.append(row[1])
        montharray.append(row[0])
    finalmax = 0
    for i in range(len(profitarray)-1):
        testmax = int(profitarray[i+1]) - int(profitarray[i])
        if testmax > finalmax:
            finalmax = testmax
            monthmax = montharray[i+1]
    finalmin = 0
    for i in range(len(profitarray)-1):
        testmin = int(profitarray[i+1]) - int(profitarray[i])
        if testmin < finalmin:
            finalmin = testmin
            monthmin = montharray[i+1]
        
    avgchange = (finalyr - begyr)/(monthcount-1)

    print("Financial Analysis")
    print("----------------------")
    print("Total Months: " + str(monthcount))
    print("Total: $" + str(netprofit))
    print("Average Change: $" + str(round(avgchange,2)))
    print("Greatest Increase in Profits: " + str(monthmax))
    print("($" + str(finalmax) + ")")
    print("Greatest Decrease in Profits: " + str(monthmin))
    print("($" +str(finalmin) + ")")

    output_path = os.path.join("analysis","analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
    file1 = open(output_path, 'w')
    file1.write("Financial Analysis\n")
    file1.write("----------------------\n")
    file1.write("Total Months: " + str(monthcount) + "\n")
    file1.write("Total: $" + str(netprofit) + "\n")
    file1.write("Average Change: $" + str(round(avgchange,2)) + "\n")
    file1.write("Greatest Increase in Profits: " + str(monthmax) + "\n")
    file1.write("($" + str(finalmax) + ")\n")
    file1.write("Greatest Decrease in Profits: " + str(monthmin) + "\n")
    file1.write("($" +str(finalmin) + ")\n")