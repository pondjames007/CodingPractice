# TIPS:
#
# Recursive
# check recursively if (1.left == 2.left and 1.right == 2.right) or (1.left == 2.right and 1.right == 2.left)
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)))
                