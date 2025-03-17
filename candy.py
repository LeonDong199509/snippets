class Solution:
    def candy(self, ratings: List[int]) -> int:

        # Greedy with 2 passes strategy
        # Time complexity O(n), Space Complexity O(n)
        # candies = [1] * len(ratings)

        # # From left to right traverse
        # for i in range(1, len(ratings)):
        #     if ratings[i] > ratings[i-1]:
        #         candies[i] = candies[i-1] + 1
        
        # # From right to left traverse
        # for i in range(len(ratings)-2, -1, -1):
        #     if ratings[i] > ratings[i+1]:
        #         candies[i] = max(candies[i], candies[i+1]+1)
        
        # return sum(candies)
        
        # Optimized Solution; Space O(1)
        n = len(ratings)
        if n == 1:
            return 1

        # Variables for tracking
        decreasing = 0  # Track decreasing sequence length
        total = 1  # Running total of candies
        prev = 1  # Previous child's candy count
        peak = 1 # Peak candy


        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:  # Increasing sequence
                peak  = prev + 1
                prev += 1
                decreasing = 0
                total += prev
            elif ratings[i] == ratings[i - 1]:  # Equal rating, reset sequence
                prev = 1
                decreasing = 0
                peak = 1
                total += prev
            else:  # Decreasing sequence
                decreasing += 1
                if peak > decreasing:
                    total += decreasing
                else:
                    total += decreasing + 1 # Make sure peak is always larger
                prev = 1

        return total
