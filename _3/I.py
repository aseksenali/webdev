import math
x = int(input())

counter = 2
for i in range(2, math.ceil(math.sqrt(x + 1)) + 1):
    if x % i == 0:
        counter += 2
if int(math.sqrt(x)) == math.sqrt(x):
    counter -= 1

print(counter)
