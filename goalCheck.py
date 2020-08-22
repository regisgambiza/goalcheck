# This script is used to carry out goal check
import time


# Functions
def checker(d_code, description):
    response = input(description)
    if response == 'n':
        code_list.append(d_code)


# Dictionaries of all codes and descriptions
h_book_dict = {
    'HWB != sign': 'Is the book signed by the parent?:',
    'NTP': 'Is the total number of pages indicated?:',
    'HWK != ind': 'Is homework indicated?:',
    'G != set': 'Are goals indicated, neat and properly set?:'
}
goal_card_dict = {
    'G != set': 'Are goals written?:',
    'NTP': 'Is total number of pages written?:'
}
pace_check_dict = {
    'Goal incomp': 'Was the goal completed?:',
    'Pages not circled': 'Are all pages circled?:'
}

# Create a list of all codes
code_list = []


# Print welcome message
print('\n')
print('***** Welcome to GOAL CHECK *****')
print('***** Created by Baddaz Tech *****')
time.sleep(3)
print('\n')

# Start the actual goal check
print('********* HOMEWORK BOOK CHECKING *********')
for x, y in h_book_dict.items():
    checker(x, y)
print('\n')


# Checking the goal card
print('********* GOAL CARD CHECKING *********')
for x, y in goal_card_dict.items():
    checker(x, y)
print('\n')
print('*** Is there any CU, ST or PT? If yes record in monitor file? ***')
time.sleep(3)
print('\n')


# Checking paces one by one
print('********* PACES CHECKING *********')


# Get number of paces to be checked
while True:
    number_of_paces = input('How many paces does the learner have?:')
    try:
        pace_num = int(number_of_paces)
    except ValueError:
        print('"%(pace_num)s" is not a number. Try again.' % {'pace_num': number_of_paces})
    else:
        print('You typed "{}".'.format(pace_num))
        break


# Check the paces one by one
for n in range(1, pace_num + 1):
    print('Let us check pace number:', n)
    for x, y in pace_check_dict.items():
        checker(x, y)
    print('\n')


# Print out all the error codes
print('***** These are the the codes for this learner ****')
for x in range(len(code_list)):
    print(code_list[x])
