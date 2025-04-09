n = int(input())

for i in range(1, n+1):
    count = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if count > 0:
        print("X" * count, end=' ')
    else:
        print(i, end=' ')