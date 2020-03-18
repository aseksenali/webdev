n = int(input())
s = input().split()
x = []
for i in s:
    x.append(int(i))
isYES = False
for i in range(1, len(x)):
    if x[i] * x[i - 1] > 0:
        print('YES')
        isYES = True
        break
if not isYES:
    print('NO')
