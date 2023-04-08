class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            # 겹치는 경우 end를 업데이트
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            # 겹치는 경우 구간을 push
            else:
                res.append([start, end])
        return res