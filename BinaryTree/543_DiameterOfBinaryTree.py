# TIPS:
# Similar to #687
# do preorder traverse

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        
        best = [0]
        
        self.dfs(root, best)
        
        return best[0]
    
    def dfs(self, root, best):
        if not root: return 0
        
        left, right = self.dfs(root.left, best), self.dfs(root.right, best)
        
        if root.left: left += 1 
        if root.right: right += 1
        
        best[0] = max(best[0], left+right)
        
        return max(left, right)