def alg(n):
    m = 0
    weight = 1

    while n > 0:
        remainder = n % 10

        if remainder % 2 == 1:
            m += remainder * weight
            weight *= 10

        n //= 10

    return m