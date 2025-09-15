class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1]*n

        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer


# Optimized solution that does not need extra lists of prefix/suffix products.
# Time complexity: O(n)
# Space complexity: O(1) (output array does not count as extra space)

s = Solution()
assert(s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
assert(s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])