class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Solution with monotonic decreasing (from bottom to top) stack
        n = len(temperatures)
        stack = []
        ans = [0 for _ in range(n)]

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)  # push the index to the stack

        return ans


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
assert(s.dailyTemperatures([30,40,50,60]) == [1,1,1,0])
assert(s.dailyTemperatures([30,60,90]) == [1,1,0])