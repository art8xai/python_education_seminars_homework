# The program randomly generates a list of coefficients (values from 0 to 100) of the polynomial and writes the
# polynomial of degree k to the file. The natural degree k is specified by the user.
#
# Example:
# k = 2 -> 2*x^2 + 4*x + 5
# k = 3 -> 41*x^3 + 6*x^2 + 2*x + 98

from random import randint


def get_polynomial(lst) -> str:
    """Return the polynomial as a string."""
    degree = len(lst) - 1
    result = []
    for i in range(degree, -1, -1):
        if lst[degree - i] < 0:
            result.append(' − ')
        elif lst[degree - i] > 0:
            result.append(' + ')
        else:
            continue
        if i > 1:
            result.append(f'{abs(lst[degree - i])}*x^{i}')
        elif i == 1:
            result.append(f'{abs(lst[degree - i])}*x')
        else:
            result.append(str(abs(lst[degree - i])))
    for i in range(len(result)):
        if result[i][:3] == '1*x':
            result[i] = result[i][2:]
    if result:
        if result[0] == ' + ':
            result[0] = ''
        elif result[0] == ' − ':
            result[0] = '− '
        return ''.join(result)
    else:
        return '0'


# Initial data.
path_output = r'ex4_file.txt'
value_min = 0
value_max = 100

# Data input.
while True:
    try:
        number = int(input('Enter a natural degree k: '))
    except ValueError:
        print('Sorry, you entered an invalid value, please try again...')
    else:
        if number < 1:
            print('Sorry, you entered a wrong number, please try again...')
            continue
        break
list_coefficients = [randint(value_min, value_max) for i in range(number + 1)]

# Function call.
polynomial = get_polynomial(list_coefficients)

# Console output.
print(f'Randomly generated list of coefficients: {list_coefficients}')
print(polynomial)

# Write to file.
with open(path_output, 'w', encoding='UTF-8') as file:
    file.write(polynomial)
