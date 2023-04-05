import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(re.findall('[a-zA-Z0-9]', s)).lower()

        l = 0
        h = len(s) - 1
        while h > l:
            
            if s[l] != s[h]:
                return False
            l, h = l+1, h-1
        return True