import colorama
from colorama import Back

colorama.init(autoreset=True)

solved = [f'{Back.WHITE}W', f'{Back.WHITE}W', f'{Back.WHITE}W', f'{Back.WHITE}W', f'{Back.MAGENTA}O', f'{Back.MAGENTA}O', f'{Back.GREEN}G', f'{Back.GREEN}G', f'{Back.RED}R', f'{Back.RED}R', f'{Back.MAGENTA}O',
          f'{Back.MAGENTA}O', f'{Back.GREEN}G', f'{Back.GREEN}G', f'{Back.RED}R', f'{Back.RED}R', f'{Back.YELLOW}Y', f'{Back.YELLOW}Y', f'{Back.YELLOW}Y', f'{Back.YELLOW}Y', f'{Back.BLUE}B', f'{Back.BLUE}B', f'{Back.BLUE}B', f'{Back.BLUE}B']


def print_state(cubeState: str):
    """A simple function to display the rubik's cube state.

    Args:
        cubeState {str}: Rubik's cubes current state.
    """
    print(f"  {cubeState[0]}{cubeState[1]}")
    print(f"  {cubeState[2]}{cubeState[3]}")
    print(
        f"{cubeState[4]}{cubeState[5]}{cubeState[6]}{cubeState[7]}{cubeState[8]}{cubeState[9]}")
    print(
        f"{cubeState[10]}{cubeState[11]}{cubeState[12]}{cubeState[13]}{cubeState[14]}{cubeState[15]}")
    print(f"  {cubeState[16]}{cubeState[17]}")
    print(f"  {cubeState[18]}{cubeState[19]}")
    print(f"  {cubeState[20]}{cubeState[21]}")
    print(f"  {cubeState[22]}{cubeState[23]}")


def get_side(cube: str, side: int):
    s = []
    if side == 0:
        s = (8, 9, 14, 15)
    if side == 1:
        s = (4, 5, 10, 11)
    if side == 2:
        s = (0, 1, 2, 3)
    if side == 3:
        s = (16, 17, 18, 19)
    if side == 4:
        s = (6, 7, 12, 13)
    if side == 5:
        s = (20, 21, 22, 23)
    return s


def Move(cube: str, move: str, amount: int = 1):
    """A simple funtion to rotate(move) a side of the cube by a certian amount.

    Args:
        cube (str): Rubik's cubes current state.
        move (str): The face of the cube to be rotated.
        amount (int): The amount of the move that is going to done to do cube. Defaults to 1.
    """
    r = get_side(cube, 0)
    l = get_side(cube, 1)
    u = get_side(cube, 2)
    d = get_side(cube, 3)
    f = get_side(cube, 4)
    b = get_side(cube, 5)
    for i in range(amount):
        if move == 'R':  # Right
            _ = cube[f[1]], cube[f[3]]
            cube[f[1]] = cube[d[1]]
            cube[f[3]] = cube[d[3]]
            t = cube[u[1]], cube[u[3]]
            cube[u[1]] = _[0]
            cube[u[3]] = _[1]
            _ = cube[b[1]], cube[b[3]]
            cube[b[1]] = t[0]
            cube[b[3]] = t[1]
            cube[d[1]] = _[0]
            cube[d[3]] = _[1]
            _ = cube[r[0]]
            cube[r[0]] = cube[r[2]]
            t = cube[r[1]]
            cube[r[1]] = _
            cube[r[2]] = cube[r[3]]
            cube[r[3]] = t
        elif move == 'L':  # Left
            _ = cube[f[0]], cube[f[2]]
            cube[f[0]] = cube[u[0]]
            cube[f[2]] = cube[u[2]]
            t = cube[d[0]], cube[d[2]]
            cube[d[0]] = _[0]
            cube[d[2]] = _[1]
            _ = cube[b[0]], cube[b[2]]
            cube[b[0]] = t[0]
            cube[b[2]] = t[1]
            cube[u[0]] = _[0]
            cube[u[2]] = _[1]
            _ = cube[l[0]]
            cube[l[0]] = cube[l[2]]
            t = cube[l[1]]
            cube[l[1]] = _
            cube[l[2]] = cube[l[3]]
            cube[l[3]] = t
        elif move == 'U':  # Up
            _ = cube[f[0]], cube[f[1]]
            cube[f[0]] = cube[r[0]]
            cube[f[1]] = cube[r[1]]
            t = cube[l[0]], cube[l[1]]
            cube[l[0]] = _[0]
            cube[l[1]] = _[1]
            _ = cube[b[2]], cube[b[3]]
            cube[b[2]] = t[1]
            cube[b[3]] = t[0]
            cube[r[0]] = _[1]
            cube[r[1]] = _[0]
            _ = cube[u[0]]
            cube[u[0]] = cube[u[2]]
            t = cube[u[1]]
            cube[u[1]] = _
            cube[u[2]] = cube[u[3]]
            cube[u[3]] = t
        elif move == 'D':  # Down
            _ = cube[f[2]], cube[f[3]]
            cube[f[2]] = cube[l[2]]
            cube[f[3]] = cube[l[3]]
            t = cube[r[2]], cube[r[3]]
            cube[r[2]] = _[0]
            cube[r[3]] = _[1]
            _ = cube[b[1]], cube[b[0]]
            cube[b[1]] = t[0]
            cube[b[0]] = t[1]
            cube[l[2]] = _[0]
            cube[l[3]] = _[1]
            _ = cube[d[0]]
            cube[d[0]] = cube[d[2]]
            t = cube[d[1]]
            cube[d[1]] = _
            cube[d[2]] = cube[d[3]]
            cube[d[3]] = t
        elif move == 'F':  # Front
            _ = cube[l[1]], cube[l[3]]
            cube[l[1]] = cube[d[0]]
            cube[l[3]] = cube[d[1]]
            t = cube[u[2]], cube[u[3]]
            cube[u[2]] = _[1]
            cube[u[3]] = _[0]
            _ = cube[r[0]], cube[r[2]]
            cube[r[0]] = t[0]
            cube[r[2]] = t[1]
            cube[d[0]] = _[1]
            cube[d[1]] = _[0]
            _ = cube[f[0]]
            cube[f[0]] = cube[f[2]]
            t = cube[f[1]]
            cube[f[1]] = _
            cube[f[2]] = cube[f[3]]
            cube[f[3]] = t
        elif move == 'B':  # Back
            _ = cube[r[1]], cube[r[3]]
            cube[r[1]] = cube[d[3]]
            cube[r[3]] = cube[d[2]]
            t = cube[u[0]], cube[u[1]]
            cube[u[0]] = _[0]
            cube[u[1]] = _[1]
            _ = cube[l[0]], cube[l[2]]
            cube[l[0]] = t[1]
            cube[l[2]] = t[0]
            cube[d[2]] = _[0]
            cube[d[3]] = _[1]
            _ = cube[b[0]]
            cube[b[0]] = cube[b[2]]
            t = cube[b[1]]
            cube[b[1]] = _
            cube[b[2]] = cube[b[3]]
            cube[b[3]] = t


def Scramble(scramble: list, cube: str):
    """Scrambles the cube using the given scramble

    Args:
        scramble (list): Scramble to be aplied
        cube (str): Cubes current state
    """
    for move in scramble:
        print_state(cube)
        if len(move) == 2:
            if move[1] == "'":
                Move(cube, move[0], amount=3)
            elif move[1] == "2":
                Move(cube, move[0], amount=2)
        else:
            Move(cube, move)

        print("\nMove: ", move, "\n")
        print_state(cube)
        print("\n-----------------------------------------------------\n")


# Debug
scramble = "R2 U2 R U' F2 R F2 U' R' U'".split(" ")
Scramble(scramble, solved)
# print_state(solved)

# TODO: Calculate all posible combinations with graphs!
