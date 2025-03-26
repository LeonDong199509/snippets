class Solution(object):

    def getArea(self, index_start, index_end, height):

        height_min = min([height[index_start], height[index_end]])
        span = index_end - index_start
        area = height_min * span
        return area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Greedy Solution, Time O(n), Space O(1)
        result = 0

        left = 0
        right = len(height) - 1
        while (left < right):
            if self.getArea(left, right, height) > result:
                result = self.getArea(left, right, height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result



            




        


        
