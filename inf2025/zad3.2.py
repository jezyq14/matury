FILE_NAME = "./files/dron.txt"

file = open(FILE_NAME)
content = file.read()
lines = content.splitlines()

coordinates = []

pos = [0, 0]
count = 0
for i in range(len(lines)):
    data = lines[i].split(" ")

    pos[0] += int(data[0])
    pos[1] += int(data[1])

    coordinates.append([pos[0], pos[1]])

    if(
        pos[0] >= 0 and pos[0] <= 5000 
        and
        pos[1] >= 0 and pos[1] <= 5000
    ): count += 1

print(f"a) {count}")

output = []
for i in range(len(coordinates)):
    start = coordinates[i]

    for j in range(i + 1, len(coordinates)):
        end = coordinates[j]

        if((int(start[0]) + int(end[0])) % 2 == 0 and (int(start[1]) + int(end[1])) % 2 == 0):
            dx = (int(start[0]) + int(end[0])) // 2
            dy = (int(start[1]) + int(end[1])) // 2

            target = [dx, dy]

            if target in coordinates: 
                output = [start, target, end]

print(f"b) {output}")

