'''Problem 704: Binary Search
# Find the required integer in an array sorted in ascending order.
# The closer to the right, the larger the value is.
# Return the index of the required integer.
# Return -1 if there is None.'''
from typing import List

def search(array: List[int], target: int) -> int:
	
	target_index = -1 # default return value

	# the first constraint
	if (len(array) < 1) or (len(array) > 10000):
		return target_index

	# the second constraint
	if (target < -10000) or (target > 10000):
		return target_index

	L = 0 # left pointer # left index
	R = len(array) - 1 # right pointer # right index
	M = 0 # midpoint index

	while L <= R: # unless the two pointers meet
		M = ((R - L) // 2) + L

		if array[M] == target: # if the midpoint index has the required integer
			target_index = M
			break

		'''# if the midpoint index does not have the required integer >>> shift the pointers'''

		elif array[M] > target: # if the left part has the required integer
			R = M - 1 # shift the right pointer to the left side of the midpoint # the left pointer stays the same

		else: # if the right part has the required integer
			L = M + 1 # shift the left pointer to the right side of the midpoint # the right pointer stays the same
	
	return target_index

# test
a, t = [-1,0,3,5,9,12], 9
print(search(a, t)) # expect 4