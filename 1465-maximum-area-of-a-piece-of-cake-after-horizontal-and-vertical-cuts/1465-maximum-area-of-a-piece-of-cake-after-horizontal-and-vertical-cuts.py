class Solution(object):
    def maxArea(self, h, w, hc, vc):
        hc.sort()
        vc.sort()
        max_h, max_v = max(hc[0], h - hc[-1]), max(vc[0], w - vc[-1])
        for i in range(1, len(hc)):
            max_h = max(hc[i] - hc[i-1], max_h)
        for i in range(1, len(vc)):
            max_v = max(vc[i] - vc[i-1], max_v)
        return (max_h * max_v) % 1000000007