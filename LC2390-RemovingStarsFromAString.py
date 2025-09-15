class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c != '*':
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.removeStars("leet**cod*e") == "lecoe")
assert(s.removeStars("erase*****") == "")