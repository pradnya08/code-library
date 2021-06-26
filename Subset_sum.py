def subsetSum(arr, targetSum):
    n = len(arr)
    dp = [[False]*(targetSum+1) for i in range(n+1)]
    # Init
    for i in range(n+1):
        dp[i][0] = True
    # Loop
    for i in range(1,n+1):
        for j in range(targetSum+1):
            if dp[i-1][j]:
                dp[i][j] = True
            else:
                if j > arr[i-1]:
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i-1][j-arr[i-1]]
    for i in dp:
        print(i)
    return dp[n][targetSum]

if __name__ == "__main__":
    n, targetSum = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    print(subsetSum(arr, targetSum))