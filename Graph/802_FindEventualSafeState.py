# TIPS:
#
# Use the concept similar to #417
# DP concept and do backtracing -> TLE
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph: return []
        
        n = len(graph)
        safe = [True if not graph[i] else False for i in range(n)]
        can_take = [i for i in range(n) if not graph[i]]
        
        while True:
            changed = False
            
            for i in range(n):
                if safe[i]: continue
                
                tmp = [safe[j] for j in graph[i]]
                if all(tmp):
                    safe[i] = True
                    changed = True
                    break
            if not changed: break
                
        return [i for i in range(n) if safe[i]]

# Do Simple DFS -> TLE        
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph: return []
        
        n = len(graph)
        
        safe = [True for _ in range(n)]
        
        for i in range(n):
            self.lookup(graph, i, [i], safe)
        
        return [i for i in range(n) if safe[i]]
            
    
    def lookup(self, graph, i, visited, safe):
        if not graph[i]: return
        
        for j in graph[i]:
            if j in visited:
                for k in visited:
                    safe[k] = False
                    return
            else:
                self.lookup(graph, j, visited + [j], safe)
                
        return

# Do DFS but with state tag
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        ans = []
        seen = [0] * n
        def dfs(node):
            if seen[node] != 0:
                return seen[node] == 2
            seen[node] = 1
            for neighbor in graph[node]:
                if seen[neighbor] == 1 or not dfs(neighbor):
                    return False
            seen[node] = 2
            return True           
        for node in range(n):
            if dfs(node):
                ans.append(node)
        return ans