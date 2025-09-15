import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Solution with priority queue - using Min-Heap to track k largest
        # elements, the root has the minimum of the heap. It is the k-th
        # largest element.
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


# Time complexity: O(n log k)
# Space complexity: O(k)

s = Solution()
assert(s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5)
assert(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4)