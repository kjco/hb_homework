std_melon_cost = 1.00


def get_customer_acct(acct_file, melon_price):
    ''' Take in a text file of customer orders and produces a list of
    underpaid customer orders.

    The input file acct_file should be in the following format for each entry:
    'entry number'|'Customer first name' 'Customer last name'|
    'purchased melon number'|'paid amount'
    Example:
        6|Phyllis Chapman|9|6.37

    The output of function generates a new text file with the format:
    'Customer first name' paid 'paid amount', expected 'expected amount'
    Example:
        Phyllis paid 6.37, expected 9.00
    '''

    the_file = open(acct_file)
    # consider checking for open file exceptions
    output_str = ''
    for line in the_file:
        line = line.rstrip()
        cust_info = line.split('|')
        cust_paid = float(cust_info[-1])
        cust_expected = float(cust_info[2])*melon_price
        if cust_expected > cust_paid:
            cust_info_str = ''
            cust_info_str = '{} paid {:.2f}, expected {:.2f}'.format(
                cust_info[1].split(' ')[0], cust_paid,
                cust_expected)
            output_str = output_str + cust_info_str + '\n'
    return output_str


underpaid_info = get_customer_acct('customer-orders.txt', std_melon_cost)
underpaid_file = open('underpaying_customers.txt', 'w+')
underpaid_file.write(underpaid_info)
underpaid_file.close()
