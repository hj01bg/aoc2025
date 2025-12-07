
input = []
with open("input") as f:
    input = [x.strip() for x in f.readlines()]



beams = []

part1res = 0

for l in input:
    tmpbeams = beams.copy()
    print()
    for c in range(len(l)):
        if l[c] == 'S':
            tmpbeams.append(c)
            print("S",end="")
        elif l[c] == '^' and c in beams:
            print("^",end="")
            tmpbeams.remove(c)
            if c-1 not in tmpbeams:
                tmpbeams.append(c-1)
            if c+1 not in tmpbeams:
                tmpbeams.append(c+1)
            part1res += 1
        elif c in beams:
            print("|",end="")
        else:
            print(l[c],end="")

    beams = tmpbeams

print(part1res)


import functools
@functools.cache
def split(x, y):
    if y == len(input):
        return 1
    for d in range(y, len(input)):
        if input[d][x] == '^':
            return split(x-1, d+1) + split(x+1, d+1)
    return 1

part2res = 0

for c in range(len(input[0])):
    if input[0][c] == 'S':
        part2res = split(c, 1)

print(part2res)



#Start at S moving down
