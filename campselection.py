P = int(input())
C = int(input())
n = int(input())
scores = []
for i in range(0, P):
    scores.append(input().split(' '))
    
    
for i in range(0, P):
    score = sorted(scores[i], reverse = True)
    avg = 0
    for j in range(0, n):
        avg += int(score[j])
    print(avg//n)