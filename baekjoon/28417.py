n = int(input())
max_score = 0
for _ in range(n):
    scores = list(map(int, input().split()))
    normal = sorted(scores[:4], reverse=True)[:2]
    trick = max(scores[4], scores[5])
    total = sum(normal) + trick
    max_score = max(max_score, total)
print(max_score)
