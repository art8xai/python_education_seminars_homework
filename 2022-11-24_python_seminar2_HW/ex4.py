# A program that calculates the sum of even numbers located between the numbers 1 and N inclusive.
#
# Example:
# N = 8 -> 20, i.e. 2+4+6+8=20
# N = -7 -> -20, i.e. (-6)+(-4)+(-2)=-12

def get_sum_even_number(x):
    """Return the sum of even numbers between 1 and N inclusive."""
    result = 0
    if number > 0:
        for i in range(2, number+1, 2):
            result += i
    elif number < 0:
        for i in range(-2, number-1, -2):
            result += i
    return result


number = int(input('Enter an integer number: '))

sum_even_number = get_sum_even_number(number)
print(f'The sum of even numbers located between the numbers 1 '
      f'and N={number} inclusive is equal to {sum_even_number}')
