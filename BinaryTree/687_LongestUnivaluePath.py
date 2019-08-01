# TIPS:
# Since the longest path may not pass through the root
# get the length of left and right of a node, then compare left+right
# but only return the longer one between left and right since if the longer one contains the parent, 
# left + right won't be the answer
#
# do preorder traverse

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        best = [0]
        self.dfs(root, best)
        
        return best[0]
    
    def dfs(self, root, best):
        if not root: return 0
        
        left, right = self.dfs(root.left, best), self.dfs(root.right, best)
        
        left = left+1 if root.left and root.left.val == root.val else 0
        right = right+1 if root.right and root.right.val == root.val else 0
        best[0] = max(best[0], left + right)
        
        return max(left, right)