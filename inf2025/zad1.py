count = 0

def przedstaw(n):
    global count
    count = count + 1

    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    if n > 0:
        w = a + 10 * b + 100 * przedstaw(n)
        return w
    else:
        if a > 0:
            w = a + 10 * b
            return w
        else:
            w = b
            return w
        
numbers = [43657688, 154005710, 998877665544321]

for i in range(3):
    number = numbers[i]
    
    w = przedstaw(number)
    print(str(number) + " => " + str(w) + " (" + str(count) + ")")
    count = 0