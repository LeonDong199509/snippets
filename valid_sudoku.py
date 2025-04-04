class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Time O(9*9), Space O(9*9*3)
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(0,9):
            for j in range(0,9):
                # Skip non-digit
                if board[i][j] == '.':
                    continue

                # check rows
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                
                # check columns
                if board[i][j] in columns[j]:
                    return False
                columns[j].add(board[i][j])

                # check boxes, we use the tuple as the key of boxes
                # There are 9 boxes, (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)
                # which can be calculated from index // 3
                if board[i][j] in boxes[(i//3, j//3)]:
                    return False
                boxes[(i//3, j//3)].add(board[i][j])
        
        return True

        
