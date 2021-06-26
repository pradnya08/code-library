# https://www.hackerearth.com/challenges/competitive/may-circuits-21/algorithm/quadratic-equation-4-22fecbd9/

import math
T = int(input())
for t in range(T):
    L, R = input().split(' ')
    L, R = int(L), int(R)
    count = 0
    b = int(math.sqrt(L))
    c = b**2
    cu = 1
    while True:
        if (c >= L and c <= R):
            count+=1
        if ((2*b - 1) > R):
            break
        c = (b**2) - (cu**2)
        cu += 1
        if (c < (2*b - 1)):
            b += 1
            c = b**2
            cu = 1
    print(count)