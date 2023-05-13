def knapsack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0

    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)

    else:
        return max(
            val[n - 1] + knapsack(
                W - wt[n - 1], wt, val, n - 1),
            knapsack(W, wt, val, n - 1))


# Driver Code
if __name__ == '__main__':
    profit = [5, 3, 2, 1, 2, 4]
    weight = [1, 2, 3, 4, 5, 6]
    W = 6
    n = len(profit)
    print(f"The maximum profit is {knapsack(W, weight, profit, n)}")
