class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [] # 온도, 인덱스
        res = [0 for _ in range(len(T))]
        
        for i, t in enumerate(T):
            # 스택의 맨 위의 값보다 작아질 때 까지 pop
            while stack and t > stack[-1][0]:
                t2, i2 = stack.pop()
                res[i2] = (i - i2) 

            stack.append([t, i])
        return res
        