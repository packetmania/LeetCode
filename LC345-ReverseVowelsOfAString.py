class Solution:
    def reverseVowels(self, s: str) -> str:
        # solution with single loop + two pointers
        vowels = "AEIOUaeiou"
        start, end = 0, len(s) - 1
        s = list(s)

        while start < end:
            # find the next vowel from the starting point
            while start < end and s[start] not in vowels:
                start += 1

            # find the next vowel from the ending point
            while start < end and s[end] not in vowels:
                end -= 1

            if start < end:
                # swap these two vowels
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        return "".join(s)


# Time complexity: O(n)
# Space complexity: O(n) (for the list conversion of the string)

s = Solution()
assert(s.reverseVowels("IceCreAm") == "AceCreIm")
assert(s.reverseVowels("hello") == "holle")
assert(s.reverseVowels("leetcode") == "leotcede")