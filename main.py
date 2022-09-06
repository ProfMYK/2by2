solved = ['W', 'W', 'W', 'W', 'O', 'O', 'G', 'G', 'R', 'R', 'O',
          'O', 'G', 'G', 'R', 'R', 'a', 'b', 'c', 'd', 'B', 'B', 'B', 'B']


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


def Move(cube: str, move: int, amount: int = 1):
    """A simple funtion to rotate(move) a side of the cube by a certian amount.

    Args:
        cube (str): Rubik's cubes current state.
        move (int): The face of the cube to rotate represented as a number. (0->R, 1->L, 2->U, 3->D, 4->F, 5->B).
        amount (int): The amount of the move that is going to done to do cube. Defaults to 1.
    """
    r = get_side(cube, 0)
    l = get_side(cube, 1)
    u = get_side(cube, 2)
    d = get_side(cube, 3)
    f = get_side(cube, 4)
    b = get_side(cube, 5)
    for i in range(amount):
        if move == 0:  # Right
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
        elif move == 1:  # Left
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
        elif move == 2:  # Up
            _ = cube[f[0]], cube[f[1]]
            cube[f[0]] = cube[r[0]]
            cube[f[1]] = cube[r[1]]
            t = cube[l[0]], cube[l[1]]
            cube[l[0]] = _[0]
            cube[l[1]] = _[1]
            _ = cube[b[0]], cube[b[1]]
            cube[b[0]] = t[0]
            cube[b[1]] = t[1]
            cube[r[0]] = _[0]
            cube[r[1]] = _[1]
            _ = cube[u[0]]
            cube[u[0]] = cube[u[2]]
            t = cube[u[1]]
            cube[u[1]] = _
            cube[u[2]] = cube[u[3]]
            cube[u[3]] = t
        elif move == 3:  # Down
            _ = cube[f[2]], cube[f[3]]
            cube[f[2]] = cube[l[2]]
            cube[f[3]] = cube[l[3]]
            t = cube[r[2]], cube[r[3]]
            cube[r[2]] = _[0]
            cube[r[3]] = _[1]
            _ = cube[b[2]], cube[b[3]]
            cube[b[2]] = t[0]
            cube[b[3]] = t[1]
            cube[l[2]] = _[0]
            cube[l[3]] = _[1]
            _ = cube[d[0]]
            cube[d[0]] = cube[d[2]]
            t = cube[d[1]]
            cube[d[1]] = _
            cube[d[2]] = cube[d[3]]
            cube[d[3]] = t
        elif move == 4:  # Front
            print("F")
        elif move == 5:  # Back
            print("B")


print_state(solved)
print(get_side(solved, 0))
Move(solved, 3)
print_state(solved)
