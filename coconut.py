# https://www.codechef.com/JUNE21C/problems/COCONUT

T = int(input())
for t in range(T):
    xa, xb, Xa, Xb = map(int, input().split(' '))
    result = int(Xa / xa) + int(Xb / xb)
    print(result)