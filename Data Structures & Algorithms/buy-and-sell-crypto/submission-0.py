class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f, r, p = 0, 1, 0

        while r < len(prices):
            if prices[f] < prices[r]:
                profit = prices[r] - prices[f]
                p = max(p, profit)
            else:
                f = r
            r += 1
        return p
        