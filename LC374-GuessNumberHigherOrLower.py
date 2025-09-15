# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # The search range is [low, high),
        # where high is always greater than low.
        low, high = 1, n + 1

        while low < high:
            mid = (low + high) // 2
            ret = guess(mid)

            if ret == -1:
                # mid > pick
                high = mid
            elif ret == 1:
                # mid < pick
                low = mid + 1
            else:
                # mid == pick
                break

        return mid


# Time complexity: O(log n)
# Space complexity: O(1)