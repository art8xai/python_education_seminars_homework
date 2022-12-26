# The program displays letters and numbers separately from the given list. The filter function is used.
#
# Example:
# [12, 'sadf', 5643] -> ['sadf'], [12, 5643]

list_source = [12, 'sadf', 5643]

list_output_str = list(filter(lambda i: type(i) == str, list_source))
list_output_int = list(filter(lambda i: type(i) == int, list_source))

print('Source:', list_source)
print(f'Output: {list_output_str}, {list_output_int}')
