i = input().split(' ')
N = int(i[0])
A = int(i[1])
B = int(i[2])

count = 0
c = 0

while True:
    if (A > N - c + 1):
        count += N - c
        break
    else:
        c += A
        count += A
        if c == N:
            break
    if (B > N - c + 1):
        break
    else:
        c += B
        if c == N:
            break
            
print(count)