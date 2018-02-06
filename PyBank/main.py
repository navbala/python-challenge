# Modules
import os
import csv
import datetime
import numpy as np

# Set path for file
dataset1_csv = os.path.join("C:/Users/navba/Desktop/GitHub/python-challenge/PyBank/", "budget_data_1.csv")
dataset2_csv = os.path.join("C:/Users/navba/Desktop/GitHub/python-challenge/PyBank/", "budget_data_2.csv")
#^^^ Maybe getcwd instead??


# Create list for total months
date_list = []

# Create variable to store total revenue value
total_revenue = 0

# Create dictionary for months and corresponding Count
month_rev= {}

# Create variables and lists pertaining to revenue data calculations
rev_delta = 0
avg_rev_delta = 0
rev_list = []
rev_deltas = []


# Open and read the first data set
with open(dataset1_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header rows
    next(csvfile)

    # Loop through all rows to identify the month
    for row in csvreader:

        # Convert the data string into a date element and add the to date_list
        d = datetime.datetime.strptime(row[0], "%b-%y").date()

        # Conditional statement for adding revnue deltas to a list aadd the dictionary to hold month delta/revenue values
        cur_rev = int(row[1])

        # Count total revenue
        total_revenue = total_revenue + cur_rev

        # Add date and rev to month_rev dictionary
        month_rev[d] = cur_rev


# Open and read the second data set
with open(dataset2_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header rows
    next(csvfile)

    # Loop through all rows to identify the month
    for row in csvreader:

        # Conditional statement for adding revnue deltas to a list aadd the dictionary to hold month delta/revenue values
        cur_rev = int(row[1])

        # Convert the data string into a date element and add the to data date_list
        d = datetime.datetime.strptime(row[0], "%b-%Y").date()

        # Check to see if date it already in date_list from running through first dataset
        ## If it exts, add the value of the rev to the existing value for the date key. Else, append to the dict.
        if d in month_rev:
            month_rev[d] += cur_rev
        else:
            month_rev[d] = cur_rev

        # Count total revenue
        total_revenue = total_revenue + int(row[1])


# Order the month_rev dict and create the dictionary for the ordered list of tuples
ordered = sorted(month_rev.items(), key = lambda t:t[0])
ordered_dict = {}

# Add the tuple pairs comprising the ordered list into a new dictionary
for (x,y) in ordered:
    ordered_dict[x] = y

# Append the date keys from the ordered_dict to a new date list and a new revenue list
for date in ordered_dict:
    date_list.append(date)
    rev_list.append(ordered_dict[date])

# Calculate the revenue deltas between months and append the values to new revenue deltas list
for i in range(len(rev_list)-1):
    rev_delta = rev_list[i+1] - (rev_list[i])
    rev_deltas.append(rev_delta)

# Calculate the mean from rev_deltas list
avg_rev_delta = np.mean(rev_deltas)

# Create another dictionary by zipping the dates list and rev_deltas
## Add a zero value in the first index of the list so that the first date of the dict has no deltas
rev_deltas.insert(0, 0)

# Zip up the date_list and rev_deltas list to make a dictionary with the months and correspoding revenue deltas
date_rev_dict = dict(zip(date_list, rev_deltas))

# Retrieve the max values in the date_rev_dict to identify the date with greatest revenue increase
## Format the datetime month-year
max_date = max(date_rev_dict, key=date_rev_dict.get)
max_date_formatted = max_date.strftime("%b-%y")
max_rev = date_rev_dict[max_date]

# Retrieve the max values in the date_rev_dict to identify the date with greatest revenue decrease
## Format the datetime month-year
min_date = min(date_rev_dict, key=date_rev_dict.get)
min_date_formatted = min_date.strftime("%b-%y")
min_rev = date_rev_dict[min_date]


# Print outputs to terminal
print()
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(len(month_rev)))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(int(avg_rev_delta)))
print("Greatest Increase in Revenue: " + str(max_date_formatted) + " " + "($" + str(max_rev) + ")")
print("Greatest Decrease in Revenue: " + str(min_date_formatted) + " " + "($" + str(min_rev) + ")")

# Write the outputs to .csv file
