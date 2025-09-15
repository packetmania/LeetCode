class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Optimized solution with in-place operation and O(1) space.
        """
        write_ptr = 0
        n = len(nums)

        for i in range(n):
            # fill a non-zero element into the write position
            if nums[i] != 0:
                nums[write_ptr] = nums[i]
                write_ptr += 1

        # filling zero for the rest
        for i in range(write_ptr, n):
            nums[i] = 0


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
nums1 = [0,1,0,3,12]
s.moveZeroes(nums1)
assert(nums1 == [1,3,12,0,0])

nums2 = [0]
s.moveZeroes(nums2)
assert(nums2 == [0])
