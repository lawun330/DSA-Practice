'''Problem 76: Minimum Window Substring
### USING DICT CACHE
# Find the shortest sub-string in a given string such that every character in the second given string is included.
#	1. Convert the string into a list of characters
	2. Make an empty dictionary of cache: keys represent characters, values represent occurrences
	3. Values of cache will vary. Generally:
    	- A character in the second string will have 1 or more occurrences
    	- A character in the first string, but not in the second string will have -1 or less occurrences
    	- A character in the first and second strings will have a value greater than or equal to 0'''
def minWindow(first_string: str, second_string: str) -> str:
	
	shortest_substr = ""
	
	# impossible to contain the second string if the first string is shorter
	if len(first_string) < len(second_string):
		return shortest_substr # return empty string
	
	L = 0 # left pointer
	R = 0 # right pointer
	first_string_list = list(first_string) # convert the string into list
	second_string_list = list(second_string) # convert the string into list
	min_window_size = float("infinity") # arbitrarily-large size
	cache = {} # cache to store the occurrence of Unicode characters
	counter = 0 # variable to count whether all second string characters are found in the cache
	indexes = [0, 0] # list containing the indexes for the start-point and end-point of first string (to be returned)
	
	for i in second_string_list: # store the second string characters into cache
		cache[i] = cache.get(i, 0) + 1 # whenever a character is in the second string, there will be 1 additional occurrence # get() returns 0 for a new character

	while R < len(first_string_list): # iterate the right pointer

		# if that character is not in the second string, value is -1 or less
		cache[first_string_list[R]] = cache.get(first_string_list[R], 0) - 1 # whenever a character is in the first string, reduce 1
	
		if cache[first_string_list[R]] >= 0: # a character that is in the first and second strings will have a value greater than or equal to 0
			counter += 1 # count that character

		while counter == len(second_string_list): # if characters count so far is equal to the number of characters of the second strings, we have found the sub-string in the first string
			
			current_window_size = R - L + 1 # get the window size # add 1 because index starts at 0
			if current_window_size < min_window_size: # if the current window is shorter
				min_window_size = current_window_size # update the shortest window
				indexes[0] = L # update start-index
				indexes[1] = R + 1 # update end-index # add 1 because last index is not counted

			cache[first_string_list[L]] = cache.get(first_string_list[L], 0) + 1 # a character in the cache will be updated to get unique value
			if cache[first_string_list[L]] > 0: # if the constraint is still valid
				counter -= 1 # pop the leftmost character # shrink the window
			L += 1
		R += 1

	shortest_substr = ''.join(first_string_list[indexes[0]:indexes[1]]) # reconstruct the string via the list and indexes

	return shortest_substr


# test
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t)) # expect "BANC"