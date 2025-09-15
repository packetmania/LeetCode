import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        # Solution with two Min-Heaps and two pointers
        heap_left, heap_right = [], []
        left, right = 0, len(costs) - 1
        total_cost = 0

        for i in range(k):
            # fill in left heap, check boundary to avoid duplicates
            while len(heap_left) < candidates and left <= right:
                heapq.heappush(heap_left, costs[left])
                left += 1

            # fill in right heap, check boundary to avoid duplicates
            while len(heap_right) < candidates and left <= right:
                heapq.heappush(heap_right, costs[right])
                right -= 1

            if not heap_right or (heap_left and heap_left[0] <= heap_right[0]):
                total_cost += heapq.heappop(heap_left)
            else:
                total_cost += heapq.heappop(heap_right)

        return total_cost


# Time complexity: O(k log(n)) where k is the number of workers to hire
#     and n is the number of candidates to consider from each side.
# Space complexity: O(n) for the two heaps.

s = Solution()
assert(s.totalCost([17,12,10,2,7,2,11,20,8], 3, 4) == 11)
assert(s.totalCost([1,2,4,1], 3, 3) == 4)