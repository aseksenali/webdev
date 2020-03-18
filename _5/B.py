n = int(input())
s = input().split()
x = []
for i in s:
    i = int(i)
    if i % 2 == 0:
        x.append(i)
for i in x:
    print(i)
