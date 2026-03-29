# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, currMax):
            if not root:
                return 0
            
            res = 1 if root.val >= currMax else 0
            newMax = max(currMax, root.val)
            res += dfs(root.left, newMax) + dfs(root.right, newMax)
            return res
        
        return dfs(root, root.val)