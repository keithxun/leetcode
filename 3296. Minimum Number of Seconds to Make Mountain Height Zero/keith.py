import heapq
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []
        
        # (next_finish_time, worker_time, completed_units)
        for w in workerTimes:
            heap.append((w, w, 1))
        
        heapq.heapify(heap)
        res = 0
        
        while mountainHeight > 0:
            finish_time, w, k = heapq.heappop(heap)
            res = finish_time
            mountainHeight -= 1
            
            # increase next work time
            next_time = finish_time + (k + 1) * w
            heapq.heappush(heap, (next_time, w, k + 1))
        
        return res