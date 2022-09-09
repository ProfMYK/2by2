#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define CUBE_LENGTH 24
#define SCRAMBLE_LENGTH 1
#define RECURSION_LIMIT 3

char solved[CUBE_LENGTH] = "WWWWOOGGRROOGGRRYYYYBBBB";
char scrambled[CUBE_LENGTH] = "WWWWOOGGRROOGGRRYYYYBBBB";

void print_state(char cube[CUBE_LENGTH])
{
    printf("  %c%c\n", cube[0], cube[1]);
    printf("  %c%c\n", cube[2], cube[3]);
    printf("%c%c%c%c%c%c\n", cube[4], cube[5], cube[6], cube[7], cube[8], cube[9]);
    printf("%c%c%c%c%c%c\n", cube[10], cube[11], cube[12], cube[13], cube[14], cube[15]);
    printf("  %c%c\n", cube[16], cube[17]);
    printf("  %c%c\n", cube[18], cube[19]);
    printf("  %c%c\n", cube[20], cube[21]);
    printf("  %c%c\n", cube[22], cube[23]);
}

int *get_side(int side)
{
    int *s = malloc(sizeof(int) * 4);
    switch (side)
    {
    case 0:
        s[0] = 8;
        s[1] = 9;
        s[2] = 14;
        s[3] = 15;
        break;
    case 1:
        s[0] = 4;
        s[1] = 5;
        s[2] = 10;
        s[3] = 11;
        break;
    case 2:
        s[0] = 0;
        s[1] = 1;
        s[2] = 2;
        s[3] = 3;
        break;
    case 3:
        s[0] = 16;
        s[1] = 17;
        s[2] = 18;
        s[3] = 19;
        break;
    case 4:
        s[0] = 6;
        s[1] = 7;
        s[2] = 12;
        s[3] = 13;
        break;
    case 5:
        s[0] = 20;
        s[1] = 21;
        s[2] = 22;
        s[3] = 23;
        break;
    default:
        break;
    }
    return s;
}

void Move(char *cube, const char move, const int amount)
{
    int *r = get_side(0);
    int *l = get_side(1);
    int *u = get_side(2);
    int *d = get_side(3);
    int *f = get_side(4);
    int *b = get_side(5);
    for (size_t i = 0; i < amount; i++)
    {
        char _[2], t[2];
        switch (move)
        {
        case 'R':
            _[0] = cube[f[1]];
            _[1] = cube[f[3]];
            cube[f[1]] = cube[d[1]];
            cube[f[3]] = cube[d[3]];
            t[0] = cube[u[1]];
            t[1] = cube[u[3]];
            cube[u[1]] = _[0];
            cube[u[3]] = _[1];
            _[0] = cube[b[1]];
            _[1] = cube[b[3]];
            cube[b[1]] = t[0];
            cube[b[3]] = t[1];
            cube[d[1]] = _[0];
            cube[d[3]] = _[1];
            _[0] = cube[r[0]];
            cube[r[0]] = cube[r[2]];
            t[0] = cube[r[1]];
            cube[r[1]] = _[0];
            cube[r[2]] = cube[r[3]];
            cube[r[3]] = t[0];
            break;
        case 'L':
            _[0] = cube[f[0]];
            _[1] = cube[f[2]];
            cube[f[0]] = cube[u[0]];
            cube[f[2]] = cube[u[2]];
            t[0] = cube[d[0]];
            t[1] = cube[d[2]];
            cube[d[0]] = _[0];
            cube[d[2]] = _[1];
            _[0] = cube[b[0]];
            _[1] = cube[b[2]];
            cube[b[0]] = t[0];
            cube[b[2]] = t[1];
            cube[u[0]] = _[0];
            cube[u[2]] = _[1];
            _[0] = cube[l[0]];
            cube[l[0]] = cube[l[2]];
            t[0] = cube[l[1]];
            cube[l[1]] = _[0];
            cube[l[2]] = cube[l[3]];
            cube[l[3]] = t[0];
            break;
        case 'U':
            _[0] = cube[f[0]];
            _[1] = cube[f[1]];
            cube[f[0]] = cube[r[0]];
            cube[f[1]] = cube[r[1]];
            t[0] = cube[l[0]];
            t[1] = cube[l[1]];
            cube[l[0]] = _[0];
            cube[l[1]] = _[1];
            _[0] = cube[b[2]];
            _[1] = cube[b[3]];
            cube[b[2]] = t[1];
            cube[b[3]] = t[0];
            cube[r[0]] = _[1];
            cube[r[1]] = _[0];
            _[0] = cube[u[0]];
            cube[u[0]] = cube[u[2]];
            t[0] = cube[u[1]];
            cube[u[1]] = _[0];
            cube[u[2]] = cube[u[3]];
            cube[u[3]] = t[0];
            break;
        case 'D':
            _[0] = cube[f[2]];
            _[1] = cube[f[3]];
            cube[f[2]] = cube[l[2]];
            cube[f[3]] = cube[l[3]];
            t[0] = cube[r[2]];
            t[1] = cube[r[3]];
            cube[r[2]] = _[0];
            cube[r[3]] = _[1];
            _[0] = cube[b[1]];
            _[1] = cube[b[0]];
            cube[b[1]] = t[0];
            cube[b[0]] = t[1];
            cube[l[2]] = _[0];
            cube[l[3]] = _[1];
            _[0] = cube[d[0]];
            cube[d[0]] = cube[d[2]];
            t[0] = cube[d[1]];
            cube[d[1]] = _[0];
            cube[d[2]] = cube[d[3]];
            cube[d[3]] = t[0];
            break;
        case 'F':
            _[0] = cube[l[1]];
            _[1] = cube[l[3]];
            cube[l[1]] = cube[d[0]];
            cube[l[3]] = cube[d[1]];
            t[0] = cube[u[2]];
            t[1] = cube[u[3]];
            cube[u[2]] = _[1];
            cube[u[3]] = _[0];
            _[0] = cube[r[0]];
            _[1] = cube[r[2]];
            cube[r[0]] = t[0];
            cube[r[2]] = t[1];
            cube[d[0]] = _[1];
            cube[d[1]] = _[0];
            _[0] = cube[f[0]];
            cube[f[0]] = cube[f[2]];
            t[0] = cube[f[1]];
            cube[f[1]] = _[0];
            cube[f[2]] = cube[f[3]];
            cube[f[3]] = t[0];
            break;
        case 'B':
            _[0] = cube[r[1]];
            _[1] = cube[r[3]];
            cube[r[1]] = cube[d[3]];
            cube[r[3]] = cube[d[2]];
            t[0] = cube[u[0]];
            t[1] = cube[u[1]];
            cube[u[0]] = _[0];
            cube[u[1]] = _[1];
            _[0] = cube[l[0]];
            _[1] = cube[l[2]];
            cube[l[0]] = t[1];
            cube[l[2]] = t[0];
            cube[d[2]] = _[0];
            cube[d[3]] = _[1];
            _[0] = cube[b[0]];
            cube[b[0]] = cube[b[2]];
            t[0] = cube[b[1]];
            cube[b[1]] = _[0];
            cube[b[2]] = cube[b[3]];
            cube[b[3]] = t[0];
        default:
            break;
        }
    }
}

char *MoveNum(char cube[CUBE_LENGTH], int num)
{
    if (num == 0)
    {
        Move(cube, 'R', 1);
        return "R ";
    }
    else if (num == 1)
    {
        Move(cube, 'R', 2);
        return "R2";
    }
    else if (num == 2)
    {
        Move(cube, 'R', 3);
        return "R'";
    }
    else if (num == 3)
    {
        Move(cube, 'L', 1);
        return "L ";
    }
    else if (num == 4)
    {
        Move(cube, 'L', 2);
        return "L2";
    }
    else if (num == 5)
    {
        Move(cube, 'L', 3);
        return "L'";
    }
    else if (num == 6)
    {
        Move(cube, 'U', 1);
        return "U ";
    }
    else if (num == 7)
    {
        Move(cube, 'U', 2);
        return "U2";
    }
    else if (num == 8)
    {
        Move(cube, 'U', 3);
        return "U'";
    }
    else if (num == 9)
    {
        Move(cube, 'D', 1);
        return "D ";
    }
    else if (num == 10)
    {
        Move(cube, 'D', 2);
        return "D2";
    }
    else if (num == 11)
    {
        Move(cube, 'D', 3);
        return "D'";
    }
    else if (num == 12)
    {
        Move(cube, 'F', 1);
        return "F ";
    }
    else if (num == 13)
    {
        Move(cube, 'F', 2);
        return "F2";
    }
    else if (num == 14)
    {
        Move(cube, 'F', 3);
        return "F'";
    }
    else if (num == 15)
    {
        Move(cube, 'B', 1);
        return "B ";
    }
    else if (num == 16)
    {
        Move(cube, 'B', 2);
        return "B2";
    }
    else if (num == 17)
    {
        Move(cube, 'B', 3);
        return "B'";
    }
}

void Scramble(char scramble[SCRAMBLE_LENGTH * 2], char cube[CUBE_LENGTH])
{
    printf("\n-----------------------------------------------------\n\n");
    print_state(cube);
    for (size_t i = 0; i < SCRAMBLE_LENGTH; i++)
    {
        if (scramble[i * 2 + 1] == ' ')
        {
            Move(cube, scramble[i * 2], 1);
        }
        else if (scramble[i * 2 + 1] == '\'')
        {
            Move(cube, scramble[i * 2], 3);
        }
        else if (scramble[i * 2 + 1] == '2')
        {
            Move(cube, scramble[i * 2], 2);
        }
    }

    printf("\nScramble: ");
    for (size_t i = 0; i < SCRAMBLE_LENGTH; i++)
    {
        printf("%c%c ", scramble[i * 2], scramble[i * 2 + 1]);
    }
    printf("\n\n");
    print_state(cube);
    printf("\n-----------------------------------------------------\n\n");
}

char *Solve(char cube[CUBE_LENGTH], char *sol, size_t rec)
{
    if (rec == 0)
        printf("Finding a solution...\n");
    char *solution = "";
    // strcpy(solution, sol);

    char *nexts[18];
    for (size_t i = 0; i < 18; i++)
    {
        char curr[CUBE_LENGTH];
        strncpy(curr, cube, sizeof(curr));
        char move[2];
        strncpy(move, MoveNum(curr, i), sizeof(move));
        bool solve = true;
        for (size_t i = 0; i < CUBE_LENGTH; i++)
            if (curr[i] != solved[i])
                solve = false;

        if (solve)
        {
            char m[3];
            // strncpy(m, (char *){move[0], move[1], '\0'}, sizeof(m));
            // strncat(solution, m, sizeof(solution));
            //  printf(solution);
        }
        nexts[i] = curr;
    }

    for (size_t i = 0; i < 18; i++)
    {
        // print_state(nexts[i]);
        // printf("\n");
    }

    // solutions = []

    // if rec < recursion_limit:
    //     for i, next in enumerate(nexts):
    //         a = Solve(next, solution + f" {MoveNum(temp, i)}", rec+1)
    //         if a != -1:
    //             print("Debug:", a, rec)
    //             if a[0] != " ":
    //                 solutions.append(a.split(" "))
    //             else:
    //                 solutions.append(a[1:].split(" "))

    // if len(solutions) > 0:
    //     solution = []
    //     smal = 10000
    //     for sl in solutions:
    //         if len(sl) < smal:
    //             smal = len(sl)
    //             solution = sl

    //     solutionStr = ""
    //     for char in solution:
    //         solutionStr += f"{char} "

    //     return solutionStr

    // return -1

    return "-1";
}

int main()
{
    char scramble[SCRAMBLE_LENGTH * 2] = "R ";
    Scramble(scramble, scrambled);

    Solve(scrambled, "", 0);
}