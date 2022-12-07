# A program that finds the difference between the maximum and minimum
# values ​​of the fractional part of elements. The list of real numbers
# is entered by the user.
#
# Example:
# [1.1, 1.2, 3.1, 10.01] => 0.19
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

def get_difference_max_and_min_fractional_part(lst):
    """Return the difference between the maximum and minimum values
    ​​of the fractional part of the elements.
    """
    lst_new = [round(i % 1, 2) for i in lst]
    return max(lst_new) - min(lst_new)


try:
    list_source = [float(i) for i in (
        input('Enter real numbers separated by spaces: \n').split())]
except:
    print("Sorry, only real numbers are allowed, please try again")
else:
    difference = get_difference_max_and_min_fractional_part(list_source)
    print('The difference between the maximum and minimum values',
          '​of the fractional part of the elements is', difference)
