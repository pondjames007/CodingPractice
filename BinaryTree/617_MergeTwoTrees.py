# TIPS:
# * RECURSION!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: return None
        
        if not t1: 
            node = TreeNode(t2.val)
            node.left = t2.left
            node.right = t2.right
            
        elif not t2: 
            node = TreeNode(t1.val)
            node.left = t1.left
            node.right = t1.right
        else:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        
        return node