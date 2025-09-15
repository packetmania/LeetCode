class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Solution with hashmap (Python set)
        # Close <=> Three conditions all met
        #     1. Both are of the same length.
        #     2. Both consist of the same letter set.
        #     3. The frequencies of alphabets are mutual permutations.
        #
        # Note the difference between sorted() and list.sort().
        # The former returns a new sorted list from the iterable,
        # while the latter sorts the list in place and returns None.

        # Check length first
        if len(word1) != len(word2):
            return False

        # Generate the sets and compare
        set1, set2 = set(word1), set(word2)
        if set1 != set2:
            return False

        # Generate the frequency lists, sort then compare
        count1, count2 = [], []
        for w1 in list(set1):
            count1.append(word1.count(w1))
        for w2 in list(set2):
            count2.append(word2.count(w2))
        if sorted(count1) != sorted(count2):
            return False

        return True


# Time complexity: O(n log n) due to sorting the frequency lists
# Space complexity: O(1) since the size of the frequency lists is bounded by 26

s = Solution()
assert(s.closeStrings("abc", "bca") == True)
assert(s.closeStrings("a", "aa") == False)
assert(s.closeStrings("cabbba", "abbccc") == True)