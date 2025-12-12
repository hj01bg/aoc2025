import numba
import numpy as np

input = []

with open("input") as f:
    input = [x.strip() for x in f.readlines()]

VERBOSE = False
print(input)
NUMPRESENTS = 6
PRESENTSHAPE = 3
presents = []


def printpresent(present):
    for y in range(present.shape[0]):
        for x in range(present.shape[1]):
            print("#" if present[y][x] else ".", end="")
        print()


for i in range(NUMPRESENTS):
    print(i)
    tmpp = input[5 * i + 1 : 5 * i + 4]
    p = np.zeros((PRESENTSHAPE, PRESENTSHAPE), dtype=np.uint8)
    for y, l in enumerate(tmpp):
        for x, c in enumerate(l):
            p[y][x] = 1 if c == "#" else 0

    fliparr = []
    for f in range(10):
        p = np.flip(p)
        for r in range(10):
            p = np.rot90(p)
            if not any(np.array_equal(p, arr) for arr in fliparr):
                fliparr.append(np.copy(p))
    presents.append(fliparr)
for i, present in enumerate(presents):
    print(i, len(present))
    for f in present:
        print()
        printpresent(f)

regions = []

for r in input[NUMPRESENTS * 5 :]:
    s = r.split(" ")
    i = [int(x) for x in s[1:]]
    reg = s[0].split("x")
    print(reg)
    regions.append([[int(reg[0]), int(reg[1][:-1])], i])
    print(s)

print(regions)


@numba.njit
def does_fit(board, tofit, i):
    bs = board.shape
    y, x = i // bs[1], i % bs[1]
    if y + tofit.shape[0] > bs[0] or x + tofit.shape[1] > bs[1]:
        return False
    return not np.any(board[y : y + tofit.shape[0], x : x + tofit.shape[1]] + tofit > 1)


@numba.njit
def place(board, tofit, i):
    bc = board.copy()
    bs = board.shape
    y, x = i // bs[1], i % bs[1]
    bc[y : y + tofit.shape[0], x : x + tofit.shape[1]] += tofit
    return bc


@numba.njit
def fitpresents(board, tofit, i, depth=0, presents_array=None):
    bs = board.shape

    if i == bs[0] * bs[1]:
        return 0
    y, x = i // bs[1], i % bs[1]
    presentsleft = sum(tofit)
    if presentsleft == 0:
        return 1

    while board[y][x] == 1:
        i += 1
        y, x = i // bs[1], i % bs[1]

    while i < bs[0] * bs[1]:
        if depth < 2:
            print(depth, tofit, i)
        for index, f in enumerate(tofit):
            if f > 0:
                for variant in presents_array[index]:
                    if np.all(variant == 0):  # Skip empty variants
                        continue
                    if does_fit(board, variant, i):
                        fcopy = tofit.copy()
                        fcopy[index] -= 1
                        if fitpresents(place(board, variant, i), fcopy, i, depth + 1, presents_array):
                            return 1
        i += 1
    return 0


max_variants = max(len(fliparr) for fliparr in presents)

presents_array = np.zeros((len(presents), max_variants, PRESENTSHAPE, PRESENTSHAPE), dtype=np.uint8)

for i, fliparr in enumerate(presents):
    for j, variant in enumerate(fliparr):
        presents_array[i, j, : variant.shape[0], : variant.shape[1]] = variant


part1res = 0

for region_shape, num_presents in regions:
    board = np.zeros((region_shape[1], region_shape[0]), dtype=np.uint8)
    tofit = []
    cache = {}
    for i, p in enumerate(num_presents):
        tofit.append(p)
    if VERBOSE:
        print(tofit)
    attempted_area = np.sum([x * np.sum(presents[i][0]) for i, x in enumerate(tofit)])
    print(attempted_area, region_shape[0] * region_shape[1])
    if attempted_area <= region_shape[0] * region_shape[1]:
        part1res += fitpresents(board, tofit, 0, presents_array=presents_array)
    print(part1res)


print("Part1:", part1res)
