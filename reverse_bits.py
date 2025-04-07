class Solution:
    def reverseBits(self, n: int) -> int:
        # 1.   2.   3.  4
        # 1, 10, 11, 100
        
        # 1 % 2 = 1, 1 // 2 = 0
        # 2 % 2 = 0, 2 // 2 = 1
        # 3 % 2 = 1, 3 // 2 = 1
        # 4 % 2 = 0, 4 // 2 = 2

        # Time O(32), Space O(32)
        # Get reversed bits
        bits = []
        mod = n % 2
        left = n // 2
        n = left
        bits.append(mod)
        while (left >= 2):
            mod = n % 2
            left = n // 2
            bits.append(mod)
            n = left
        bits.append(left)

        l = len(bits)
        if l < 32:
            bits = bits + ([0] * (32-l))
        
        # Get integer from bits
        result = 0
        for i, d in enumerate(bits):
            if d == 0:
                continue
            result += 2 ** (31-i)
        return result
            

        
        
