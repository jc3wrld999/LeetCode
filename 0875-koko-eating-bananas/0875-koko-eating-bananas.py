class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_h = r
        while l <= r:
            mid = (l + r) // 2
            # 빨리 먹은 경우 속도를 작게
            hour = sum([math.ceil(i / mid) for i in piles])
            print(hour, mid)
            if hour <= h:
                r = mid - 1
                min_h = min(min_h, mid)
            else:
                l = mid + 1
        return min_h
        
        