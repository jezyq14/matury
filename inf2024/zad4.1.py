file = open("files/liczby.txt")
lines = file.read().splitlines()

primes = lines[0].split(" ")
numbers = lines[1].split(" ")

count = 0
for prime in primes:
    prime = int(prime)
    for number in numbers:
        number = int(number)

        if(number % prime == 0):
            count += 1
            break

print(count)