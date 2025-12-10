input = []

with open("input") as f:
    input = [x.split("-") for x in f.readlines()[0].split("\n")[0].split(",")]


part1 = 0
part2 = 0
for p in input:
    for i in range(int(p[0]), int(p[1]) + 1):
        i = str(i)
        if i[: len(i) // 2] == i[len(i) // 2 :]:
            print(i)
            part1 += int(i)
        for stride in range(1, len(i)):
            if stride * (len(i) // stride) != len(i):
                continue
            passpart2 = True
            cmp = i[:stride]
            for counter in range(len(i) // stride):
                if i == "565657":
                    print("check part2: ", i, cmp, i[counter * stride : (counter + 1) * stride], counter, stride)
                if i[counter * stride : (counter + 1) * stride] != cmp:
                    passpart2 = False
                    break
            if passpart2:
                print("Part2 ", i)
                part2 += int(i)
                break
print(part1)
print(part2)
