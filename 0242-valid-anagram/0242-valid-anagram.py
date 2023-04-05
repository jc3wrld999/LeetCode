
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = list(set(s))
        T = list(set(t))
        S.sort()
        T.sort()
        if S != T:
            return False
        for i in S:
            if s.count(i) != t.count(i):
                return False
        return True
