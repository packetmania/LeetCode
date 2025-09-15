class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Simple backtracking solution
        if not digits:
            return []

        # digits to letters mapping
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(path: str, index: int):
            if index == len(digits):
                ans.append(path)
                return

            digit = digits[index]
            for letter in phone_map[digit]:
                backtrack(path + letter, index + 1)

        backtrack("", 0)
        return ans


# Time complexity: O(3^m * 4^n),
#     m is the count of digits with 3 letters, n is the count of digits with 4 letters
# Space complexity: O(m + n)

s = Solution()
assert(s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
assert(s.letterCombinations("") == [])
assert(s.letterCombinations("2") == ["a", "b", "c"])