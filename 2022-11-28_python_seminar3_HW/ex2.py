# A program that finds the product of pairs of numbers in a list.
# A pair is the first and last element, the second and penultimate,
# and so on.
#
# Example:
# [2, 3, 4, 5, 6] -> [12, 15, 16]
# [2, 3, 5, 6] -> [12, 15]

def get_multiplication_pairs(lst):
    """Return the product of pairs of numbers in a list as a list."""
    res = []
    for i in range(len(lst)//2 + len(lst) % 2):
        res.append(int(lst[i]) * int(lst[len(lst) - i - 1]))
    return res


try:
    list_source = [int(i) for i in (
        input('Enter integers separated by spaces:\n').split())]
except:
    print("Sorry, only integers are allowed, please try again")
else:
    multiplication = get_multiplication_pairs(list_source)
    print('The product of pairs of numbers in the list is',
          multiplication)
