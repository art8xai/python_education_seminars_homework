# A program that finds the sum of the elements of a list in an odd
# position. A list of several numbers is specified by the user.
#
# Example:
# [2, 3, 5, 9, 3] -> elements 3 and 9 in odd positions, answer: 12

def get_sum_odd_position(lst):
    """Return the sum of the elements of the list in an odd position."""
    res = 0
    for i in range(1, len(lst), 2):
        res += int(lst[i])
    return res


try:
    list_source = [int(i) for i in (
        input('Enter integers separated by spaces:\n').split())]
except:
    print("Sorry, only integers are allowed, please try again")
else:
    sum_odd_position = get_sum_odd_position(list_source)
    print('The sum of the list elements in an odd position is',
          sum_odd_position)
