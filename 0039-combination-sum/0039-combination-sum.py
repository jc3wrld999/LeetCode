class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # target을 만들면 res에 추가하고 리턴
            if total == target:
                res.append(cur.copy())
                return
            # target을 못 만들면 리턴
            if i >= len(c) or total > target:
                return
            # 초과하기 전까지 추가하고 깊이 우선탐색
            cur.append(c[i])
            dfs(i, cur, total + c[i])
            # 한개 꺼내고 높이 한칸 높여서 다시 깊이 우선탐색
            k = cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)

        return res
        