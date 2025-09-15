class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # Solution with backtracking (combination + special condition)
        ans = []

        def backtrack(path: list[int], start: int, curr_sum: int):
            if len(path) > k or curr_sum > n:
                return  # cut the branch as it would never meet the requirement

            if len(path) == k and curr_sum == n:
                ans.append(path[:])
                return

            for i in range(start, 10):
                path.append(i)
                backtrack(path, i + 1, curr_sum + i)
                path.pop()

        backtrack([], 1, 0)
        return ans


# Time complexity: O(9! / (k-1)!)
# Space complexity: O(k)

s = Solution()
assert(s.combinationSum3(3, 7) == [[1, 2, 4]])
assert(s.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
assert(s.combinationSum3(4, 1) == [])