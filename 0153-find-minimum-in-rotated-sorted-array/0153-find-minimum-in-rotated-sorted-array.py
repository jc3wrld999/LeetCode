class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         r -= 1
        #     elif r != len(nums) - 1:
        #         return nums[r]
        #     else:
        #         return nums[r+1]
        return min(nums)
        