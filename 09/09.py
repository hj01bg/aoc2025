import numpy as np

input = []

with open("input") as f:
    input = [x.strip() for x in f.readlines()]

input = [x.split(",") for x in input]

for f in range(len(input)):
    input[f] = [int(input[f][0]), int(input[f][1])]
print(input)

areas = []
part1res = 0
for f in range(len(input)):
    for l in range(f, len(input)):
        fx = input[f][0]
        fy = input[f][1]
        lx = input[l][0]
        ly = input[l][1]
        area = (1 + np.abs(lx - fx)) * (1 + np.abs(ly - fy))
        areas.append([area, [fx, fy], [lx, ly]])
        if area > part1res:
            part1res = area

areas = sorted(areas, key=lambda x: x[0])
print(areas)
print("part1res", part1res)

greenedge = [input[-1]]

maxx = 0
maxy = 0

for x, y in input:
    lx, ly = greenedge[-1]
    if lx < x:
        for dx in range(lx + 1, x + 1):
            greenedge.append([dx, y])
    if lx > x:
        for dx in range(lx - 1, x - 1, -1):
            greenedge.append([dx, y])
    if ly < y:
        for dy in range(ly + 1, y + 1):
            greenedge.append([x, dy])
    if ly > y:
        for dy in range(ly - 1, y - 1, -1):
            greenedge.append([x, dy])
    maxx = max(maxx, x)
    maxy = max(maxy, y)


edgeset = set()
for e in greenedge:
    edgeset.add(str(e))

print(greenedge)
print(edgeset)

import functools


@functools.cache
def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


@functools.cache
def seek1(x, y):
    for lx in range(x - 1, -1, -1):
        if str([lx, y]) in edgeset:
            ep = greenedge.index([lx, y])
            ex = greenedge[ep][0] - greenedge[ep - 1][0]
            ey = greenedge[ep][1] - greenedge[ep - 1][1]
            if dot(ex, ey, lx - x, 0) > 0:
                return False
            else:
                return True
    return False


@functools.cache
def seek2(x, y):
    for lx in range(x, maxx + 1):
        if str([lx, y]) in edgeset:
            ep = greenedge.index([lx, y])
            ex = greenedge[ep][0] - greenedge[ep - 1][0]
            ey = greenedge[ep][1] - greenedge[ep - 1][1]
            if dot(ex, ey, lx - x, 0) > 0:
                return False
            else:
                return True
    return False


@functools.cache
def seek3(x, y):
    for ly in range(y - 1, -1, -1):
        if str([x, ly]) in edgeset:
            ep = greenedge.index([x, ly])
            ex = greenedge[ep][0] - greenedge[ep - 1][0]
            ey = greenedge[ep][1] - greenedge[ep - 1][1]
            if dot(ex, ey, 0, ly - y) > 0:
                return False
            else:
                return True
    return False


@functools.cache
def seek4(x, y):
    for ly in range(y, maxy + 1):
        if str([x, ly]) in edgeset:
            ep = greenedge.index([x, ly])
            ex = greenedge[ep][0] - greenedge[ep - 1][0]
            ey = greenedge[ep][1] - greenedge[ep - 1][1]
            if dot(ex, ey, 0, ly - y) > 0:
                return False
            else:
                return True
    return False


@functools.cache
def isinside(x, y):
    if str([x, y]) in edgeset:
        return True

    if not seek1(x, y):
        return False
    if not seek2(x, y):
        return False
    if not seek3(x, y):
        return False
    if not seek4(x, y):
        return False

    return True


part2res = 0
for areasol in areas[::-1]:
    print(areasol)
    area, f, l = areasol
    fx, fy = f
    lx, ly = l

    inside = True

    valid = False
    for x in range(min(fx, lx), max(fx, lx) + 1):
        if valid and str([x, fy]) in edgeset:
            valid = False
        if not valid and not isinside(x, fy):
            inside = False
            break
        elif str([x, fy]) not in edgeset:
            valid = True
    if inside:
        valid = False
        for y in range(min(fy, ly), max(fy, ly) + 1):
            if valid and str([fx, y]) in edgeset:
                valid = False
            if not valid and not isinside(fx, y):
                inside = False
                break
            elif str([fx, y]) not in edgeset:
                valid = True
    if inside:
        valid = False
        for x in range(min(fx, lx), max(fx, lx) + 1):
            if valid and str([x, ly]) in edgeset:
                valid = False
            if not valid and not isinside(x, ly):
                inside = False
                break
            elif str([x, ly]) not in edgeset:
                valid = True
    if inside:
        valid = False
        for y in range(min(fy, ly), max(fy, ly) + 1):
            if valid and str([lx, y]) in edgeset:
                valid = False
            if not valid and not isinside(lx, y):
                inside = False
                break
            elif str([lx, y]) not in edgeset:
                valid = True

    if inside:
        print(area)
        part2res = area
        import matplotlib.pyplot as plt

        plt.plot([x[0] for x in greenedge], [x[1] for x in greenedge])
        plt.plot([fx, lx, lx, fx, fx], [fy, fy, ly, ly, fy])
        plt.show()
        break


print("part2res", part2res)
