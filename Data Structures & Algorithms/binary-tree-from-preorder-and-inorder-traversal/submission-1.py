# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: index for index, val in enumerate(inorder)}

        self.preIndex = 0
        def dfs(l, r):
            if l > r:
                return None
            
            rootVal = preorder[self.preIndex]
            self.preIndex += 1
            root = TreeNode(rootVal)
            inIndex = indices[rootVal]
            root.left = dfs(l, inIndex - 1)
            root.right = dfs(inIndex + 1, r)
            return root
        
        return dfs(0, len(preorder) - 1)