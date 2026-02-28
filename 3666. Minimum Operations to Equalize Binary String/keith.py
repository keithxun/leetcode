# Note that order of bits does not matter
        # let z be #0 picked, then k-z be number of 1, x be #0, n be #1
        # end #0 = x - 2z + k 
        # z valid range [max(0, x + k - n), min(k, x)]
        # we then do bfs for sp with nodes as #0 and edge as valid transition
        # optimize using parity, dsu ds to reduce linear search via pruning

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        start = s.count('0')
        if start == 0: #edge case
            return 0
        if k == 0:
            return -1

        dist = [-1] * (n + 1) # store steps to reach xx state
        dist[start] = 0
        q = deque([start])

        # parent[p][i] = smallest unvisited number >= i with parity p, (n+1) = none 
        parent = [list(range(n + 2)) for _ in range(2)]
        def find(p: int, i:int) -> int:
            # return smallest unvisited y >= i with parity p
            if (i & 1) != p:
                i += 1
            if i > n:
                return n + 1
            if parent[p][i] == i:
                return i
            parent[p][i] = find(p, parent[p][i]) # Path compression
            return parent[p][i]
        
        def remove(p: int, i: int) -> None:
            parent[p][i] = find(p, i + 2)

        remove(start & 1, start)

        while q:
            x = q.popleft()
            d = dist[x]
        
            ones = n - x
        
            z_min = max(0, k - ones)
            z_max = min(k , x)

            if z_min > z_max:
                continue

            U = x + k - 2 * z_min
            L = x + k - 2 * z_max
            if U < 0 or L > n:
                continue
            L = max(L, 0)
            U = min(U, n)

            p = (x + k) & 1
            y = find(p, L)
            while y <= U:
                dist[y] = d + 1
                if y == 0:
                    return dist[y]
                q.append(y)
                remove(p, y)
                y = find(p, y)
        return -1 