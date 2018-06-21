log_file = open("um-server-01.txt")
pick_day = input('Select day of week:')
print(pick_day)

# Setup function to capture sales report for given day
def sales_reports(log_file):
    # takes in each line of the file
    for line in log_file:
        # Returns a copy of the string with trailing characters removed.
        line = line.rstrip()
        # Takes the first three characters of the line which correspond
        # to the days of the week in this current file format
        # NOTE: [0:3] is NOT inclusive of the last position
        day = line[0:3]
        # only print the line if the day is a given day
        if day == "Mon":
            print(line)


def select_sales_report(log_file, pick_day):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]

        if day == pick_day:
            print(line)


# sales_reports(log_file)
select_sales_report(log_file, pick_day)