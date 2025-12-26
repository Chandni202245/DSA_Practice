# Brute force 
"""def buyAndSell(prices):
    n=len(prices)
    max_profit=0
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                p=prices[j]-prices[i]
                max_profit=max(p,max_profit)
    return max_profit

prices = [7,1,5,3,6,4,8]
print("Maximum profit:",buyAndSell(prices))"""

# TC-> O(N^2)
# SC-> O(1)

# Optimal solution
def buyAndSell(prices):
    n=len(prices)
    min_price=float("inf")
    max_profit=0
    for i in range(0,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
    return max_profit

prices = [7,1,5,3,6,4,8]
print("Maximum profit:",buyAndSell(prices))

# TC-> O(N)
# SC-> O(1)