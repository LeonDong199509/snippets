class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Time Complexity O(n), Space Complexity O(n)
        # Stratgy: Use 2 arrays to store pre-calculated suffix and prefix product for each index

        # n = len(nums)
        # prefix_array = [1] * n
        # suffix_array = [1] * n
        # result = [1] * n

        # # calculate prefix product
        # prefix_product = 1
        # for i in range(1, n):
        #     prefix_array[i] = prefix_product * nums[i-1]
        #     prefix_product = prefix_array[i]

        # # calculate suffix product
        # suffix_product = 1
        # for i in range(n-2, -1, -1):
        #     suffix_array[i] = suffix_product * nums[i+1]
        #     suffix_product = suffix_array[i]
        
        # # calculate result
        # for i in range(n):
        #     if i == 0:
        #         result[i] = suffix_array[i]
        #     elif i == n-1:
        #         result[i] = prefix_array[i]
        #     else:
        #         result[i] = suffix_array[i] * prefix_array[i]
        
        # return result

        # Optimised solution with only O(1) Space Complexity
        n = len(nums)
        result = [1] * n

        # Left to right traverse
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Right to left traverse
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result



