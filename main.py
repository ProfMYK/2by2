from functions import *


def Solve(cube, sol):
    solution = sol

    nexts = []
    curr = list(cube)
    for i in range(18):
        curr = list(cube)
        a = MoveNum(curr, i)
        if curr == solved:
            solution += f"{a} "
            return solution
        nexts.append(list(curr))

    # for i, next in enumerate(nexts):
    #     print(i)
    #     print_state(next)
    #     print("\n===============================\n")
        # a = Solve(next, solution)
        # if a != -1:
        #     solution += f"{a} "
        #     return solution
    a = Solve(list(nexts[8]), "")

    return "-1"


scrambled = list(solved)
Scramble(["R2", "U"], scrambled)

print(Solve(scrambled, ""))


# TODO: Calculate all posible combinations with graphs!
