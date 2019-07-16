# TIPS:
# Go through the tree and find out the minimum val except root
# slow

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        
        stack = [root]
        ans = root.val
        
        while stack:
            node = stack.pop()
            if ans == root.val: ans = node.val
            if node.val > root.val and node.val < ans: ans = node.val
                
            if node.left: 
                stack.append(node.left)
                stack.append(node.right)
                
        if ans == root.val: return -1
        
        return ans



# Only check the side equal to root.val
# another side will be the candidate
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        if not root.left: return -1
        
        if root.left.val > root.right.val:
            stack = [root.right]
            candidate = root.left.val
        elif root.right.val > root.left.val:
            stack = [root.left]
            candidate = root.right.val
        else:
            stack = [root]
            candidate = root.val
            
        ans = root.val
        
        while stack:
            node = stack.pop()
            if ans == root.val: ans = node.val
            if node.val > root.val and node.val < ans: ans = node.val
                
            if node.left: 
                stack.append(node.left)
                stack.append(node.right)
                
        if ans == root.val and candidate == root.val: return -1
        if ans == root.val and candidate != root.val: return candidate
        if ans > candidate: return candidate
        
        return ans
                