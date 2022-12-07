# The program compiles a list of Fibonacci numbers, including those
# for negative indices. The initial number is set by the user.
#
# Example:
# for k = 8 the list will look like this:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# See more https://en.wikipedia.org/wiki/Fibonacci_number

def get_fibonacci_list(n):
    """Return a list of Fibonacci numbers, including those
    for negative indices.
    """
    res = [0]
    a, b = 0, 1
    for i in range(n):
        res.append(b)
        a, b = b, a + b

    a, b = 0, 1
    for i in range(n):
        a, b = b, a - b
        res.insert(0, a)
    return res


try:
    number = int(input('Enter a non-negative integer: '))
    if number < 0:
        raise
except:
    print('Sorry, only non-negative integers are allowed, '
          'please try again')
else:
    # Uncomment to display a list of N numbers:
    # number_list = list(range(-number, number + 1))
    # print(f'n: {number_list}')
    fibonacci_list = get_fibonacci_list(number)
    print(f'F: {fibonacci_list}')
