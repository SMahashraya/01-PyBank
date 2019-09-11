# Import dependencies
import csv
import os

# Load csv file and create an output placeholder file
load_file = os.path.join("budget_data.csv")
output_file = os.path.join("budget_analysis.txt")

# Create lists and counters for each of the parameters in your budget analysis
total_months = 0
month = []
net_d_pnl = []
greatest_inc_pnl = ["", 0]
greatest_dec_pnl = ["", 9999999999999999999]
total_net_d = 0


# Read csv and convert to list of dictionaries
with open(load_file) as budget_data:
    reader = csv.reader(budget_data)

    # Read header row
    header = next(reader)

    # Extract first row
    first_row = next(reader)
    total_months = total_months + 1
    net_pnl = net_d_pnl + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total number of months and total net Profit and Losses
        total_months = total_months + 1
        net_pnl = net_pnl + int(row[1])


