class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Use a stack for backtracking
        res = []
        chars = ['a', 'b', 'c']

        def backtrack(curr):
            if len(res) == k:
                return
            if len(curr) == n:
                res.append("".join(curr))
                return
            
            for ch in chars:
                if not curr or curr[-1] != ch:
                    curr.append(ch)
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return res[k - 1] if k <= len(res) else ""

            

