n = int(input())
if n < 10:
    n *= 10
count = 0
original = n
while 1:
    tens = n // 10
    ones = n % 10
    s = tens + ones
    n = (ones * 10) + (s % 10)
    count += 1
    if n == original:
        break
print(count)