class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        res = []
        for i in nums:
            if i not in s:
                s.add(i)
                res.append(i)
            else:
                res.remove(i)
        return res[-1]