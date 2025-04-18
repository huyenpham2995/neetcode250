from collections import defaultdict
from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)
    square_dict = defaultdict(set)

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == ".":
                continue
            if board[r][c] in row_dict[r] or board[r][c] in col_dict[c] or board[r][c] in square_dict[(r // 3, c // 3)]:
                return False
            row_dict[r].add(board[r][c])
            col_dict[c].add(board[r][c])
            square_dict[(r // 3, c // 3)].add(board[r][c])
    return True