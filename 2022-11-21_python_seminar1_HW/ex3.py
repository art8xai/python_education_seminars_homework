# A program that takes as input the coordinates of a point (X and Y),
# with X ≠ 0 and Y ≠ 0, and outputs the number of a quarter of the plane
# in which this point is located (or which axis it is on).
#
# Example:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

def get_quadrant(x, y):
    """Return the number of the quarter of the plane.
    See more https://en.wikipedia.org/wiki/Quadrant_(plane_geometry)
    """
    if (x > 0) and (y > 0):
        return 1
    elif (x < 0) and (y > 0):
        return 2
    elif (x < 0) and (y < 0):
        return 3
    elif (x > 0) and (y < 0):
        return 4
    else:
        return None


x = float(input('Input X: '))
y = float(input('Input Y: '))

if x == 0 and y == 0:
    print('The point is at the origin of the X and Y axes')
elif x == 0 and y != 0:
    print('The point is on the Y axis')
elif x != 0 and y == 0:
    print('The point is on the X axis')
else:
    quadrant = get_quadrant(x, y)
    print(f'Quadrant = {quadrant}')
