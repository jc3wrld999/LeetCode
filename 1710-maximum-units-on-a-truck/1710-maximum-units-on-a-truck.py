class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for b,n in boxTypes:
            count = min(b, truckSize)
            ans += count * n
            truckSize -= count
            if truckSize == 0: return ans
        return ans
        