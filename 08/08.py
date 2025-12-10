import functools

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


@functools.cache
def distance(x1, x2, y1, y2, z1, z2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


directly_connected = []


def closest_pair():
    min_d = 9999999999999999
    pair = []
    for fc in range(len(circuits) - 1):
        for lc in range(fc + 1, len(circuits)):
            for f in circuits[fc]:
                for l in circuits[lc]:
                    d = distance(cords[f][0], cords[l][0], cords[f][1], cords[l][1], cords[f][2], cords[l][2])
                    if d < min_d:
                        min_d = d
                        pair = (fc, lc)
    return pair


for i in range(10):
    p = closest_pair()
    print(cords[p[0]], cords[p[1]])
    circuits[p[0]] += circuits[p[1]]
    circuits.remove(circuits[p[1]])
    print(circuits)
    print(len(circuits))

print()
part1res = 0

lens = []
for c in circuits:
    print(c)
    lens.append(len(c))
lens = sorted(lens)
print(lens)
print(lens[-1] * lens[-2] * lens[-3])
