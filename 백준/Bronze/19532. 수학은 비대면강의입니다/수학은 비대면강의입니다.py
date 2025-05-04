a, b, c, d, e, f = map(int, input().split())

if b == 0:
    x = int(c / a)
    y = int((f - d * x) / e)
# elif a*e == b*d:
#     x = 0
#     y = 0
else:
    x = int((c*e - b*f) / (a*e - b*d))
    y = int((c - a * x) / b)
print(x, y)

