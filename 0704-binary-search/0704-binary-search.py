class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if nums.count(target) > 0 else -1
        