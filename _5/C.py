n = int(input())
s = input().split()
counter = 0
for i in s:
    i = int(i)
    if i > 0:
        counter += 1
print(counter)

