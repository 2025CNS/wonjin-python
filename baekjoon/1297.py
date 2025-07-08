import math
D,H,W = map(int, input().split())
x = D / math.sqrt(H**2 + W**2)

print(int(H * x), int(W * x))
