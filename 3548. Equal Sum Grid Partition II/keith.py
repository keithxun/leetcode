class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])

        total = 0
        row_sum = [0] * row
        col_sum = [0] * col

        for r in range(row):
            for c in range(col):
                v = grid[r][c]
                total += v
                row_sum[r] += v
                col_sum[c] += v

        def add_row(freq, r):
            for c in range(col):
                freq[grid[r][c]] += 1

        def remove_row(freq, r):
            for c in range(col):
                v = grid[r][c]
                freq[v] -= 1
                if freq[v] == 0:
                    del freq[v]

        def add_col(freq, c):
            for r in range(row):
                freq[grid[r][c]] += 1

        def remove_col(freq, c):
            for r in range(row):
                v = grid[r][c]
                freq[v] -= 1
                if freq[v] == 0:
                    del freq[v]

        # Horizontal cuts
        topset = defaultdict(int)
        botset = defaultdict(int)
        for r in range(row):
            add_row(botset, r)

        topsum = 0
        for cut in range(row - 1):
            add_row(topset, cut)
            remove_row(botset, cut)
            topsum += row_sum[cut]
            botsum = total - topsum

            if topsum == botsum:
                return True

            if topsum > botsum:
                diff = topsum - botsum
                top_h = cut + 1

                if top_h >= 2 and col >= 2:
                    if diff in topset:
                        return True
                elif top_h == 1:
                    if grid[0][0] == diff or grid[0][col - 1] == diff:
                        return True
                else:
                    if grid[0][0] == diff or grid[cut][0] == diff:
                        return True

            else:
                diff = botsum - topsum
                bot_h = row - cut - 1

                if bot_h >= 2 and col >= 2:
                    if diff in botset:
                        return True
                elif bot_h == 1:
                    r = cut + 1
                    if grid[r][0] == diff or grid[r][col - 1] == diff:
                        return True
                else:
                    if grid[cut + 1][0] == diff or grid[row - 1][0] == diff:
                        return True

        # Vertical cuts
        leftset = defaultdict(int)
        rightset = defaultdict(int)
        for c in range(col):
            add_col(rightset, c)

        leftsum = 0
        for cut in range(col - 1):
            add_col(leftset, cut)
            remove_col(rightset, cut)
            leftsum += col_sum[cut]
            rightsum = total - leftsum

            if leftsum == rightsum:
                return True

            if leftsum > rightsum:
                diff = leftsum - rightsum
                left_w = cut + 1

                if row >= 2 and left_w >= 2:
                    if diff in leftset:
                        return True
                elif left_w == 1:
                    if grid[0][0] == diff or grid[row - 1][0] == diff:
                        return True
                else:
                    if grid[0][0] == diff or grid[0][cut] == diff:
                        return True

            else:
                diff = rightsum - leftsum
                right_w = col - cut - 1

                if row >= 2 and right_w >= 2:
                    if diff in rightset:
                        return True
                elif right_w == 1:
                    c = cut + 1
                    if grid[0][c] == diff or grid[row - 1][c] == diff:
                        return True
                else:
                    if grid[0][cut + 1] == diff or grid[0][col - 1] == diff:
                        return True

        return False