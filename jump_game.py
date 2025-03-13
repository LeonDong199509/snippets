class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Initial Solution with Time Complexity O(n^3), Space Complexity O(n^2)

        # length = len(nums)
        # if length <= 1:
        #     return True
        # storage = [[False for _ in range(length)] for _ in range(length)]

        # for i in range(length-2, -1, -1):
        #     for j in range(i+1, length):
        #         gap = j - i
        #         # Direct access
        #         if nums[i] >= gap:
        #             storage[i][j] = True
        #         # Check indirect access
        #         else:
        #             for g in range(1, gap):
        #                if storage[i][i+g] and storage[i+g][j]:
        #                    storage[i][j] = True
        #                    break

        # return storage[0][length-1]

        
        # Best Solution with Backward Greedy; Time Complexity O(n), Space Complexity O(1)
        # 1️⃣ Greedy Choice Property
        # •	A problem exhibits the Greedy Choice Property if making a locally optimal choice at each step leads to a globally optimal solution.
        # •	In this approach, at each step, we greedily choose the earliest index (goal) that can reach the last index.
        # •	Instead of checking all possible jumps from an index, we immediately update goal if the current position can reach it.
        # •	Locally optimal choice: Moving goal backward if we can reach it.
        # •	Globally optimal result: If goal reaches index 0, we can reach the end.

        # 2️⃣ Optimal Substructure
        # 	•	A problem has Optimal Substructure if an optimal solution to the whole problem can be built from optimal solutions of subproblems.
        # 	•	Here, we reduce the problem step by step, shrinking the required path.
        # 	•	If we determine goal = 3 can reach n-1, then reaching goal = 3 becomes the new subproblem.
        # 	•	We repeat this until we either:
        # 	•	Reach index 0 (Success ✅)
        # 	•	Run out of possible jumps (Fail ❌)

        # length = len(nums)
        # if length <= 1:
        #     return True
        
        # goal = length - 1
        # current_index = length - 2
        # while(current_index >= 0):
        #     if nums[current_index] >= (goal - current_index):
        #         goal = current_index
        #     current_index -= 1
        #     if goal == 0:
        #         return True
        
        # return False


        # Forward Greedy; Time Complexity O(n), Space Complexity O(1)
        # Greedy choice property: at every iteration, we are getting the max reach distance we can have. And it will also be the global max reach distance.
        # Optimal substructure: For max reach length at i, it relys on the max reach length at i-1: max_reach_distance = max(max_reach_distance, i+nums[i])
        
        # length = len(nums)
        # if length <= 1:
        #     return True
        
        # max_reach_distance = nums[0]
        # for i in range(0,length-1):
        #     if i > max_reach_distance:
        #         return False
        #     max_reach_distance = max(max_reach_distance, i+nums[i])
        #     if max_reach_distance >= length - 1:
        #         return True
        
        # return False

        
        # DP, time complexity O(n^2), space complexity O(n)
        length = len(nums)
        dp = [False] * length
    
        # Always can jump to itself
        dp[-1] = True

        for i in range(length-2, -1, -1):
            # The gap between target and current index
            gap = (length - 1) - i
            for j in range(gap, 0, -1):
                if nums[i] >= j and dp[i+j]:
                    dp[i] = True
                    break

        return dp[0]

        

        
