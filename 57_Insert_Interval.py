class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        # Time O(n), Space O(n)
        i = 0
        result = []
        n = len(intervals)

        # Append all intervals at the left of new interval
        while(i < n and intervals[i][0] < newInterval[0]):
            result.append(intervals[i])
            i += 1

        # Merge new interval to the left
        if len(result) > 0:
            left_interval = result.pop()
            if newInterval[0] <= left_interval[1]:
                newInterval[0] = min(newInterval[0], left_interval[0])
                newInterval[1] = max(newInterval[1], left_interval[1])
            else:
                result.append(left_interval)
        
        # Keep merging new interval to the right
        while (i < n and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Append all intervals at the right of new interval
        while (i < n):
            result.append(intervals[i])
            i += 1
        
        return result



        
