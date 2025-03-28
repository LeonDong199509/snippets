class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Sliding window. Time O(n), Space O(1)
        left = 0
        right = 0
        current_sum = 0
        result = float('inf')

        # Expand sliding window by moving right pointer
        for right in range(len(nums)):
            current_sum += nums[right]
            if current_sum >= target:
                current_result = right - left + 1
                # Shrink sliding window by moving left pointer
                while (current_sum - nums[left] >= target and left <= right):
                    current_result -= 1
                    current_sum = current_sum - nums[left]
                    left += 1
                result = min(result, current_result)
        
        return result if result != float('inf') else 0
                    


            

        
