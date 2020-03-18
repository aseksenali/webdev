def m(a, b, c, d):
    return min(a, b, c, d)


s = input().split()
x = []
for i in s:
    x.append(int(i))
print(m(x[0], x[1], x[2], x[3]))
