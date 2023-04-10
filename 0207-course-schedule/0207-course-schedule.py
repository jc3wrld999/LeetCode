class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 만들기
        preMap = { i: [] for i in range(numCourses)} 
        for n, pre in prerequisites:
            preMap[n].append(pre)
        # dfs 탐색
        visitSet = set()
        def dfs(node):
            if node in visitSet:
                return False
            if preMap[node] == []:
                return True
            visitSet.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            visitSet.remove(node)
            preMap[node] = []
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True