# https://www.codechef.com/MAY21C/problems/XOREQUAL

T = int(input())
queries = []

for i in range(T):
    N = int(input())
    r = (1 << N) - 1 - 1
    ans = (r >> 1) + 1
    ans = ans %((10**9) + 7)
    print(int(ans))
    