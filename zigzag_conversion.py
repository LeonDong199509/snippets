class Solution:
    def convert(self, s: str, numRows: int) -> str:
    #     4# 0 4 8   12  n + n-2= 4
    #     2# 13579 1113  n=3, n-2=1
    #     4# 2 6 10      n + n-2= 4

    #     6  # 0  6    12 n+ n-2 = 6
    #     4,2# 1 57  1113 n=4, n-2=2
    #     2,4# 24 810    n-2=2, n=4
    #     6  # 3  9      n + n-2= 4


    #     8 # 0.  8
    #    6,2# 1  79  (n-1-i)*2, i + i
    #     4 # 2 610    
    #    2,6# 35 1113 
    #     8 # 4  12

        # Time complexity O(n), Space Complexity O(1)
        # Handle edge cases
        if numRows == 1:
            return s
        
        result = ""
        current_row = 0
        s_l = len(s)
        while (current_row < min(numRows, s_l)):
            # Staring point
            current_index = current_row
            result += s[current_index]
            
            # For current row, loop for downward and upward, until the index is out of length
            while (current_index < s_l):
                # Going downward, then upward
                down_index_gap = (numRows-1-current_row) * 2
                if down_index_gap > 0:
                    current_index += down_index_gap
                    if current_index < s_l:
                        result += s[current_index]
                
                # Going upward, then downward
                up_index_gap = current_row * 2
                if up_index_gap > 0:
                    current_index += up_index_gap
                    if current_index < s_l:
                        result += s[current_index]
                
                # Handle Edge case
                if down_index_gap == 0 == up_index_gap:
                    break

            current_row += 1
        return result

