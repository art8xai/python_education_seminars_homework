# A program that takes as input the coordinates of two points
# and finds the distance between them in 2D space.
#
# Example:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21

import math


def get_data(name):
    """Return the number entered by the user."""
    return int(input(f'Input {name}: '))


def get_distance_2D(p1, p2, q1, q2):
    """Return distance between two points in 2D space.
    See more https://en.wikipedia.org/wiki/Euclidean_distance
    """
    return math.sqrt(pow(q1-p1, 2) + pow(q2-p2, 2))


print('Enter point A coordinates')
x1 = get_data('X1')
y1 = get_data('Y1')

print('Enter point B coordinates')
x2 = get_data('X2')
y2 = get_data('Y2')

distance_2D = get_distance_2D(x1, y1, x2, y2)
print(f'The distance between the points A ({x1},{y1}) '
      f'and B ({x2},{y2}) is {distance_2D}')
