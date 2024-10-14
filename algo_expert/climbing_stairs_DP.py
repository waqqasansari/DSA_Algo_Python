def climb_stairs(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Create a list to store the number of ways to reach each step
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Initialize base cases


    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Fill in the dp array
        print(dp)

    return dp[n]

# Example usage
n = 10
print(climb_stairs(n))  # Outputs the number of ways to climb 6 steps