h,b,c,s = map(int, input(). split())
e = (h * b * c * s)/(8*1024*1024)

print(format(e, ".1f"), end='')

print(' MB')
