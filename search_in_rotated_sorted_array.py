class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Initial attempt
        # left = 0
        # right = len(nums) - 1
        # while (left <= right):
        #     middle = (left + right) // 2
        #     if nums[middle] == target:
        #         return middle
        #     elif nums[middle] > target:
        #         if nums[0] <= nums[middle]:
        #             if nums[0] == target:
        #                 return 0
        #             elif nums[0] > target:
        #                 left = middle + 1
        #             else:
        #                 right = middle - 1
        #         else:
        #             right = middle - 1
        #     else:
        #         if nums[-1] <= nums[middle]:
        #             left = middle + 1
        #         else:
        #             if nums[-1] == target:
        #                 return len(nums) - 1
        #             elif nums[-1] > target:
        #                 left = middle + 1
        #             else:
        #                 right = middle - 1
        
        # return -1

        # Solution
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            # Pivot at right, which means left part is strictly increasing
            if nums[left] <= nums[middle]:
                # Check if target is at left
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                # Check the possible at right
                else:
                    left = middle + 1
            # Pivot at left, which means right part is strictly increasing
            else:
                # Check if target is at right
                if  nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1



        
