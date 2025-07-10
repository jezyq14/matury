def alg(n):
    count = 0

    b = 1
    c = 0
    while n > 0:
        a = n % 10
        n //= 10
        if(a % 2 == 0):
            c = c + b * (a // 2)
        else:
            c = c + b
            count += 1
        b *= 10

    return [c, count]

print(alg(333333666666999999))