# The program from the list of integers entered by the user in one line, separated by a space, leaves only two-digit
# numbers in the list. The filter function has been applied. The result is displayed on the screen as a sequence of
# other numbers in one line separated by a space.
#
# Example:
# 1 2 3 4 22 234 24 -> 22 24

def get_list_int() -> list:
    """Return a list of integers entered by the user."""
    while True:
        try:
            result = list(map(int, input('Enter integers separated by spaces: ').split()))
        except ValueError:
            print('Sorry, you entered an invalid value, please try again...')
        else:
            if not result:
                print('Sorry, you entered an empty value, please try again...')
                continue
            return result


def get_two_digit_numbers_as_string(lst: list) -> None or str:
    """Return a sequence of two-digit numbers as a string, separated by a space."""
    result = " ".join(map(str, filter(lambda i: 9 < abs(i) < 100, lst)))
    if result == '':
        return None
    else:
        return result


list_input = get_list_int()
print('Input:', *list_input)
print('Output:', get_two_digit_numbers_as_string(list_input))
