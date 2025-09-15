class Solution:
    def decodeString(self, s: str) -> str:
        # Solution with two stacks
        numStack, strStack = [], []
        currNum, currStr = 0, ""

        for char in s:
            if char.isdigit():
                currNum = currNum * 10 + int(char)
            elif char == '[':
                # push the current number and string
                numStack.append(currNum)
                strStack.append(currStr)
                currNum = 0
                currStr = ""
            elif char == ']':
                repeat = numStack.pop()
                preStr = strStack.pop()
                currStr = preStr + currStr * repeat
            else:
                currStr += char

        return currStr


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.decodeString("3[a]2[bc]") == "aaabcbc")
assert(s.decodeString("3[a2[c]]") == "accaccacc")
assert(s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")