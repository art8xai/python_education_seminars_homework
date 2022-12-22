# A program that compiles a list of prime factors of the number N. The natural number N is specified by the user.
#
# Example:
# 24 -> [2, 2, 2, 3]

from math import sqrt


def get_prime_factors(num: int) -> list:
    """Return a list of prime factors of the given number."""
    result = []
    if num == 1:
        return result
    while num % 2 == 0:
        result.append(2)
        num = num / 2
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            result.append(i)
            num = num / i
    if num > 2:
        result.append(int(num))
    return result


while True:
    try:
        number = int(input('Enter a natural number: '))
    except ValueError:
        print('Sorry, you entered an invalid value, please try again...')
    else:
        if number < 1:
            print('Sorry, you entered a wrong number, please try again...')
            continue
        break

prime_factors = get_prime_factors(number)
print(f'List of prime factors of N: {prime_factors}')
