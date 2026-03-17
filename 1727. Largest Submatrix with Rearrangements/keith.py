class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Build heights of consecutive 1s
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        ans = 0

        # For each row, sort heights descending
        for r in range(rows):
            heights = sorted(matrix[r], reverse=True)

            for i in range(cols):
                height = heights[i]
                width = i + 1
                ans = max(ans, height * width)

        return ans