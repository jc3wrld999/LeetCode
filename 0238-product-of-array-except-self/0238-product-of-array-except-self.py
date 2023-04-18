class Solution(object):
    def productExceptSelf(self, nums):
        '''
        Leetcode 238. Product of Array Except Self
        '''
        res = [1] * (len(nums))
        # 왼쪽으로 누적 곱
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            print(prefix)
        # 오른쪽으로 누적 곱
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        