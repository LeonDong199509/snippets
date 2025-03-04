class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        # Leetcode 120. Triangle

        # Brutal Force time complexity is O(2^n)
        
        # Dymamic Programing,Time complexity O(n^2), Space complexity O(n^2)
        # import copy
        # dp = copy.deepcopy(triangle)
        # for i in range(len(triangle)-2, -1,-1):
        #     for j, num in enumerate(triangle[i]):
        #         dp[i][j] = min(dp[i+1][j+1], dp[i+1][j]) + num
        
        # return dp[0][0]
        
        # Dymamic Programing,Time complexity O(n^2), Space complexity O(n)
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1,-1):
            for j, num in enumerate(triangle[i]):
                dp[j] = min(dp[j], dp[j+1]) + num
        
        return dp[0]
        
