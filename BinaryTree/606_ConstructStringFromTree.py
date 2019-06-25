# TIPS:
# * remember to check right child when adding "left"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""
        
        left = "({})".format(self.tree2str(t.left)) if t.left or t.right else ""
        right = "({})".format(self.tree2str(t.right)) if t.right else ""
        
        return "{}{}{}".format(t.val, left, right)