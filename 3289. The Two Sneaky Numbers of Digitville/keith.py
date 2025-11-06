from common_imports import *

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        h = {}
        res = []
        for n in nums:
            h[n] = h.get(n, 0) + 1
            if h[n] > 1:
                res.append(n)

        return res        
    
s = Solution().getSneakyNumbers([4,3,2,7,8,2,3,1])
print(s)