class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Time O(n), Space O(n)
        if not nums:
            return 0

        nums_set = set(nums)
        result = 1
        for n in nums_set:
            if n-1 in nums_set:
                continue
            else:
                length = 1
                while (n+1 in nums_set):
                    n += 1
                    length += 1
                result = max(length, result)
        return result


        
