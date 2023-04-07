class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]    

        while q and fresh > 0:
            for i in range(len(q)):
                r1, c1 = q.pop(0)
                for x, y in directions:
                    r2, c2 = r1 + x, c1 + y
                    if r2 in range(ROWS) and c2 in range(COLS) and grid[r2][c2] == 1:
                        grid[r2][c2] = 2
                        q.append([r2, c2])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1