class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        start, end = 0, 0  # window pointers
        count, maxvws = 0, 0

        while end < len(s):
            if s[end] in vowels:
                count += 1

            if end >= k - 1:
                maxvws = max(maxvws, count)
                if s[start] in vowels:
                    count -= 1
                start += 1

            end += 1

        return maxvws


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.maxVowels("abciiidef", 3) == 3)
assert(s.maxVowels("aeiou", 2) == 2)
assert(s.maxVowels("leetcode", 3) == 2)