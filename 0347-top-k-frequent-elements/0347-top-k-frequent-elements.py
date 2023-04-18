class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # {1: 3, 2: 2, 3: 1}
        for n, c in count.items():
            freq[c].append(n) # [[], [3], [2], [1], [], [], []]
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res