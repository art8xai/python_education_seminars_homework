# A program that displays a list of non-repeating elements of the original sequence (output of those elements that
# were not repeated). The sequence of numbers is set by the user.
#
# Example:
# Input: 1 2 3 2 4 4
# Output: 1 3

def get_non_repeating_elements(lst: list) -> list:
    """Return the non-repeating elements of the given list."""
    result = []
    for i in lst:
        if lst.count(i) == 1:
            result.append(i)
    return result


while True:
    try:
        list_input = [int(i) for i in (
            input('Enter integers separated by spaces: ').split())]
    except ValueError:
        print('Sorry, you entered an invalid value, please try again...')
    else:
        if not list_input:
            print('Sorry, you entered an empty value, please try again...')
            continue
        break

print('Input:', " ".join(map(str, list_input)))
list_output = get_non_repeating_elements(list_input)
print('Output:', " ".join(map(str, list_output)))
