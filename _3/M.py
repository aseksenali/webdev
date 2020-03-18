n = int(input())

counter = 0
for i in range(n):
    if int(input()) == 0:
        counter += 1
print(counter)