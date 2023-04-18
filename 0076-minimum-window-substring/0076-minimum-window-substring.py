class Solution(object):
    def minWindow(self, s, t):
        if t == "": return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            # 윈도우 크기 완성하면
            while have == need:
                # 1. 최소값 갱신
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # 2. 오른쪽으로 l좌표 이동
                
                window[s[l]] -= 1 # 윈도우에서 빼고
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1 # have에서 빼고
                l += 1 # l++
        l, r = res
        return s[l:r+1] if resLen != float("infinity")  else ""
        