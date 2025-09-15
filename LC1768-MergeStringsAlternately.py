class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        w1len = len(word1)
        w2len = len(word2)
        repeat = min(w1len, w2len)

        # Merge the chars alternately from two strings
        for i in range(repeat):
            merged += [word1[i], word2[i]]

        ret = ''.join(merged)

        # Append the remaining chars from the longer string
        if repeat == w1len:
            ret += word2[repeat:]
        else:
            ret += word1[repeat:]

        return ret


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
s.mergeAlternately("ab", "pqrs")
assert(s.mergeAlternately("ab", "pqrs") == "apbqrs")
s.mergeAlternately("abcd", "pq")
assert(s.mergeAlternately("abcd", "pq") == "apbqcd")