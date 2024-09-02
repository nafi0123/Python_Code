from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[] for _ in range(9) ]
        col=[[] for _ in range(9) ]
        boxes = [ [ [] for _ in range(9) ] for _ in range(9) ]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                num=board[i][j]
                if num in row [i] or num in col[j] or num in boxes[i//3][j//3]:
                    return False
                row[i].append(num)
                col[j].append(num)
                boxes[i//3][j//3].append(num)
        return True
s=Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","5","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

# Time Complexity: O(1)
# Sapce Complexity: O(1)
