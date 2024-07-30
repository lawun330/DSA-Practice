'''Problem 42: Trapping Rain Water
# Find the total water accumulated between an array of heights.
# Water can only accumulated in indexes whose heights are lesser than its consecutive walls' heights.'''

from typing import List

def trappedWater(heights: List[int]) -> int:
	n = len(heights) # length of the array

	total_water = 0 # total water accumulated within two walls
	highest_wall_height = 0 # highest wall so far
	left_wall_height = heights[0] # the leftmost wall
	right_wall_height = heights[n-1] # the rightmost wall
	
	if n<3: # two walls cannot hold any water
		print("No water can be trapped within two consecutive walls")
		return total_water # total_water = 0

	# find the highest wall
	for wall_height in heights:
		if wall_height > highest_wall_height:
			highest_wall_height = wall_height
			highest_wall_index = heights.index(highest_wall_height)

	# accumulated water from the leftmost wall to the highest wall
	for i in range(highest_wall_index): 
		left_wall_height = max(left_wall_height, heights[i])
		'''if a particular height is greater, it cannot hold any water >>> add 0 in that case
		if a particular height is lesser, it holds water (wall_height - this_particular_height) amount'''
		total_water += left_wall_height - heights[i]

	# accumulated water from the rightmost wall to the highest wall
	for i in range(n-2, highest_wall_index, -1):
		right_wall_height = max(right_wall_height, heights[i])
		'''if a particular height is greater, it cannot hold any water >>> add 0 in that case
		if a particular height is lesser, it holds water (wall_height - this_particular_height) amount'''
		total_water += right_wall_height - heights[i] 

	return total_water