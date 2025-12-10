input = []
with open("input") as f:
    input = f.readlines()


part1 = 0
for line in input:
    largest = 0
    line = line.split("\n")[0]
    for f in range(len(line)):
        for l in range(f + 1, len(line)):
            v = int(f"{line[f]}{line[l]}")
            if v > largest:
                largest = v
    part1 += largest
print("part1", part1)
print("=" * 10)


part2 = 0
NBATS = 12

for line in input:
    print()
    line = line.split("\n")[0]
    pos = 0
    jolt = ""
    while len(jolt) < NBATS:
        maxval = 0
        maxvalpos = pos
        for rpos in range(pos, len(line) - NBATS + 1 + len(jolt)):
            if int(line[rpos]) > maxval:
                maxval = int(line[rpos])
                maxvalpos = rpos
            print(line[rpos])
        jolt += line[maxvalpos]
        pos = maxvalpos + 1
    part2 += int(jolt)

print("part2", part2)
