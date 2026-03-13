class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish(seconds: int) -> bool:
            total = 0
            for w in workerTimes:
                # Solve: w * k * (k + 1) // 2 <= seconds
                # => k^2 + k - 2*seconds/w <= 0
                # k = floor((-1 + sqrt(1 + 8*seconds/w)) / 2)
                k = int((math.sqrt(1 + 8 * seconds / w) - 1) // 2)
                total += k
                if total >= mountainHeight:
                    return True
            return False

        left, right = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left