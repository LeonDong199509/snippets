class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Time O(n), Space O(n)
        n = len(digits)
        no_adding = False
        results = []
        for i in range(n-1, -1, -1):
            if no_adding:
                results.append(digits[i])
                continue

            if digits[i] + 1 < 10:
                results.append(digits[i] + 1)
                no_adding = True
            else:
                results.append(0)
                if i == 0:
                    results.append(1)
        
        results.reverse()
        return results
        
