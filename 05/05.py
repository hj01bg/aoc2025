input = []

with open("input") as f:
    input = [x[:-1] for x in f.readlines()]

print(input)

freshIds = []
ingredientIds = []

for i in range(len(input)):
    if input[i] == "":
        freshIds = [[int(x.split("-")[0]), int(x.split("-")[1])] for x in input[:i]]
        ingredientIds = [int(x) for x in input[i + 1 :]]

print(freshIds)
print(ingredientIds)

part1res = 0
for ing in ingredientIds:
    for start, end in freshIds:
        if ing >= start and ing <= end:
            print(ing, start, end)
            part1res += 1
            break

print(part1res)


part2res = 0
uFresh = [freshIds[0]]
while True:
    uFresh = [freshIds[0]]
    for start, end in freshIds:
        foundExisting = False
        for i in range(len(uFresh)):
            if start < uFresh[i][0] and end > uFresh[i][1]:
                uFresh[i] = [start, end]
                foundExisting = True
            elif (start >= uFresh[i][0] and start <= uFresh[i][1]) or (end >= uFresh[i][0] and end <= uFresh[i][1]):
                uFresh[i] = [min(start, uFresh[i][0]), max(end, uFresh[i][1])]
                foundExisting = True

        if not foundExisting:
            uFresh.append([start, end])
        print(uFresh)
    if len(uFresh) == len(freshIds):
        break
    freshIds = uFresh

for start, end in uFresh:
    part2res += end - start + 1

print(part2res)
