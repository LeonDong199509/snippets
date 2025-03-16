class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Greedy; Time O(n); Space O(1)

        # Greedy Choice Property: At each exploring range, we always choose the max reach
        # •	Instead of considering all possible paths, we only track the farthest index we can reach in the current exploring range.
        # •	This guarantees that we reach the goal in the minimum number of jumps, as we’re always making the best possible move at each step.

        # Optimal Substructure: ith exploring range's max reach is max(i,(i-1)th exploring range's max reach)
        
        length = len(nums)
        # Number of jumps took
        jumps = 0
        # The end of current range we are exploring
        current_end = 0
        # The max reach we explored
        max_reach = 0

        for i in range(length-1):
            # Update max reach by comparing every index in the current range we are exploring
            max_reach = max(max_reach, nums[i] + i)
        
            # If we have arrived at the end of current range, we got nothing to explore and we have to jump to explore the next range.
            # Then next range we will exploring will be end at the current max_reach. So we set next range's end to max_reach. And of course, we also have the ability to jump to any index smaller than max_reach, so next exploring range will be start at i+1, which is our next iteration.
            if i == current_end:
                jumps += 1
                current_end = max_reach

            # If the end is larger than last index, we return the answer
            if current_end >= (length - 1):
                break
        
        return jumps
