map = []

with open("input") as f:
    map = [[p for p in y] for y in [x.split()[0] for x in f.readlines()]]
print(map)


def printmap(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            n = countneighbors(map, x, y)
            if n < 5:
                print("x", end="")
            else:
                print(map[y][x], end="")
        print()


def countneighbors(map, x, y):
    if map[y][x] == ".":
        return 1000
    rolls = 0
    for dy in range(y - 1, y + 2):
        for dx in range(x - 1, x + 2):
            if dx < 0 or dy < 0 or dy >= len(map) or dx >= len(map[dy]):
                continue
            if map[dy][dx] == "@":
                rolls += 1
    return rolls


part1res = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if countneighbors(map, x, y) < 5:
            part1res += 1

printmap(map)
print(part1res)


part2res = 0
while True:
    remove = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if countneighbors(map, x, y) < 5:
                part2res += 1
                remove.append((x, y))
    for x, y in remove:
        map[y][x] = "."
    if len(remove) == 0:
        break

printmap(map)
print(part2res)
