# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        # bfs
        s = [(root, 0)]
        while s:
            node, cur = s.pop()
            cur = (cur << 1) | node.val

            if not node.left and not node.right:
                res += cur
                continue
            
            if node.left:
                s.append((node.left, cur))
            if node.right:
                s.append((node.right, cur))
        return res