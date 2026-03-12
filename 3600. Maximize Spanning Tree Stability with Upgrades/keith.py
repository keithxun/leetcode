from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


class Solution:
    def can(self, X, n, edges, k):
        dsu = DSU(n)
        comps = n
        used_upgrades = 0

        free_edges = []
        upgrade_edges = []

        # Mandatory edges
        for u, v, s, must in edges:
            if must == 1:
                if s < X:
                    return False
                if not dsu.union(u, v):
                    # mandatory edges create a cycle
                    return False
                comps -= 1
            else:
                if s >= X:
                    free_edges.append((u, v))
                elif 2 * s >= X:
                    upgrade_edges.append((u, v))

        # Free optional edges
        for u, v in free_edges:
            if dsu.union(u, v):
                comps -= 1

        # Upgraded edges only if needed
        for u, v in upgrade_edges:
            if dsu.union(u, v):
                comps -= 1
                used_upgrades += 1
                if used_upgrades > k:
                    return False

        return comps == 1

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Quick impossible check: even with all edges, graph must be connectable
        dsu = DSU(n)
        for u, v, _, _ in edges:
            dsu.union(u, v)
        root = dsu.find(0)
        for i in range(1, n):
            if dsu.find(i) != root:
                return -1

        low = 0
        high = max(2 * s if must == 0 else s for _, _, s, must in edges)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.can(mid, n, edges, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans