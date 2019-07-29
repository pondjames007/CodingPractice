class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.sum = val
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, root):
        self.root = None
    
    def buildTree(self, start, end, vals):
        if start == end: return SegmentTreeNode(start, end, vals[start])
        mid = (start + end)//2
        left = self.buildTree(start, mid, vals)
        right = self.buildTree(mid+1, end, vals)
        return SegmentTree(start, end, left.sum+right.sum, left, right)

    def updateTree(self, root, index, val):
        if root.start == root.end == index:
            root.sum = val
            return
        mid = (start+end)//2
        if index <= mid: self.updateTree(root.ledt, index, val)
        else: self.updateTree(root.right, index, val)
        
        root.sum = root.left.sum + root.right.sum

    def querySum(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        mid = (start + end)//2
        if j <= mid: return self.querySum(root.left, i, j)
        elif i > mid: return self.querySum(root.right, i, j)
        else:
            return self.querySum(root.left, i, mid) + self.querySum(root.right, mid+1, j)
