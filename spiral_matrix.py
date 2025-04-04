class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])
        total = m * n

        result = []
        visited = set()

        # Start from index (0,0)
        i = 0
        j = 0

        # 4 mode. 1 means going right; 2 means down; 3 means left; 4 means up
        # Start from going right
        mode = 1
        pre_index = (0, 0)
        while (len(result) < total):
            result.append(matrix[i][j])
            visited.add((i,j))
            
            # Mode 1
            if mode % 4 == 1:
                j += 1
            # Mode 2
            elif mode % 4 == 2:
                i += 1
            # Mode 3
            elif mode % 4 == 3:
                j -= 1
            # Mode 4
            else:
                i -= 1

            # Change mode
            if (i,j) in visited or j < 0 or j >= n or i <0 or i >= m:
                mode += 1
                if mode % 4 == 1:
                    i += 1
                    j += 1
                elif mode % 4 == 2:
                    i += 1
                    j -= 1
                elif mode % 4 == 3:
                    i -= 1
                    j -= 1
                else:
                    i -= 1
                    j += 1
        return result
            




            




        
