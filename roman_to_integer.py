class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        double_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        single_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0
        result = 0
        while(i < len(s)):
            if i+1 < len(s) and f"{s[i]}{s[i+1]}" in double_dict:
                result += double_dict[f"{s[i]}{s[i+1]}"]
                i += 2
            else:
                result += single_dict[s[i]]
                i += 1
        
        return result
