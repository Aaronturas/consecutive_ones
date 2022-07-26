# Run python solution.py in the shell 


def consecutive_ones(lst):
    max_count = 0
    curr_count = 0
    for num in lst:
        if num == 1:
            curr_count += 1
        else:
            curr_count = 0

        if curr_count > max_count:
            max_count = curr_count

    return max_count


print(consecutive_ones([1, 1, 1, 0, 1]))
print(consecutive_ones([0, 1, 0, 1, 1, 0, 0]))
print(consecutive_ones([0]))
print(consecutive_ones([1]))
print(consecutive_ones([1, 0]))
print(consecutive_ones([0, 1]))
