def power(a, n):
    result = 1
    while n > 0:
        result *= a
        n -= 1
    return result


s = input().split()
print(power(float(s[0]), int(s[1])))
