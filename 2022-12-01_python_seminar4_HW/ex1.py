# The program calculates the number Pi with a given accuracy d (in the
# range 1 ≤ d ≤ 10, i.e. it is equivalent to 0.1 to 0.0000000001)
# without using the round() function.
#
# Example:
# d: 0.001 -> π = 3.142

from math import pi


def get_rounding(num: float, d: int) -> float:
    """Return a rounded number with the given precision."""
    d = 10 ** d
    num = d * num
    if (num * 10) % 10 >= 5:
        return int(num + 1) / d
    else:
        return int(num) / d


number = pi

while True:
    try:
        accuracy_str = input('Enter the rounding precision (value from 0.1 to 0.0000000001): ')
        accuracy_float = float(accuracy_str)
        accuracy_str_list = accuracy_str.split('.')
    except ValueError:
        print('Sorry, you entered an invalid value, please try again...')
    else:
        if accuracy_float > 1e-01 or accuracy_float < 1e-10:
            print('Sorry, you entered a value out of range, please try again...')
            continue
        break

print('Initial π =', number)
accuracy = int(len(accuracy_str_list[1]))
rounding = get_rounding(number, accuracy)
print('Rounded π =', rounding)
