class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        # Leetcode 189. Rotate Array

        # Initial solution - .pop(), but got time limit exceeded
        # Time Complexity is O(n*n), as nums.insert(0, value)) is o(n)
        # l = len(nums)
        # rotate_num = k % l
        # while (rotate_num > 0):
        #     nums.insert(0, nums.pop())
        #     rotate_num -= 1

        # Best Solution, Time Complexity O(n), Space Complexity O(1)
        # def reverse(array, left, right):

        #     while (left < right):
        #         array[left], array[right] = array[right], array[left]
        #         left += 1
        #         right -= 1
        
        # l = len(nums)
        # rotate_num = k % l
        # reverse(nums, 0, l-1)
        # reverse(nums, 0, rotate_num-1)
        # reverse(nums, rotate_num, l-1)


        # Another solution, Time Complexity O(n), Space Complexity O(n)
        l = len(nums)
        k = k % l
        nums[:] = nums[-k:] + nums[:-k]



