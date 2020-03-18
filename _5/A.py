n = int(input())
x = []
s = input().split()

for i in s:
    x.append(int(i))

result = x[::2]
for i in result:
    print(i)
