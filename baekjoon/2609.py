def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))