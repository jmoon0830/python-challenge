import os
import csv

csvpath = os.path.join("Resources","election_data.csv")


votercount = 0
Khan = 0
Correy = 0
Li = 0
Otooley = 0

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        votercount += 1

        if (row[2]) == "Khan":
            Khan += 1
        elif (row[2]) == "Correy":
            Correy += 1
        elif (row[2]) == "Li":
            Li += 1
        elif (row[2]) == "O'Tooley":
            Otooley += 1

    percentkhan = (int(Khan)/int(votercount))*100
    percentcorrey = (int(Correy)/int(votercount))*100
    percentli = (int(Li)/int(votercount))*100
    percentotooley = (int(Otooley)/int(votercount))*100
    
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(votercount))
    print("-----------------------------")
    print("Khan: " + str(round(percentkhan,3)) + "% (" + str(Khan) + ")")
    print("Correy: " + str(round(percentcorrey,3)) +"% (" + str(Correy) + ")")
    print("Li: " + str(round(percentli,3)) + "% (" + str(Li) + ")")
    print("O'Tooley: " + str(round(percentotooley,3)) + "% (" + str(Otooley) + ")")
    print("----------------------------")
    popvote = [Khan,Correy,Li,Otooley]
    winnervote = max(popvote)
    if winnervote == Khan:
        winner = "Khan"
    elif winnervote == Correy:
        winner = "Correy"
    elif winnervote == Li:
        winner = "Li"
    elif winnervote == Otooley:
        winner = "O'tooley"
    print("Winner: " + winner)
    print("-----------------------------")

    output_path = os.path.join("analysis","analysis.txt")

    file1 = open(output_path,'w') 
    
    file1.write("Election Results\n")
    file1.write("-----------------------------\n")
    file1.write("Total Votes: " + str(votercount) + "\n")
    file1.write("-----------------------------\n")
    file1.write("Khan: " + str(round(percentkhan,3)) + "% (" + str(Khan) + ")\n")
    file1.write("Correy: " + str(round(percentcorrey,3)) +"% (" + str(Correy) + ")\n")
    file1.write("Li: " + str(round(percentli,3)) + "% (" + str(Li) + ")\n")
    file1.write("O'Tooley: " + str(round(percentotooley,3)) + "% (" + str(Otooley) + ")\n")
    file1.write("----------------------------\n")
    popvote = [Khan,Correy,Li,Otooley]
    winnervote = max(popvote)
    if winnervote == Khan:
        winner = "Khan"
    elif winnervote == Correy:
        winner = "Correy"
    elif winnervote == Li:
        winner = "Li"
    elif winnervote == Otooley:
        winner = "O'tooley"
    file1.write("Winner: " + winner + "\n")
    file1.write("-----------------------------")
