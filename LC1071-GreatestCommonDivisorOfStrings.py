class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if a common divisor string can exist
        if str1 + str2 != str2 + str1:
            return ""

        # Calculate the GCD of the two strings' lengths
        gcd_length = math.gcd(len(str1), len(str2))

        # The GCD string is the prefix of str1 (or str2) with the calculated GCD length
        return str1[:gcd_length]


# Reference implementation for GCD()
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Time complexity: O(n + m) where n and m are the lengths of str1 and str2
# Space complexity: O(1)

assert(gcd(2, 3) == 1)
assert(gcd(24, 36) == 12)
assert(gcd(8, 0) == 8)