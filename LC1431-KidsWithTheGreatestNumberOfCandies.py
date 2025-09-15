class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        curr_max = max(candies)
        bool_list = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= curr_max:
                bool_list[i] = True

        return bool_list


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.kidsWithCandies([2,3,5,1,3], 3)==[True, True, True, False, True])
assert(s.kidsWithCandies([4,2,1,1,2], 1)==[True, False, False, False, False])