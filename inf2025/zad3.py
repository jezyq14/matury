FILE_NAME = "./files/dron.txt"

file = open(FILE_NAME)
content = file.read()
lines = content.splitlines()

count = 0
for i in range(len(lines)):
    data = lines[i].split(" ")

    a = abs(int(data[0]))
    b = abs(int(data[1]))

    if b == 0 and a > 1: 
        count += 1
    else: 
        while b != 0:
            temp = b
            b = a % b
            a = temp

        if a > 1: 
            count += 1

print(count)