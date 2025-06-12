n = int(input())
money = []

for i in range(n):
    m = int(input())
    money.append(m)
    if m == 0:
        money.pop()
        money.pop()
print(sum(money))