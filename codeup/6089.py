a, r, c = map(int, input().split())
b = 0

for i in range(1, c):
    b = a*r
    a = b
print(b)