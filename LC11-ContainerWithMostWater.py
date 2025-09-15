class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Solution with two pointers
        left, right = 0, len(height) - 1
        maxvol = 0

        while left < right:
            if height[left] < height[right]:
                lower = height[left]
            else:
                lower = height[right]
            vol = lower * (right - left)
            if maxvol < vol:
                maxvol = vol

            if height[left] < height[right]:
                saved = height[left]
                while height[left + 1] < saved and left + 1 < right:
                    left += 1
                left += 1
            else:
                saved = height[right]
                while height[right - 1] < saved and left < right - 1:
                    right -= 1
                right -= 1

        return maxvol

# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
assert(s.maxArea([1,1]) == 1)