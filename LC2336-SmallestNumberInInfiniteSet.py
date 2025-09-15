import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []  # MinHeap for added-back numbers
        self.added_set = set()
        self.curr_min = 1  # The minimum of the consecutive sequence

    def popSmallest(self) -> int:
        if self.heap:
            # case 1：heap (added-back) not empty, pop out the smallest
            smallest = heapq.heappop(self.heap)
            self.added_set.remove(smallest)
        else:
            # Case 2：no added numbers, return current minimum
            smallest = self.curr_min
            self.curr_min += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.added_set and num < self.curr_min:
            self.added_set.add(num)
            heapq.heappush(self.heap, num)


# Time complexity: O(log m) for popSmallest and addBack, where m is the size of the heap
# Space complexity: O(m) for the heap and set, where m is the size of the heap

# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
obj.addBack(2)
assert(obj.popSmallest() == 1)
assert(obj.popSmallest() == 2)
assert(obj.popSmallest() == 3)
obj.addBack(1)
assert(obj.popSmallest() == 1)
assert(obj.popSmallest() == 4)
assert(obj.popSmallest() == 5)
