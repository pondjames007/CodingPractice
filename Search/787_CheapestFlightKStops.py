# TIPS:
# Search
# SLOW
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if not flights: return -1
        
        dic = {}
        
        for s, d, p in flights:
            if s not in dic: dic[s] = [(d,p)]
            else: dic[s].append((d,p))
        
        best = [float('inf')]
        self.lookup(dic, src, dst, [src], K, 0, best)
    
        return int(best[0]) if best[0] != float('inf') else -1
        
    def lookup(self, dic, src, dst, path, K, price, best):
        
        if K >= -1:
            if src == dst: best[0] = min(best[0], price)
            else:
                if src in dic:
                    for next_s, p in dic[src]:
                        if next_s in path or price + p >= best[0]: continue
                        self.lookup(dic, next_s, dst, path+[next_s], K-1, price+p, best)

# USE DP -> fast enough, Standard ANSWER