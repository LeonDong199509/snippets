class Solution:
    def minWindow(self, s, t):
        # Input: s = "ADOBECODEBANC", t = "ABC"
        # Output: "BANC"

        # 🧪 Strategy: Sliding Window + Two HashMaps
        # 1.	Count frequencies of each char in t using a Counter.
        # 2.	Expand the window by moving the right pointer to include enough chars.
        # 3.	Once the window is valid (i.e., contains all of t), try shrinking it from the left.
        # 4.	Track the smallest valid window encountered.

        # Changed Sliding Window
        # Time O(m+n)
        
        # count the letter in target
        t_count = {}
        for l in t: # O(m)
            t_count[l] = t_count.get(l, 0) + 1
        letters_to_match = len(t_count)
        
        window_count = {}
        left = 0
        letters_matched = 0
        min_len = float('inf')
        result = (0, 0)
        has_result = False
        for right, c in enumerate(s): # O(n)
            if c in t_count:
                window_count[c] = window_count.get(c, 0) + 1
                if window_count[c] == t_count[c]:
                    letters_matched += 1
            
            # Shrink the window by moving the left pointer
            while (letters_to_match == letters_matched): # O(right-left)
                has_result = True
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    result = (left, right)

                left += 1
                if s[left-1] in t_count:
                    window_count[s[left-1]] -= 1
                    if window_count[s[left-1]] < t_count[s[left-1]]:
                        letters_matched -= 1

        left, right = result
        return s[left: right+1] if has_result else ""
