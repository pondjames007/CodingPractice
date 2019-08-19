# TIPS:
#
# BFS
# State(node, color)
# One Queue, 2 HashTables (one for each color)
# Swap colors for next step
# Start: {(0,0), {0,1}}
# T: O(V+E)
# S: O(V+E) 
import queue

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        edges_r = [set() for _ in range(n)]
        edges_b = [set() for _ in range(n)]
        for e in red_edges:
            edges_r[e[0]].add(e[1])
        for e in blue_edges:
            edges_b[e[0]].add(e[1])
        
        seen_r = set()
        seen_b = set()
        ans = [-1]*n
        q = queue.Queue() # (node, color)
        q.put((0,0)) # blue
        q.put((0,1)) # red
        seen_r.add(0)
        seen_b.add(0)
        
        steps = 0
        while not q.empty():
            size = q.qsize()
            while size:
                size -= 1
                p, is_red = q.get()
                
                ans[p] = min(ans[p], steps) if ans[p] >= 0 else steps
                edges = edges_r if is_red else edges_b
                seen = seen_r if is_red else seen_b
                
                for nxt in edges[p]:
                    if nxt in seen: continue
                    seen.add(nxt)
                    q.put((nxt, 1-is_red))
            
            steps += 1
        
        return ans
        
        