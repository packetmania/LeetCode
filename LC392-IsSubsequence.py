class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s, ptr_t = 0, 0
        match_count = 0

        while ptr_s < len(s) and ptr_t < len(t):
            while s[ptr_s] != t[ptr_t] and ptr_t < len(t) - 1:
                ptr_t += 1

            if s[ptr_s] != t[ptr_t]:
                break

            match_count += 1
            ptr_s += 1
            ptr_t += 1

        return True if match_count == len(s) else False


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.isSubsequence("abc", "ahbgdc") == True)
assert(s.isSubsequence("axc", "ahbgdc") == False)