class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # For each row, find rightmost 1
        zeroes = []
        for r in range(n):
            cur = 0
            for c in range(n-1, -1, -1):
                if grid[r][c] == 0:
                    cur += 1
                else:
                    break
            zeroes.append(cur)

        # Stimulate from top -> down
        swap = 0
        for i in range(n):
            need = n - 1 - i
            
            # Find suitable row, works because difficulty gets "easier" as you go down
            j = i
            while j < n and zeroes[j] < need:
                j += 1
            if j == n:
                return -1

            while j > i:
                zeroes[j], zeroes[j - 1] = zeroes[j - 1], zeroes[j]
                swap += 1
                j -= 1
            
        return swap
