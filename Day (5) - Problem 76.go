/*Problem 76: Minimum Window Substring
### USING LIST CACHE
1. Convert the string into a list of characters
2. Convert each Unicode character into corresponding integer representation
3. Make an empty list of cache: indexes represent the integer representations, values represent the occurrences
4. Values of cache whose indexes are integer representations of characters will vary. Generally:
    - A character in the second string will have 1 or more occurrences
    - A character in the first string, but not in the second string will have -1 or less occurrences
    - A character in the first and second strings will have a value greater than or equal to 0
*/
func minWindow(s string, t string) string {
    if len(s) < len(t) {
        return ""
    }

    original, need := []rune(s), []rune(t)

    L, R, counter := 0, 0, 0

    cache := make([]rune, 128)
    for _, r := range need {
        cache[r]++
    }

    indexes := []int{-1, 1}

    minWindow := math.MaxInt32

    for R < len(original) {
        right := original[R]
        cache[right]--
        if cache[right]>=0 {
            counter++
        }

        for counter == len(need) {
            curWindow := R - L + 1
            if curWindow < minWindow {
                minWindow = curWindow
                indexes[0] = L
                indexes[1] = R + 1
            }

            left := original[L]
            cache[left]++
            if cache[left] > 0 {
                counter--
            }
            L++
        }
        R++
    }

    if indexes[0] == -1 {
        return ""
    }

    return string(original[indexes[0]:indexes[1]])        
}