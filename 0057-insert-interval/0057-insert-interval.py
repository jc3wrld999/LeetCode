class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # 기존 구간의 앞이 new보다 뒤에 있으면 new를 추가하고 기존 구간 뒤 부분을 추가해서 리턴
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # 기존 구간의 끝이 new보다 앞에 있으면 기존 구간 push
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # 겹치는 경우 최솟값부터 최댓값 까지 추가
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res