class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row_nums = [sudoku.copy() for _ in range(9)]
        col_nums = [sudoku.copy() for _ in range(9)]
        box_nums = [sudoku.copy() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box_i = (i // 3) * 3 + j // 3
                val = board[i][j]
                row_remaining = row_nums[i]
                col_remaining = col_nums[j]
                box_remaining = box_nums[box_i]
                if val == ".":
                    continue
                # if duplicate found in row, col, or box
                if (
                    val not in row_remaining
                    or val not in col_remaining
                    or val not in box_remaining
                ):
                    return False
                row_remaining.remove(val)
                col_remaining.remove(val)
                box_remaining.remove(val)
        
        return True