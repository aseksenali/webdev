n = int(input())
s = input().split()
x = []
for i in s:
    x.append(int(i))
l = len(x) - 1
for i in range(len(x) // 2):
    x[i] += x[l - i]
    x[l - i] = x[i] - x[l - i]
    x[i] -= x[l - i]
for i in x:
    print(i)
