# https://www.codechef.com/MAY21C/problems/SOLBLTY

n = int(input())

queries = []
for i in range(n):
    queries.append(input().split(" "))

for i in range(n):
    X = int(queries[i][0])
    A = int(queries[i][1])
    B = int(queries[i][2])
    res = A + (100 - X)*B
    res*=10
    print(res)