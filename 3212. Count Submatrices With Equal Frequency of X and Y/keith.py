class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        balance = [[0] * (col + 1) for _ in range(row + 1)]
        xcount = [[0] * (col + 1) for _ in range(row + 1)]

        res = 0

        for r in range(row):
            for c in range(col):
                balance[r + 1][c + 1] = (
                    balance[r][c + 1]
                    + balance[r + 1][c]
                    - balance[r][c]
                )

                xcount[r + 1][c + 1] = (
                    xcount[r][c + 1]
                    + xcount[r + 1][c]
                    - xcount[r][c]
                )

                if grid[r][c] == 'X':
                    balance[r + 1][c + 1] += 1
                    xcount[r + 1][c + 1] += 1
                elif grid[r][c] == 'Y':
                    balance[r + 1][c + 1] -= 1

                if balance[r + 1][c + 1] == 0 and xcount[r + 1][c + 1] > 0:
                    res += 1

        return res