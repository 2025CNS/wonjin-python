n = int(input())
result = []
for i in range(n):
    data = list(map(int, input().split()))
    data1 = []
    for j in data:
        if j % 2 == 0:
            data1.append(j)
    result.append([sum(data1), min(data1)])
for i in result:
    print(*i)