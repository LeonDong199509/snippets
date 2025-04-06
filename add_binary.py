class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        # Time O(max(m, n)), Space O(max(m, n))
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >=0 or j >=0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            carry = total // 2
            digit = total % 2
            result.append(str(digit))
        
        result.reverse()
        return "".join(result)
