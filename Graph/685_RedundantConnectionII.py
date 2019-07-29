# TIPS:
#
# Case 1: No Duplicate Parents -> Same to #684
# Case 2: A node v has 2 parents (u1, u2)
#       2.1: No cycle -> return the second edge that creates duplicate parents
#       2.2: Cycle -> return {u1, v} or {u2, v} that creates the loop
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [0] * (n+1)
        roots = [0] * (n+1)
        sizes = [1] * (n+1)
        
        ans1 = []
        ans2 = []
        
        for edge in edges:
            x, y = edge
            # A node has 2 parents
            if parents[y] > 0:
                ans1 = [parents[y], y]
                ans2 = edge.copy()
                
                # Delete the latter edge
                edge[0] = edge[1] = -1
                
            parents[y] = x
            
        
        for x, y in edges:
            # Invalid edge (we deleted in step 1)
            if x < 0 or y < 0: continue
            
            if not roots[x]: roots[x] = x
            if not roots[y]: roots[y] = y
            
            px, py = self.find(x, roots), self.find(y, roots)
            
            # Both px and py are already in the tree
            if px == py:
                return ans1 if ans1 else [x, y]
            
            # Union, always merge smaller set (py) to larger set (px)
            if sizes[py] > sizes[px]:
                px, py = py, px
            
            roots[py] = px
            sizes[px] += sizes[py]
            
        
        return ans2
    
    def find(self, node, roots):
        while roots[node] != node:
            roots[node] = roots[roots[node]]
            node = roots[node]
            
        return node