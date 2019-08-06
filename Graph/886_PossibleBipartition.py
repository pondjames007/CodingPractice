# TIPS:
# Graph Coloring
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes: return True
        
        graph = collections.defaultdict(list)
        color = [0]*(N+1) # 0: unknown, 1: blue, -1: red
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1, N+1):
            if color[i] == 0 and not self.coloring(graph, color, i, 1): return False
            
        return True
    
    
    def coloring(self, graph, color, cur, col):
        color[cur] = col
        for nxt in graph[cur]:
            if color[nxt] == col: return False
            if color[nxt] == 0 and not self.coloring(graph, color, nxt, -col): return False
            
        return True
            