class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        windows = []
        l = 0
        for r in range(len(nums)):

            # 오름차순일 때 작은값들 다 뺌
            while windows and nums[windows[-1]] < nums[r]:
                windows.pop()
            windows.append(r)

            if l > windows[0]:
                windows.pop(0)

            if (r+1) >= k:
                res.append(nums[windows[0]])
                l += 1

        return res
        