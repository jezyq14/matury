count = 0

def przestaw(n):
    global count
    count = count + 1

    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
        return w
    else:
        if a > 0:
            w = a + 10 * b
            return w
        else:
            w = b
            return w
        
# 1.1
print("1.1")

numbers = [43657688, 154005710, 998877665544321]

for i in range(len(numbers)):
    number = numbers[i]
    
    w = przestaw(number)
    print(str(number) + " => " + str(w) + " (" + str(count) + ")")
    count = 0

# 1.2
print("\n1.2")

def countRuns(n):
    global count
    count = 0

    przestaw(n)

    return count

# Some random numbers
input = [ 2, 59, 103, 5821, 57239 ]
output = [True, True, True, True]

for i in range(len(input)):
    number = input[i]
    
    k = len(str(number))

    c = countRuns(number)

    if not (c == k / 2): 
        output[0] = False

    if not (c == (k+1) // 2): 
        output[1] = False

    if not (k % 2 == 0 and c == k / 2 or k % 2 == 1 and c == (k + 1) / 2): 
        output[2] = False

    if not (c == (k + 1) / 2): 
        output[3] = False

for i in range(len(output)):
    print(str(i + 1) + ". " + str(output[i]))

# 1.3
print("\n1.3")

def przestaw2(n):
    w = 0
    p = 1

    while n > 0:
        r = n % 100
        a = r // 10
        b = r % 10

        if n > 9:
            w = p * a + 10 * p * b + w
        else:
            w = p * b + w
        
        n = n // 100
        p *= 100
    
    return w

for i in range(len(numbers)):
    number = numbers[i]
    
    w = przestaw(number)
    w2 = przestaw2(number)

    print(str(number) + ": " + ("poprawnie" if w == w2 else "błąd"))