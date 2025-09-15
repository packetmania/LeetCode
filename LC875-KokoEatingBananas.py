import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Binary search solution:
        # k should be in the range [1, max(piles)]
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            # calculate the hours needed
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours > h:
                # mid is too less
                low = mid + 1
            else:
                high = mid

        return low


# Binary search for k in the range [1, max(piles)].
# The time complexity is O(N*logM)
#     N is the pile list length and M is the max(piles).
# Space complexity: O(1)

s = Solution()
assert(s.minEatingSpeed([3,6,7,11], 8) == 4)
assert(s.minEatingSpeed([30,11,23,4,20], 5) == 30)
assert(s.minEatingSpeed([30,11,23,4,20], 6) == 23)