A, X = map(int, input(). split())
A1 = list(map(int, input(). split()))
for i in range(A):
    if A1[i] < X:
        print(A1[i], end=" ")
