class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        iSize = []
        def bfs(r, c):
            temp_s = 1
            q = [(r, c)]
            visit.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r1, c1  = q.pop(0)
                for x, y in directions:
                    r2, c2 = r1 + x, c1 + y
                    if r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == 1 and (r2, c2) not in visit:
                        q.append((r2, c2))
                        visit.add((r2, c2))
                        temp_s += 1

            iSize.append(temp_s)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    bfs(r, c)
        return max(iSize) if len(iSize) > 0 else 0 
                
        