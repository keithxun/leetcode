class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        res = 0
        rowCount = [0] * n
        colCount = [0] * m

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1 and rowCount[r] == 1 and colCount[c] == 1:
                    res += 1
        return res