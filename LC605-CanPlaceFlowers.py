class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Padding with zeros simplifies checking for empty neighbors at the edges
        flowerbed = [0] + flowerbed + [0]

        flowers_planted = 0

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                flowers_planted += 1

            if flowers_planted >= n:
                return True

        return False


# Time complexity: O(m) where m is the length of flowerbed
# Space complexity: O(1)

s = Solution()
assert(s.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True)
assert(s.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False)