n = int(input())
arr = map(int, input().split())
arr = list(arr)
m = max(arr)
result = -100000
for i in arr:
    if result < i != m:
        result = i
print(result)
