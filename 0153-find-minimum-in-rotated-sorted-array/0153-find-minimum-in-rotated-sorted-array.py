class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = inf
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                res = min(res, nums[l])
                l = m + 1
            else:
                r = m - 1
                res = min(res, nums[m])
        return res
        