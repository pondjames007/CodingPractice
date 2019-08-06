# TIPS:
# Build a graph from the tree
# Do Search from the graph


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        self.buildGraph(root, graph)
        
        ans = []
        self.lookup(graph, target.val, K, 0, -1, ans)
        
        return ans
        
        
    def buildGraph(self, root, graph):
        if not root: return
        
        if root.left:
            graph[root.val].append(root.left.val)
            graph[root.left.val].append(root.val)
            self.buildGraph(root.left, graph)
        if root.right:
            graph[root.val].append(root.right.val)
            graph[root.right.val].append(root.val)
            self.buildGraph(root.right, graph)
            
        return
            
    def lookup(self, graph, cur, K, dist, prev, ans):
        if dist == K: 
            ans.append(cur)
            return
        
        for nxt in graph[cur]:
            if nxt == prev: continue
            self.lookup(graph, nxt, K, dist+1, cur, ans)
        
        return
        