import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Solution with Priority Queue (Min-Heap)
        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        pairs.sort(key=lambda x: x[1], reverse=True)  # reverse sort by nums2

        heap = []  # Min-Heap
        sum_val, max_score = 0, 0

        for i, (n1, n2) in enumerate(pairs):
            # since n2 is the current min, n1 must in
            heapq.heappush(heap, n1)
            sum_val += n1

            if len(heap) > k:
                sum_val -= heapq.heappop(heap)  # remove the minimum

            if len(heap) == k:
                max_score = max(max_score, sum_val * n2)

        return max_score


# Time complexity: O(n log n) due to sorting and heap operations
# Space complexity: O(n) for storing pairs and the heap

s = Solution()
assert(s.maxScore([1,3,3,2], [2,1,3,4], 3) == 12)
assert(s.maxScore([4,2,3,1,1], [7,5,10,9,6], 1) == 30)