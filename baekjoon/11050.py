def  binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

n, k = map(int, input().split())
print(binomial_coefficient(n, k))
