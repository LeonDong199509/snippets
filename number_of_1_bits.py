class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # Time O(logn), Space O(1)
        result = 0
        while (n > 0):
            mod = n % 2
            if mod == 1:
                result += 1
            n = n // 2
        return result
