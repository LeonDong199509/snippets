class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Time O(n), Space O(1)
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            last_digit = x % 10
            left_digits = x // 10
            reversed_num = last_digit
            while (left_digits != 0):
                last_digit = left_digits % 10
                left_digits = left_digits // 10
                reversed_num = reversed_num * 10 + last_digit
            
            return reversed_num == x


        
