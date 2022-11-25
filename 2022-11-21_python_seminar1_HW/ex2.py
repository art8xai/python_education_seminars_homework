# A program for checking the truth of the statement
# ¬(x ∨ y ∨ z) = ¬x ∧ ¬y ∧ ¬z for all values ​​of the predicate,
# i.e. (0,0,0), (0,0,1), etc.

def check_truth(x, y, z):
    """Check if the condition is met."""
    left_side = not (x or y or z)
    right_side = not (x) and not (y) and not (z)
    if left_side == right_side:
        return True
    else:
        return False


print('Checking the truth of the statement ¬(x ∨ y ∨ z) = ¬x ∧ ¬y ∧ ¬z '
      'for all values ​​of the predicate...')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'For the predicate ({x},{y},{z}), '
                  f'the condition is {check_truth(x, y, z)}')
