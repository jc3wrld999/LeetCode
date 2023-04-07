class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        iSize = []
        iCnt = 0
        def bfs(r, c):
            s = 1
            q = [(r, c)]
            visit.add((r, c))
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r1, c1 = q.pop(0)
                for x, y in direction:
                    r2, c2 = r1 + x, c1 + y
                    if r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == '1' and (r2, c2) not in visit:
                        q.append((r2, c2))
                        visit.add((r2, c2))
                        s += 1
            iSize.append(s)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    iCnt += 1
        print(len(visit)) # 1 개수
        print(iSize) # 섬의 사이즈
        print(iCnt) # 섬 개수
        return iCnt
        