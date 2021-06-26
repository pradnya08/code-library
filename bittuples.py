# https://www.codechef.com/JUNE21C/problems/BITTUP

T = int(input())

for t in range(T):
    n, m = map(int, input().split(' '))
    u = 10**9 + 7
    k = pow(2, n, u) - 1
    l = pow(k, m, u)
    print(l)