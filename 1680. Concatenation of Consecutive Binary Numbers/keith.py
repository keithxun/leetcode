class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        mod = 1000000007
        for i in range(1, n + 1):
            l = i.bit_length()
            res = ((res << l) + i) % mod

        return res