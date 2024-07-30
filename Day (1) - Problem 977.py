'''Problem 977: Squares of a Sorted Array
# Find the sorted array which contains the squared values of a given array.
# The sorted array should be in non-decreasing order.'''

from typing import List

def sorter(array: List[int]) -> List[int]:
	n = len(array) # length of original array
	L = 0 # left index
	R = n-1 # right index

	new_array = [None] * n # new array is initialized with the same length

	while(L <= R): # until the two pointers meet
		if (array[L]**2) < (array[R]**2): # compare the squared values
			new_array[n-1] = array[R]**2 # add the larger squared from the rightmost
			R-=1 # right index comes to left
		else:
			new_array[n-1] = array[L]**2 # add the larger squared from the rightmost
			L+=1 # left index comes to right

		n-=1 # the index of the new array must come from right to left 
	return new_array

# tests
print(sorter([5, 6, 7]))
print(sorter([-10, -9, -8, -7, -6]))
print(sorter([-5, -3, -1, 2, 4]))
