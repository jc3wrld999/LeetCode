class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # 짝수
            l, r = i, i
            # 같은 동안 루프문
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 최대 길이보다 클 경우 최대값과 최대 길이 업데이트
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # 홀수
            l, r = i, i + 1
            # 같은 동안 루프문
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 최대 길이보다 클 경우 최대값과 최대 길이 업데이트
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
        
        
        