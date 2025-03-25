class Solution:
    def isHappy(self, n: int) -> bool:
        
        #We use a set to track numbers we’ve seen before. If we encounter a number we’ve seen before, we know we’re in a cycle and can return False. If we reach 1, we return True.
        # Complexity Analysis
        # •	Each number n has at most O(log n) digits.
        # •	The sum of the squares operation takes O(log n).
        # •	Since numbers repeat in a cycle or reach 1, the process is O(log n) in time.
        # •	We use O(log n) extra space for the seen set.
        already_met_numbers = set()
        while (n != 1):
            print(n)
            n = sum(int(d) ** 2 for d in str(n))
            if n in already_met_numbers:
                return False
            elif n == 1:
                return True
            else:
                already_met_numbers.add(n)
        
