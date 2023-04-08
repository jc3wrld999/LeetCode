import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = []
        for w in stones:
            heapq.heappush(maxH, -w)
        while len(maxH) > 1:
            a, b = -heapq.heappop(maxH), -heapq.heappop(maxH)
            w = abs(a - b)
            if w != 0:
                heapq.heappush(maxH, -w)
        return -maxH[-1] if maxH else 0