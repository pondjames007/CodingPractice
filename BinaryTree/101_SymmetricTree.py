# Tips
#
# Recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        return self.lookup(root.left, root.right)
    
    def lookup(self, left, right):
        if not left or not right:
            return left == right
        
        if left.val != right.val: return False
        
        return self.lookup(left.left, right.right) and self.lookup(left.right, right.left)

# Iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        stack = []
        stack.append((root.left, root.right))
        
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        
        return True