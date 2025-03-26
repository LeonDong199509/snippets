class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 2 pointers; Tome O(n), Space O(1)
        left = 0
        right = len(numbers) - 1
        while (left <= right):
            s = sum((numbers[left], numbers[right]))
            if s < target:
                left += 1
            elif s > target:
                right -= 1 
            else:
                return [left + 1, right + 1]
        
