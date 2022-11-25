# A program that, given a quarter number, shows the range of possible
# coordinates of points in that quarter (x and y).

def get_coordinate_range(quadrant):
    """Return the range of possible point coordinates.
    See more https://en.wikipedia.org/wiki/Quadrant_(plane_geometry)
    """
    if quadrant == 1:
        return 'Range of possible coordinates: x > 0, y > 0'
    elif quadrant == 2:
        return 'Range of possible coordinates: x < 0, y > 0'
    elif quadrant == 3:
        return 'Range of possible coordinates: x < 0, y < 0'
    elif quadrant == 4:
        return 'Range of possible coordinates: x > 0, y < 0'
    else:
        return 'This quadrant does not exist'


quadrant = int(input('Input quadrant: '))
coordinate_range = get_coordinate_range(quadrant)
print(coordinate_range)
