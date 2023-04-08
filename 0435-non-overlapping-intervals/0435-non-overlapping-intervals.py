class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # 겹치지 않을 경우
            if start >= prevEnd:
                prevEnd = end
            # 겹칠 경우 끝 지점이 큰 구간을 삭제
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res