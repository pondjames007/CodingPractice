# TIPS:
# * The way I am doing is post-order traversal
#   By stacking left and right nodes
# * No. 112 Path Sum I

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        ans = []
        stack = [[root.val, [root.val], root]]
        
        while stack:
            cur_val, cur_list, cur = stack.pop()
            # candidate = cur_list.copy()
            
            if not cur.left and not cur.right:
                if cur_val == sum:
                    ans.append(cur_list)
            
            if cur.left:
                stack.append([cur_val+cur.left.val, cur_list+[cur.left.val], cur.left])
            if cur.right:
                stack.append([cur_val+cur.right.val, cur_list+[cur.right.val], cur.right])
        
        return ans