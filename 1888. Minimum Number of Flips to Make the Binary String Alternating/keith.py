class Solution:
    def minFlips(self, s: str) -> int:
        # Rotation = consider string of s + s, then sliding window
        n = len(s)
        ss = s + s

        tem1 = []
        tem2 = []
        for i in range(2 * n):
            tem1.append('0' if i % 2 == 0 else '1')
            tem2.append('1' if i % 2 == 0 else '0')

        diff1 = 0
        diff2 = 0
        res = float('inf')
        left = 0

        for right in range(2 * n):
            if ss[right] != tem1[right]:
                diff1 += 1
            if ss[right] != tem2[right]:
                diff2 += 1
            
            if right - left + 1 > n:
                if ss[left] != tem1[left]:
                    diff1 -= 1
                if ss[left] != tem2[left]:
                    diff2 -= 1
                left += 1
            
            if right - left + 1 == n:
                res = min(diff1, diff2, res)

        return res