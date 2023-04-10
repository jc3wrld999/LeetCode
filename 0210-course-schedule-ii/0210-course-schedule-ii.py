class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        # 그래프 만들기
        preMap = {i: [] for i in range(numCourses)}
        for n, pre in prerequisites:
            preMap[n].append(pre)
        cycle, visit = set(), set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        for i in preMap:
            if not dfs(i):
                return []
        return res
                