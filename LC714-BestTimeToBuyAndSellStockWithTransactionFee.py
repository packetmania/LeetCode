class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # Dynamic programming
        # hold[i]：the max profit w/ owning stock share at the end of day i
        # cash[i]：the max profit w/o owning stock share at the end of day i
        size = len(prices)
        hold = [0 for _ in range(size)]
        cash = [0 for _ in range(size)]

        hold[0] = -prices[0]

        for i in range(1, size):
            # Either we do nothing, or we sell the stock we have
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i] - fee)
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i])

        return cash[size - 1]


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.maxProfit([1,3,2,8,4,9], 2) == 8)
assert(s.maxProfit([1,3,7,5,10,3], 3) == 6)
