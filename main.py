from functions import *


def Solve(cube, sol, rec):
    solution = sol

    nexts = []
    curr = list(cube)
    for i in range(18):
        curr = list(cube)
        a = MoveNum(curr, i)
        if curr == solved:
            solution += f" {a}"
            return solution
        nexts.append(list(curr))

    solutions = []

    if rec < 6:
        for i, next in enumerate(nexts):
            a = Solve(next, solution + f" {MoveNum(temp, i)}", rec+1)
            if a != -1:
                solutions.append(a[1:].split(" "))

    if len(solutions) > 0:
        solutionStr = ""
        for char in solutions[0]:
            solutionStr += f"{char} "

        print(solutionStr, rec)

    return -1


scrambled = list(solved)
Scramble("L' U' L U' L' U2 L".split(" "), scrambled)

print(Solve(scrambled, "", 0))


# TODO: Calculate all posible combinations with graphs!
