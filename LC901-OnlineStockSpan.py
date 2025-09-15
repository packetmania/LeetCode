class StockSpanner:

    def __init__(self):
        self.stack = [] # a monotonous decreasing stack

    def next(self, price: int) -> int:
        current_span = 1
        while self.stack and self.stack[-1][0] <= price:
            p, span = self.stack.pop()
            current_span += span
        self.stack.append((price, current_span))
        return current_span


# Optimized solution with single monotonic decreasing (from bottom to top)
# stack which has elements of the set (price, current_span).
# Time complexity: O(1) amortized for each call to next()


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
assert(obj.next(100) == 1)
assert(obj.next(80) == 1)
assert(obj.next(60) == 1)
assert(obj.next(70) == 2)
assert(obj.next(60) == 1)
assert(obj.next(75) == 4)
assert(obj.next(85) == 6)