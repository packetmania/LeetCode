class Solution:
    def compress(self, chars: list[str]) -> int:
        read, write = 0, 0
        n = len(chars)

        while read < n:
            current_char = chars[read]
            count = 0
            # Count consecutive occurrences
            while read < n and chars[read] == current_char:
                count += 1
                read += 1

            # Write the character
            chars[write] = current_char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.compress(["a","a","b","b","c","c","c"]) == 6)
assert(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4)