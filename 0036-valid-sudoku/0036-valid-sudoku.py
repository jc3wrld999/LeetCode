class Solution(object):
    def isValidSudoku(self, board):
        '''
        Leetcode 36. Valid Sudoku
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or
                  board[r][c] in cols[c] or
                  board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True

        