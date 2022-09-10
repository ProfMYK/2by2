import time

from colorama import Fore

from functions import *

recursion_limit = 4


def SolveWithRecursion(cube, sol, rec):
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
            a = SolveWithRecursion(
                next, solution + f" {MoveNum(temp, i)}", rec+1)
            if a != -1:
                print(f"{Fore.RED}Debug: {Fore.RESET}{a} {Fore.BLUE}{rec}")
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
scramble = "F' U R2 U B U'"
recursion_limit = len(scramble.split(" ")) - 1
Scramble(scramble.split(" "), scrambled)

a = time.time()
print(f"{Fore.GREEN}Solution:{Fore.RESET}",
      SolveWithRecursion(scrambled, "", 0))
print(f"Took {Fore.GREEN}{int(time.time()-a)}{Fore.RESET} seconds to calculate!")

# TODO: Try to solve it with algorithms and stuff
