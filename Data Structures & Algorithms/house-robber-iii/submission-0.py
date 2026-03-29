# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node) -> [int, int]:
            if not node:
                return [0, 0]
            
            withLeft, withoutLeft = dfs(node.left)
            withRight, withoutRight = dfs(node.right)

            return [node.val + withoutLeft + withoutRight, max(withLeft, withoutLeft) + max(withRight, withoutRight)]
        
        withRoot, withoutRoot = dfs(root)
        return max(withRoot, withoutRoot)