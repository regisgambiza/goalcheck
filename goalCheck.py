# This script is used to carry out goal check
import time


# Functions
def checker(d_code, description):
    response = input(description)
    if response == 'n':
        code_list.append(d_code)


# Dictionaries of all codes and descriptions
goal_check = {
    'NR g/ch': 'Not ready for goal check?:',
    'PWO': 'Paces in wrong order?:',
    'P open inc': 'Paces opened on incorrect pages?:',
    'HWB != g/ch': 'Homework book not in goal check?:',
    'PACE != 4PT': 'Pace(s) not handed in for PACE Test(s)?:',
    'G changed': 'Goals self-adjusted(not Foundation Phase)?:'
}
h_book_dict = {
    'HWB != sign': 'Is the book signed by the parent?:',
    'NTP': 'Is the total number of pages indicated?:',
    'HWK != ind': 'Is homework indicated?:',
    'G != set': 'Are goals indicated, neat and properly set?:',
    'HW != rec != ink': 'Homework not recorded or not in blue ink?:'
}
goal_card_dict = {
    'G != set': 'Are goals written?:',
    'NTP': 'Is total number of pages written?:',
    'IG': 'Insufficient goals?:',
    'NPS': 'No supervisor initial to pass Score strip(no pass/work pass score strip)?:',
    'NS/S': 'No score strip at the end of a goal?:',
    'Comp g!=x': 'Goals scored, but not scored?:',
    'Gx != sc': 'Goals crossed off, but not scored?:',
    'NN on G/C': 'No name or week number om goal card?:',
    'U G/C': 'Untidy goal card?:'
}
pace_check_dict = {
    'Goal incomp': 'Was the goal completed?:',
    'P0': 'Are all pages circled?:',
    'S/S inc': 'Is there any incomplete score strip?',
    'X0': 'No circle around Red X after correction is done?:',
    'SB': 'Scoring behind?:',
    'SV': 'Scoring violation?:',
    'cor != sign': 'No supervisors initial for three mistakes?:',
    'page != sign': 'No supervisors initials at yellow strip, where required?:',
    'proj d != sign': 'Project dates not signed by parents to acknowledge project requirements?:',
    'Read != sign': 'No signature for Reading(Foundation)?:',
    'Proj date': 'No due date for project?:',
    'CU/ST sc': 'Check up or self test scores not filled in?:',
    'CU/ST != //': 'Check up or self test not double checked?:',
    '!=x ref': 'Cross reference not done at check up or self-test?:',
    'U write/rub': 'Untidy handwriting/Running out?:'
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
