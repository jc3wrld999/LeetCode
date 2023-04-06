
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # 빠져나옴
            if i >= len(nums):
                res.append(subset.copy())
                return
            # 추가할때
            subset.append(nums[i])
            dfs(i+1)

            # 추가안할때
            subset.pop()
            dfs(i+1)
        dfs(0)

        return res
        