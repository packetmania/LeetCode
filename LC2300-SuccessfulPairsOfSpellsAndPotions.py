class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        spells_num = len(spells)
        pairs = [0] * spells_num
        potions_sorted = sorted(potions)
        potions_num = len(potions)

        for i in range(spells_num):
            # Do binary search for the potion with the least strength
            low = 0
            high = potions_num

            while low < high:
                mid = (low + high) // 2
                if potions_sorted[mid] * spells[i] >= success:
                    high = mid
                else:
                    low = mid + 1

            if low == potions_num:
                pairs[i] = 0
            elif potions_sorted[low] * spells[i] >= success:
                pairs[i] = potions_num - low
            else:
                pairs[i] = potions_num - low - 1

        return pairs


# Time complexity: O(m log m + n log m) where
#     n is the number of spells and m is the number of potions.
#     Sorting: O(m log m)
#     For each spell: O(n log m)
# Space complexity: O(m) (for the sorted potions list and result array).

s = Solution()
assert(s.successfulPairs([5,1,3], [1,2,3,4,5], 7) == [4,0,3])
assert(s.successfulPairs([3,1,2], [8,5,8], 16) == [2,0,2])