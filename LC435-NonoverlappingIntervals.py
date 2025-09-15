class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        total = len(intervals)

        if total <= 1:
            return 0

        # Sort the list by the end point
        intervals.sort(key=lambda x: x[1])

        # Greedy algorithm to max kept intervals
        keep_count = 1  # minimum one interval
        current_end = intervals[0][1]

        for i in range(1, total):
            if intervals[i][0] >= current_end:
                # This interval has no overlap with the last one
                keep_count += 1
                current_end = intervals[i][1]

        return total - keep_count


# Use greedy algorithm after sorting.
# Time complexity: O(N log N) due to sorting where N is the number of intervals
# Space complexity: O(1)

s = Solution()
assert(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1)
assert(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2)
assert(s.eraseOverlapIntervals([[1,2],[2,3]]) == 0)