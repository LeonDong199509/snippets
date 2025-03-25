class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Time complexity O(n), space complexity O(n)
        # hash_map = {}
        # for i, n in enumerate(nums):
        #     if n in hash_map:
        #         if i - hash_map[n][-1] <= k:
        #             return True
        #         else:
        #             hash_map[n].append(i)
        #     else:
        #         hash_map[n] = [i]
        # return False

        # Optimised solution where only store the last index
        num_index = {}

        for i, num in enumerate(nums):
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i  # Update the latest index
        
        return False

