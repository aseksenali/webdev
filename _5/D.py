n = int(input())
s = input().split()
x = []
for i in s:
    x.append(int(i))
counter = 0
for i in range(1, len(x)):
    if x[i] > x[i - 1]:
        counter += 1
print(counter)