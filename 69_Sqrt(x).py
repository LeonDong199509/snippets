class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Original Solution Time O(n)
        # pre = 0
        # for i in range(x+1):
        #     cur_sqr = i * i
        #     if cur_sqr == x:
        #         return i
        #     elif cur_sqr < x:
        #         pre = i
        #     else:
        #         break
        # return pre

        # Binary Search, Time O(logn)
        if x < 2:
            return x
        left = 0
        right = x
        while (left <= right):
            middle = (left + right) // 2
            sqr = middle * middle
            if sqr == x:
                return middle
            elif sqr > x:
                right = middle -1
            else:
                left = middle + 1

        return right
