class Solution:
    def maximumProfit(self, arr):
        
        min_price = arr[0]
        max_profit = 0
        
        for i in range(1,len(arr)):
            cost = arr[i] - min_price
            max_profit = max(max_profit,cost)
            min_price = min(min_price,arr[i])
        
        return max_profit
