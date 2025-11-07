from typing import List, Optional

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 = empty, 1 = wall, 2 = guard, 3 = seen/guarded
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2

        # left -> right
        for r in range(m):
            seen = False
            for c in range(n):
                if grid[r][c] == 1:          # wall blocks
                    seen = False
                elif grid[r][c] == 2:        # guard starts vision
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3

        # right -> left
        for r in range(m):
            seen = False
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3

        # top -> bottom
        for c in range(n):
            seen = False
            for r in range(m):
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3

        # bottom -> top
        for c in range(n):
            seen = False
            for r in range(m - 1, -1, -1):
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen and grid[r][c] == 0:
                    grid[r][c] = 3

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    res += 1
        return res
