class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # Time complexity O(nlogn), Space complexity O(n)
        citations.sort()
        length = len(citations)
        result = 0
        for index, citation in enumerate(citations):
            if citation <= (length - index):
                result = max(result, citation)
            else:
                result = max(result, length - index)
        
        return result
