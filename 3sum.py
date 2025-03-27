class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort Solution. Time complexity O(n^2), Space O(n)
        nums.sort()
        def two_sum(nums, target, left, right):
            result = []

            while (left < right):
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip same elements to remove duplicate triplets
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1                   
            
            return result
        
        results = []
        for i, n in enumerate(nums):
            # Skip same elements to remove duplicate triplets 
            if i > 0 and nums[i] == nums[i-1]:
                continue
    
            # Convert 3 sum to 2 sum problem
            two_sum_target = 0 - n
            two_sum_result = two_sum(nums, two_sum_target, i+1, len(nums)-1)

            if two_sum_result:
                for t_s_r in two_sum_result:
                    results.append([n] + t_s_r)
        
        return results
