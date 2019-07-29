# TIPS:
# store the answer and the stack for every price smaller than the last one
# if larger than the last one, keep pop out the price and the span
# add the pop out span number will be the answer

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []
        
    def next(self, price: int) -> int:
        if not self.stack or price < self.stack[-1]:
            self.stack.append(price)
            self.span.append(1)
            return 1
        
        ans = 1
        while self.stack and price >= self.stack[-1]:
            self.stack.pop()
            ans += self.span.pop()
        
        self.stack.append(price)
        self.span.append(ans)
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)