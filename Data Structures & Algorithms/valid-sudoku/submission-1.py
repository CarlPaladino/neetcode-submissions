class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])
        
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                
                seen.add(board[j][i])

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                seen = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in seen:
                            return False
                        
                        seen.add(board[row][col])

        return True