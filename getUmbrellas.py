"""def unboundedKnapsack(W, n, val, wt): 
  
    # dp[i] is going to store maximum  
    # value with knapsack capacity i. 
    dp = [0 for i in range(W + 1)] 
  
    ans = 0
  
    # Fill dp[] using above recursive formula 
    for i in range(W + 1): 
        for j in range(n): 
            if (wt[j] <= i): 
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j]) 
    print dp  
    return dp[W] 
  
# Driver program 
W = 20
val = [1, 1, 1] 
wt = [5, 10, 15] 
n = len(val) 

print unboundedKnapsack(W, n, val, wt);"""

def knapsack_01_exact_min(weights, values, W):
    # 0-1 knapsack, exact total weight W, minimizing total value
    n = len(weights)
    values = [0] + values
    weights = [0] + weights
    K = [[0 for i in range(W+1)] for j in range(n+1)]
    choice = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            K[i][w] = K[i-1][w]
            choice[i][w] = '|'
            if w >= weights[i]:
                t = K[i-1][w-weights[i]]
                if (w==weights[i] or t) and (K[i][w]==0 or t+values[i] < K[i][w]):
                    choice[i][w] = '\\'
                    K[i][w] = t+values[i]
    return K[n][W]

def getUmbrellas(n, p):
   return knapsack_01_exact_min(n,[1]*len(n),p)

print getUmbrellas([1,2,3,9],5)
