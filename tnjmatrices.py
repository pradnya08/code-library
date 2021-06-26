# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/tom-and-jerry-love-matrices-16fd6e8e/

M, N, X, Q = input().split()
M, N, X, Q = int(M), int(N), int(X), int(Q)
matrix = []

for i in range(1, M + 1):
    row = []
    for j in range(1, N + 1):
        row.append(X + i + j)
        
    matrix.append(row)

for q in range(Q):
    ins = input().split(' ')
    if (len(ins) == 2):
        qtype = int(ins[0])
        A = int(ins[1]) - 1
    else:
        qtype = int(ins[0])
        A = int(ins[1]) - 1
        B = int(ins[2]) - 1
        C = int(ins[3]) - 1
    if (qtype == 1):
        matrix[A] = matrix[A][:B] + matrix[A][C + 1:]
    elif (qtype == 2):
        for c in range(B, C + 1):
            x = matrix[c].pop(A)
    elif (qtype == 3):
        count = A
        isSet = True
        for j in range(M):
            # matrix[j] = sorted(matrix[j], reverse=False)
            if (count < len(matrix[j])):
                print(matrix[j][count])
                isSet = False
                break
            else:
                count -= len(matrix[j])
        if isSet:
            print(-1)