# The program takes a real number than input and outputs the sum of its digits.
#
# Example:
# 6782 -> 23
# 0.56 -> 11

def get_number_as_string() -> str:
    while True:
        """Return the number as a string."""
        result = input('Enter the number: ')
        try:
            float(result)
        except ValueError:
            print('Sorry, you entered an invalid value, please try again...')
        else:
            if not result:
                print('Sorry, you entered an empty value, please try again...')
                continue
            return result


def sum_digits(number: str) -> int:
    return sum(map(int, number.replace('-', '').replace('.', '')))


print('The sum of the digits in the number:', sum_digits(get_number_as_string()))
