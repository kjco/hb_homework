# Function will pass in a file and output a string (or 3 variables?)
import os


def melon_report(melon_file):
    the_file = open(melon_file)
    f_name = os.path.basename(the_file.name)
    # Extract date from the filename, e.g.,
    # `20140519` from `um-deliveries-20140519.txt`.
    f_name_parse = f_name.split('.')
    f_date = f_name_parse[0].split('-')[-1]
    print('Delivery date: '+str(f_date))
    
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print('Delivered {} {}s for total of ${}'.format(
            count, melon, amount))
    the_file.close()


melon_report('um-deliveries-20140519.txt')
