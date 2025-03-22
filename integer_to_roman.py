class Solution:
    def intToRoman(self, num: int) -> str:

        # Recursive solution, Time complexity O(n), Space Complexity On()
        mapping = {
            3000: "MMM",
            2000: "MM",
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            300: "CCC",
            200: "CC",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            30: "XXX",
            20: "XX",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            3: "III",
            2: "II",
            1: "I",
        }
        
        if num == 0:
            return ""
        
        for k in mapping.keys():
            if num >= k:
                current_roman = mapping[k]
                remaining_num = num - k
                return current_roman + self.intToRoman(remaining_num)
        
        
        

        
