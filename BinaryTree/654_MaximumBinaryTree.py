# TIPS:
# slice the array and recursively assign it

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        rootVal = max(nums)
        idx = nums.index(rootVal)
        
        root = TreeNode(rootVal)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        
        return root


# Use stack to track
# when a new number > last element in the stack: pop the last element until stack is empty or the element is > the new number
# if stack still has the element: the new number should be its right child
# if there is last: last should be new number's left child

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        
        stack = [TreeNode(nums[0])]
        last = None
        
        for num in nums[1:]:
            while stack and stack[-1].val < num:
                last = stack.pop()
            
            node = TreeNode(num)
            if stack:
                stack[-1].right = node
            if last:
                node.left = last
            
            stack.append(node)
            last = None
            
            
        return stack[0]        