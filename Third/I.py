a = int(input())

counter = 0
i = 2
while a != 1:
    if a % i == 0:
        counter += 1
        a /= i
        continue
    i += 1

print(counter + 1)
