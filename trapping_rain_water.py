class Solution:
    def trap(self, height: List[int]) -> int:
        # [4,2,0,3,2,5]
        #      1
        # 1    1
        # 1  1 1
        # 11 111
        # 11 111

        # DP solution, Time O(n), Space O(n)
        # n = len(height)
        # if n < 3:
        #     return 0
        # left_max = [0] * n
        # right_max = [0] * n
        # water = [0] * n

        # for i in range(0, n):
        #     if i == 0:
        #         left_max[i] = height[i]
        #     else:   
        #         left_max[i] = max(height[i], left_max[i-1])
        
        # for i in range(n-1, -1, -1):
        #     if i == n-1:
        #         right_max[i] = height[i]
        #     else:
        #         right_max[i] = max(height[i], right_max[i+1])
        
        # for i in range(1, n-1):
        #     water[i] = min(left_max[i], right_max[i]) - height[i]
        
        # return sum(water)

        # Greedy with 2 pointers, Time O(n), Space O(1)
        n = len(height)
        max_left = height[0]
        left_pointer = 0
        max_right = height[n-1]
        right_pointer = n-1
        water = 0

        while (left_pointer <= right_pointer):
            if max_left < max_right:
                max_left = max(max_left, height[left_pointer])
                water += max_left - height[left_pointer]
                left_pointer += 1
            else:
                max_right = max(max_right, height[right_pointer])
                water += max_right - height[right_pointer]
                right_pointer -= 1
        
        return water




