# TIPS:
# Calculate Height for every node
# if height difference >= 2: return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        if abs(self.height(root.left) - self.height(root.right)) < 2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        return False
        
        
        return 
    
    def height(self, root):
        if not root: return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1


# Check height difference during getting height will reduce a lot of time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        self.flag = False
        self.getHeight(root)
        return not self.flag
        
    
    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1: 
            self.flag = True
        return max(left, right) + 1