class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
                return
            board[r][c] = "T"
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                capture(r+x, c+y)

        # O -> T
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS-1] or c in [0, COLS-1]) and board[r][c] == "O":
                    capture(r, c)
        # O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # T -> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        print(board)