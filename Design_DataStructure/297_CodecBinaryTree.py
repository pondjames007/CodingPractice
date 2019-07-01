# TIPS:
# * use DFS (in stack) to encode
# * use DFS (in recursion) to decode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        tree = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                tree.append(str(node.val))
            else:
                tree.append(str(node))
        
        return ','.join(tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode(data):
            if not data: return None
            val = data.pop(0)
            if val == 'None': return None
            
            root = TreeNode(int(val))
            root.left = decode(data)
            root.right = decode(data)
            
            return root
        l_data = data.split(',')
        return decode(l_data)