# https://www.codechef.com/JUNE21C/problems/SHROUTE

T = int(input())
for t in range(T):
    N, M = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    arr2 = list(map(int, input().split(' ')))
    maxi = 10**9
    u = [-5] * N
    v = [-5] * N
    for i in range(N):
        if (arr[i] == 1):
            u[i] = 0
    u[0] = 0
    for i in range(1, N):
        if (u[i] == -5):
            if (i != 1):
                if (u[i - 1] == -1):
                    u[i] = -1
                else:
                    u[i] = u[i - 1] + 1
            else:
                if (arr[0] == 1):
                    u[i] = 1
                else:
                    u[i] = -1
    for i in range(0, N):
        if (arr[i] == 2):
            v[i] = 0
    v[0] = 0
    if (arr[N - 1] == 0):
        v[N - 1] = -1
    else:
        if (arr[N - 1] != 1):
            v[N - 1] = 0
        else:
            v[N - 1] = -1
    for i in reversed(range(1, N - 1)):
        if (v[i] == -5):
            if (v[i + 1] == -1):
                v[i] = -1
            else:
                v[i] = v[i + 1] + 1
    for i in range(0, N):
        if (arr[i] == 2):
            u[i] = 0
        if (arr[i] == 1):
            v[i] = 0
    ans = [-5] * N
    for i in range(0, N):
        if (arr[i] != 0):
            ans[i] = 0
    for i in range(0, N):
        if (ans[i] == -5):
            if (u[i] == -1 and v[i] == -1):
                ans[i] = -1
            elif (u[i] != -1 and v[i] == -1):
                ans[i] = u[i]
            elif (u[i] == -1 and v[i] != -1):
                ans[i] = v[i]
            else:
                ans[i] = min(u[i], v[i])
    for i in range(0, M):
        print(ans[arr2[i] - 1], end=' ')
    print()