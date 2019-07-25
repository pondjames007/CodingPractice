class UnionFindSet:
    def __init__(self, n):
        self.parents = [0]*(n+1) # every node is independent, don't care 0, node i has id i
        self.ranks = [0]*(n+1)

        for i in range(n+1):
            self.parents[i] = i

    def Find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.Find(self.parents[x])
        
        return self.parents[x]

    def Union(self, x, y):
        px, py = self.Find(x), self.Find(y)
        if px == py: return False # they are in the same cluster
        
        if self.ranks[px] > self.ranks[py]: self.parents[py] = px
        if self.ranks[py] > self.ranks[px]: self.parents[px] = py
        if self.ranks[px] == self.ranks[py]:
            self.parents[py] = px
            self.ranks[px] += 1

        return True