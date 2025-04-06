class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Initial solution
        # Time O(mn), Space O(m+n)
        # m = len(matrix)
        # n = len(matrix[0])

        # rows = set()
        # cols = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        # O(1) Space, O(mn) Time
        m = len(matrix)
        n = len(matrix[0])
        # Set flag of first row and first col
        first_row_has_0 = 0 in matrix[0]
        first_col_has_0 = 0 in [matrix[i][0] for i in range(m)]
        # Use first row and first col to denote if there is 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # Update each index based on first row and first col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # Update first row and first col based on flag
        if first_row_has_0:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_0:
            for i in range(m):
                matrix[i][0] = 0
        
