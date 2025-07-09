FILE_NAME = "./files/symbole.txt"

file = open(FILE_NAME)
content = file.read()
lines = content.splitlines()

# 2.1
print("2.1")

for i in range(len(lines)):
    line = lines[i]

    output = True
    for j in range(len(line)):
        if not line[j] == line[len(line) - j - 1]:
            output = False

    if output:
        print(line)

# 2.2
print("\n2.2")

def checkThreeCharacters(line, j, character):
    if len(line) >= j + 3 and line[j] == line[j + 1] == line[j+2] == character:
        return True
    else:
        return False

output = []
for i in range(len(lines)):
    line = lines[i]

    for j in range(len(line)):  
        character = line[j]

        if(len(lines) >= i + 3 
           and checkThreeCharacters(line, j, character) 
           and checkThreeCharacters(lines[i+1], j, character) 
           and checkThreeCharacters(lines[i+2], j, character)):
            output.append([i + 2, j + 2])

print("Ilość: " + str(len(output)))
for x in output:
    print(str(x[0]) + ", " + str(x[1]) + "; ")

# 2.3
print("\n2.3")

max = [0, 0]
for i in range(len(lines)):
    line = lines[i].replace("o", "0").replace("+", "1").replace("*", "2")

    sum = 0
    for j in range(len(line)):
        sum += int(line[len(line) - 1 - j]) * pow(3, j)
    
    if sum > max[0]:
        max = [sum, i]

print(f"{max[0]} {lines[max[1]]}")

# 2.4
print("\n2.4")

summed = 0
for i in range(len(lines)):
    line = lines[i].replace("o", "0").replace("+", "1").replace("*", "2")

    sum = 0
    for j in range(len(line)):
        sum += int(line[len(line) - 1 - j]) * pow(3, j)
    
    summed += sum

print(summed)

res = ""

while summed > 0:
    res = str(summed % 3) + res
    summed //= 3

print(res.replace("0", "o").replace("1", "+").replace("2", "*"))