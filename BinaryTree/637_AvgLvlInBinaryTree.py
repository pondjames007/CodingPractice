# TIPS:
# Use BFS to find the answer
# BFS in stack: have 2 stacks, curr and next
# store next level nodes in next
# go through all nodes in curr
# swap curr and next, then clear next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        
        curr_lvl = [root]
        next_lvl = []
        ans = []
        
        while curr_lvl:
            res = 0
            for node in curr_lvl:
                res += node.val
                if node.left: next_lvl.append(node.left)
                if node.right: next_lvl.append(node.right)
            
            res /= len(curr_lvl)
            ans.append(res)
            
            curr_lvl, next_lvl = next_lvl, curr_lvl
            next_lvl = []
            
        return ans
            