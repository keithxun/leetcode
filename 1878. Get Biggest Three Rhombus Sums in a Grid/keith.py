from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # down-right diagonal prefix sums (\)
        dr = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dr[i + 1][j + 1] = dr[i][j] + grid[i][j]

        # down-left diagonal prefix sums (/)
        dl = [[0] * (n + 2) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                dl[i + 1][j] = dl[i][j + 1] + grid[i][j]

        def sum_dr(r1: int, c1: int, r2: int, c2: int) -> int:
            # sum on \ diagonal from (r1,c1) to (r2,c2), inclusive
            return dr[r2 + 1][c2 + 1] - dr[r1][c1]

        def sum_dl(r1: int, c1: int, r2: int, c2: int) -> int:
            # sum on / diagonal from (r1,c1) to (r2,c2), inclusive
            return dl[r2 + 1][c2] - dl[r1][c1 + 1]

        vals = set()

        for r in range(m):
            for c in range(n):
                # size 0 rhombus
                vals.add(grid[r][c])

                # try larger rhombuses
                max_k = min(c, n - 1 - c, (m - 1 - r) // 2)
                for k in range(1, max_k + 1):
                    top = (r, c)
                    right = (r + k, c + k)
                    bottom = (r + 2 * k, c)
                    left = (r + k, c - k)

                    border = 0
                    border += sum_dr(top[0], top[1], right[0], right[1])       # top -> right
                    border += sum_dl(right[0], right[1], bottom[0], bottom[1]) # right -> bottom
                    border += sum_dr(left[0], left[1], bottom[0], bottom[1])   # left -> bottom
                    border += sum_dl(top[0], top[1], left[0], left[1])         # top -> left

                    # each corner counted twice
                    border -= grid[top[0]][top[1]]
                    border -= grid[right[0]][right[1]]
                    border -= grid[bottom[0]][bottom[1]]
                    border -= grid[left[0]][left[1]]

                    vals.add(border)

        return sorted(vals, reverse=True)[:3]