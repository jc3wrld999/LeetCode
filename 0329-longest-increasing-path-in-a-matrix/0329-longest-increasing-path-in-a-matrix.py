class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        visit = []
        memo = {}
        L, M = len(matrix), len(matrix[0])
        def move(r, c, visit, prev):

            if r not in range(L) or c not in range(M) or (r, c) in visit and matrix[r][c] <= prev:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            # 탐색
            cnt = 1
            for r1, c1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r2, c2 = r + r1, c + c1

                visit.append((r2, c2))
                cnt = max(cnt, 1 + move(r2, c2, visit, matrix[r][c]))
                visit.remove((r2, c2))

            memo[(r, c)] = cnt
            return memo[(r, c)]
        max_cnt = 0
        for r in range(L):
            for c in range(M):
                visit.append((r, c))
                max_cnt = max(move(r, c, visit, -1), max_cnt)
                visit.remove((r, c)) 
        return max_cnt
                    
        