input = []

with open("input") as f:
    input = f.readlines()


dial = 50
zerocount = 0
pn = dial
for l in input:
    print(l[:-1], dial, zerocount)
    direction = 0
    if l[0] == "R":
        direction = 1
    else:
        direction = -1
    turns = int(l[1:])
    while turns > 0:
        dial = (dial + direction) % 100
        if dial == 0:
            zerocount += 1
        turns -= 1
    print(dial)

print(dial)
print(zerocount)
