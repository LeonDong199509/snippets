class Solution:
    def isValid(self, s: str) -> bool:
        
        # Data Structure: Stack
        # Time O(n), Space O(n)
        
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not stack or c != mapping[stack.pop()]:
                    return False
        return not stack
        
