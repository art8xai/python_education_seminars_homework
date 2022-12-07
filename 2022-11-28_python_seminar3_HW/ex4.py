# A program that converts a decimal number to binary.
#
# Example:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def get_convert_decimal_to_binary(decimal):
    """Return a binary number converted from a decimal number."""
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return int(binary)


try:
    decimal = int(input('Enter a positive integer: '))
    if decimal <= 0:
        raise
except:
    print("Sorry, only positive integers are allowed, please try again")
else:
    binary = get_convert_decimal_to_binary(decimal)
    print(f'{decimal} -> {binary}')
