class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Greedy is not working
        # result = []
        # l = 0
        # for i in nums:
        #     if not result:
        #         result.append(i)
        #         l += 1
        #     else:
        #         if i == result[-1]:
        #             result[-1] = i
        #         elif i < result[-1]:
        #             if (l > 1 and result[-2] != i) or l == 1:
        #                 result[-1] = i
        #         else:
        #             result.append(i)
        #             l += 1
        
        # return len(result)

        # Dynamic Programing, time complexity O(n*n), space complexity O(n)
        # dp = [1] * len(nums)
        # for i, n in enumerate(nums):
        #     if i == 0:
        #         continue
        #     for j, n_i in enumerate(nums[:i]):
        #         if n_i < n:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)

        # Greedy + Binary Search, time complexity O(nlogn), space complexity O(n)
        def binary_search(n, tails):
            left = 0
            right = len(tails) - 1
            while (left <= right):
                middle = (left + right) // 2
                if tails[middle] == n:
                    return middle
                elif tails[middle] > n:
                    right = middle - 1
                else:
                    left = middle + 1
            
            return left

        # A list used to store the smallest tail of index + 1 length subsequence
        tails = []
        for i, n in enumerate(nums):
            # If it's the first num or it's bigger than the longest subsequence's tail, add it to the list
            if i == 0 or tails[-1] < n:
                tails.append(n)
            else:
                # Otherwise we find the position where we have a smaller tail for the longest subsequence we can update (Greedy Algo); Because the smaller the tail and the longer the subsequence is, the more change we can have a longer subsequence in the next iteration
                position = binary_search(n, tails)
                tails[position] = n
        
        return len(tails)
