class Solution:
    def countBits(self, n: int) -> list[int]:
        ret = []
        for i in range(n+1):
            c = 0
            while i != 0:
                c += 1
                i &= i-1
            ret.append(c)
        return ret


# Elegant solution with n &= n-1 check for each bit-1.
# Time: O(n log n)
# Space: O(1)

s = Solution()
assert(s.countBits(2) == [0, 1, 1])
assert(s.countBits(5) == [0, 1, 1, 2, 1, 2])