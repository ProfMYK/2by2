from functions import *
import time

recursion_limit = 4


def Solve(cube, sol, rec):
    if rec == 0:
        print("Finding a solution...")
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

    if rec < recursion_limit:
        for i, next in enumerate(nexts):
            a = Solve(next, solution + f" {MoveNum(temp, i)}", rec+1)
            if a != -1:
                print(a, rec)
                if a[0] != " ":
                    solutions.append(a.split(" "))
                else:
                    solutions.append(a[1:].split(" "))

    if len(solutions) > 0:
        solution = []
        smal = 10000
        for sl in solutions:
            if len(sl) < smal:
                smal = len(sl)
                solution = sl

        solutionStr = ""
        for char in solution:
            solutionStr += f"{char} "

        return solutionStr

    return -1


scrambled = list(solved)
scramble = input("Enter your scramble: ")
recursion_limit = len(scramble.split(" ")) - 1
Scramble(scramble.split(" "), scrambled)

a = time.time()
print(Solve(scrambled, "", 0))
print(f"Took {int(time.time()-a)} seconds to calculate!")

# TODO: Calculate all posible combinations with graphs!
