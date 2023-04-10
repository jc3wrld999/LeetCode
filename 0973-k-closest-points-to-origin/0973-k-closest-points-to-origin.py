import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minH = []
        for i, p in enumerate(points):
            x = p[0]
            y = p[1]
            closet = x ** 2 + y ** 2
            print(p, closet)
            heapq.heappush(minH, (closet, i))

        for i in range(k):
            minC, minP = heapq.heappop(minH)
            res.append([points[minP][0], points[minP][1]])
        return res
            
        