# https://www.codechef.com/MAY21C/problems/LKDNGOLF

n = int(input())


queries = []
for i in range(n):
    queries.append(input().split(" "))

for i in range(n):
    N = int(queries[i][0])
    x = int(queries[i][1])
    k = int(queries[i][2])
    l = x%k
    if (l == 0):
        print("YES")
        continue
    p = N + 1 - x
    l = p%k
    if (l == 0):
        print("YES")
        continue
    print("NO")