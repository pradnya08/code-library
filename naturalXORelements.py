# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/natural-xor-25d22168/

T = int(input())
for t in range(T):
    N = int(input())

    r = N % 4
    if (r == 1):
        print(1, 1)
    elif (r == 2):
        print(2, N, 1)
    elif (r == 3):
        print(0)
    elif (r == 0):
        print(1, N)