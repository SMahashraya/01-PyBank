# Import dependencies
import csv
import os

# Load csv file and create an output placeholder file
load_file = os.path.join("budget_data.csv")
output_file = os.path.join("budget_analysis.txt")

# Create lists and counters for each of the parameters in budget analysis
total_months = 0
month = []
net_change_list = []
greatest_inc_pnl = ["", 0]
greatest_dec_pnl = ["", 9999999999999999999]
net_pnl = 0


# Read csv and convert to list of dictionaries
with open(load_file) as budget_data:
    reader = csv.reader(budget_data)

    # Read header row
    header = next(reader)

    # Extract first row to avoid double-counting 
    first_row = next(reader)
    total_months = total_months + 1
    net_pnl = net_pnl + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total number of months and total net Profit and Losses
        total_months = total_months + 1
        net_pnl = net_pnl + int(row[1])

        # Track the net change in Profit and Losses
        net_change = 
        # testing


