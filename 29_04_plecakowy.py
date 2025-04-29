def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:

                option1 = dp[i - 1][w]
                option2 = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(option1, option2)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage
values = [100, 200, 150,100,150,50]
weights = [252,205,315,441,630,126]
capacity = 500
result = knapsack(weights,values, capacity)

print("Maksymalna liczba kalorii mieszcząca się w 500g:", result, "kcal")