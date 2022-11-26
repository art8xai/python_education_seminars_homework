# The program specifies a list of 2*N+1 elements filled with numbers
# from the interval [-N, N] and finds the product of the elements
# on the specified INDICES. The five INDEXES are stored in a list
# that is filled in by the user.
#
# Example:
# List of INDEXES: [2, 2, 3, 1, 8]
# Input: 4
# Output:
# [-4, -3, -2, -1, 0, 1, 2, 3, 4] -> index[2]*index[2]*index[3]*index[1]*index[8] -> (-2)*(-2)*(-1)*(-3)*4=48

import random


def get_multiplication_specified_index(number, list_interval, index_list):
    """Return the product of the elements by the specified INDICES."""
    result = 1
    flag = False
    for i in index_list:
        # Indexes out of range are ignored.
        if i <= number*2:
            result = list_interval[i] * result
            flag = True
    if flag != True:
        result = None
    return result


index_list = []
index_amount = 5

# Comment out the following lines, and uncomment subsequent lines
# if you want to enter indices manually:
index_begin = 0
index_end = 10
for i in range(0, index_amount):
    index_list.append(random.randint(index_begin, index_end))

# Uncomment the following lines if you want to enter indexes manually:
# for i in range(0, index_amount):
#     index = int(input(f'Enter an non-negative integer in element [{i}] '
#                       f'of an index list of {index_amount} indexes: '))
#     # Indexes cannot be negative.
#     while index < 0:
#         print('Sorry, please enter a non-negative number. Try again...')
#         index = int(input(f'Enter an index [{i}] of {index_amount} '
#                           'indexes: '))
#     index_list.append(index)

print(f'List of INDEXES: {index_list}')

number = abs(int(input('Enter an integer number (N): ')))

if number != 0:
    list_interval = list(range(-number, number+1))
    print(f'List of intervals from -N to N: {list_interval}')
else:
    list_interval = [0]
    print(f'The list of intervals consists of one element N:',
          list_interval)

multiplication_specified_index = get_multiplication_specified_index(
    number, list_interval, index_list)
if multiplication_specified_index != None:
    print(f'The product of the elements on the indicated INDICES '
          f'is equal to {multiplication_specified_index}')
else:
    print('The specified INDICES are out of range')
