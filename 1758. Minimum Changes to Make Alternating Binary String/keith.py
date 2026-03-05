class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t0 = ("01" * (n // 2)) + ("0" if n % 2 else "")
        t1 = ("10" * (n // 2)) + ("1" if n % 2 else "")
        
        mism0 = sum(a != b for a, b in zip(s, t0))
        mism1 = sum(a != b for a, b in zip(s, t1))
        return min(mism0, mism1)