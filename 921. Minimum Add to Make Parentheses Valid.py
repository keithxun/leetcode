class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left, right = 0, 0
        for c in s:
            if c == '(':
                right += 1
            elif c == ')':
                if right > 0:
                    right -= 1
                else:
                    left += 1
        
        return left + right