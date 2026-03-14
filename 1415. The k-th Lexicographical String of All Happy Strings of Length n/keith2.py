class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        k -= 1  # make k 0-based
        ans = []

        # First character: 3 choices
        block = 1 << (n - 1)
        first_idx = k // block
        ans.append("abc"[first_idx])
        k %= block

        # Remaining characters: 2 choices each
        for i in range(1, n):
            block >>= 1
            prev = ans[-1]

            if prev == 'a':
                choices = ['b', 'c']
            elif prev == 'b':
                choices = ['a', 'c']
            else:
                choices = ['a', 'b']

            idx = k // block
            ans.append(choices[idx])
            k %= block

        return "".join(ans)