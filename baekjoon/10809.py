s = input()
n = 'abcdefghijklmnopqrstuvwxyz'

for i in n:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1, end=" ")
    