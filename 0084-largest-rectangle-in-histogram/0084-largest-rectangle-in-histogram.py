class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        N = len(h)
        stack = []
        m = []
        for i in range(N):

            # pop
            if stack and stack[-1][1] > h[i]:
                j = i
                while stack and stack[-1][1] >= h[i]:
                    index, height = stack.pop()
                    m.append((i - index) * height)
                    j = index

                stack.append((j, h[i]))
            else:
                stack.append((i, h[i]))
        
        while stack:
            index, height = stack.pop()
            m.append((N - index) * height)

        
        print(m)
        return max(m)
        