# Modules
import os
import csv

# Set path for file
budget_data1_csv = os.path.join("C:/Users/navba/Documents/GitHub/UT-Data-Analytics-Bootcamp/Homework/python-challenge/PyBank/", "budget_data_1.csv")
budget_data2_csv = os.path.join("C:/Users/navba/Documents/GitHub/UT-Data-Analytics-Bootcamp/Homework/python-challenge/PyBank/", "budget_data_2.csv")
#^^^ Maybe getcwd instead??

# Create dictionary for total months
total_months = []

# Create variable to store total revenue value
total_revenue = 0

# Create a list to hold average revenue differences
average_revenue_chg = []

# Open the budget_data_1 csv
with open(budget_data1_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header rows
    next(csvfile)

    # Loop through all rows to identify the month
    for row in csvreader:

        ## Count total months by splitting first row elements and comparing to other months
        ## It will only count if the month is unique

        # Isolate the sub-elements within the row elements for comparison
        date_list = row[0].split("-")
        month = date_list[0]
        #date = date_list[1]
        #year = date_list[2]

        # Comparison conditional if current month not already in the total_months list
        if month not in total_months:
            total_months.append(month)

        # count total revenue
        total_revenue = total_revenue + int(row[1])

# Open the budget_data_2 csv
with open(budget_data2_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header rows
    next(csvfile)

    # Loop through all rows to identify the month
    for row in csvreader:

        ## Count total months by splitting first row elements and comparing to other months
        ## It will only count if the month is unique

        # Isolate the sub-elements within the row elements for comparison
        date_list = row[0].split("-")
        month = date_list[0]
        #date = date_list[1]
        #year = date_list[2]

        # Comparison conditional if the current month is not already in the total_months list


        # count total revenue
        total_revenue = total_revenue + int(row[1])

print(total_months)

# Print outputs
print()
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(len(total_months))) #suppose to be 12 (budget 1) + 86 (budget 2) = 98 total months
print("Total Revenue: $" + str(total_revenue))

# Write the outputs to another .csv file
