# Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# Thoughts
- The constrain is that you can only hold ONE stock at a time, so there won't be a situation where the you buy something then buy something again before selling the first stock first.
- Greedy algorithm: the moment we see the stock prices go higher than when we buy it, we sell it right away.
    - Why will this guarantee we will have max profit? We are allowed to sell and buy the stock on the same day, so for example, if the price is [1,3,7], the maximum profit is reached when we buy at 1 and sell at 7 (profit = 6). But this is no difference than when you buy at 1, sell at 3, buy immediately at 3, then sell at 7 (profit = 3-1+7-3 = 2+4 = 6).

# BigO
- Time: O(N)
- Space: O(1)