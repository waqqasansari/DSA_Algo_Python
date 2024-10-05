class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        i, j = 0, 1
        print(prices)
        while(i < len(prices) or j < len(prices)):
            print(j)
            if prices[j] >= prices[i]:
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
                j += 1
            else:
                if prices[j] < prices[i]:
                    i += 1
        
        return max



# Create an instance of the Solution class
solution = Solution()

prices = [7,1,5,3,6,4]

# Call the twoSum method
result = solution.maxProfit(prices)

# Print the result
print(result)