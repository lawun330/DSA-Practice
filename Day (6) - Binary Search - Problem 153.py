'''Problem 153: Find Minimum in Rotated Sorted Array
# The array is sorted in ascending order.
# It is rotated between 1 to 'n' times.
# Find the minimum element in that array using binary search.'''

from typing import List

def findMin(array: List[int]) -> int:
	
	n = len(array)
	L = 0 # left index # left pointer
	R = n - 1 # right index # right pointer
	M = 0 # midpoint index

	# the first constraint
	if (n < 1) or (n > 5000):
		return -1

	if (n == 1): return array[0] # for an array with a single element

	while (L <= R): # add equality for two-element arrays

		# Example: 1, 2, 3, 4, 5 (not rotated)
		if array[L] <= array[R]: # if the right part is larger, the array has no rotation # add equality for two-element arrays
			return array[L] # the leftmost element is the smallest element

		'''# if the right part is not larger, the array is rotated >>> shift the pointers'''
		
		M = ((R - L) // 2) + L # get midpoint index

		# Example: 3, 4, 5, 1, 2 (rotated)
		if array[R] < array[M]: # if the right part is smaller than the middle part, seek the right part
			L = M + 1 # shift the left pointer # the right pointer stays the same
		# Example: 4, 5, 1, 2, 3 (rotated)
		else: # if the left part is smaller than the middle part, seek the left part
			R = M # shift the right pointer # the left pointer stays the same

	return -1

# test
a = [2, 1]
print(findMin(a)) # expect 1 
