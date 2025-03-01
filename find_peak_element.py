class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while (left < right):
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                # There must be a peak at the left of middle (including middle, because middle could be the peak), because there are only 3 cases:
                # Case 1: The left is strictly decreasing, where nums[0] will be the Peak
                # Case 2: The left is strictly increasing, where nums[middle] will be the Peak
                # Case 3: Neither strictly increaing nor increasing, which means there is a peak between nums[0] and nums[middle].
                right = middle
            elif nums[middle] < nums[middle + 1]:
                # There numst be a peak at the right of the middle (excluding middle, because middle + 1 could be the peak and middle is impossiable), because there are only 3 cases:
                # Case 1: the right is strictly decreasing, where nums[middle+1] will be the peak
                # Case 2: the right is strictly increasing, where nums[-1] will be the peak
                # Case 3: Neither strictly increaing nor increasing, which means there is a peak between nums[middle+1] and nums[-1]
                left = middle + 1
            elif nums[middle] == nums[middle + 1]:
                # This case is impossible, as there is constraint that nums[i] != nums[i + 1] for all valid i.
                pass
                
        return left
        
