from typing import List

### Not Applicable Sliding Windows
'''Problem 485: Max Consecutive Ones
# Find the maximum number of consecutive 1s in a given array.
# This problem is an example to understand whether the "sliding windows" method is applicable or not.'''

def maxC1s(array: List[int]) -> int:
	count = 0
	max_count = 0
	for i in array: # array traversal
		if i == 1: # add count for consecutive 1s
			count += 1
		else: # reset count
			count = 0
		if count > max_count: # update the best count so far
			max_count = count
	return max_count



### Applicable Sliding Windows
'''Problem 1004: Max Consecutive Ones III
# Find the longest consecutive 1s for a given array containing 0s and 1s.
# We can flip 0s "max_flip" times to make it 1s to count into the longest consecutive array.
# This problem is an example to understand whether the "sliding windows" method is applicable or not.'''

def maxC1sIII(array: List[int], max_flip: int) -> int:
	flipped_zero = 0 # the number of zeros flipped
	max_count = 0 # the longest 1s so far
	L = 0 # left index for the first pointer
	R = 0 # right index for the second pointer

	# first constraint
	if (len(array) < 1) or (len(array) > 100000): # if the array length is out of this constraint, quit the program
		return 0

	# second constraint
	for i in range(len(array)):
		if array[i] not in [0, 1]: # if there are elements we do not want, quit the program
			return 0

	# third constraint
	if (max_flip < 0) or (max_flip > len(array)): # if the number of flipped zeros is out of bound, quit the program
		return 0

	while (R <= len(array)-1): # the right pointer can traverse the array till its end

		# zero flip
		if array[R] == 0:
			flipped_zero += 1 # increase total number of flipped zeros

		# not valid # move the L, stop the R
		while (flipped_zero > max_flip): # it is not valid to flip more zeros than allowed
			if array[L] == 0: # if the left pointer points at 0
				flipped_zero -= 1 # unflip one 0
			L += 1 # shrink the window by moving the left pointer to right
		
		# valid # move the R, stop the L
		R += 1 # expand the window by moving the right pointer to right 

		max_count = max(max_count, R - L) # the longest 1s is simply the max length of elements within two pointers of the array

	return max_count

### test
test = [1,1,1,0,0,0,1,1,1,1,0]
print(maxC1s(test))
print(maxC1sIII(test, 2))