# The program generates a file containing the sum of polynomials from two other files with polynomials.
#
# Example:
# Input File 1: 2*x^2 + 4*x + 5
# Input File 2: 41*x^3 + 6*x^2 + 2*x + 98
# Output File 3: 41*x^3 + 8*x^2 + 6*x + 103

def get_parse_polynomial(data: str) -> dict:
    """Return a dictionary of polynomial values."""
    data = data.replace(' + ', ' ').replace(' - ', ' -').replace('- ', ' -').replace('x ', 'x^1 ')
    data = data.split(' ')
    for index in range(len(data)):
        if '*x^' not in data[index]:
            data[index] = data[index] + '*x^0'
    result = {}
    for element in data:
        element = element.split('*x^')
        result[int(element[1])] = int(element[0])
    return result


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
path_file1 = r'ex5_file1.txt'
path_file2 = r'ex5_file2.txt'
path_file3 = r'ex5_file3.txt'

# Data input.
with open(path_file1, 'r') as file:
    data_file1 = file.readline()
with open(path_file2, 'r') as file:
    data_file2 = file.readline()

# Creating a dictionary with variables of the original polynomials.
parse1 = get_parse_polynomial(data_file1)
parse2 = get_parse_polynomial(data_file2)

# Creating a dictionary that is the sum of two other dictionaries.
parse_sum = {}
for i in range(max(len(parse1), len(parse2)), -1, -1):
    if parse1.get(i) or parse2.get(i):
        parse_sum[i] = (parse1.get(i) if parse1.get(i) else 0) + (parse2.get(i) if parse2.get(i) else 0)

# Create a polynomial that is the sum of two other polynomials.
data_file3 = get_polynomial(list(parse_sum.values()))

# Write the result to a file.
with open(path_file3, 'w', encoding='UTF-8') as file:
    file.write(data_file3)

print('The result is written to a file.')
