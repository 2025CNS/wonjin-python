n = int(input())
num = list(map(int, input().split()))
cnt = 0
result = []
for i in num:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt== 2:
        result.append(cnt)

print(len(result))


          
    
        
    
