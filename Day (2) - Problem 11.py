'''Problem 11: Container With Most Water
# Find the largest possible area to contain water by removing unnecessary heights.
# The two heights represent the two sides of the container.
# Given that there are a list of heights to choose from.'''

from typing import List

def maxArea(heights: List[int]) -> int:
	n = len(heights) # length of an array # array consisting different heights
	maxArea = 0 # variable to store max index
	L = 0 # left index
	R = n-1 # right index # ends one less than the total number of an array
	
	while(L<R):
		left_height = heights[L]
		right_height = heights[R]

		currentArea = min(left_height, right_height) * (R - L) # area = shorter height * width

		if currentArea > maxArea: # update maxArea
			maxArea = currentArea

		if left_height < right_height:
			L+=1 # left index comes to right
		else:
			R-=1 # right index comes to left
	
	return maxArea
