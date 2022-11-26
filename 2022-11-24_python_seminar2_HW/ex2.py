# The program finds the smallest natural divisor
# of an integer N other than 1.
#
# Example:
# For N=15 -> answer: 3
# For N=35 -> answer: 5

def get_smallest_divisor(x):
    """Return the smallest natural divisor of an integer N other than 1."""
    if x == 0 or abs(x) == 1:
        return None
    else:
        for i in range(2, abs(x)+1):
            if x % i == 0:
                return i


number = int(input('Enter an integer number: '))

smallest_divisor = get_smallest_divisor(number)
print(f'The smallest natural divisor of an integer N={number} '
      f'(other than 1) is {smallest_divisor}')

# Uncomment the following lines if you want to see the least natural
# divisors of all numbers from -100 to 100:
# for i in range(-100, 101):
#     print(f'For N={i} -> answer: {get_smallest_divisor(i)}')
