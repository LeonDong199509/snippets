class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Slicing Window; Time O(n); Space O(n)
        c_index = {}
        current_len = 0
        left = -1
        result = 0

        # Keep right as the looping 
        for right, c in enumerate(s):
            # If c is existing in the current substring, which means the char is in the dict and it's in the current window ( > left bound)
            # We move the left bound
            if c in c_index and c_index[c] > left:
                left = c_index[c]

            c_index[c] = right

            current_len = right - left
            result = max(result, current_len)
        return result
                



        
        
