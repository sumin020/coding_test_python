// 숫자의 합 구하기(11720)
n = input()
nums = input()
sum = 0

for i in nums :
    sum += int(i) 
    
print(sum)

// 평균 구하기(11720)
n = int(input())
grades = list(map(int, input().split()))
M = 0
sum = 0

for i in grades:
    sum += i
    if i > M:
        M = i
        
newAvg = (sum / M * 100) / n
print(newAvg)

// 구간 합 구하기1 (11659)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

S = [0]
temp = 0

for i in nums:
    temp += i
    S.append(temp)
    
for m in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i-1])

// 구간 합 구하기2 (11660)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[0]*(N + 1) for _ in range(N + 1)]
sum = [[0]*(N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):  
    row = list(map(int, input().split()))  
    for j in range(1, N + 1):  
        arr[i][j] = row[j - 1]  

for i in range(1, N + 1):  
    for j in range(1, N + 1):  
        sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1] + arr[i][j] 
        
for i in range(M):  
    x1, y1, x2, y2 = map(int, input().split())
    result = sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1]
    print(result)    
    
