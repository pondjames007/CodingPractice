# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TIPS:
# * RECURSION!!!!!
# * 2D list initialization: [[""] * w for _ in range(h)]
# * wrong way: [[""] * w] * h -> this will make every row has the same reference

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(root: TreeNode) -> int:
            if not root: return 0
            
            return max(getHeight(root.left), getHeight(root.right))+1
        
        def fill(root: TreeNode, row: int, left: int, right: int) -> None:
            if not root: return
            mid = int((left+right)/2)
            self.res[row][mid] = str(root.val)
            
            fill(root.left, row+1, left, mid-1)
            fill(root.right, row+1, mid+1, right)
            
        
        h = getHeight(root)
        w = 2**h - 1
        
        self.res = [[""] * w for _ in range(h)]
        
        fill(root, 0, 0, w-1)
        
        return self.res