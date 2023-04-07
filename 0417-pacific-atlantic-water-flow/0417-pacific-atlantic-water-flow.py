class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # 태평양, 대서양
        # dfs
        def dfs(r, c, visit, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                dfs(r + x, c + y, visit, heights[r][c])
        # 동서남북에서 시작해서 깊이 우선탐색으로 pac, atl 방문 노드 저장      
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res