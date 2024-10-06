class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        i, j = 0, 1
        
        while j < len(prices):
            if prices[j] >= prices[i]:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
            else:
                # Update buying price to current price if it's lower
                i = j  # Move buying point to the current selling point
            j += 1  # Always move to the next selling price
        
        return max_profit


# Create an instance of the Solution class
solution = Solution()

prices = [7,1,5,3,6,4]

# Call the twoSum method
result = solution.maxProfit(prices)

# Print the result
print(result)