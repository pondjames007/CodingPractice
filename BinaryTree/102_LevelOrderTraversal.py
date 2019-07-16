# TIPS:
# Use deque to make queue
# s1 = s2 then s2.clear will also clear s1 since they use the same reference


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        s1 = deque([root])
        s2 = deque([])
        tmp = []
        ans = [[root.val]]
        while s1:
            node = s1.popleft()
            
            if node.left:
                s2.append(node.left)
                tmp.append(node.left.val)
            if node.right: 
                s2.append(node.right)
                tmp.append(node.right.val)
            

            if not s1 and s2:
                ans.append(tmp)
                s1 = s2
                s2 = deque()
                tmp = []
            
        return ans