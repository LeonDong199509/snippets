class Solution:
    def reverseWords(self, s: str) -> str:

        # Pythonic solution
        # •	Time Complexity:
        # •	.split() takes O(n), where n is the length of s.
        # •	.reverse() (or [::-1]) takes O(n).
        # •	" ".join() takes O(n).
        # •	Overall, the time complexity is O(n).
        # •	Space Complexity:
        # •	.split() creates a list of words O(n).
        # •	.reverse() or slicing takes O(n) space.
        # •	" ".join() creates the final string O(n).
        # •	Overall, the space complexity is O(n) (excluding the output).
        # s = s.split() 
        # s.reverse()
        # return " ".join(s)

        # Use 2 pointers to implement custom reverse()
        s = s.split()
        i = 0
        j = len(s) - 1

        # Reverse s
        while (i <= j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return " ".join(s)



