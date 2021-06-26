# https://www.codechef.com/JUNE21C/problems/CHFHEIST

T = int(input())

for t in range(T):
    D, d, P, Q = map(int, input().split(' '))
    q = D//d
    r = D%d
    presum = (q*(q-1))//2
    # print('p', presum)
    total = d*((q*P) + (Q*(presum)))
    if (r != 0):
        total += (r)*(P+Q*q)
    print(total)    