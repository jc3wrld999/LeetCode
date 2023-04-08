
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            l = m[0]
            h = m[-1]
            if target in range(l, h+1):
                for j in m:
                    if j == target:
                        return True
                return False
            else:
                continue
        return False
        