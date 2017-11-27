# def maxProfit(prices):
#     if not prices:
#         return 0
#     max_profit = 0
#     min_price = prices[0]
#     for i in range(1, len(prices)):
#         min_price = min(min_price, prices[i])
#         max_profit = max(prices[i] - min_price, max_profit)
#     return max_profit
def maxProfit(prices):
    buy1 = buy2 = float("-inf")
    sell1 = sell2 = 0
    for i in xrange(0, len(prices)):
        buy1 = max(-prices[i], buy1)
        sell1 = max(buy1 + prices[i], sell1)
        buy2 = max(sell1 - prices[i], buy2)
        sell2 = max(buy2 + prices[i], sell2)
    return sell2
print maxProfit([12,2,4,0,6,9,3])