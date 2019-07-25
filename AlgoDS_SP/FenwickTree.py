class FenwickTree: # Binary Inedxed Tree
    def __init__(self, n):
        self.sums_ = [0]*(n+1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, delta):
        while i < len(self.sums_):
            sums_[i] += delta
            i += self.lowbit(i)

    def query(self, i):
        sum_ = 0
        while i > 0:
            sum_ += sums_[i]
            i -= self.lowbit(i)

        return sum_