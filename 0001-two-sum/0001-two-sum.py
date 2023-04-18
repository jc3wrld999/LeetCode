class Solution(object):
    def twoSum(self, nums, target):
        prev = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in prev.keys():
                return [prev.get(diff), i]
            prev[v] = i
            
        