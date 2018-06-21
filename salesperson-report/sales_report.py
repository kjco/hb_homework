"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []
sales_report_dict = {}

# Open file
f = open("sales-report.txt")

# Read the file line by line, splitting by the | character.
# The 0th element is the salesperson. The 2nd element is the amt of melons sold.

for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])

    # Add salespeople into a dictionary as the keys.
    # If the salesperson does not exist in the dictionary, 
    # initialize with first entry of melons sold as corresponding value.

    if salesperson not in sales_report_dict:
        sales_report_dict[salesperson] = melons

    # If the salesperson already exists in dictionary,
    # add new melon count to previous melon count value

    elif salesperson in sales_report_dict:
        sales_report_dict[salesperson] += melons

# Iterate through the dictionary and print total number of melons
# each sales person sold.

# for person, melon_amt in sales_report_dict.items():
#     print("{} sold {} melons".format(person, melon_amt))

for person in sorted(sales_report_dict.keys()):
    print("{} sold {} melons".format(person, sales_report_dict[person]))