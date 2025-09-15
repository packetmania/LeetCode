class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer = [[],[]]

        answer[0] = list(set1-set2)
        answer[1] = list(set2-set1)

        return answer


# Time complexity: O(m + n) where m and n are the lengths of nums1 and nums2
# Space complexity: O(m + n) where m and n are the lengths of nums1 and nums2

s = Solution()
assert(s.findDifference([1,2,3], [2,4,6]) == [[1,3],[4,6]])
assert(s.findDifference([1,2,3,3], [1,1,2,2]) == [[3],[]])