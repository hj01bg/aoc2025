import functools

input = []
with open("input") as f:
    input = f.readlines()

connections = {}
for i in input:
    labels = i.strip().split(" ")
    connections[labels[0][:-1]] = labels[1:]


START = "you"
END = "out"


@functools.cache
def recurse_path_p1(label, depth):
    if label == END:
        return 1
    res = 0
    for n in connections[label]:
        res += recurse_path_p1(n, depth + 1)
    return res
    pass


print("part1:", recurse_path_p1(START, 0))


@functools.cache
def recurse_path_p2(label, depth, dac, fft):
    if label == END:
        return dac and fft
    if label == "dac":
        dac = True
    if label == "fft":
        fft = True
    res = 0
    for n in connections[label]:
        res += recurse_path_p2(n, depth + 1, dac, fft)
    return res
    pass


print("part2:", recurse_path_p2("svr", 0, False, False))
