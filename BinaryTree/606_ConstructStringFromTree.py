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
        
        # s: root, l: left child tree, r: right child tree
        # case0: l == null, r == null
        #       -> s
        # case1: r == null
        #       -> s(l)
        # case2: l == null or l,r has something (since you don't omit () when left is null unless right is also null)
        #       -> general pattern: s(l)(r)

        left = "({})".format(self.tree2str(t.left)) if t.left or t.right else ""
        right = "({})".format(self.tree2str(t.right)) if t.right else ""
        
        return "{}{}{}".format(t.val, left, right)