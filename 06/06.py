
def part1():
    with open("input") as file:
        input = file.readlines()

    input = [x.split("\n")[0] for x in input]

    input = [x.split(" ") for x in input]

    input = [[i for i in item if i != ''] for item in input]

    operations = input[-1]
    input.pop()
    input = [[int(i) for i in item if i != ''] for item in input]


    print(input)

    res = input[-1]
    input.pop()
    for l in input:
        for i in range(len(res)):
            if operations[i] == '+':
                res[i] += l[i]
            elif operations[i] == '*':
                res[i] *= l[i]

    part1res = 0
    for l in res:
        part1res += l
    print(part1res)


def part2():
    with open("input") as file:
        input = file.readlines()

    input = [x.split("\n")[0] for x in input]


    operations = input[-1].split()
    input.pop()
    print(operations)



    print(input, operations)

    part2res = 0
    colres = 0
    for c in range(len(input[0]), 0, -1):
        c = c - 1
        emptycol = True
        nrstring = ""
        for r in range(len(input)):
            nrstring += input[r][c]
        nrstring = nrstring.strip()
        print(nrstring.strip())
        if (len(nrstring) == 0):
            print("Res: ",colres)
            part2res += colres
            colres = 0
            operations.pop()
        elif colres == 0:
            colres = int(nrstring)
        else:
            if operations[-1] == '*':
                colres *= int(nrstring)
            if operations[-1] == '+':
                colres += int(nrstring)
    part2res += colres
    print(part2res)

part2()
