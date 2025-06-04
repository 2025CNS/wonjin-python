while True:
    s = input()
    reverse_s = s[::-1]
    if s == '0':
        break
    if "".join(reverse_s) == s:
        print('yes')
    else:
        print('no')