class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        # Sort Solution
        # Time O(nlogn), Space O(n)
        intervals = sorted(intervals, key=lambda x: x[0])
        pre = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= pre[1]:
                pre = [pre[0], max(pre[1], cur[1])]
            else:
                result.append([pre[0], pre[1]])
                pre = [cur[0], cur[1]]

        result.append([pre[0], pre[1]])
        return result

        
