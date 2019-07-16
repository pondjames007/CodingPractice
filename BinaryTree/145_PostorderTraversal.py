# TIPS:
# use stack and do preorder right subtree first version
# then reverse the ans array will get postorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        stack = [root]
        ans = []
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            
        return ans[::-1]