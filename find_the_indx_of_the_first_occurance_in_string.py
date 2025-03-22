class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Time complexity O(mn), Space complexity O(1)
        needle_l = len(needle)
        if needle_l > len(haystack):
            return -1

        for i in range(0, len(haystack)):
            if needle_l > (len(haystack) - i):
                return -1
            needle_index = 0
            for j in range(i, i+needle_l):
                if haystack[j] == needle[needle_index]:
                    if needle_index == needle_l - 1:
                        return i
                    needle_index += 1
                else:
                    break
            
        
        return -1
        
