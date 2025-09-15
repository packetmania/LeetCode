class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)


# Time complexity: O(n) for n calls to ping
# Space complexity: O(n) for n calls to ping

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
assert(obj.ping(1) == 1)
assert(obj.ping(100) == 2)
assert(obj.ping(3001) == 3)
assert(obj.ping(3002) == 3)