class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                # Take left and top then minus overlap
                top = grid[r - 1][c] if r > 0 else 0
                left = grid[r][c - 1] if c > 0 else 0
                diag = grid[r - 1][c - 1] if r > 0 and c > 0 else 0

                grid[r][c] = grid[r][c] + top + left - diag

                if grid[r][c] <= k:
                    res += 1

        return res