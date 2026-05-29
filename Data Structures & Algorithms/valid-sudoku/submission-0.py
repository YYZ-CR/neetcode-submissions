class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == ".":
                    continue
                #row check
                if board[row][column] in board[row][column+1:]: #doesn't double check
                    return False
                #column check
                if board[row][column] in [board[r][column] for r in range(row+1, len(board))]: #doesn't double check
                    return False
                #box check
                for i in range(3*(row//3)+row%3, 3*(row//3)+3):
                    for j in range(3*(column//3), 3*(column//3)+3):
                        if (board[row][column] == board[i][j]) and row!=i and column != j:
                            return False
        return True


