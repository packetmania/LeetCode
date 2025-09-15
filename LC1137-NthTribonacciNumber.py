class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]

        if n < 3:
            return T[n]

        i = 3
        while i < n + 1:
            newT = T[i - 3] + T[i - 2] + T[i - 1]
            T.append(newT)
            i += 1

        return T[n]


# Time Complexity: O(n)
# Space Complexity: O(n)

s = Solution()
assert(s.tribonacci(4) == 4)
assert(s.tribonacci(25) == 1389537)

# Recursive solution (inefficient for large due to the exponential time
# complexity O(3^n) caused by repeat calculations)
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
'''

# Optimized recursive solution with memoization: it stores previously computed
# values to avoid redundant calculations, reducing the time complexity to O(n)
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        def helper(k):
            if k in memo:
                return memo[k]
            memo[k] = helper(k - 1) + helper(k - 2) + helper(k - 3)
            return memo[k]
        return helper(n)
'''
