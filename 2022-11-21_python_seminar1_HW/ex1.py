# A program that takes as input a number representing the day of the week
# and checks if that day is a holiday.
#
# Example:
# 6 -> Yes
# 7 -> Yes
# 1 -> No

def check_holiday(x):
    """Check if the day is a holiday."""
    if x < 1 or x > 7:
        return 'Invalid number entered'
    elif x >= 6:
        return 'Yes'
    else:
        return 'No'


print(check_holiday(int(input('Enter a number representing the day '
                              'of the week to find out if this day is a holiday: '))))
