from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks) # Counter({'A': 3, 'B': 3})
        maxHeap = [-cnt for cnt in count.values()] # [-3, -3]
        heapq.heapify(maxHeap)
        time = 0
        q = []
        while maxHeap or q:
            time += 1
            if maxHeap: # 대기열에서 꺼냄
                cnt = 1 + heapq.heappop(maxHeap) # 수행
                if cnt: # cnt != 0 남은 개수가 0보다 클 때 큐에 넣어줌
                    q.append([cnt, time + n])
            if q and q[0][1] == time: # 큐의 첫번째 요소가 지금 시간과 같으면 대기열에 넣어줌
                heapq.heappush(maxHeap, q.pop(0)[0])
        return time