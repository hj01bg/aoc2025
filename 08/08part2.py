import numpy as np

input = []

with open("input") as f:
    input = f.readlines()


cords = []
connected = []
circuits = []

for i, l in enumerate(input):
    x, y, z = [int(x) for x in l[:-1].split(",")]
    cords.append([x, y, z])
    circuits.append([i])

import functools


@functools.cache
def distance(x1, x2, y1, y2, z1, z2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


distlist = []


def builddistlist():
    for f in range(len(cords) - 1):
        for l in range(f + 1, len(cords)):
            d = distance(cords[f][0], cords[l][0], cords[f][1], cords[l][1], cords[f][2], cords[l][2])
            distlist.append([d, f, l])
    return sorted(distlist, key=lambda x: x[0])


distlist = builddistlist()
print(distlist[:5])
frontcount = 0


def closest_pair():
    global frontcount
    pair = distlist[frontcount][1:]
    frontcount += 1
    return pair


while len(circuits) > 1:
    p = closest_pair()
    connected.append(set(p))
    print(cords[p[0]], cords[p[1]])

    c1 = 0
    for i, c in enumerate(circuits):
        if p[0] in c:
            c1 = i
    c2 = 0
    for i, c in enumerate(circuits):
        if p[1] in c:
            c2 = i
    if c1 != c2:
        circuits[c1] += circuits[c2]
        circuits.remove(circuits[c2])
    print(circuits)
    print(len(circuits))
    print(cords[p[0]], cords[p[1]])
    print(cords[p[0]][0] * cords[p[1]][0])
