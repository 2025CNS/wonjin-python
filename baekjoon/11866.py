n, k = map(int, input().split())
people = list(range(1, n+1))
result = []

idx = 0

while people:
    idx =(idx + k - 1) % len(people)
    result.append(people.pop(idx))
print("<" + ", ".join(map(str, result)) + ">")