import numpy as np
from scipy import optimize

input = []

with open("input") as f:
    input = f.readlines()


manuals = []

for i in input:
    things = i.strip("\n").split(" ")
    print(things)
    lights = []
    for l in things[0][1:-1]:
        if l == "#":
            lights.append(True)
        else:
            lights.append(False)

    jolts = [int(x) for x in things[-1][1:-1].split(",")]

    buttons = []
    for wireing in things[1:-1]:
        buttons.append([int(x) for x in wireing[1:-1].split(",")])
    manuals.append([lights, buttons, jolts])

    print(lights, buttons, jolts)


def pressbutton(lights, button):
    lights = lights.copy()
    for w in button:
        lights[w] = not lights[w]
    return lights


def recursediagram(sollights, lights, buttons, depth, presses):
    if sollights == lights:
        return True, presses
    if depth >= len(buttons):
        return False, 99999999999999999

    no_press_success, no_press_presses = recursediagram(sollights, lights, buttons, depth + 1, presses)
    press_success, press_presses = recursediagram(
        sollights, pressbutton(lights, buttons[depth]), buttons, depth + 1, presses + 1
    )

    return no_press_success or press_success, min(no_press_presses, press_presses)


def pressbuttonjolt(jolt, button):
    for w in button:
        jolt[w] += 1
    return jolt


def recursediagramjolt(soljolt, jolt, buttons, depth, presses):
    if np.all(soljolt == jolt):
        print("Found ", presses)
        return True, presses
    if depth >= len(buttons):
        return False, 99999999999999999
    minpresses = 99999999999999999
    foundSuccess = False
    mask = np.where(buttons[depth])[0]
    for j in range(int(np.ceil(1 + np.min(soljolt[mask] - jolt[mask])))):
        press_success, press_presses = recursediagramjolt(
            soljolt, j * buttons[depth] + jolt, buttons, depth + 1, presses + j
        )
        if press_success:
            minpresses = min(minpresses, press_presses)
            foundSuccess = True

    return foundSuccess, minpresses


print("Begin")
part1res = 0
for manual in manuals:
    sollights, buttons, jolts = manual

    success, presses = recursediagram(sollights, [False] * len(sollights), buttons, 0, 0)
    part1res += presses

print("Part1", part1res)

print("Begin part2")
part2res = 0

# Use ProcessPoolExecutor for multi-processing
for manual in manuals:
    sollights, buttons, soljolts = manual
    for i in range(len(buttons)):
        tmpbutton = np.zeros(len(soljolts))
        for j in buttons[i]:
            tmpbutton[j] += 1
        buttons[i] = tmpbutton

    soljolts = np.array(soljolts)
    buttons = np.array(buttons)
    solution = optimize.linprog(
        [1] * len(buttons),
        A_eq=buttons.T,
        b_eq=soljolts,
        bounds=(0, None),
        method="highs",
        integrality=True,
    )
    solvalid = True

    print("solution", solution.x)
    part2res += int(np.round(np.sum(solution.x)))


print("Part2", part2res)
