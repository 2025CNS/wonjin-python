n = int(input())
score = list(map(int, input().split()))
M = max(score)
for i in range(n):
    score[i] = score[i]/M*100
print(sum(score)/n)