# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            nodeVal = node.val
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            maxOnePath = max(nodeVal, nodeVal + max(leftSum, rightSum))
            currMax = max(maxOnePath, nodeVal + leftSum + rightSum)
            self.res = max(self.res, currMax)
            return maxOnePath
        
        dfs(root)
        return self.res
