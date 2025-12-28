import os

print("\n========== INPUT FILE ==========")

instructions = []
for line in open('2025/input.txt'):
    instructions.append(line.strip("\n"))

print("Input: " + str(instructions)+"\n")

print("\n========== Part 1 ==========")
pos, zeroHits = 50, 0
move = {"L": -1, "R": 1}

for i in instructions:
    pos = (pos + move[i[0]] * int(i[1:]))%100
    if pos == 0:
        zeroHits+=1
print("Num Hits Zero:" + str(zeroHits)+"\n")

print("\n========== Part 2 ==========")

pos, zeroHits = 50, 0
for i in instructions:
    dir = i[0]
    movement = move[dir] * int(i[1:])
    prevPos = pos
    pos = (pos + movement)%100
    if pos == 0:
        zeroHits +=1
    elif (prevPos != 0 and dir == "L" and pos > prevPos) or (dir == "R" and pos < prevPos):
        zeroHits += 1
    # Add additional rotations from multiple turns
    zeroHits += int(abs(movement)/100)
print("Num Hits Zero:" + str(zeroHits)+"\n")