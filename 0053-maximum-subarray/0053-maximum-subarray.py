class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, temp = nums[0], 0
        for i in range(len(nums)):
            # 이전까지의 합이 0 이하면 초기화
            if temp < 0:
                temp = 0
            # 현재 값 더해주기
            temp += nums[i]
            # 최댓값과 비교
            if m <= temp:
                m = temp
        return m
                
        