# A program that takes the number N as input and outputs a set
# of products of numbers from 1 to N.
#
# Example:
# N = 4 -> [1, 2, 6, 24], i.e. (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Enter an integer number: '))
if number < 0:
    print('Invalid input: factorial does not exist for negative numbers')
elif number == 0:
    print("The factorial of 0 is 1")
elif number == 1:
    print("The factorial of 1 is 1")
else:
    factorial = 1
    factorial_set = []
    for i in range(1, number + 1):
        factorial *= i
        factorial_set.append(factorial)
    print(f'The factorial of numbers from 1 to N={number} '
          f'is {factorial_set}')
