class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            arr = [0] * 9
            for i in range(len(row)):
                if row[i] != '.':
                    arr[int(row[i]) - 1] += 1
                    if arr[int(row[i]) - 1] > 1:
                        return False
        for i in range(len(board)):
            arr = [0] * 9
            for j in range(len(board)):
                if board[j][i] != '.':
                    arr[int(board[j][i]) - 1] += 1
                    if arr[int(board[j][i]) - 1] > 1:
                        return False
        x = 0
        for topoffset in range(0, 9, 3):
            for leftoffset in range(0, 9, 3):
                arr = [0] * 9
                for i in range(0, 3, 1):
                    for j in range(0,3,1):
                        if board[i + topoffset][j + leftoffset] != '.':
                            arr[int(board[i + topoffset][j + leftoffset]) - 1] += 1
                            if arr[int(board[i + topoffset][j + leftoffset]) - 1] > 1:
                                return False
        return True
            