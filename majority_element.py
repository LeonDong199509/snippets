class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # O(n) Space Complexity with Hash Map
        # count = {}
        # majority = None
        # majority_count = 0
        
        # for i in nums:
        #     count[i] = count.get(i, 0) + 1
        #     if count[i] > majority_count:
        #         majority = i
        #         majority_count = count[i]
        
        # return majority

        # O(1) Space Complexity
        majority = None
        count = 0
        for i in nums:
            # Update majority, when count is reset to 0
            if count == 0:
                majority = i
            
            # Update count by checking if the value equals to the majority, finally the majority will always be the one who reset the count to 0
            if i == majority:
                count += 1
            else:
                count -= 1
        
        return majority



        
