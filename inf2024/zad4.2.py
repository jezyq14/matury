file = open("files/liczby.txt")
lines = file.read().splitlines()

primes = list(map(int, lines[0].split(" ")))

def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]

    left = []
    middle = []
    right = []

    for x in array:
        if(x > pivot):
            left.append(x)
        elif x < pivot:
            right.append(x)
        else:
            middle.append(x)
    
    return quickSort(left) + middle + quickSort(right)

primes = quickSort(primes)

if(len(primes) >= 101):
    print(primes[100])
else:
    print(primes[101 % len(primes)])

