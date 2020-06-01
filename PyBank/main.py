import csv
import os

#path the csv file to the main file
csvpath = os.path.join("Resources","budget_data.py")

#open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

    csvheader = next(csvreader)
    print(f"CSV Header: {csv_header}")