def max_profit(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Update min_price to the current price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            print(max_profit)
    
    return max_profit

# Example usage
prices1 = [7, 1, 5, 3, 6, 4]
print(f"Max profit for [7, 1, 5, 3, 6, 4]: {max_profit(prices1)}")  # Output: 5