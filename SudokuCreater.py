import threading
import time

check = False

sudoku1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudoku2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudoku3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudoku4 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudoku5 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

f = open("test.txt", "r")
res = list(f.read())

def dizzi():
    for a in range(len(res)):
        if(res[a]=='\n'):
            res.pop(a)
            return dizzi()
dizzi()


def other():
    for b in range(0, 6):
        for a in range(0, 18):
            if a < 9:
                sudoku1[b][a] = res[a + (18 * b)]
            elif a >= 9:
                sudoku2[b][a - 9] = res[a + (18 * b)]

    for b in range(6, 9):
        for a in range(0, 21):
            if a < 9:
                sudoku1[b][a] = res[108 + (a + (21 * (b - 6)))]
            elif 12 > a >= 9:
                sudoku3[b - 6][a - 6] = res[108 + (a + (21 * (b - 6)))]
            elif a >= 12:
                sudoku2[b][a - 12] = res[108 + (a + (21 * (b - 6)))]

    for b in range(3, 6):
        for a in range(0, 9):
            if a < 9:
                sudoku3[b][a] = res[171 + (a + (9 * (b - 3)))]

    for b in range(0, 3):
        for a in range(0, 21):
            if a < 9:
                sudoku4[b][a] = res[198 + (a + (21 * b))]
            elif 12 > a >= 9:
                sudoku3[b + 6][a - 6] = res[198 + (a + (21 * b))]
            elif a >= 12:
                sudoku5[b][a - 12] = res[198 + (a + (21 * b))]

    for b in range(3, 9):
        for a in range(0, 18):
            if a < 9:
                sudoku4[b][a] = res[261 + (a + (18 * (b - 3)))]
            elif a >= 9:
                sudoku5[b][a - 9] = res[261 + (a + (18 * (b - 3)))]

other()
def orta():
    for b in range(6, 9):
        for a in range(6, 9):
            if a < 9:
                sudoku3[b - 6][a - 6] = sudoku1[b][a]

    for b in range(6, 9):
        for a in range(0, 3):
            if a < 9:
                sudoku3[b - 6][a + 6] = sudoku2[b][a]

    for b in range(0, 3):
        for a in range(6, 9):
            if a < 9:
                sudoku3[b + 6][a - 6] = sudoku4[b][a]

    for b in range(0, 3):
        for a in range(0, 3):
            if a < 9:
                sudoku3[b + 6][a + 6] = sudoku5[b][a]


def puzzle(a):
    for i in range(0,9):
        for j in range(0,9):
            if a[i][j]=='*':
                a[i][j]=0
            a[i][j]=int(a[i][j])
            print(a[i][j], end=" ")
        print()
    print()

def checker(a):
    for i in range(0,9):
        for j in range(0,9):
            if a[i][j]==0:
                return True


def puz():
    puzzle(sudoku1)
    puzzle(sudoku2)
    puzzle(sudoku3)
    puzzle(sudoku4)
    puzzle(sudoku5)

orta()
puz()