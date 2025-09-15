class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        x=x[::-1]
        return " ".join(x)

# Can use online:  return ' '.join(s.split()[::-1])
# Time complexity: O(n)
