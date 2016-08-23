def maxProfit(prices):
    
    minPrice = prices[0]
    profit = 0

    for i in range(len(prices)):
    	profit = max(profit, prices[i] - minPrice)
    	minPrice = min(prices[i], minPrice)
    return profit

prices = [100,80,120,130,70,60,100,125]
print(maxProfit(prices))