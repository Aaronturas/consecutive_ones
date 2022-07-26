# Given a list lst with 0s and 1s, find the count of the maximum number of consecutive 1s present in the list.

# Example

# Input: lst = [1, 1, 1, 0, 1]
# Output: 3

# Input: lst = [0, 1, 0, 1, 1, 0, 0]
# Output: 2

def consecutives_ones(lst):
  max_ones = 0#overall maximum number of 1s
  curr_ones = 0#Current number of consecutive 1s
  

  for num in lst:
    if num == 1:
      curr_ones += 1
    else:
      curr_ones = 0

    if curr_ones > max_ones:#if current consecutive 1s is greater than maximum 1s then we set it equal to current 1s 
      max_ones = curr_ones
  return max_ones

lst = [1, 1, 1, 0, 1]
print(consecutives_ones(lst), '\n')

lst = [0, 1, 0, 1, 1, 0, 0]
print(consecutives_ones(lst), '\n')