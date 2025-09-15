class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        num = len(points)

        if num < 1:
            return num

        points.sort(key=lambda x: x[1])

        arrow_count = 1  # Minimum one arrow
        arrow_pos = points[0][1]  # The 1st arrow points at the 1st X_end.

        # Greedy algorithm
        for i in range(1, num):
            if points[i][0] > arrow_pos:
                # The same arrow cannot shoot the current ballon.
                # It needs a new arrow which can shot its end point.
                arrow_count += 1
                arrow_pos = points[i][1]

        return arrow_count

# Greedy algorithm applied after sorting with the end point.
# Time complexity: O(NlogN) due to sorting where N is the number of balloons.
# Space complexity: O(1)

s = Solution()
assert(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2)
assert(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4)
assert(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2)