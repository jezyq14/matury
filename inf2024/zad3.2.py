file = open("files/skrot.txt")
numbers = file.read().splitlines()

count = 0
max = 0

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

    if(res == 0):
        count += 1
        if(number > max):
            max = number

print(count, max)