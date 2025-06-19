a,b = map(int, input().split())
sequence = []
num = 1
while len(sequence) < b:
    sequence += [num] * num
    num += 1
print(sum(sequence[a-1:b]))
