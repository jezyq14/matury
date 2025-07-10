file = open("files/skrot2.txt")
numbers = file.read().splitlines()

output = []

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

for number in numbers:
    number = int(number)

    res = alg(number)

    a = number
    b = res

    while b != 0:
        temp = b
        b = a % b
        a = temp

    if a == 7: 
        output.append(number)

for item in output:
    print(item)