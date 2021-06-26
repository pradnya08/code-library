N = int(input())
numbers = input().split(' ')
count = 0
for i in range(0, N):
    num = int(numbers[i])
    count += bin(num).count('1')
print(count)