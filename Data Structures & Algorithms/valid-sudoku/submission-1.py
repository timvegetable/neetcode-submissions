class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = [[0] * 9 for _ in range(9)]
        col_nums = [[0] * 9 for _ in range(9)]
        box_nums = [[0] * 9 for _ in range(9)]
        one = ord("1")
        empty = ord(".") - one

        for i in range(9):
            for j in range(9):
                box_i = (i // 3) * 3 + j // 3
                val = ord(board[i][j]) - one
                row_found = row_nums[i]
                col_found = col_nums[j]
                box_found = box_nums[box_i]
                if val == empty:
                    continue
                # if duplicate found in row, col, or box
                if row_found[val] or col_found[val] or box_found[val]:
                    return False
                row_found[val] = 1
                col_found[val] = 1
                box_found[val] = 1
        
        return True