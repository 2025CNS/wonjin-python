w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)
e = (w*h*b)/(8*1024*1024)

print(format(e, ".2f"), end='')
print(' MB')