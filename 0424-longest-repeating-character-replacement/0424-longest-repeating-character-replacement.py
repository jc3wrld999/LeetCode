
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            # 문자마다 누적 개수를 세준다.
            count[s[r]] = 1 + count.get(s[r], 0)
            # 현재까지 최대 문자 수
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            # 최댓값 업데이트
            res = max(res, r - l + 1)
        return res
            
        
        