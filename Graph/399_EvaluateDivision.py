from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations: return [-1.0]*len(queries)
        
        graph = defaultdict(list)
        
        for pair, val in zip(equations, values):
                graph[pair[0]].append((pair[1], val))
                graph[pair[1]].append((pair[0], 1/val))
                
        ans = []
        for start, end in queries:
            res = 1.0
            v = self.lookup(graph, start, end, [start], res)
            ans.append(v)
            
        return ans
    
    
    def lookup(self, graph, start, end, path, res):
        if start not in graph or end not in graph: 
            return -1.0
        
        if start == end: return 1.0

        ans = -1
        for node, val in graph[start]:
            if node == end:
                return res * val

            if node not in path:
                tmp = self.lookup(graph, node, end, path+[node], res*val)
                if tmp != -1:
                    ans = tmp
                
        return ans