# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("C:/Users/navba/Desktop/GitHub/UT-Data-Analytics-Bootcamp/Homework/python-challenge/PyBank/", "budget_data_1.csv")
csvpath = os.path.join("C:/Users/navba/Desktop/GitHub/UT-Data-Analytics-Bootcamp/Homework/python-challenge/PyBank/", "budget_data_2.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through all rows to identify the month
    for row in csvreader
