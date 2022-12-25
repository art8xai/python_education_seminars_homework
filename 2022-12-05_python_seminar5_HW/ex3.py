# The program implements the RLE algorithm: data compression and recovery module.
# The input data is stored in separate text files.
#
# Example:
# Input File 1: aaaaaaaaaaaabbbbccbbbd
# Console output: 12a4b2c3b1d
# Input File 2: 12a4b2c3b1d
# Console output: aaaaaaaaaaaabbbbccbbbd


def get_encode(sequence: str) -> None or str:
    """Return the encoded sequence as a string."""
    if len(sequence) == 0:
        return None
    result = ''
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            count += 1
            i += 1
        result += str(count) + sequence[i]
        i += 1
    return result


def get_decode(sequence: str) -> None or str:
    """Return the decoded sequence as a string."""
    if len(sequence) < 2:
        return None
    number = ''
    result = ''
    for i in sequence:
        if i.isdigit():
            number += i
        else:
            result += int(number) * i
            number = ''
    if result == '':
        return None
    return result


# Initial data.
path_file1 = r'ex3_file1.txt'
path_file2 = r'ex3_file2.txt'

# Data input.
with open(path_file1, 'r', encoding='UTF-8') as file:
    data_file1 = file.readline()
with open(path_file2, 'r', encoding='UTF-8') as file:
    data_file2 = file.readline()

# Function call.
encode = get_encode(data_file1)
decode = get_decode(data_file2)

# Output data to the console.
print(f'File 1 text "{data_file1}" after data compression: {encode}')
print(f'File 2 text "{data_file2}" after data recovery: {decode}')
