class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # Classic prefix sum solution
        highest = 0
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            if highest < alt:
                highest = alt

        return highest


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.largestAltitude([-5, 1, 5, 0, -7]) == 1)
assert(s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0)