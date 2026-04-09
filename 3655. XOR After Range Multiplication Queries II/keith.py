class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        T = int(n ** 0.5) + 1

        def mod_pow(a: int, e: int) -> int:
            res = 1
            a %= self.MOD
            while e > 0:
                if e & 1:
                    res = (res * a) % self.MOD
                a = (a * a) % self.MOD
                e >>= 1
            return res

        small = [[] for _ in range(T)]

        for l, r, k, v in queries:
            if k >= T:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % self.MOD
                    i += k
            else:
                small[k].append((l, r, v))

        for k in range(1, T):
            if not small[k]:
                continue

            dif = [1] * (n + k + 1)

            for l, r, v in small[k]:
                last = l + ((r - l) // k) * k
                R = last + k

                dif[l] = (dif[l] * v) % self.MOD
                if R < len(dif):
                    dif[R] = (dif[R] * mod_pow(v, self.MOD - 2)) % self.MOD

            for i in range(n):
                if i - k >= 0:
                    dif[i] = (dif[i] * dif[i - k]) % self.MOD
                nums[i] = (nums[i] * dif[i]) % self.MOD

        ans = 0
        for x in nums:
            ans ^= x
        return ans